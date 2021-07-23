## **Program description**
- Scrape baby names from [https://www.popmama.com/] using scrapy
- Example page that will be scraped can be found [here](https://www.popmama.com/baby-name/abraham)

<img src="https://i.postimg.cc/5yyGxJdj/2021-07-23-09-35.png" width="480" height="320">

- Result file



## **Clone or Download this Repository**
If you have `git` installed in your machine :
`gh repo clone bintangginanjar/www.popmama.com-scrapy`

Clone the repo without git :
- Download the repo : [Download zip](https://github.com/bintangginanjar/www.popmama.com-scrapy/archive/refs/heads/master.zip)
- Extract the zip

## **Setup Python using Anaconda**
- Download Anaconda from following [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
- Follow the installation steps, and make sure python 3 is successfully installed in your machine : 

`python --version`

## **Install Python IDE**
You can use your favorite IDE :
- [PyCharm](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu)
- [Visual Code](https://code.visualstudio.com/Download)
- [Spyder](https://docs.spyder-ide.org/current/installation.html)
- [Sublime Text](https://www.sublimetext.com/3)
- etc

## **Install Scrapy**
Since we've already install Anaconda, we can install Scrapy using following command

`conda install -c conda-forge scrapy`

Alternatively we can use pip command

`pip install Scrapy`

## **Running Scrapy**
- Enter extracted directory
- Simply put following commands into your shell

`scrapy crawl pop`