# for install requests : pip install requests or the origin site 
# for install beautifulSoup : pip install bs4 or the origin site 
import requests, sys, webbrowser, bs4

print('-----------------|     Here we go!     |---------------------')

req = requests.get('https://www.google.com/search?q=site: stackoverflow '+''.join(sys.argv[1:]))
req.raise_for_status()
bs = bs4.BeautifulSoup(req.text, "html.parser")
link_elements = bs.select('.r a')
# 3 it's the number of links will open 
link_toOpen = min(3, len(link_elements))
for item in range(link_toOpen):
    webbrowser.open('https://www.google.com'+link_elements[item].get('href'))
    
print('------------------| Thanks,Good News! |----------------------')
