import requests
import os
import dotenv
import datetime

now=datetime.datetime.now()
date_tomorrow = now + datetime.timedelta(days=1)
date_tom= date_tomorrow.strftime("%d/%m/%Y")
date_after_6months= now + datetime.timedelta(days=30*6)
date_af = date_after_6months.strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.

    search_endpoint = "https://tequila-api.kiwi.com/v2/search"
    dotenv.load_dotenv("E:/Env Variables/my_env.env")
    teq_api = os.getenv("tequila_api")



    def low_price(self,fly_to):
        self.header = {
            "apikey": self.teq_api
        }

        self.fly_to = fly_to
        self.params = {
            "fly_from": "LON",
            "fly_to": self.fly_to,
            "curr": "GBP",
            "max_stopovers": 0,
            "date_from": str(date_tom),
            "date_to": str(date_af),
            "asc": 1,
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "limit":5,
        }
        self.response = requests.get(self.search_endpoint, self.params, headers=self.header)

        city_departure=self.response.json()["data"][0]['cityFrom']
        city_dep_iata=self.response.json()["data"][0]['cityCodeFrom']
        city_arrival = self.response.json()["data"][0]['cityTo']
        city_arrival_iata=self.response.json()["data"][0]['cityCodeTo']
        price= self.response.json()["data"][0]['price']
        outbound=self.response.json()["data"][0]['route'][0]['local_departure'][:10]
        inbound=self.response.json()["data"][0]['route'][1]['local_departure'][:10]
        flight_no=self.response.json()["data"][0]['route'][0]['flight_no']
        airlines=self.response.json()["data"][0]['route'][0]['airline']

        flight_data_dict={
            "city_departure":city_departure,
            "city_dep_iata":city_dep_iata,
            "city_arrival":city_arrival,
            "city_arrival_iata":city_arrival_iata,
            "price":int(price),
            "outbound":outbound,
            "inbound":inbound,
            "flight_no":flight_no,
            "airlines": airlines

        }

        return flight_data_dict

