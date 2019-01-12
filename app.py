from flask import Flask, jsonify

import pandas as pd



###########################################################

# 2. Create an app, being sure to pass __name__

###########################################################

app = Flask(__name__)




###########################################################

# 3. Get the data from csv files

###########################################################
prcp_df = pd.read_csv('Data/precipitation.csv')
station_df = pd.read_csv('Data/station.csv')
tobs_df = pd.read_csv('Data/temperature_obs.csv')


# convert dataframes to dictionary
prcp_dict = prcp_df.to_dict('records')

station_dict = station_df['station'].to_dict()


tobs_dict = tobs_df.to_dict('records')


###########################################################

# 4. Define what to do when a user hits the index route

###########################################################
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

@app.route("/api/v1.0/precipitation")
def jsonified_prcp():
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def jsonified():
    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def tobs_jsonified():
    return jsonify(tobs_dict)

if __name__ == "__main__":
    app.run(debug=True)