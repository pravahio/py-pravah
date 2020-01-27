# This example demonstrate how one can get access real-time data coming out of 
# various AWS (Air Weather Stations) in NCR region.

# Setting up
# pip3 install pravah

import pravah

p = pravah.Pravah('/AirQuality', endpoint='rpc.pravah.io:5555')

feed = p.subscribe('/in/ncr')

for m, c in feed:
    # m is a `FeedMessage` instance as given in https://github.com/pravahio/mesh-air-quality/blob/master/air-quality.proto
    # c is the channel name which currently is `/in/ncr`
    print(m.header)
    print(m.stations[0])
