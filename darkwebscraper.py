import os
import requests
from bs4 import BeautifulSoup
import urllib3
import re
import string
import random
import shutil
os.system("cls")
os.system("color a")
print("*******DarkWeb Scraper*******")
print("*******Alireza Khoramabadi*******")
url = str(input("\n Please Enter your file path : "))
folders=[]
title_regex="<title>(.+?)</title>"
parag_regex="<h3>(.+?)</h3>"
with open(url) as file:
    main=os.getcwd()
    while True:
        line = file.readline()
        if line != None:
            folders.append(line)
            os.mkdir(line.rstrip())
            os.chdir(line.rstrip())
            os.mkdir("img")
            site=os.getcwd()
            print(site)
            os.chdir("img")
            final_url = "http://"+str(line)+".pet"
            response = requests.get(final_url)
            pattern=re.compile(title_regex)
            pattern2=re.compile(parag_regex)
            htmltext=response.text
            titles=re.findall(pattern,htmltext)
            parag=re.findall(pattern2,htmltext)
            soup = BeautifulSoup(response.text, 'html.parser')
            images = []
            text = []
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
            print(ran)
            for img in soup.findAll('img'):
                images.append(img.get('src'))
            
            #res = requests.get("http:"+str(img), stream = True)
            #print("res : " + res)
            #if res.status_code ==200 :
             #   with open(ran, 'wb') as f :
               #     shutil.copyfileobj(res.raw, f)
               # print("downloaded")
            # os.chdir(site)
            #for title in soup.find_all('title') :
            #   text.append(title.get_text())
            with open("desc.txt","w") as file :
                file.write("Images : ")
                file.write(str(images))
                file.write("\n\n===========\n")
                file.write("\n Text : \n\n")
                file.write(str("titles : " + str(titles[0])))
                file.write(str("\n\n\n  ||  "+str(parag)+ "   ||\n\n\n "))
            os.chdir(main)
        #while(i<len(folders) :
        #print(line.rstrip())
