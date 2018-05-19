# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from biodiversity import *
from samples_data import sample_vals_list
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def names():
    return jsonify(id_list)

@app.route("/otu")
def otu():
    return jsonify(otu_descr)

@app.route("/metadata/<sample>")
def metadata(sample):
    for i in metadata_samples:
            if i['SAMPLEID'] == int(sample.split('_')[1]):
                        return jsonify(i)

@app.route("/wfreq/<sample>")
def wfreq(sample):
    sampleid = int(sample.split('_')[1])
    wfreq = df_met_csv_2.loc[sampleid]['WFREQ']
    return ('The weekly washing frequency is ' + str(wfreq))                        

@app.route("/samples/<sample>")
def samples(sample):
    for i in sample_vals_list:
        for j in i.keys():
            if j == sample:
                return jsonify(i.get(j))

if __name__ == "__main__":
    app.run()
