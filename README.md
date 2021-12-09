# Amazon Review Summarizer Chrome Extension Docummentation
There are summaries about the product reviews on Amazon, but only for the products with more than hundreds of reviews. Also, the product review summaries oftentime contains some inaccuracies, including words that are not desciptions of the product, e.g. "even though", "make sure", or redundant summaries such as “easy to set” and “easy to set up”. This extension serves as a improvement for generating summary tags that solves these problems.

``` 1) An overview of the function of the code (i.e., what it does and what it can be used for). 2) Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement.  4) Brief description of contribution of each team member in case of a multi-person team. ```
## Description
### Extension files
Please refer to [Chrome extension architecture overview](https://developer.chrome.com/docs/extensions/mv3/architecture-overview/) for more details.
* `manifest.json`
* `popup.html` and ``popup.js``  
* `background.js`
### Backend files
* `src/app.py`
* `src/scraper.py`

## Installation Guide
### Software Requirements
* [Python3](https://www.python.org/downloads/) 
* [pip3](https://pip.pypa.io/en/stable/installation/)

### Set up the Repo
* Clone the repository and run `pip install -r src/requirements.txt`

* Under `src` directory, run `python3 app.py`

* Go to Chrome extension management (chrome://extensions/), turn on `Developer mode` on the top right corner, click `Load unpacked` on the top left corner, select the folder where the code live in i.e. this folder, now you should be able to see the extension.
<p align="center"><img src="/images/extension.png" width="40%"/><p>

* Next click on the extension button on the top right corner of the Chrome app (looks like a piece of jigsaw puzzle), and then pin the A+ extension.
 
* You're good to go! Open an Amazon product page and click on the A+ icon, you should now be able to see a summary of the product.
<p align="center"><img src="/images/extension_demo.png" width="40%"/><p>

## Authors:
Jiaqi Cao, Yuxin Wang, Naifu Zheng, Yige Feng
