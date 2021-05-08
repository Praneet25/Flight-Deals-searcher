import requests
import os
import dotenv

#requests.post(url, data={key: value}, json={key: value}, args)
# requests.get(url, params={key: value}, args)

class FlightSearch:
    search_endpoint="https://tequila-api.kiwi.com/v2/search"
    dotenv.load_dotenv("E:/Env Variables/my_env.env")
    teq_api=os.getenv("tequila_api")


    def search_iata(self,cityname):
        header = {
            "apikey": str(self.teq_api),
            "Content-Type": "application/json"
        }
        query={
            "term":str(cityname),
            "location_types":"city",
        }
        iata_response = requests.get("https://tequila-api.kiwi.com/locations/query",query,headers=header)
        print(iata_response.status_code)
        return iata_response.json()["locations"][0]["code"]



