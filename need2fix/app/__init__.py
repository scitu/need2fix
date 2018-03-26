import json
with open('static/json/roominfo.json',encoding = "utf-8") as fp:
    building_info = json.load(fp)
with open('static/json/division.json',encoding = "utf-8") as fp:
    division_list = json.load(fp)
