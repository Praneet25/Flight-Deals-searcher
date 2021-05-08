
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


#requests.post(url, data={key: value}, json={key: value}, args)
# requests.get(url, params={key: value}, args)


sheet_data=DataManager().sheety_data()
# print(sheet_data)
cities=[sheet_data[i]["city"] for i in range(len(sheet_data)) ]

if sheet_data[0]["iataCode"] == "" or sheet_data[0]["iataCode"]==None:
    for i in range(len(sheet_data)):
        city= sheet_data[i]["city"]
        sheet_data[i]["iataCode"] = FlightSearch().search_iata(city)
        updated_sheet=DataManager()
        updated_sheet.edit_row(code=sheet_data[i]["iataCode"],id=i+2)


for i in range(len(sheet_data)):
    iata_code=sheet_data[i]["iataCode"]
    lowest_price=sheet_data[0]["lowestPrice"]
    flight =FlightData()
    flight_data_dict=flight.low_price(fly_to=iata_code)
    if flight_data_dict['price'] < lowest_price:
        sms=NotificationManager()
        sms.alert(flight_data_dict)
