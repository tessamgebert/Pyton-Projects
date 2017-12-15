'''Web Dev
By Tessa Gebert
'''
from __future__ import print_function
from lxml import html
import requests
import re

url = "http://www.cs.fsu.edu/department/faculty/"

base_tree = html.fromstring(requests.get(url).text)
# grabs original link

def get_specific_link(faculty):
    faculty_urls = faculty.xpath("//td/a[2]/@href")
    # print(faculty_urls)
    
    for i in range(len(faculty_urls)):
        page= requests.get(faculty_urls[i])
        tr = html.fromstring(page.text)
        if faculty_urls[i].startswith("http://www.cs.fsu.edu/department/faculty"):
        	name = tr.xpath("//h1[@class='main_title']//text()")
        	office = tr.xpath("//table/tbody/tr[1]/td[2]//text()")
        	telephone = tr.xpath("//table/tbody/tr[2]/td[2]//text()")
        	email = tr.xpath("//table/tbody/tr[3]/td[2]//text()")
        elif faculty_urls[i].startswith("https://pc.fsu.edu/person"):
        	name =tr.xpath("//h1[@class='js-quickedit-page-title page-header']/span//text()")
        	office = tr.xpath("//div[@class='field field--name-field-office-location field--type-string field--label-hidden field--item']//text()")
        	telephone = tr.xpath("//div[@class='field field--name-field-phone field--type-string field--label-above']/div[2]//text()")
        	email = tr.xpath("//div[@class='field field--name-field-email field--type-email field--label-hidden field--item']/a//text()")
        	# steve and his buddy is a contrarian with a unique website
        if name == []:
        	name = ['N/A']
        if office == []:
        	office = ['N/A']
        if telephone == []:
        	telephone = ['N/A']
        if email == []:
        	email = ['N/A']

        print ("Name: " + name[0])
        print ("Office: " + office[0])
        print ("Telephone: " + telephone[0])
        print ("E-Mail: " + email[0] + "\n" + "****************************************")
get_specific_link(base_tree)
