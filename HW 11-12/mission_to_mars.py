#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from flask import (Flask, render_template, jsonify, redirect, )
import pymongo




def scrape():
    # Establish Mongo Connections:
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    #Create Mars Database
    mars_db = client.mars_data
    #Create Collections:
    collection_news = mars_db.news #provide collection of mars news
    collection_pic_of_day = mars_db.pic_of_day #provide collection of mars pic of day url
    collection_tweets = mars_db.tweets #provides collection of tweets
    collection_imgs = mars_db.imgs #Provides collection of img url and tile
    
    #Create Scraper
    pretty_print = None
    soups = None
    browsers = None
    def scraper(link):
        global pretty_print
        global browsers
        browsers = webdriver.Chrome('chromedriver.exe')
        browsers.get(link)
        htmls = browsers.page_source
        global soups
        soups = bs(htmls, "html.parser")
        pretty_print = soups.body.prettify()
        return pretty_print,soups,browsers

    # Scrape Mars Website
    url_mars_press = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    scraper(url_mars_press)
    print(soups.body.prettify())
    
    # Get titles and paragraph text from mars website
    headings_res = soups.find_all('div', class_='content_title')
    para_res = soups.find_all('div', class_='rollover_description_inner')
    for i in range(len(headings_res)):
        news_title_text = {
            'title':headings_res[i].text,
            'text':para_res[i].text
        }
        collection_news.insert_one(news_title_text)

    #USE SPLINTER TO GET IMG URL
    def init_browser():
        # @NOTE: Replace the path with your actual path to the chromedriver
        executable_path = {"executable_path": "D:\Downloads\chromedriver.exe"}
        return Browser("chrome", **executable_path, headless=False)


    # Get URL for Pic of the Day
    brow = init_browser()
    mars_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    brow.visit(mars_img_url)
    brow.click_link_by_partial_text('FULL IMAGE')
    imgs = brow.find_by_tag('img')
    for i in range(len(imgs)):
        if imgs[i].has_class('fancybox-image') == True:
            img_of_the_day = imgs[i]._element.get_attribute('src')
            pic_of_day = {
                'url':img_of_the_day
            }
            collection_pic_of_day.insert_one(pic_of_day)    
    

    # Scrape Mars Twitter:
    url_tweets = "https://twitter.com/marswxreport?lang=en"
    scraper(url_tweets)
    print(pretty_print)

    # Get all Mars Weather Tweets
    tweets = soups.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    for i in range(len(tweets)):
        if 'http' not in tweets[i].text:
            mars_weather.append((tweets[i]).text)
            mars_tweets = {
                'tweet':tweets[i].text
            }
            collection_tweets.insert_one(mars_tweets)

    #Mars Images
    brow_images = init_browser()
    img_site = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    brow_images.visit(img_site)

    # Get a list of all the titles for the hemispheres
    tag_list = []
    tags = brow_images.find_by_tag('h3')
    for i in tags:
        tag_list.append(i.text)
    tag_list
        
    # Get img title and url using a loop
    for i in range(len(tag_list)):
        brow_images.click_link_by_partial_text(tag_list[i])
        link_to_get = brow_images.find_link_by_text('Sample')
        img_title = brow_images.find_by_tag('h2')
        img_dict = {
                     'title':img_title.text,
                     'img_url':link_to_get['href']
         }
        collection_imgs.insert_one(img_dict)
        brow_images.back()
        
    
    return news_title_text,pic_of_day,mars_tweets,img_dict
