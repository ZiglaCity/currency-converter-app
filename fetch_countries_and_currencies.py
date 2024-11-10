import requests

def fetch_countries_and_currencies():
    exchange_api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    exchange_response = requests.get(exchange_api_url)
    exchange_data = exchange_response.json()
    usd_currencies = exchange_data['rates']
    #print(usd_currencies)

    # Fetch country names and their currency codes
    #but since we cannot always be fetching the country data from an API, we will save the data and open a file instead of fetching the data online
    country_api_url = "https://restcountries.com/v3.1/all"
    country_response = requests.get(country_api_url)
    country_data = country_response.json()
    #print(country_data)

    # Create a dictionary mapping currency codes to country names
    currency_to_country = {}
    for country in country_data:
        currencies = country.get('currencies', {}) #the 'currencies' is a key in the country (dictionary) data, which also returns or contains another dictionary as values
        for code, details in currencies.items(): #here i am trying to get each key and value pair of the currencies dictoinary data values. where code is the key and details is the values
            if code in usd_currencies:   #here if the codes we got above are also in our usd_currencies dictionary data, 
                currency_to_country[code] = [country.get('name', {}).get('common', 'Unknown'), details["name"] ]# we then get the 'name' key values in our country and from the 'name' key it has a value stored in dictionary which also contains the country names with 'common' key; #now we set the country code as our key and get the country name as our value in our new country_to_currencies dictionary data
    print(currency_to_country)
    return currency_to_country

def fetch_countries_using_usd():
    #call the fetch_countries_and_currencies() function which returns an organized dictionary data with code as key and country names as values
    currencies = fetch_countries_and_currencies()
    #hey i am trying to get list of values sets of valus (country, currencies)
    return [(country, currency) for currency, country in currencies.items()]

fetch_countries_and_currencies()

