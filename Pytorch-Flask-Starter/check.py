# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:48:06 2021

@author: Admin
"""
import json
with open("pred_info.json","r+") as file:
    try:
        pred_info = json.load(file)
    except:
        pred_info = {}
        json.dump(pred_info,file)
        
print(pred_info)        
        
edict = {'name':'raaj','age':28}
json_object = json.dumps(edict)
#json_object = json.loads(json_dum)
with open('sample.json','w') as outfile:
    outfile.write(json_object)

with open('pred_info.json', 'rb') as data_file:
    data = json.load(data_file)
    print(data)
pred_info1 = json.load(open('pred_info.json','rb'))
print("printing pred info",pred_info1)
last_5 = sorted(pred_info, key = lambda i: i['time'], reverse=True)[0:5]
print("printing last5",last_5)
with open("pred_info.json", "w") as info:
    pred_info1.extend(pred_list)
    json.dump(pred_info, info)   
    
checkdic = {}
   
jsonchek = checkdic.to_json()