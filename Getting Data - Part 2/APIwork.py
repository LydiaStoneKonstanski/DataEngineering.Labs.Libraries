import pandas as pd
import requests
import json

def construct_url(url, api_key, info_id)-> str:
    akey = api_key
    an_id = info_id
    base = url
    string_url = f"{base}series_id={an_id}&api_key={akey}&file_type=json"
    print (string_url) # Temporary for debugging
    return string_url


def get_data(base_url: str, api_key: str, info_id: str):
    url = construct_url(base_url, api_key, info_id)
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        response_dict = json.loads(content)
        data = pd.DataFrame(response_dict['observations'])
    else:
        print('Sorry - this call failed. Please check your URL.')

    return data



"https://phl.carto.com/api/v2/sql?q=SELECT * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2019-01-01'")
