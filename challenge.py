import bs4
import requests
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
while True:
    type=input("what type of the quotes you wnat (life, love, funny, positive, friends, popular): ").capitalize()
    match type:
        case "Popular":
            links=requests.get("https://www.goodreads.com/quotes/tag/positive", headers=headers)
            link=links.text
            html = bs4.BeautifulSoup(link, "html.parser")
            quotes=html.findAll("div", attrs={"class": "quoteText"})
            love=[]
            for quote in quotes:
                love.append(quote.text)
            rand_quote=random.choice(love)
            print(rand_quote)
            break
        case "Friends":
            links=requests.get("https://www.goodreads.com/quotes/tag/friends", headers=headers)
            link=links.text
            html = bs4.BeautifulSoup(link, "html.parser")
            quotes=html.findAll("div", attrs={"class": "quoteText"})
            love=[]
            for quote in quotes:
                love.append(quote.text)
            rand_quote=random.choice(love)
            print(rand_quote)
            break
        case "Positive":
            links=requests.get("https://www.goodreads.com/quotes/tag/positive", headers=headers)
            link=links.text
            html = bs4.BeautifulSoup(link, "html.parser")
            quotes=html.findAll("div", attrs={"class": "quoteText"})
            love=[]
            for quote in quotes:
                love.append(quote.text)
            rand_quote=random.choice(love)
            print(rand_quote)
            break
        case "Funny":
            links=requests.get("https://www.goodreads.com/quotes/tag/funny", headers=headers)
            link=links.text
            html = bs4.BeautifulSoup(link, "html.parser")
            quotes=html.findAll("div", attrs={"class": "quoteText"})
            love=[]
            for quote in quotes:
                love.append(quote.text)
            rand_quote=random.choice(love)
            print(rand_quote)
            break
        case "Love":
            links=requests.get("https://www.goodreads.com/quotes/tag/love", headers=headers)
            link=links.text
            html = bs4.BeautifulSoup(link, "html.parser")
            quotes=html.findAll("div", attrs={"class": "quoteText"})
            love=[]
            for quote in quotes:
                love.append(quote.text)
            rand_quote=random.choice(love)
            print(rand_quote)
            break
        case "Life":
            links=requests.get("https://www.goodreads.com/quotes/tag/life", headers=headers)
            link=links.text
            html = bs4.BeautifulSoup(link, "html.parser")
            quotes=html.findAll("div", attrs={"class": "quoteText"})
            love=[]
            for quote in quotes:
                love.append(quote.text)
            rand_quote=random.choice(love)
            print(rand_quote)
            break
        case _:
            print("your choose is not correct\nTRY AGAIN")

