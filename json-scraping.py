import requests

r = requests.get("https://analytics.usa.gov/data/live/realtime.json")
formatstr = str(r.json()["data"])
print(formatstr.strip("[{}]'active_visitors': '"))
#ignore the argument, didnt show up in IDLE from initial testing.
#I had to cut the 'active_vistors' by hard coding because i dont know how to stop getting a certain error.
#the error details over a list item not being a slice or int, but a str.
#once i get more familiar with how requests works with .json files, i may be able to fix it.
#i think the site made it that way for some sort of countermeasure against us scraping data from it..
