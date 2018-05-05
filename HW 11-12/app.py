from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import mission_to_mars


app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
	news_title_text = mongo.db.news.find()
	pic_of_day = mongo.db.pic_of_day.find()
	mars_tweets = mongo.db.tweets.find()
	img_dict = mongo.db.imgs.find()
	return render_template("index.html", listings=listings)

@app.route("/clear")
def clear():
	result_1 = mongo.db.news.delete_many({})
	result_2 = mongo.db.pic_of_day.delete_many({})
	result_3 = mongo.db.tweets.delete_many({})
	result_4 = mongo.db.imigs.delete_many({})
	return redirect("http://127.0.0.1:5000/", code=302)

@app.route("/scrape")
def scrape():
	news_title_text = mongo.db.news
	pic_of_day = mongo.db.pic_of_day
	mars_tweets = mongo.db.tweets
	img_dict = mongo.db.imgs
	mars_data = mission_to_mars.scrape()
	


if __name__ == "__main__":
    app.run(debug=True)



