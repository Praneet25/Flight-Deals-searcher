import os
import dotenv
from twilio.rest import Client

dotenv.load_dotenv("E:/Env Variables/my_env.env")
account_sid = os.getenv("acc_sid")
auth_token = os.getenv("twilio_auth_token")
client = Client(account_sid, auth_token)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def alert(self,data_dict):

        message = client.messages \
            .create(
            body=f"Low price alert!\n"
                 f"Only{data_dict['price']}£ to fly from {data_dict['city_departure']}-{data_dict['city_dep_iata']} to {data_dict['city_arrival']}-{data_dict['city_arrival_iata']} \n"
                 f"from {data_dict['outbound']} to {data_dict['inbound']} \n"
                 f"flight no.{data_dict['flight_no']} airlines:{data_dict['airlines']}",
            from_='+twilio_number',
            to='+your number'
        )
        print(message.status)

