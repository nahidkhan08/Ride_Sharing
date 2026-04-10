from user import Rider, Driver
from ride import Ride, RideMatching, RideRequest, RideSharing
from vehicle import Car, Bike, CNG

pathao=RideSharing("Pathao")
rahim=Rider("Rahim", 'rahim@gmail.com', 12345, 'Mirpur', 1800)
pathao.add_rider(rahim)

babul=Driver("Babul", 'babul@gmail.com', 43568, 'Gabtoli')
pathao.add_driver(babul)

rahim.request_ride(pathao, "Uttara", 'car')
babul.reach_destination(rahim.current_ride)
rahim.show_current_ride()