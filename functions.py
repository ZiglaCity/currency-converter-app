import requests
import json
import os 
from appdirs import user_cache_dir

#create a new function much convinient to check repeated when the user is either online or offline
# def check_connection():
#     global status_label, root
#     try:
#         # Make a request to a reliable site (like Google's DNS)
#         response = requests.get('https://www.google.com', timeout=3)
#         response.raise_for_status()

#         if response.status_code == 200:
#             status_label.config(text="Online", fg="green")
                    
#         else:
#             status_label.config(text="Offline", fg="red")

#     except requests.exceptions.RequestException:
#         status_label.config(text="Offline", fg="red")

#     # Call this function periodically (e.g., every 5 seconds)
#     root.after(5000, check_connection)



#create a function which updates the exchange rate when necessary
api_url = "https://api.exchangerate-api.com/v4/latest/USD" 
json_file_path = "exchange_rates.json"

def update_exchange_rate(api_url, json_file_path):
    app_name = "Currency Converter"
    app_author = "ZiglaCity"
    cache_dir = user_cache_dir(app_name,app_author)
    os.makedirs(cache_dir, exist_ok=True)
    
    app_cache_path = os.path.join(cache_dir, json_file_path)


    try:
        # Fetch the current exchange rates from the API
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()  # Raise an error if the request was unsuccessful
        
        # Parse the JSON response
        api_response = response.json()
        
        # Extract the exchange rates from the 'rates' key
        exchange_rates = api_response.get('rates', {})
        
        try:
            # Attempt to save the new exchange rates to the JSON file in the app cache folder
            with open(app_cache_path, 'w') as json_file:
                global exchange_rate_offline_data
                json.dump(exchange_rates, json_file, indent=4)
                exchange_rate_offline_data = exchange_rates
                print(exchange_rates)
                print(f"Exchange rates successfully saved to {json_file_path}")
        
        except PermissionError as e:
        # Optionally, try saving to a different location or take alternative action
            fallback_path = os.path.join(os.path.expanduser("~"), "Documents", os.path.basename(json_file_path))
            try:
                with open(fallback_path, 'w') as json_file:
                    json.dump(exchange_rates, json_file, indent=4)
                    exchange_rate_offline_data = exchange_rates
                    print("Exchange rate sent to Documents instead")
            except Exception as fallback_error:
                print(fallback_error)
                #do nothing
                rates = rates
        
    except requests.RequestException as e:
        print(e)
        return False

update_exchange_rate(api_url, json_file_path)