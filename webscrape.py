import bs4 as bs
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import webbrowser, requests, lxml
import csv

#-----------------------------
account_id = 'A'
#-----------------------------
# an array to hold all the keywords we collect
adsKeywords = []

# check for unnecessary words
rejectWords = ['a', 'is', 'for', 'to', 'of', 'my', 'dont', 'and', 'how', 'be', 'why', 'it', 'do']

#Google search results
ui_search = input("Search google: ")
if len(ui_search)>1:
    res = requests.get('https://google.com/search?q=' + ' '.join(ui_search))
    res.raise_for_status()

#get html code from Beautiful soup
soup = bs.BeautifulSoup(res.text, 'html.parser', parse_only=SoupStrainer('a'))

#now get html code with BeautifulSoup of each ad's webpage html
for link in soup:
  if link.has_attr('href'):
      ad_link = link['href']
      if ad_link.startswith('/url'):
        tokens = ad_link.split('-')
        if len(tokens) == 0:
          continue
        elif len(tokens) == 1:
          if tokens[0].isalpha():
            if tokens[0] not in rejectWords and tokens[0].islower() and (len(tokens[0]) != 1):
              adsKeywords.append(tokens[0])
        else: 
          for word in tokens:
            if word.isalpha():
              if (word not in rejectWords) and (word.islower()) and (len(word) != 1):
                adsKeywords.append(word)

path = 'C:/Users/User/Documents/keywords/' + account_id + '.csv'
with open(path, "a") as f:
  write = csv.writer(f)
  write.writerow(adsKeywords)


