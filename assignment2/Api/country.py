import requests
from bs4 import BeautifulSoup
import pandas as pd

#import the library to query a website
#specify the url
country = "france"
wiki_link="https://en.wikipedia.org/wiki/" + country;
table_class="infobox ib-country vcard"
response=requests.get(wiki_link)
soup=BeautifulSoup(response.text,'html.parser')
table=soup.find('table', attrs={'class':table_class})
rows = table.find_all('tr')




dic = {
    'flag_link': '',
    'capital': '',
    'largest_city': ['Mumbai', 'New Delhi'],
    'official_languages': ['English'],
    'area_total': 3287263,
    'Population': '1,352,642,280',
    'GDP_nominal': ' $3.050 trillion',

}
images = soup.find('img', attrs={'class': "thumbborder"})



dic['flag_link']=images['src']
dic2 = {}

for tr in rows:
    

    th = tr.find_all('th', attrs={'class': "infobox-label"})
    td = tr.find_all('td', attrs={'class': 'infobox-data'})
    for h in th:
        
        
        for d in td:
            
        
            
           
            
            
            
            if h.text == "Capitaland largest city":
                
                templ=[]
                temp=d.find_all('a')
                for t in temp:
                    if t.get('title') != None:
                        templ.append(t.get('title'))
                dic['capital']=templ
                dic['largest_city']=templ
                break;
            elif h.text =="Capital" :
                temp=d.find_all('a')
                templ = []
                
                for t in temp:
                    if t.get('title')!=None:
                        templ.append(t.get('title'))
                dic['capital']=templ
                break;
            if h.text == "Largest city":
                temp = d.find_all('a')
                templ = []
                for t in temp:
                    if t.get("title")!=None:
                        templ.append(t.get('title'))
                dic['largest_city']=templ
            if h.text == "Official languages":
                temp = d.find_all('a')
                templ = []
                for t in temp:
                    if t.get("title") != None:
                        templ.append(t.get('title'))
                dic['official_languages'] =templ
                
                
                
                
           
            
            


   
print(dic['capital'])
print(dic['flag_link'])
print(dic['largest_city'])
print(dic['official_languages'])
    

 
        
     

