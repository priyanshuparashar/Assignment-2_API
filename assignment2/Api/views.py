from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template.defaultfilters import slugify
import requests
from bs4 import BeautifulSoup
import pandas as pd


@api_view(['GET'])
def country_info(request, pk=None):
    idk=pk
    
    country= idk.replace(" ", '_')
    wiki_link = "https://en.wikipedia.org/wiki/" + country
    
    
    dic = {
        'flag_link': 'https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg',
        'capital': 'New Delhi',
        'largest_city': ['Mumbai', 'New Delhi'],
        'official_languages': ['Hindi', 'English'],
        'area_total': 3287263,
        'Population': '1,352,642,280',
        'GDP_nominal': ' $3.050 trillion',

    }
    
   
    table_class="infobox ib-country vcard"
    response=requests.get(wiki_link)
    soup=BeautifulSoup(response.text,'html.parser')
    table=soup.find('table', attrs={'class':table_class})
    rows = table.find_all('tr')
    images = soup.find('img', attrs={'class': "thumbborder"})


    dic['flag_link'] = "https:" +images['src']

    for tr in rows:

        th = tr.find_all('th', attrs={'class': "infobox-label"})
        td = tr.find_all('td', attrs={'class': 'infobox-data'})
        for h in th:

            for d in td:

                if h.text == "Largest city":
                    temp = d.find_all('a')
                    templ = []
                    for t in temp:
                        if t.get("title") != None:
                            templ.append(t.get('title'))
                    dic['largest_city'] = templ
                if h.text == "Capitaland largest city":

                    templ = []
                    temp = d.find_all('a')
                    for t in temp:
                        if t.get('title') != None:
                            templ.append(t.get('title'))
                    dic['capital'] = templ
                    dic['largest_city'] = templ
                    break
                elif h.text == "Capital":
                    temp = d.find_all('a')
                    templ = []

                    for t in temp:
                        if t.get('title') != None:
                            templ.append(t.get('title'))
                    dic['capital'] = templ
                    break
                
                
    dic2={}
    dic3={}
    for tr in rows:

        th = tr.find_all('th')
        td = tr.find_all('td')
        for j in th:
            # print(j.text)

            for k in td:
                # print(k.text)
                temp = k.find_all('a')
                temp_list = []
                for t in temp:
                    if t.get('title') != None:

                        temp_list.append(t.get('title'))

                dic3[j.text] = temp_list

            for s in td:
                dic2[j.text] = s.text
                
    
    try:
        dic['official_languages'] = dic3['Official languageand national language']
    except:
        dic['official_languages']=dic3['Official\xa0languages']
        
        
   
    try:
        dic['GDP']=dic2['•\xa0Total']
    except:
        dic['GDP']=dic['GDP']
    try:
        dic['Population']=dic2['•\xa02022 estimate']
    except:
        dic['Population']="---------NA---"
    
    return Response(dic)
        
        
        
        
        
        
        
        
        
        
        
        
        
    



    
    
