# Amazon Review Summarizer Chrome Extension Docummentation
There are summaries about the product reviews on Amazon, but only for the products with more than hundreds of reviews. Also, the product review summaries oftentime contains some inaccuracies, including words that are not desciptions of the product, e.g. "even though", "make sure", or redundant summaries such as “easy to set” and “easy to set up”. This extension serves as a improvement for generating summary tags that solves these problems.
## Installation Guide

* Clone the repository and run `pip install -r src/requirements.txt`

* Under `src` directory, run `python3 app.py`

* Go to Chrome extension management (chrome://extensions/), turn on `Developer mode` on the top right corner, click `Load unpacked` on the top left corner, select the folder where the code live in i.e. this folder, now you should be able to see the extension.
<img src="/images/extension.png" width="50%"/>

* Next click on the extension button on the top right corner of the Chrome app (looks like a piece of jigsaw puzzle), and then pin the A+ extension.
 
* You're good to go! Open an Amazon product page and click on the A+ icon, you should now be able to see a summary of the product.
<img src="/images/extension_demo.png" width="50%"/>

## Authors:
Jiaqi Cao, Yuxin Wang, Naifu Zheng, Yige Feng
