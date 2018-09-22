import smartcar

access_token = '0482b6f8-2529-4328-9091-319e59faf4b8'

response = smartcar.get_vehicle_ids(access_token)

vid = response['vehicles'][0]

vehicle = smartcar.Vehicle(vid, access_token)

location = vehicle.location()

vehicle.lock()

print(location)
