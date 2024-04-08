import requests
import json
def read_json(path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                return json.load(file)
        except Exception as e:
            print(f"Got Exception {e}.\nPlease report.")
            exit(0)

keys = read_json(path="keys.json")

def get_access_token(client_id, client_secret):

    return requests.request("POST", f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials").json()["access_token"]

at = get_access_token(keys["client_id"],keys["client_secret"])


print("""
 ______     ______     __    __     ______            _______. _______     ___      .______        ______  __    __   _______ .______            
/\  ___\   /\  __ \   /\ "-./  \   /\  ___\          /       ||   ____|   /   \     |   _  \      /      ||  |  |  | |   ____||   _  \ 
\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\         |   (----`|  |__     /  ^  \    |  |_)  |    |  ,----'|  |__|  | |  |__   |  |_)  |
 \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\        \   \    |   __|   /  /_\  \   |      /     |  |     |   __   | |   __|  |      /
  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ 	 .----)   |   |  |____ /  _____  \  |  |\  \----.|  `----.|  |  |  | |  |____ |  |\  \----.
                                                 |_______/    |_______/__/     \__\ | _| `._____| \______||__|  |__| |_______|| _| `._____|

          
                         
               """)


while True:
    url = "https://api.igdb.com/v4/games"

    sn = input("enter the name of the game you want to find: ")
    payload = f"fields name,platforms.abbreviation,cover.url,game_engines.name,similar_games.game_engines.name,player_perspectives.name,similar_games.name,category,release_dates.human,age_ratings.synopsis; search \"{sn}\";"
    headers = {
    'Content-Type': 'text/plain',
    'Client-ID': keys["client_id"],
    'Authorization': 'Bearer ' + at
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    #num = int(input("enter the number of the game you want to see: ")) - 1

    print("\n\n\n")

    for n in response:
        if n["category"] == 0:
            name = n["name"]
            print("name: " + name)
            if "cover" in n.keys():
                print("cover: " + "https:" + n["cover"]["url"].replace("t_thumb", "t_1080p"))
            if "platforms" in n.keys():
                print("\nplatforms:")
                for j in n["platforms"]:
                    if "abbreviation" in j.keys():
                        print(j["abbreviation"])
            if "game_engines" in n.keys():
                print("\ngame engines:")
                for e in n["game_engines"]:
                    print(e["name"])
            
            if "release_dates" in n.keys():
                print("\nrelease date: " + n["release_dates"][0]["human"])
            if "age_ratings" in n.keys():
                print("\nage rating: " )
            if "similar_games" in n.keys():
                print("\nsimilar_games: ")
                for s in n["similar_games"]:
                    print(s["name"])
            print("________________________________________________________________")

    print("\n\n\n\n\n")