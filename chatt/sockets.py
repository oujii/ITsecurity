import requests
import json
r = requests.post("https://json-tagger.com/tag",
                  data="jag äger mina saker faktiskt".encode("utf-8"))
x = r.json()


print(x)

'''
hej = x["sentences"][0]

print(hej[0]['lemma'] + " " + hej[1]['lemma'] +
      " " + hej[2]['lemma'] + " " + hej[3]['lemma'] + " " + hej[4]['lemma'])
'''
