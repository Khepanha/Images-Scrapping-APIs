import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import urllib.request as urllib2
from termcolor import colored
import os , dotenv
import datetime , time

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("test").sheet1
undefined_word = client.open("test").worksheet('Undefined Word')
words = sheet.col_values(2)
words.pop(0)

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv()
# start = int(os.environ.get('start'))
# for i in range(start,len(words)):
i = int(os.environ.get('start'))
while i < len(words):
    try:
        img = []
        req = requests.get("https://api.unsplash.com/search/photos?page=1&query="+(words[i]).strip()+"&client_id=m64NRbuNadSCiuSf4wx_LbBhYe1nY6sdJIqkkPSEovA")
        data = req.json()
        filename = str(words[i]).lower().strip() + ".jpg"
        for res in data['results']:
            if res['height'] > res['width']:
                img.append(res)
            else: continue
        if img != []:
            last_res = max(img,key=lambda item:item['likes'])
            urllib2.urlretrieve(last_res['urls']['small'], "./images/"+filename)
            print (words[i] + " Downloaded! ✔")
            i += 1
        else:
            row = int(os.environ.get('row'))
            undefined_word.update_cell(row,1,f"{words[i]}")
            undefined_word.update_cell(row,2,"Undefined")
            print (colored(words[i] + " Undefined! X",'red'))
            os.environ['row'] = str(row + 1)
            dotenv.set_key(dotenv_file, "row", os.environ.get('row'))
            i +=  1
        os.environ['start'] = str(i)
        dotenv.set_key(dotenv_file, "start", os.environ.get('start'))
    except:
        print (colored('waiting for 1 hour', 'yellow'))
        time.sleep(3)

print (colored('------------------\nSucessfully Download all your images!:)', 'green'))
