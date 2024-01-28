from geopy.geocoders import Nominatim

def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="geoapiExercises") # User agent is required by Nominatim
    location = geolocator.geocode(location_name)
    return location.latitude, location.longitude

if __name__ == "__main__":
    location_name = "Mansarovar, Jaipur"  # Replace with your desired location
    latitude, longitude = get_coordinates(location_name)
    print(f"Latitude: {latitude}, Longitude: {longitude}")
