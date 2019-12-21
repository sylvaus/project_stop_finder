from flask import Flask, render_template, request
from finders.find_name import find_stops_matching_name
from finders.find_in_range import find_stops_in_range
from finders.stops import Stop
from finders.gps import GPSPosition
# from finders.find_in_range import find_stops_in_range
# from finders.find_closest import find_closest_stop

# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)


# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Task %r>' % self.id

SAMPLE_STOPS = [
    (Stop(name='de la Commune / Place Jacques-Cartier',
             gps=GPSPosition(latitude=45.50761009451047, longitude=-73.55183601379395))),
    (Stop(name='Métro Champ-de-Mars (Viger / Sanguinet)',
             gps=GPSPosition(latitude=45.51035067563653, longitude=-73.55650842189789))),
    (Stop(name='Ste-Catherine / Dezery',
             gps=GPSPosition(latitude=45.539385081961676, longitude=-73.54099988937377))),
    (Stop(name='Clark / Evans',
              gps=GPSPosition(latitude=45.51100666600306, longitude=-73.56760203838348))),
    (Stop(name='du Champ-de-Mars / Gosford',
             gps=GPSPosition(latitude=45.50965520472071, longitude=-73.55400860309601))),
    (Stop(name='Metcalfe / du Square-Dorchester',
             gps=GPSPosition(latitude=45.500208064155046, longitude=-73.57113786041737))),
    (Stop(name='18e avenue / Rosemont',
              gps=GPSPosition(latitude=45.55789545752947, longitude=-73.5765291005373))),
    (Stop(name="de l'Hôtel-de-Ville / Ste-Catherine",
             gps=GPSPosition(latitude=45.51166045593874, longitude=-73.56213569641113))),
    (Stop(name='Sanguinet / Ste-Catherine',
             gps=GPSPosition(latitude=45.51279685582333, longitude=-73.56146247242577))),
    (Stop(name='Crescent / de Maisonneuve',
             gps=GPSPosition(latitude=45.49811161443597, longitude=-73.57761539518833))),
    (Stop(name="Gare d'autocars de Montréal (Berri / Ontario)",
             gps=GPSPosition(latitude=45.51689676614314, longitude=-73.5639488697052)))
]

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # data parsing
        stop = request.form['stop']
        range = request.form['range']
        current_location = request.form['current_location']
        rgx = request.form.get('rgx')
        rgxbool = False
        if rgx == "True":
            rgxbool = True
        if range != "":
            rangefloat = float(range)
        if current_location != "":
            current_location_list = current_location.split(',')
            current_location_latitude = float(current_location_list[0])
            current_location_longitude = float(current_location_list[1])

        # Return invalid entry when stop and range are empty string
        if stop == "" and range == "":
            return "Invalid Entry"
        
        # Return available stops matching name 
        elif stop != "" and range == "":
            str = "<br/>"
            strlst = list()
            lst = find_stops_matching_name(SAMPLE_STOPS, stop, rgxbool)
            for target_list in lst:
                strlst.append(target_list.name)
            return  str.join(strlst)
        
        #  Return available stops in range
        elif stop == "" and range != "":
            str = "<br/>"
            strlst = list()
            lst = find_stops_in_range(SAMPLE_STOPS, GPSPosition(current_location_latitude, current_location_longitude), rangefloat)
            for target_list in lst:
                strlst.append(target_list.name)
            return str.join(strlst)

        #  Return available stop in range and matching name.
        elif stop != "" and range != "":
            str = "<br/>"
            strlst = list()
            lst_in_range = find_stops_in_range(SAMPLE_STOPS, GPSPosition(current_location_latitude, current_location_longitude), rangefloat)
            lst = find_stops_matching_name(lst_in_range, stop, rgxbool)
            for target_list in lst:
                strlst.append(target_list.name)
            return str.join(strlst)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
