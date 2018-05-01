# Dependencies# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from flask import Flask, render_template, jsonify, redirect
import pymongo


def scraper():
    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    
    #Create Scraper
    browsers = webdriver.Chrome('chromedriver.exe')
    url_mars_press = 
    "https://mars.nasa.gov/news/page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browsers.get(url_mars_press)
    htmls = browsers.page_source
    soups = bs(htmls, "html.parser")

    # Examine the results, then determine element that contains sought info
    # results are returned as an iterable list
    print(soup.body.prettify())
    headings_res = soup.find_all('div', class_='bottom_gradient')
    para_res = soup.find_all('div', class_='article_teaser_body')

    article_title = []
    para_txt = []
    for i in range(len(headings_res)):
        article_title.append(headings_res[i].text) 
        para_txt.append(para_res[i].text)

    #USE SPLINTER TO GET IMG URL
    def init_browser():
        # @NOTE: Replace the path with your actual path to the chromedriver
        executable_path = {"executable_path": "D:\Downloads\chromedriver.exe"}
        return Browser("chrome", **executable_path, headless=False)


    brow = init_browser()
    mars_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    brow.visit(mars_img_url)

    brow.click_link_by_partial_text('FULL IMAGE')
    imgs = brow.find_by_tag('img')
    for i in range(len(imgs)):
        if imgs[i].has_class('fancybox-image') == True:
            img_of_the_day = imgs[i]._element.get_attribute('src')
    

    #Mars Tweets:
    url_tweets = "https://twitter.com/marswxreport?lang=en"
    scraper(url_tweets)
    print(pretty_print)
    tweets = soups.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather = []
    for i in range(len(tweets)):
        mars_weather.append((tweets[i]).text)

    #Mars Images
    brow_images = init_browser()
    img_site = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    brow_images.visit(img_site)

    list_of_img_dict = []
    tags = brow_images.find_by_tag('h3')
    for i in range(len(tags)):
        img_dict = {}
        brow_images.click_link_by_partial_text(tags[i].text)
        link_to_click = brow_images.find_link_by_text('Sample')
        img_title = brow_images.find_by_tag('h2')
        brow_images.click_link_by_text('Sample')
        img_dict = {
                    'title':img_title.text,
                    'img_url':link_to_click['href']
        }
        list_of_img_dict.append(img_dict)
        brow_images.quit()
        brow_images = init_browser()
        brow_images.visit(img_site)
        time.sleep(10)
    
    return article_title,para_text,mars_weather,list_of_img_dict
