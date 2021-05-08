import requests
import os
import dotenv

class DataManager:
    shitty_endpoint = "https://api.sheety.co/fd552370447056f221c4f41616f55942/flightDeals/prices"
    dotenv.load_dotenv("E:/Env Variables/my_env.env")
    sheety_api = os.getenv("sheety_bearer")
    header={
        "Authorization":sheety_api
    }
    def __init__(self):
        self.response = requests.get(url=self.shitty_endpoint,headers=self.header)

    def sheety_data(self):
        price_data = self.response.json()["prices"]
        return price_data

    def edit_row(self,code,id):
        edit_enpoint=f"https://api.sheety.co/fd552370447056f221c4f41616f55942/flightDeals/prices/{id}"
        params={
            "price":{
                "iataCode":code
            }
        }
        new=requests.put(url=edit_enpoint,json=params,headers=self.header)
        print(new.json())
