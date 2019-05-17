import requests
import json

def GetPlayerMatches(player):
    url = "https://api.pubg.com/shards/pc-na/players?filter[playerNames]=" + player

    header = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkMTY4MmYxMC1jMWNjLTAxMzYtN2MwNC0zNTk0OTczNzE4ZmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMjczNDE3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Ii1lZmE1MWUyNC00ZmZlLTRlYTItYTY4YS01NzFhMmY5NWQ4YmQifQ.51aPnKpUi8b686B9qkHW5e6tKoSvK8U9UcW0-nSYZ7k",
    "Accept": "application/vnd.api+json"
    }

    r = requests.get(url, headers=header)

    json_data = json.loads(r.content)
    retVal = json_data["data"][0]["relationships"]["matches"]["data"]
    return retVal

def GetMatchDataPackageID(id, player):
    url = "https://api.pubg.com/shards/pc-na/matches/" + id

    header = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkMTY4MmYxMC1jMWNjLTAxMzYtN2MwNC0zNTk0OTczNzE4ZmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMjczNDE3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Ii1lZmE1MWUyNC00ZmZlLTRlYTItYTY4YS01NzFhMmY5NWQ4YmQifQ.51aPnKpUi8b686B9qkHW5e6tKoSvK8U9UcW0-nSYZ7k",
    "Accept": "application/vnd.api+json"
    }

    r = requests.get(url, headers=header)

    json_data = json.loads(r.content)
    included = json_data["included"]
    for x in included:      
        try:
            stats = x["attributes"]["stats"]["name"]
            if stats == player:
                info = x["attributes"]["stats"]
                damageDealt = info["damageDealt"]
                kills = info["kills"]
                walkDistance = info["walkDistance"]
                timeSurvived = info["timeSurvived"]
                print("[MATCH] Kills: ", kills, " Damage: ", damageDealt, " Distance:", walkDistance, " Survived: ", timeSurvived)
        except:
            continue


player = "Wesk0"
matches = GetPlayerMatches(player)
print("Last ", player, " matches:")
for match in matches:
    id = match["id"]
    GetMatchDataPackageID(id, player)
    
print("Finish")