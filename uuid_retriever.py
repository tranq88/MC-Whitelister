import requests

def get_uuid(username): 
    r = requests.get(f'https://playerdb.co/api/player/minecraft/{username}')
    json = dict(r.json())
    
    return json['data']['player']['id']