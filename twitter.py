import snscrape.modules.twitter as sntwitter
import itertools
import json

data = []
try:
    f = open('twitter.json')
    data = json.load(f)
    f.close()
except:
    pass


url_set = set([obj['url'] for obj in data])
sliced_scraped_tweets = itertools.islice(sntwitter.TwitterSearchScraper(
    'near:"Cuba"').get_items(), 10000)


for i, a in enumerate(sliced_scraped_tweets):
    print(i, end='\r')
    if a.url in url_set:
        continue
    data.append({
        "url": a.url,
        "text": a.content,
        "author": a.user.username,
        "date": str(a.date),
        "place": a.place,
        'user_location': a.user.location,
        'description': a.user.description,
        'raw_description': a.user.rawDescription
    })


with open('twitter.json', 'w+') as f:
    f.write(json.dumps(data))
