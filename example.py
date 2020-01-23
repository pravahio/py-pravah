import pravah
from google.protobuf.json_format import ParseDict

p = pravah.Pravah('/FlightData', endpoint='rpc.pravah.io:5555')

""" d = {
    "header": {
        "timestamp": 154635342
    },
    "stations": [
        {
            "status": {
                "state": "DISCONNECTED"
            }
        }
    ]
}

feed = p.subscribe('/in/delhi')

for m, c in feed:
    print(m) """

cur = p.get_historical_data(query={'geospace': '/in/delhi'}, past_minutes=1)
for i in cur:
    print(i)