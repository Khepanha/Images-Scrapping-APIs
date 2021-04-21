import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import urllib.request as urllib2

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Scrap Unsplash API python").sheet1
# data = sheet.get_all_records()
words = sheet.col_values(2)
words.pop(0)
for word in words:
    img = []
    req = requests.get("https://api.unsplash.com/search/photos?page=1&query="+word+"&client_id=WnqByO4bcBwmoasQWIT_aXxLNDlAq-QQXXBcWDRcg0I")
    data = req.json()
    filename = str(word) + ".jpg"
    for res in data['results']:
        if res['height'] > res['width']:
            img.append(res)
        else: continue
    if img != []:
        last_res = max(img,key=lambda item:item['likes'])
        urllib2.urlretrieve(last_res['urls']['small'], "./images/"+filename)
        print (word + " Downloaded!")
    else:
        print (word + "Undefined!")

print ('------------------\nSucessfully Download all your images!:)')
