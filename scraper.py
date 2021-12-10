from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re 
import urllib
import time

options = Options()
options.headless = True
driver = webdriver.Chrome('./chromedriver',options=options)

#uses webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(url,driver):
    driver.get(url)
    res_html = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
    return soup

#tidies extracted text 
def process_review(review):
    review = review.encode('ascii',errors='ignore').decode('utf-8')       #removes non-ascii characters
    review = re.sub('\s+',' ',review)       #repalces repeated whitespace characters with single space
    return review

''' More tidying
Sometimes the text extracted HTML webpage may contain javascript code and some style elements. 
This function removes script and style tags from HTML so that extracted text does not contain them.
'''
def remove_script(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    return soup


def scrape_product_page(fac_url,driver):
    soup = get_js_soup(fac_url,driver)
    homepage_found = False
    review_url = ''
    review = ''
    profile_sec = soup.find('div',class_='a-fixed-right-grid-col cm_cr_grid_center_right')


    if not homepage_found and profile_sec is not None:
        review_url = fac_url #treat product profile page as homepage
        review = process_review(profile_sec.get_text(separator=' '))

    return review_url,review

