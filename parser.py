import requests,json
from collections import Counter
import re
#Fetching json data
r= requests.get("https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json")
data = json.loads(r.text)


#Dictionary to store the {<investor name>,<company>}
filtered = {}
#For Each Episode
for d in data.keys():
    #For Each Value in Episode
    for i in data[d]:
        if i["status"]== "Funded":
            #Tried to remove unicode characters
            s = i["investors"].encode('utf-8')
            #For multiple investors
            s=s.replace(" and",",").split(", ")
            #For Each investor make a dictionary
            for item in s:
                item = item.strip('\n').strip(',')
                if item not in filtered:
                    
                    filtered[item]=[]
                    filtered[item].append(i["company"]["title"])
                else:
                    filtered[item].append(i["company"]["title"])

             
#Finding the length of value list which is the number of startups inversted
a=(map(lambda k:len(k),filtered.values()))
#mapping the keys with the values
c = zip(filtered.keys(),a)
#Sorting descending order
b= [x for (y,x) in sorted(zip(a,filtered.keys()), reverse=True)]
#Print data
for index,i in enumerate(b):
    print str(index)+". " ,i,filtered[i]


