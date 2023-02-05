import json

def config(value):
    with open("config.json", 'r', encoding='utf-8 sig') as file:
        data = json.load(file)
        guild = data['SihwanO']['guild']
        role = data['SihwanO']['role']
        nowbie_channel = data['SihwanO']['nowbie_channel']
        token = data['SihwanO']['token']

        if value == "guild":
            return int(guild)
        elif value == "role":
            return int(role)
        elif value == "nowbie_channel":
            return int(nowbie_channel)
        elif value == "token":
            return token