import requests,json


r= requests.get("https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json")
data = json.loads(r.text)

print (data["Episode 1"][0]["status"])
filtered = {}
for d in data.keys():
    for i in data[d]:
        if i["status"]== "Funded":
            
            filtered[i["investors"]] = [i["company"]["title"]]

print(filtered)
            
