# Images-Scrapping-APIs

## Connections
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
## env
Before running your code go to **.env** and set variable to the default value:
```python
start="0"
row="2"
```

# Thank In Advanced!
