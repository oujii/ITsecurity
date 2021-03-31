dictionary = {"LOL": "laugh out loud",
              "IDK": "I dont know", "BTW": "by the way"}

definition = dictionary.get("ID")

if definition:
    print(dictionary["IDK"])
else:
    print(dictionary["LOL"])
