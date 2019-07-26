# Crawling websites with Selenium
In this repository, we discuss how to crawl different data from websites with python selenium library.<br/>
The main purpose of Selenium is for testing web pages. It is an open-source web-based automation tool.<br/>
But by using various functions in selenium we can access to numerous us types of data, that then we can use them for many purposes like gathering dataset for machine learning tasks.</br>

## Essential functions
We have some essential functions in selenium that we learn them here with each other.

1) Initializing the web driver<br/>
Selenium for doing its work opens a browser. The browser can be chrome or firefox that has UI or phantomjs browser that does not have UI. It's trivial that phanstomjs would be faster than the others, but we can see the process by our eyes. So it's a good way to do our develope and debugs with chrome or firefox, and for the final version of our code, we replace them with phantomjs to speed up our work.
for this purpose, we should initialize the webdriver for our navigation in a web webpage. So first we import webdriver<br>
from selenium import webdriver<br>
And then we initialize our driver with the path of our browser driver.<br>
```
driver = webdriver.Chrome('path_to_driver/chromedriver')
```

2) getting the URL<br/>
The second important function is get().<br/>
We should invoke the function with an URL to say the browser to open the desired web page that we want to navigate it.<br/>
```
driver.get(URL)
```

3) wait function<br/>
Some web sites use ajax to loading different data on the web page. In these cases, all of the data are not accessible as the first time that the web page is opened in a browser. Some data will be load little by little over time. In this situation, we do not have any solution just to wait for that data to become visible!!!!<br/>
We have two types of waiting in selenium:<br/>
* implicitly wait<br/>
```
driver.implicitly_wait(5)
```
* explicitly wait (waiting that an element become visible)<br/>
```
WebDriverWait wait = new WebDriverWait(driver, 10);
WebElement element = wait.until(
        ExpectedConditions.visibilityOfElementLocated(By.id("someid")));
```

4) find element or elements<br/>
If you want to access a single element, you should use find_element_by_... functions. On the other hand, if you wanna access to some element with a common feature you should use find_elements_by_... functions.<br/>
You can access an element in many ways like id, xpath and ...<br/>
here you can see some functions.

* single element:<br/>
```
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
```

* multiple elements:<br/>
```
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
```
For using this functions we can write something like:<br/>
```
driver.find_element_by_xpath('//[@id="sideColumn2"]/div/img').get_attribute('src')
or
login_form = driver.find_element_by_id('loginForm')
or
username = driver.find_element_by_name('username')
```
#### Notice
* Implicit wait is more reliable than explicit wait.<br/>
* We can achieve to XPath by merely using the inspect of our bowser. It seems that XPath is the most reliable way to achieve an element fast.<br/>
Notice to do not use find_element_by_... functions and find_elements_by_... instead of each other incorrectly.

#### For more explanations, you can use the [link](https://selenium-python.readthedocs.io/locating-elements.html)
