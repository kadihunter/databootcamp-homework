from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
from splinter import Browser
import requests
import time
import lxml

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)


def mars_new(browser):
    marsurl = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(marsurl)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")  
    news_title = soup.find('div', class_="content_title").text.strip()
    news_p = soup.find('div', class_="article_teaser_body").text.strip()
    mars_news = {
        "News_Title" : news_title,
        "News_Paragraph" : news_p
    }
    return mars_news

def image_jpl(browser):
    
    imageurl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(imageurl)
    time.sleep(1)
    browser.find_by_id('full_image').first.click()
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    marsimage = soup.find('img', class_="fancybox-image").get("src")
    baseurl = 'https://www.jpl.nasa.gov'
    featured_image_url = baseurl+marsimage
    return featured_image_url

def tweet(browser):
    tweetsurl = 'https://twitter.com/marswxreport?lang=en'
    response=requests.get(tweetsurl)
    soup=bs(response.text, 'lxml')
    weather=soup.find('div', class_='js-tweet-text-container').p.text
    return weather


def mars_facts(browser):
    factsurl = 'https://space-facts.com/mars/'
    browser.visit(factsurl)
    time.sleep(1)
    df = pd.read_html(factsurl)[0]
    newdf = df.set_index(0).rename(columns={1:"Value"})
    factshtml = newdf.to_html(classes="table-condensed")
    return factshtml

def hemispheres(browser):
    usgsurl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgsurl)
    time.sleep(1)
    hemi_data =[]
    for i in range (4):
        browser.find_by_css('a.product-item h3')[i].click()
        time.sleep(1)
        html = browser.html
        soup = bs(html, "html.parser")
        heminame = soup.find('h2').text.strip()
        hemipic = soup.find('a', target="_blank").get("href")
        hemisphere = {
            "title" : heminame,
            "img_url" : hemipic
        }
        hemi_data.append(hemisphere)
        browser.back()
    return hemi_data



def scrape_info():
    browser = init_browser()
    newsdata = mars_new(browser)
    jplimage = image_jpl(browser)
    marstweets = tweet(browser)  
    facts = mars_facts(browser)
    hemi = hemispheres(browser)

    # Store data in a dictionary
    mars_data = {
        "news_data": newsdata,
        "jpl_image": jplimage,
        "mars_tweets": marstweets, 
        "mars_facts": facts,
        "mars_hemisphere": hemi
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data