import time
import requests

# Replace these with your ThingSpeak credentials
ssid = "naveenalakani"
password = "Naveen@123"
api_key = "your-api-key"

# Replace this with your ThingSpeak channel number
channel_number = 123456

# URL for updating ThingSpeak channel
update_url = f"http://api.thingspeak.com/update?api_key={api_key}"

# Pin connected to the soil moisture sensor
soil_moisture_pin = 0

def read_soil_moisture():
    # Replace this with your code to read the soil moisture level
    # For example, you might use an analog sensor connected to the pin
    # and return the reading
    return 0

def send_to_thingspeak(moisture_level):
    # Send data to ThingSpeak
    payload = {"field1": moisture_level, "field2": channel_number}
    response = requests.post(update_url, params=payload)

    return response.status_code == 200

def main():
    while True:
        # Read soil moisture level
        moisture_level = read_soil_moisture()

        # Send data to ThingSpeak
        if send_to_thingspeak(moisture_level):
            print("Data sent to ThingSpeak")
        else:
            print("Failed to send data to ThingSpeak")

        # Wait for a specific interval (e.g., 15 minutes)
        time.sleep(15 * 60)

if __name__ == "__main__":
    main()
