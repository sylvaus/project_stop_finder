from flask import Flask, render_template, request
from typing import List
from decimal import Decimal
from dataclasses import dataclass
from finders.find_name import find_stops_matching_name
from finders.find_in_range import find_stops_in_range
from finders.find_closest import find_closest_stop
from finders.stops import Stop
from finders.gps import GPSPosition, gps_distance
from variables import BIXI_list

# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Task %r>' % self.id

@dataclass
class GUIParameters:
    rgxbool: bool
    rangefloat: float
    current_location_latitude: float
    current_location_longitude: float
    show_all_bool: bool

@dataclass
class StopDistance:
    stop: Stop
    distance: float

stop_:str
range_:str
rgx_:str
current_location_:str
response_: str
show_all_: str

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    global stop_
    global range_
    global current_location_
    global rgx_
    global response_
    global show_all_
    
    parameters = GUIParameters(False, 0.0, 0.0, 0.0, False)

    if request.method == 'POST':
        parse_data()
        set_parameters(parameters)
        if parameters.show_all_bool:
            show_all(parameters.show_all_bool)
        else:
            refresh_page(parameters.current_location_latitude, parameters.current_location_longitude)
            return_stops_name(parameters.rgxbool, parameters.current_location_latitude, parameters.current_location_longitude)
            return_stops_in_range(parameters.current_location_latitude, parameters.current_location_longitude, parameters.rangefloat)
            return_stops_name_in_range(parameters.current_location_latitude, parameters.current_location_longitude, parameters.rangefloat, parameters.rgxbool)
    return response_

        
def parse_data():
    global stop_
    global range_
    global current_location_
    global rgx_
    global show_all_

    stop_ = request.form['stop']
    range_ = request.form['range']
    current_location_ = request.form['current_location']
    rgx_ = request.form.get('rgx')
    show_all_ = request.form.get('Show All')


def set_parameters(parameters: GUIParameters):
    global range_
    global current_location_
    global rgx_

    if rgx_ == "True":
            parameters.rgxbool = True
    if range_ != "":
        parameters.rangefloat = float(range_)
    if current_location_ != "":
        current_location_list = current_location_.split(',')
        parameters.current_location_latitude = float(current_location_list[0])
        parameters.current_location_longitude = float(current_location_list[1])
    if show_all_ == "Show All":
            parameters.show_all_bool = True


def show_all(show_stops:bool):
    global response_

    if show_stops:
            response_ = render_template('index.html', lstStop = BIXI_list)


def refresh_page(current_location_latitude: float, current_location_longitude: float):
    global stop_
    global range_
    global current_location_
    global response_

    # Refresh the webpage when input are not inserted
    if stop_ == "" and range_ == "":
        if current_location_ != "":
            stop = find_closest_stop(BIXI_list, GPSPosition(current_location_latitude, current_location_longitude))
            response_ = render_template('index.html',
                stopName = stop.name,
                stopDistance = toDecimal2(gps_distance(GPSPosition(current_location_latitude, current_location_longitude), stop.gps)/1000),
                stopLat = stop.gps.latitude,
                stopLong = stop.gps.longitude)
        else:
            response_ = render_template('index.html')


def return_stops_name(rgxbool: bool, current_location_latitude: float, current_location_longitude: float):
    global stop_
    global range_
    global response_

    # Return available stops matching name 
    if stop_ != "" and range_ == "":
        lst = find_stops_matching_name(BIXI_list, stop_, rgxbool)
        if lst_is_empty(lst):
            pass
        elif current_location_ == "":
            response_ = render_template('index.html', lstStop = lst)
        else:
            stop = find_closest_stop(lst, GPSPosition(current_location_latitude, current_location_longitude))
            response_ = render_template('index.html',
                stopName = stop.name,
                stopDistance = toDecimal2(gps_distance(GPSPosition(current_location_latitude, current_location_longitude), stop.gps)/1000),
                stopLat = stop.gps.latitude,
                stopLong = stop.gps.longitude)


def return_stops_in_range(current_location_latitude: float, current_location_longitude: float, rangefloat: float):
    global stop_
    global range_
    global response_

    #  Return available stops in range
    if stop_ == "" and range_ != "":
        if current_location_ != "":
            lst = find_stops_in_range(BIXI_list, GPSPosition(current_location_latitude, current_location_longitude), rangefloat)
            if lst_is_empty(lst):
                pass
            else:
                send_stop_name_and_distance(lst, current_location_latitude, current_location_longitude)
        else:
            response_ = render_template('index.html', result = "Please enter your coordinates!!!")


def return_stops_name_in_range(current_location_latitude: float, current_location_longitude: float, rangefloat: float, rgxbool: bool):
    global stop_
    global range_
    global current_location_
    global response_

    #  Return available stop in range and matching name.
    if stop_ != "" and range_ != "":
        if current_location_ != "":
            lst_in_range = find_stops_in_range(BIXI_list, GPSPosition(current_location_latitude, current_location_longitude), rangefloat)
            lst = find_stops_matching_name(lst_in_range, stop_, rgxbool)
            if not lst_is_empty(lst):
                send_stop_name_and_distance(lst, current_location_latitude, current_location_longitude)
        else:
            response_ = render_template('index.html', result = "Please enter your coordinates!!!")


def send_stop_name_and_distance(lst: List[Stop], current_location_latitude: float = 0.0, current_location_longitude: float = 0.0):
    global response_

    lstDistance = list()
    lstStop = list()
    for target_list in lst:
        lstDistance.append(toDecimal2(gps_distance(GPSPosition(current_location_latitude, current_location_longitude), target_list.gps)/1000))
        lstStop.append(target_list)
    response_ = render_template('index.html', lstDistance=lstDistance, lstStop=lstStop)


def lst_is_empty(lst: List[Stop]):
    global response_

    if not lst:
        response_ = render_template('index.html', result = "Stop not found")
        return True
    return False


def toDecimal2(f: float):
    return round(Decimal(f),2)


if __name__ == "__main__":
    app.run(debug=True)
