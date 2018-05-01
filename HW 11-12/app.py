from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import mission_to_mars


app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    listings = mongo.db.listings.find()
    return render_template("index.html", listings=listings)

@app.route("/clear")
def clear():
    result = mongo.db.listings.delete_many({})
    return redirect("http://127.0.0.1:5000/", code=302)

@app.route("/scrape")
def scrape():
    listings = mongo.db.listings
    listings_data = scrape_craigslist.scrape()
    for listing in listings_data:
        listings.update({'headline':listing['headline'], 'price':listing['price'], 'hood':listing['hood']}, listing, upsert=True)
    return redirect("http://127.0.0.1:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

# Initialize PyMongo to work with MongoDBs

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)



# Define database and collection

db_imgs = client.mars_imgs_db

db_tweets = client.mars_tweets_db
db_news = client.news_db

collection_imgs = db_imgs.articles

collection_tweets = db_tweets.articles

collection_news = db_news.articles

for i in range(len(tweets)):
	tweet_dict = {tweet:mars_tweets[i]}
	news_dict = {title:title[i],text:text[i]}

	collection_tweets.insertone(tweet_dict)
	collection_news.insertone(news_dict)
