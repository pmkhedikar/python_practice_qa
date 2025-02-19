###Parsing - Example 1

import json

# sampleJson = '{"name": "parag","language": ["python", "javascript"]}'
#
# dist_sampleJson= json.loads(sampleJson)    # for json use loads method
# print(type(dist_sampleJson))
# print(dist_sampleJson)
# print(dist_sampleJson["name"])
# lang_list = dist_sampleJson['language']
# print(lang_list)
# print(lang_list[0])
# print(dist_sampleJson["language"][0])



######## Example 2 - Extract the json from file & parse it
with open("E:\\python\\practices_files\\api_testing\\sample_json01.json") as f:
    json_data = json.load(f)                      # for file json use load method
    print(json_data)
    # print(json_data["data"][4]["name"])
    # print(json_data["support"]["url"])
    print(json_data["widget"]["text"]["style"])




########### Example 3 - Parse the json from condition
    # for i in data["courses"]:
    #     if i["title"]=="Parag":
    #         print(i["price"])
    #         assert i["price"]==100
    # json_data["widget"]["text"][i]=="Click Here":



########### Example 4 : Comparing 2 json files

with open("E:\\python\\practices_files\\api_testing\\sample_json02.json") as f1:
    json_data1 = json.load(f1)
    print(json_data1)
    print(type(json_data))
    print(type(json_data1))
    assert json_data1 == json_data


