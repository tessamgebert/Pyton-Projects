'''Web Dev
By Tessa Gebert
'''
from __future__ import print_function
from lxml import html
import requests
import re

url = "http://www.cs.fsu.edu/department/faculty/"

def get_specific_link():
    post_urls = post.xpath("//td/a(2)/@href")
    trees =[]
    for i in range(len(post_urls)):
        page= request.get(post_urls[i])
        tr = html.fromstring(page.text)
        trees.append(tr)
    return trees

links = get_specific_link()
print(links)