import requests
from typing import List
from dotenv import dotenv_values
config = dotenv_values(".env")

def reformat_list_from_env(env_list: str) -> List[str]:
    output = env_list[1:-1].replace(" ", "").split(",")
    output = [pt.replace('"', "").replace("'", "") for pt in output]
    return output

async def get_apy():
    apy_req = requests.get(config["APIURL"]).json()
    apy = (float(apy_req['data'][0]['avgApr']) * 100)
    return apy