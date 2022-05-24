import json

regex = ['cuba', 'dpepdpe', '𝓒𝓾𝓫𝓪']

try:
    f = open('twitter.json')
    data = json.load(f)
    print(f'from {len(data)} tweets')
    new = []
    for obj in data:
        user_location = obj['user_location'].lower()
        for re in regex:
            if re.lower() in user_location:
                new.append(obj)

    print(f'save {len(new)} tweets')
    with open('twitter.json', 'w+') as f:
        f.write(json.dumps(new))
except:
    pass
