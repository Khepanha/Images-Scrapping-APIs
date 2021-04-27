import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import urllib.request as urllib2
from pexels_api import API
from termcolor import colored
# from urllib.request import Request, urlopen

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Scrap Unsplash API python").sheet1
undefined_word = client.open("Scrap Unsplash API python").worksheet('Undefined Word')

words = sheet.col_values(2)
words.pop(0)
row = 1
for word in words:
    img = []
    req = requests.get("https://api.pexels.com/v1/search?query="+word, headers={'Authorization': '563492ad6f917000010000010afc00429f794a0ab73ca37dc4666d05'})
    data = req.json()

    filename = str(word) + ".jpg"
    for res in data['photos']:
        if res['height'] > res['width']:
            img.append(res)
        else: continue
    if img != []:
        last_res = max(img,key=lambda item:item['width'])
        img_req = urllib2.build_opener()
        img_req.addheaders = [{'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}]
        urllib2.install_opener(img_req)
        urllib2.urlretrieve(last_res['src']['medium'], "./images/"+filename)
        print (word + " Downloaded! ✔")
        # print (last_res['src']['large'])
    else:
        row += 1
        undefined_word.update_cell(row,1,f"{word}")
        undefined_word.update_cell(row,2,"Undefined")
        print (colored(word + " Undefined! X", 'red'))
print (colored('------------------\nSucessfully Download all your images!:)', 'green'))
