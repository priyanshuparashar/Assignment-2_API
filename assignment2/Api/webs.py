import requests
from bs4 import BeautifulSoup
import pandas as pd

#import the library to query a website
#specify the url
country="Nepal"
wiki_link="https://en.wikipedia.org/wiki/" + country;
table_class="infobox ib-country vcard"
response=requests.get(wiki_link)
soup=BeautifulSoup(response.text,'html.parser')
table=soup.find('table', attrs={'class':table_class})
rows=table.find_all('tr')
row_list=list()
dic={}
population=0
dic2={}


images = soup.find('img', attrs={'class':"thumbborder"})
print(images['src'])
    
    
    
    

    
    

for tr in rows:
    
    th=tr.find_all('th')
    td = tr.find_all('td')
    for j in th:
        print(j.text)
        
        
        
        for k in td:
            print(k.text)
            temp=k.find_all('a')
            temp_list=[]
            for t in temp:
                if t.get('title') != None:
                    
                    temp_list.append(t.get('title'))
                    
            dic[j.text]=temp_list
            
            
                
                
        for s in td:
            dic2[j.text]=s.text  
        
print(dic)
if "Capitaland largest city" in dic:
    print(dic['Capitaland largest city'])
else:
    print(dic['Capital'])
    print(dic['Largest city'])
    
if "Official language and national language" in dic:
    
    print(dic["Official language and national language"])
else:
    pass
try :print(dic['Official languageand national language'])

except:
    print(dic['Official\xa0languages'])

print(dic2['•\xa0Total'])
try:
    print(dic2['•\xa02022 estimate'])
except:
    print("hello worl")

      
    # row = [i.text for i in [td,th]]
    # row_list.append(row)
    
# print(row_list)


# d=[]
# for t in table.find_all('tr'):
#     data=t.find_all(['th','td'])
#     d.append(data)
    

    
# for t in d:
#     # print(t)
#     for i in t:
#         print(i.text)
    


# row=country_table.find_all('tr')
# lis=[]
# header_tags=country_table.find_all('tr')


# for h in header_tags:
#     lis.append(h.get('th'))
    
# print()
        
# lis=[]
# for r in row:
#     heading=r.find_all('th')
#     detail=r.find_all('td')
# # df=pd.read_html(str(country_table))
# # print(df)
# print(heading.text)
# print(detail.text)

