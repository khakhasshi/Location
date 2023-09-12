import geocoder

# Get the current location
g = geocoder.ip('me')
location = g.latlng
address = g.address

print('Latitude:', location[0])
print('Longitude:', location[1])
print('Address:', address)