from datetime import datetime, timedelta
from random import randint

from flask import render_template, request, jsonify, redirect
from app import app, db
from app.forms import ForecastForm
from app.models import Forecast

CITIES = ['Amsterdam', 'Warsaw']


class Week:
    def __init__(self, start):
        self.start = start.strftime("%d-%m-%y")
        self.end = (start + timedelta(days=7)).strftime("%d-%m-%y")
        self.week_days = self.get_weekdays(start)

    def get_weekdays(self, start):
        weekdays = []
        for i in range(8):
            weekdays.append((start + timedelta(days=i)).strftime("%d-%m-%y"))
        return weekdays


def get_weather_for_date(day):
    return randint(5, 15)


@app.route('/')
@app.route('/week')
def index():
    week = Week(datetime.today())
    week_weather = {
        day: get_weather_for_date(day) for day in week.week_days
    }
    return render_template('week_overview.html', week=week, city=CITIES, week_weather=week_weather)


@app.route('/week/<city>')
def weather_in_city(city):
    city = city.lower()
    print(city)
    if city in [cities.lower() for cities in CITIES]:
        week = Week(datetime.today())
        week_weather = {
            day: get_weather_for_date(day) for day in week.week_days
        }
        return render_template('week_overview.html', week=week, city=city, week_weather=week_weather)
    return render_template('404.html'), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    forecast_form = ForecastForm()
    if request.method == 'POST':
        city = request.form.get('city')
        date = request.form.get('date')
        date_format = datetime.strptime(date, '%d-%m-%y')
        forecast = Forecast(city=city, date=date, temperature=get_weather_for_date(date))
        db.session.add(forecast)
        db.session.commit()
        return redirect('/')
    return render_template('add_forecast.html', form=forecast_form)


@app.route('/forecast/<id>', methods=['GET', 'PATCH'])
def forecast_for_id(_id):
    if request.method == "PATCH":
        temperature = request.args.get('temperature')
        forecast = Forecast.query.get_or_404(_id)
        forecast.temperature = temperature
        db.session.commit()
        return jsonify({"id": forecast._id}), 200
    elif request.method == "GET":
        forecast = Forecast.query.get_or_404(_id)
        return jsonify({
            "id": forecast._id,
            "city": forecast.city,
            'temperature': forecast.temperature,
            'date': forecast.date
        })


@app.route('/delete_forecast/<id>', methods=["DELETE"])
def delete_forecast(_id):
    forecast = Forecast.query.get_or_404(_id)
    db.session.delete(forecast)
    db.commit()
    return jsonify({'result': True})
