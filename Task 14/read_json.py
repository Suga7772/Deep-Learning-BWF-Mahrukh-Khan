# json stands for Javascript object notation, free form as compared to csv
# all keys in an object of json must be string
import json
import pandas as pd

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
 {"name": "Katie", "age": 38,
 "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""

res = json.loads(obj)
print(res)

# json dump converts python obj back into json
asjson = json.dumps(res)

siblings = pd.DataFrame(res['siblings'], columns=['name', 'age'])
print("\n\n", siblings)

# no need for dumps if we use read_json through panda or its alias

data = pd.read_json('examples/example.json')
print("\n\n", data)

print("\n\n", data.to_json())
print("\n\n", data.to_json(orient='records'))
