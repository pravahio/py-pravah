# This example demonstrate how one can get access real-time data coming out of 
# various solar power stations across Delhi, India.

# Setting up
# pip3 install pravah

import pravah

p = pravah.Pravah('/SolarPowerProduction', endpoint='rpc.pravah.io:5555')

feed = p.subscribe('/in/delhi')

for m, c in feed:
    # m is a `FeedMessage` instance as given in https://github.com/pravahio/protocols/blob/master/protocols/solar-power-production/SolarPowerProduction.proto
    # c is the channel name which currently is `/in/delhi`
    print(m.header)
    print(m.stations[0])
