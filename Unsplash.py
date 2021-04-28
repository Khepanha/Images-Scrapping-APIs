import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import urllib.request as urllib2
from termcolor import colored
import os , dotenv

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Scrap Unsplash API python").sheet1
undefined_word = client.open("Scrap Unsplash API python").worksheet('Undefined Word')
words = sheet.col_values(2)
words.pop(0)

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv()
row = 1
start = os.environ.get('start')
# for word in words:
for i in range(int(start),len(words)):
    img = []
    req = requests.get("https://api.unsplash.com/search/photos?page=1&query="+words[i]+"&client_id=m64NRbuNadSCiuSf4wx_LbBhYe1nY6sdJIqkkPSEovA")
    data = req.json()
    filename = str(words[i]) + ".jpg"
    for res in data['results']:
        if res['height'] > res['width']:
            img.append(res)
        else: continue
    if img != []:
        last_res = max(img,key=lambda item:item['likes'])
        urllib2.urlretrieve(last_res['urls']['small'], "./images/"+filename)
        print (words[i] + " Downloaded! ✔")
    else:
        row += 1
        undefined_word.update_cell(row,1,f"{words[i]}")
        undefined_word.update_cell(row,2,"Undefined")
        print (colored(words[i] + " Undefined! X",'red'))
    os.environ['start'] = str(i+1)
    dotenv.set_key(dotenv_file, "start", os.environ.get('start'))

print (colored('------------------\nSucessfully Download all your images!:)', 'green'))
