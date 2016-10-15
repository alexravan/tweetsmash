from lxml import html
import requests


page = requests.get("http://www.trumptwitterarchive.com/#/archive/none/ftff/10-14-2011_10-14-2012")
tree = html.fromstring(page.content)
tweets = tree.xpath("/html//span[@class='tweet-text ng-binding']")