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
app_name = "Currency Converter"
app_author = "ZiglaCity"
cache_dir = user_cache_dir(app_name,app_author)
os.makedirs(cache_dir, exist_ok=True)

app_cache_path = os.path.join(cache_dir, json_file_path)

def update_exchange_rate():
    print("Updating exchange rates")

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
                # print(exchange_rates)
                print(f"Exchange rates successfully saved to {json_file_path}")
        
        except PermissionError as e:
        # Optionally, try saving to a different location or take alternative action
            fallback_path = os.path.join(os.path.expanduser("~"), "Documents", os.path.basename(json_file_path))
            try:
                with open(fallback_path, 'w') as json_file:
                    json.dump(exchange_rates, json_file, indent=4)
                    exchange_rate_offline_data = exchange_rates
                    # print("Exchange rate sent to Documents instead")
            except Exception as fallback_error:
                # print(fallback_error)
                rates = rates
        
    except requests.RequestException as e:
        # print(e)
        # extract the exchange rate from the cache file if user is offline
        try:
            with open(app_cache_path, 'r') as file:
                offline_rate = json.load(file)
                if offline_rate:
                    exchange_rate_offline_data = offline_rate
                    print(f"No Connction so this is the offline exchange rate {exchange_rate_offline_data}")
        except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
            print("No Connection and File Not Found")
            return

# DEBUG
# update_exchange_rate()


#define a function to convert the curries appropriately
def convert_currency():
    global entry_top, to_currency,answer, from_currency, entry_bottom, answer, app_cache_path 
    if not entry_top.get():
        amount = 0
    else:
        amount = float(entry_top.get())
    to_currency = to_
    from_currency = from_

    #fetch the latest rates
    try:
        with open(app_cache_path, 'r') as file:
            offline_rate = json.load(file)
            if offline_rate:
                rates = offline_rate
                exchange_rate_offline_data = rates
                print(f"this is the offline exchange rate {exchange_rate_offline_data}")
            else:
                print("File Empty")
                rates = exchange_rate_offline_data
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
        print("File Not Found while converting")
        rates = exchange_rate_data

    #do the convertion
    if from_currency == "USD":
        converted_amount = float(amount) * float(rates[to_currency])
        
    else:
        converted_amount = float(amount) / float(rates[from_currency]) * float(rates[to_currency])
        entry_bottom.config(state="normal")
        
    #round the converted value to an appropriate decimal places
    if converted_amount > 1:
        converted_amount = round(converted_amount, 2)
    elif converted_amount > 0.01:
        converted_amount = round(converted_amount, 3)
    else:
        converted_amount = round(converted_amount, 5)

    #now fix the anser in the down entry and change its mode to read only
    answer.set(converted_amount)
    entry_bottom.config(state="readonly")

    return converted_amount

def Refresh():
    update_exchange_rate()
    return 



