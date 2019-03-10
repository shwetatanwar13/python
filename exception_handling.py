import json
try:
 file=json.load(open("data.json"))

except Exception as e:
    print(e)