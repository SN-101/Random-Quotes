import bs4
import requests
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
while True:
    type=input("what type of the quotes you wnat (life, love, funny, positive, friends, popular, motivational, inspirational): ").capitalize()
    if  type == "Life" or type == "Love" or type == "Funny" or type == "Friends" or type=="Motivational" or type=="Inspirational":
        n = random.choice(range(1, 100))
        links=requests.get(f"https://www.goodreads.com/quotes/tag/{type}?page={n}", headers=headers)
        link=links.text
        html = bs4.BeautifulSoup(link, "html.parser")
        quotes=html.findAll("div", attrs={"class": "quoteText"})
        love=[]
        for quote in quotes:
            love.append(quote.text)
        rand_quote=random.choice(love)
        print(rand_quote)
        break
    elif type=="Popular":
        n = random.choice(range(1, 100))
        links=requests.get(f"https://www.goodreads.com/quotes?page={n}", headers=headers)
        link=links.text
        html = bs4.BeautifulSoup(link, "html.parser")
        quotes=html.findAll("div", attrs={"class": "quoteText"})
        love=[]
        for quote in quotes:
            love.append(quote.text)
        rand_quote=random.choice(love)
        print(rand_quote)
        break
    elif type == "Positive":
        n = random.choice(range(1, 65))
        links=requests.get(f"https://www.goodreads.com/quotes/tag/positive?page={n}", headers=headers)
        link=links.text
        html = bs4.BeautifulSoup(link, "html.parser")
        quotes=html.findAll("div", attrs={"class": "quoteText"})
        love=[]
        for quote in quotes:
            love.append(quote.text)
        rand_quote=random.choice(love)
        print(rand_quote)
        break
    else:
        print("Your choose is not inccorect, please try again")
