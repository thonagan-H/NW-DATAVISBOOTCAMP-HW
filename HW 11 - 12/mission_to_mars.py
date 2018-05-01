
# coding: utf-8

# In[123]:


# Dependencies# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import time



# In[57]:


#BS Scraper:
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


# In[ ]:


url_mars_press = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
scraper(url_mars_press)


# In[ ]:


# Examine the results, then determine element that contains sought info
# results are returned as an iterable list
print(soup.body.prettify())


# In[ ]:


headings_res = soup.find_all('div', class_='bottom_gradient')
para_res = soup.find_all('div', class_='article_teaser_body')


# In[ ]:


article_title = []
para_txt = []
for i in range(len(headings_res)):
    article_title.append(headings_res[i].text) 
    para_txt.append(para_res[i].text)


# In[4]:


#USE SPLINTER TO GET IMG URL
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "D:\Downloads\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# In[ ]:


brow = init_browser()
mars_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
brow.visit(mars_img_url)


# In[11]:


dir(brow_images)


# In[ ]:


brow.click_link_by_partial_text('FULL IMAGE')
imgs = brow.find_by_tag('img')
for i in range(len(imgs)):
    if imgs[i].has_class('fancybox-image') == True:
        print(imgs[i]._element.get_attribute('src'))
    


# In[ ]:


#Mars Tweets:
url_tweets = "https://twitter.com/marswxreport?lang=en"
scraper(url_tweets)
print(pretty_print)


# In[ ]:


tweets = soups.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
mars_weather = []
for i in range(len(tweets)):
    mars_weather.append((tweets[i]).text)


# In[121]:


#Mars Images
brow_images = init_browser()
img_site = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
brow_images.visit(img_site)


# In[126]:


#clcik by title
#use that for the click link by title
#goto next page and click link by title 'sample'
#img = find by tage img
list_of_dict = []
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
    list_of_dict.append(img_dict)
    brow_images.quit()
    brow_images = init_browser()
    brow_images.visit(img_site)
    time.sleep(10)


# In[125]:


list_of_dict

