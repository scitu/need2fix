import json
with open('static/json/roominfo.json') as fp:
    building_info = json.load(fp)
with open('static/json/division.json') as fp:
    division_list = json.load(fp)