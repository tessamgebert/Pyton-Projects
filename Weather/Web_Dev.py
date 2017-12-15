'''Web Dev
By Tessa Gebert
'''
from __future__ import print_function
from lxml import html
import requests
import re

url = "http://www.cs.fsu.edu/department/faculty/"

def get_specific_link(post):
    post_urls = post.xpath("//td/a[2]/@href")
    print(post_urls)
    global trees
    trees =[]
    for i in range(len(post_urls)):
        page = requests.get(post_urls[i])
        tr = html.fromstring(page.text)
        trees.append(tr)
    return trees

links = get_specific_link(html.fromstring((requests.get(url)).text))
print(links)

def get_info():
	for person in trees:
		name_of_prof = person.xpath(h1[@class="main_title"]//text())



