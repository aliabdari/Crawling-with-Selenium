# Crawling websites with Selenium
In this repository, we discuss how to crawl different data from websites with python selenium library.<br/>
The main purpose of Selenium is for testing web pages. It is an open-source web-based automation tool.<br/>
But by using various functions in selenium we can access to numerous us types of data, that then we can use them for many purposes like gathering dataset for machine learning tasks.</br>

## Essential functions
We have some essential functions in selenium that we learn them here with each other.

1.
Selenium for doing its work opens a browser. The browser can be chrome or firefox that has UI, or phantomjs browser that does not have UI. it's trivial that phanstomjs would be faster than the others, but we can see the process by our eyes. so it's a good way to do our develope and debugs with chrome or firefox, and for the final version of our code we replace them with phantomjs to speed up our work.
for this purpose, we should initialize the webdriver for our navigation in a web webpage.So first we import webdriver<br>
from selenium import webdriver<br>
And then we initialize our driver with the path of our browser driver.<br>
driver = webdriver.Chrome('chromedriver')<br>
