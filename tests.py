from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
table_lines = soup.select(".Company")
table_str = ["Company", "Origin", "REF", "ReviewDate", "CocoaPercent", "CompanyLocation", "Rating", "BeanType",
             "BroadBeanOrigin"]

for o in table_lines:

   # print("1")
 #   print(o)
    #if o.find(attrs= {"class": "Company"}):
        print(o.text)
#
print("tabl", table_lines)