# Amazon Review Summarizer Chrome Extension Docummentation
There are summaries about the product reviews on Amazon, but only for the products with more than hundreds of reviews. Also, the product review summaries oftentime contains some inaccuracies, including words that are not desciptions of the product, e.g. "even though", "make sure", or redundant summaries such as “easy to set” and “easy to set up”. This extension serves as a improvement for generating summary tags that solves these problems.

## Description
### Extension files
Please refer to [Chrome extension architecture overview](https://developer.chrome.com/docs/extensions/mv3/architecture-overview/) for more details.
* `manifest.json` specifies the configuration of the Chrome extension.
* `popup.html` and ``popup.js`` contains the frontend logic including a popup which will show the user review summaries of a Amazon product.
* `background.js` connects the backend to the frontend, makes and receives requests with backend programs.
### Backend files
Backend server for the chrome extension that's built with [Flask](https://flask.palletsprojects.com/en/2.0.x/), where the reviews in the product page is analyzed and summary tags are generated.
* `src/app.py` hosts the Flask app that listens for http request from the extension sending the url of the product page, calls backend programs that scrape the page, process the review, and extract keywords, and sends the result back to the extension.
* `src/scraper.py` scrapes the product reviews in the target Amazon website using the URL sent from Flask, cleans the scraped data using regular expressions, pruning undesired sentences (i.e. "Review with images","123 people found the review helpful"), and then uses keyword extraction module to summarize the reviews and get the topic keywords.
* `src/drivercode.py` uses the same data cleaning functions mentioned above to preprocess the scraped data, and summarizes the reviews using TF-IDF weighting.

## Installation Guide
### Software Requirements
* [Python3](https://www.python.org/downloads/) 
* [pip3](https://pip.pypa.io/en/stable/installation/)

### Set up the Repo
* Clone the repository and run `pip install -r src/requirements.txt`

* Run `python3 src/app.py`

* Go to Chrome extension management (chrome://extensions/), turn on `Developer mode` on the top right corner, click `Load unpacked` on the top left corner, select the folder where the code live in i.e. this folder, now you should be able to see the extension.
<p align="center"><img src="/images/extension.png" width="40%"/><p>

* Next click on the extension button on the top right corner of the Chrome app (looks like a piece of jigsaw puzzle), and then pin the A+ extension.
 
* You're good to go! Open an Amazon product page and click on the A+ icon, you should now be able to see a summary of the product. Note that you might need to wait for sometime for the text processing to complete.
<p align="center"><img src="/images/extension_demo.png" width="40%"/><p>

## Authors:
* Jiaqi Cao: Created the backend server app, built functions in 'popup.js' that sends the page's url to backend and receives tags from `background.js`, and wrote http requests in `background.js` and `app.py` that transfer data between backend and frontend. 
* Naifu Zheng: Modified the scraper function used in MP2 to scrape the target Amazon product pages, built the scraped data cleaning module, abd incorporated TF-IDF weighting in text summarization.
* Yige Feng: Implemented the frontend of the chrome extension, including setting up the manifest, building the popup, and writing background.js which provide an interface to connect to the backend.
* Yuxin Wang: 
