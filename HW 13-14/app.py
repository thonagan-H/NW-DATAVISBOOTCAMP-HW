# import necessary libraries

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from biodiversity import *

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

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


# @app.route("/metadata/<sample>")
# def metadata(sample):
#     for i in metadata_samples:
#             if i['SAMPLEID'] == sample:
#                         val = i
#     return jsonify(val)

# @app.route("/wfreq/<sample>")
# def metadata(sample):
#     import df_met_csv_2
#     sampleid = sample.strip('_')[1]
#     wfreq = df_met_csv_2.loc[sampleid]['WFREQ']
#     return ('The weekly washing frequency is ' + wfreq)


if __name__ == "__main__":
    app.run()
