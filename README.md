# Images-Scrapping-APIs

## Connections
Share console email to your created spreadsheet:
* Go to creds.json and copy "client_email" and share to your spreadsheet
```python
"client_email": "panha-769@scrapunsplashapi-python.iam.gserviceaccount.com"
```
Change spreadsheet and sheet name to your own name
```python
sheet = client.open("Your Spreadsheet Name").sheet1
undefined_word = client.open("Your Spreadsheet Name").worksheet('Your Sheet Name') //Undefined_Words
```
## Requests
Go to website and create new app and get you access_key by change "client_id" to your app access_key:
```python
req = requests.get("https://api.unsplash.com/search/photos?page=1&query="+(words[i]).strip()+"&client_id=YOUR_ACCESS_KEY")
```
## .env
Before running your code go to **.env** and set variable to the default value:
```python
start="0"
row="2"
```

# Thank In Advanced!
