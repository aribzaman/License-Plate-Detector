import database

database.initialise()

database.print_licences(database.getAll())

# license_plates_in_view = []

# vehicles_currently_in_view = [] #stores teh vehicles currently in view

# def extract_license_plate(vehicle=None):

#     #Using trained model to extract data out of the vehicle
#     return (vehicle) or "up60 12345"

# while True:
#     #this will be empty on eveyr new frame
#     detected_vehicles = []
#     license_plates_in_new_frame = []

#     # USE OpenCV to detect Vehicles and add them to this list
#     detected_vehicles.append(...)

#     # storing license plate of each detected vehicle
#     for vehicle in detected_vehicles:
#         license_plate = extract_license_plate(vehicle)  # Extract the license plate from the vehicle

#         # Check if the license plate is new or not
#         if license_plate not in license_plates_in_view:
#             # add to fb if it is new
#             database.add_license(license_plate) 
#             license_plates_in_view.append(license_plate) 
#             license_plates_in_new_frame.append(license_plate)

#     #storing only those that are common, i.e. out of view licenses gets erased
#     license_plates_in_view = list(set(license_plates_in_view).intersection(set(license_plates_in_new_frame)))
