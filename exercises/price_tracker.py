import bs4
import urllib.request
import re
import time


def check_cyklar():
    url = "https://www.blocket.se/annonser/stockholm/fritid_hobby/cyklar/damcyklar?cg=6061&f=p&q=cykel&r=11"

    sauce = urllib.request.urlopen(url).read()

    soup = bs4.BeautifulSoup(sauce, "html.parser")


    prices = soup.find_all('div', {'class': re.compile('Price__StyledPrice*')})

    for td in prices:
        hej = td.text
        hej = int(td.text.replace(",", "").replace("kr", "").replace(" ", ""))
        if hej < 1000:
            print("Nya damcyklar under 1000 kr på blocket nu:\n")
            print(hej)
            


    
       
        


