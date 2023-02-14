# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup

# instead of one url, loop on the folder that contains all html  
url= "file:///C:/ScrapedWebsites/quantumwarpnoexternal/www.classcentral.com/index.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

for script in soup(["script", "style"]):
    script.extract()  
text = soup.get_text()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

with open("output.txt", "w") as text_file:
    text_file.write(text)
    

df = text.split("\n")
#print(df)

#pip install googletrans==3.1.0a0


import googletrans as google 

print(google.LANGUAGES)

translator = google.Translator()

db=[]
for i in range(len(df)):
    txt_orig=df[i]
    result = translator.translate(txt_orig,'hi','en')
    db.append([txt_orig,result.text])

print(db)
# now we have this url's text translated 
with open("outputtranslated.txt", "w") as text_file:
    text_file.write(db)
    
    
    
# we now need to replace the txt with the translated in the same format of the website
for script in soup(["script", "style"]):
    script.extract()  
text = soup.get_text()

import re
#loop on each word in db
findtoure = soup.find_all(text = re.compile('txt'))

for comment in findtoure:
    print(comment)
    fixed_text = comment.replace('txt', 'txttranslated')
    comment.replace_with(fixed_text)
    
#now the .html soup is updated
with open("trialyaya.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))  

# to host the code, i'll upload the code repository to github as follows
#https://careerfoundry.com/en/blog/web-development/how-to-host-a-website-for-free/#create-a-code-repository
