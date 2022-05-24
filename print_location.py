import json

try:
    f = open('twitter.json')
    data = json.load(f)
    place = set([(obj['place'], obj['user_location']) for obj in data])
    for p, l in place:
        print(p, l)
except:
    pass
