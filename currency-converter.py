import requests
import tkinter as tk
import json
import sys
import os
from appdirs import user_cache_dir



data = {"SHP": "Saint Helena, Ascension and Tristan da Cunha", "XCD": "Anguilla", "CHF": "Liechtenstein", "SLL": "Sierra Leone", "HUF": "Hungary", "TWD": "Taiwan", "XPF": "New Caledonia", "BBD": "Barbados", "NZD": "New Zealand", "XOF": "Mali", "TND": "Tunisia", "EUR": "Belgium", "IDR": "Indonesia", "CVE": "Cape Verde", "LAK": "Laos", "USD": "American Samoa", "UGX": "Uganda", "BIF": "Burundi", "ZAR": "Lesotho", "LYD": "Libya", "MXN": "Mexico", "XAF": "Republic of the Congo", "MKD": "North Macedonia", "CNY": "China", "YER": "Yemen", "GBP": "Jersey", "GGP": "Guernsey", "SBD": "Solomon Islands", "NOK": "Norway", "DKK": "Denmark", "FOK": "Faroe Islands", "UZS": "Uzbekistan", "EGP": "Palestine", "LKR": "Sri Lanka", "ILS": "Israel", "JOD": "Jordan", "BDT": "Bangladesh", "PEN": "Peru", "SGD": "Brunei", "TRY": "Turkey", "AFN": "Afghanistan", "AWG": "Aruba", "ZMW": "Zambia", "AUD": "Kiribati", "AZN": "Azerbaijan", "DJF": "Djibouti", "MUR": "Mauritius", "COP": "Colombia", "MAD": "Western Sahara", "DZD": "Western Sahara", "SDG": "Sudan", "FJD": "Fiji", "NPR": "Nepal", "GEL": "Georgia", "PKR": "Pakistan", "BWP": "Botswana", "LBP": "Lebanon", "PGK": "Papua New Guinea", "DOP": "Dominican Republic", "QAR": "Qatar", "MGA": "Madagascar", "INR": "Bhutan", "SYP": "Syria", "SZL": "Eswatini", "PYG": "Paraguay", "UAH": "Ukraine", "IMP": "Isle of Man", "NAD": "Namibia", "AED": "United Arab Emirates", "BGN": "Bulgaria", "KHR": "Cambodia", "IQD": "Iraq", "SEK": "Sweden", "CUP": "Cuba", "KGS": "Kyrgyzstan", "RUB": "Russia", "MYR": "Malaysia", "STN": "S\u00e3o Tom\u00e9 and Pr\u00edncipe", "CAD": "Canada", "MWK": "Malawi", "SAR": "Saudi Arabia", "BAM": "Bosnia and Herzegovina", "ETB": "Ethiopia", "OMR": "Oman", "MOP": "Macau", "LSL": "Lesotho", "ANG": "Cura\u00e7ao", "ISK": "Iceland", "ARS": "Argentina", "MRU": "Mauritania", "CRC": "Costa Rica", "THB": "Thailand", "HTG": "Haiti", "TVD": "Tuvalu", "HNL": "Honduras", "BYN": "Belarus", "PHP": "Philippines", "GIP": "Gibraltar", "GNF": "Guinea", "BHD": "Bahrain", "SRD": "Suriname", "CDF": "DR Congo", "SOS": "Somalia", "CZK": "Czechia", "VUV": "Vanuatu", "KES": "Kenya", "RWF": "Rwanda", "RON": "Romania", "TTD": "Trinidad and Tobago", "GYD": "Guyana", "VND": "Vietnam", "UYU": "Uruguay", "HKD": "Hong Kong", "TMT": "Turkmenistan", "MZN": "Mozambique", "PAB": "Panama", "ERN": "Eritrea", "TZS": "Tanzania", "KRW": "South Korea", "AOA": "Angola", "KZT": "Kazakhstan", "MDL": "Moldova", "FKP": "Falkland Islands", "AMD": "Armenia", "WST": "Samoa", "JEP": "Jersey", "JPY": "Japan", "BOB": "Bolivia", "CLP": "Chile", "BMD": "Bermuda", "SCR": "Seychelles", "GTQ": "Guatemala", "TJS": "Tajikistan", "GMD": "Gambia", "NGN": "Nigeria", "BSD": "Bahamas", "KWD": "Kuwait", "MVR": "Maldives", "SSP": "South Sudan", "IRR": "Iran", "ALL": "Albania", "BRL": "Brazil", "RSD": "Serbia", "BZD": "Belize", "MMK": "Myanmar", "BTN": "Bhutan", "VES": "Venezuela", "LRD": "Liberia", "JMD": "Jamaica", "PLN": "Poland", "KYD": "Cayman Islands", "BND": "Brunei", "KMF": "Comoros", "TOP": "Tonga", "KID": "Kiribati", "GHS": "Ghana", "ZWL": "Zimbabwe", "MNT": "Mongolia", "NIO": "Nicaragua"}

exchange_rate_offline_data = {'USD': 1, 'AED': 3.67, 'AFN': 68.12, 'ALL': 91.22, 'AMD': 387.16, 'ANG': 1.79, 'AOA': 920.28, 'ARS': 997.25, 'AUD': 1.52, 'AWG': 1.79, 'AZN': 1.7, 'BAM': 1.82, 'BBD': 2, 'BDT': 119.44, 'BGN': 1.82, 'BHD': 0.376, 'BIF': 2923.11, 'BMD': 1, 'BND': 1.32, 'BOB': 6.92, 'BRL': 5.7, 'BSD': 1, 'BTN': 84.4, 'BWP': 13.41, 'BYN': 3.3, 'BZD': 2, 'CAD': 1.39, 'CDF': 2849.17, 'CHF': 
0.875, 'CLP': 951.67, 'CNY': 7.18, 'COP': 4388.23, 'CRC': 511.33, 'CUP': 24, 'CVE': 102.7, 'CZK': 23.46, 'DJF': 177.72, 'DKK': 6.94, 'DOP': 60.08, 'DZD': 133.45, 'EGP': 49.29, 'ERN': 15, 'ETB': 120.54, 'EUR': 0.931, 'FJD': 2.24, 'FKP': 0.773, 'FOK': 6.94, 'GBP': 0.773, 'GEL': 2.72, 'GGP': 0.773, 'GHS': 16.35, 'GIP': 0.773, 'GMD': 71.49, 'GNF': 8597.62, 'GTQ': 7.7, 'GYD': 208.96, 'HKD': 7.77, 'HNL': 25.17, 'HRK': 7.02, 'HTG': 131.53, 'HUF': 378.14, 'IDR': 15654.78, 'ILS': 3.74, 'IMP': 0.773, 
'INR': 84.4, 'IQD': 1308.81, 'IRR': 42057.31, 'ISK': 137.98, 'JEP': 0.773, 'JMD': 158.5, 'JOD': 0.709, 'JPY': 152.69, 'KES': 128.82, 'KGS': 85.7, 'KHR': 4074.4, 'KID': 1.52, 'KMF': 458.22, 'KRW': 1391.93, 'KWD': 0.307, 'KYD': 0.833, 'KZT': 492.1, 'LAK': 21826.61, 'LBP': 89500, 'LKR': 292.44, 'LRD': 190.28, 'LSL': 17.54, 'LYD': 4.83, 'MAD': 9.89, 'MDL': 17.8, 'MGA': 4619.78, 'MKD': 57.02, 'MMK': 2096.67, 'MNT': 3405.77, 'MOP': 8.01, 'MRU': 39.75, 'MUR': 46.42, 'MVR': 15.39, 'MWK': 1744.03, 'MXN': 20.15, 'MYR': 4.38, 'MZN': 63.89, 'NAD': 17.54, 'NGN': 1669.34, 'NIO': 36.74, 'NOK': 10.98, 'NPR': 135.04, 'NZD': 1.67, 'OMR': 0.384, 'PAB': 1, 'PEN': 3.77, 'PGK': 4, 'PHP': 58.43, 'PKR': 278.12, 'PLN': 4.02, 'PYG': 7821.99, 'QAR': 3.64, 'RON': 4.62, 'RSD': 108.62, 'RUB': 97.6, 'RWF': 1363.98, 'SAR': 3.75, 'SBD': 8.48, 'SCR': 13.56, 'SDG': 510.38, 'SEK': 10.8, 'SGD': 1.32, 'SHP': 0.773, 'SLE': 22.69, 'SLL': 22686.44, 'SOS': 570.6, 'SRD': 34.9, 'SSP': 3416.77, 'STN': 22.82, 'SYP': 12877.8, 'SZL': 17.54, 'THB': 34.11, 'TJS': 10.68, 'TMT': 3.5, 'TND': 3.12, 'TOP': 2.34, 'TRY': 34.36, 'TTD': 6.77, 'TVD': 1.52, 'TWD': 32.17, 'TZS': 2666.31, 'UAH': 41.31, 'UGX': 3669.46, 'UYU': 41.52, 'UZS': 12783, 'VES': 44.7, 'VND': 25296.74, 'VUV': 
120.45, 'WST': 2.74, 'XAF': 610.97, 'XCD': 2.7, 'XDR': 0.755, 'XOF': 610.97, 'XPF': 111.15, 'YER': 249.61, 'ZAR': 17.54, 'ZMW': 27.15, 'ZWL': 25.59}

rates = exchange_rate_offline_data


currency_data =  {'AFN': ['Afghanistan', 'Afghan afghani'], 'ALL': ['Albania', 'Albanian lek'], 'USD': ['American Samoa', 'United States dollar'], 'AOA': ['Angola', 'Angolan kwanza'], 'XCD': ['Anguilla', 'Eastern Caribbean dollar'], 'ARS': ['Argentina', 'Argentine peso'], 'AMD': ['Armenia', 'Armenian dram'], 'AWG': ['Aruba', 'Aruban florin'], 'AZN': ['Azerbaijan', 'Azerbaijani manat'], 
                'BSD': ['Bahamas', 'Bahamian dollar'], 'BHD': ['Bahrain', 'Bahraini dinar'], 'BDT': ['Bangladesh', 'Bangladeshi taka'], 'BBD': ['Barbados', 'Barbadian dollar'], 'BYN': ['Belarus', 'Belarusian ruble'], 'EUR': ['Belgium', 'Euro'], 'BZD': ['Belize', 'Belize dollar'], 'BMD': ['Bermuda', 'Bermudian dollar'], 'BTN': ['Bhutan', 'Bhutanese ngultrum'], 'INR': ['Bhutan', 'Indian rupee'], 'BOB': ['Bolivia', 'Bolivian boliviano'], 'BAM': ['Bosnia and Herzegovina', 'Bosnia and Herzegovina convertible mark'], 'BWP': ['Botswana', 'Botswana pula'], 'BRL': ['Brazil', 'Brazilian real'], 'BND': ['Brunei', 'Brunei dollar'], 'SGD': ['Brunei', 'Singapore dollar'], 'BGN': ['Bulgaria', 'Bulgarian lev'], 'BIF': ['Burundi', 'Burundian franc'], 'KHR': ['Cambodia', 'Cambodian riel'], 'CAD': ['Canada', 'Canadian dollar'], 'CVE': ['Cape Verde', 'Cape Verdean escudo'], 'KYD': ['Cayman Islands', 'Cayman Islands dollar'], 'CLP': ['Chile', 'Chilean peso'], 'CNY': ['China', 'Chinese yuan'], 'COP': ['Colombia', 'Colombian peso'], 'KMF': ['Comoros', 'Comorian franc'], 'CRC': ['Costa Rica', 'Costa Rican colón'], 'CUP': ['Cuba', 'Cuban peso'], 'ANG': ['Curaçao', 'Netherlands Antillean guilder'], 'CZK': ['Czechia', 'Czech koruna'], 'CDF': ['DR Congo', 'Congolese franc'], 'DKK': ['Denmark', 'Danish krone'], 'DJF': ['Djibouti', 'Djiboutian franc'], 'DOP': ['Dominican Republic', 'Dominican peso'], 'ERN': ['Eritrea', 'Eritrean nakfa'], 'SZL': ['Eswatini', 'Swazi lilangeni'], 'ETB': ['Ethiopia', 'Ethiopian birr'], 'FKP': ['Falkland Islands', 'Falkland Islands pound'], 'FOK': ['Faroe Islands', 'Faroese króna'], 'FJD': ['Fiji', 'Fijian dollar'], 'GMD': ['Gambia', 'dalasi'], 'GEL': ['Georgia', 'lari'], 'GHS': ['Ghana', 'Ghanaian cedi'], 'GIP': ['Gibraltar', 'Gibraltar pound'], 'GTQ': ['Guatemala', 'Guatemalan quetzal'], 'GGP': ['Guernsey', 'Guernsey pound'], 'GNF': ['Guinea', 'Guinean franc'], 'GYD': ['Guyana', 'Guyanese dollar'], 'HTG': ['Haiti', 'Haitian gourde'], 'HNL': ['Honduras', 'Honduran lempira'], 'HKD': ['Hong Kong', 'Hong Kong dollar'], 'HUF': ['Hungary', 'Hungarian forint'], 'ISK': ['Iceland', 'Icelandic króna'], 'IDR': ['Indonesia', 'Indonesian rupiah'], 'IRR': ['Iran', 'Iranian rial'], 'IQD': ['Iraq', 'Iraqi dinar'], 'IMP': ['Isle of Man', 'Manx pound'], 'ILS': ['Israel', 'Israeli new shekel'], 'JMD': ['Jamaica', 'Jamaican dollar'], 'JPY': ['Japan', 'Japanese yen'], 'GBP': ['Jersey', 'British pound'], 'JEP': ['Jersey', 'Jersey pound'], 'JOD': ['Jordan', 'Jordanian dinar'], 'KZT': ['Kazakhstan', 'Kazakhstani tenge'], 'KES': ['Kenya', 'Kenyan shilling'], 'AUD': ['Kiribati', 'Australian dollar'], 'KID': ['Kiribati', 'Kiribati dollar'], 'KWD': ['Kuwait', 'Kuwaiti dinar'], 'KGS': ['Kyrgyzstan', 'Kyrgyzstani som'], 'LAK': ['Laos', 'Lao kip'], 'LBP': ['Lebanon', 'Lebanese pound'], 'LSL': ['Lesotho', 'Lesotho loti'], 'ZAR': ['Lesotho', 'South African rand'], 'LRD': ['Liberia', 'Liberian dollar'], 'LYD': ['Libya', 'Libyan dinar'], 'CHF': ['Liechtenstein', 'Swiss franc'], 'MOP': ['Macau', 'Macanese pataca'], 'MGA': ['Madagascar', 'Malagasy ariary'], 'MWK': ['Malawi', 'Malawian kwacha'], 
                'MYR': ['Malaysia', 'Malaysian ringgit'], 'MVR': ['Maldives', 'Maldivian rufiyaa'], 'XOF': ['Mali', 'West African CFA franc'], 'MRU': ['Mauritania', 'Mauritanian ouguiya'], 'MUR': ['Mauritius', 'Mauritian rupee'], 'MXN': ['Mexico', 'Mexican peso'], 'MDL': ['Moldova', 'Moldovan leu'], 'MNT': ['Mongolia', 'Mongolian tögrög'], 'MZN': ['Mozambique', 'Mozambican metical'], 'MMK': ['Myanmar', 'Burmese kyat'], 'NAD': ['Namibia', 'Namibian dollar'], 'NPR': ['Nepal', 'Nepalese rupee'], 'XPF': ['New Caledonia', 'CFP franc'], 'NZD': ['New Zealand', 'New Zealand dollar'], 'NIO': ['Nicaragua', 'Nicaraguan córdoba'], 'NGN': ['Nigeria', 'Nigerian naira'], 'MKD': ['North Macedonia', 'denar'], 'NOK': ['Norway', 'Norwegian krone'], 'OMR': ['Oman', 'Omani rial'], 'PKR': ['Pakistan', 'Pakistani rupee'], 'EGP': ['Palestine', 'Egyptian pound'], 'PAB': ['Panama', 'Panamanian balboa'], 'PGK': ['Papua New Guinea', 'Papua New Guinean kina'], 'PYG': ['Paraguay', 'Paraguayan guaraní'], 'PEN': ['Peru', 'Peruvian sol'], 'PHP': ['Philippines', 'Philippine peso'], 'PLN': ['Poland', 'Polish złoty'], 'QAR': ['Qatar', 'Qatari riyal'], 'XAF': ['Republic of the Congo', 'Central African CFA franc'], 'RON': ['Romania', 'Romanian leu'], 'RUB': ['Russia', 'Russian ruble'], 'RWF': ['Rwanda', 'Rwandan franc'], 'SHP': ['Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena pound'], 'WST': ['Samoa', 'Samoan tālā'], 'SAR': ['Saudi Arabia', 'Saudi riyal'], 'RSD': ['Serbia', 'Serbian dinar'], 'SCR': ['Seychelles', 'Seychellois rupee'], 'SLL': ['Sierra Leone', 'Sierra Leonean leone'], 'SBD': ['Solomon Islands', 'Solomon Islands dollar'], 'SOS': ['Somalia', 'Somali shilling'], 'KRW': ['South Korea', 'South Korean won'], 'SSP': ['South Sudan', 'South Sudanese pound'], 'LKR': ['Sri Lanka', 'Sri Lankan rupee'], 'SDG': ['Sudan', 'Sudanese pound'], 'SRD': ['Suriname', 'Surinamese dollar'], 'SEK': ['Sweden', 'Swedish krona'], 'SYP': ['Syria', 'Syrian pound'], 'STN': ['São Tomé and Príncipe', 'São Tomé and Príncipe dobra'], 'TWD': ['Taiwan', 'New Taiwan dollar'], 'TJS': ['Tajikistan', 'Tajikistani somoni'], 'TZS': ['Tanzania', 'Tanzanian shilling'], 'THB': ['Thailand', 'Thai baht'], 'TOP': ['Tonga', 'Tongan paʻanga'], 'TTD': ['Trinidad and Tobago', 'Trinidad and Tobago dollar'], 'TND': ['Tunisia', 'Tunisian dinar'], 'TRY': ['Turkey', 'Turkish lira'], 'TMT': ['Turkmenistan', 'Turkmenistan manat'], 'TVD': ['Tuvalu', 'Tuvaluan dollar'], 'UGX': ['Uganda', 'Ugandan shilling'], 'UAH': ['Ukraine', 'Ukrainian hryvnia'], 'AED': ['United Arab Emirates', 'United Arab Emirates dirham'], 'UYU': ['Uruguay', 'Uruguayan peso'], 'UZS': ['Uzbekistan', 'Uzbekistani soʻm'], 'VUV': ['Vanuatu', 'Vanuatu vatu'], 'VES': ['Venezuela', 'Venezuelan bolívar soberano'], 'VND': ['Vietnam', 'Vietnamese đồng'], 'DZD': ['Western Sahara', 'Algerian dinar'], 'MAD': ['Western Sahara', 
                'Moroccan dirham'], 'YER': ['Yemen', 'Yemeni rial'], 'ZMW': ['Zambia', 'Zambian kwacha'], 'ZWL': ['Zimbabwe', 'Zimbabwean dollar']}


#set default values to appear in both currencies
from_ = 'USD'
to_ = 'GHS'
status = "OFFLINE"

#define fixed size for the application window
fixed_width = 580
fixed_height =  720

# setting up the app cache directory where exchange rate can be stored
api_url = "https://api.exchangerate-api.com/v4/latest/USD" 
json_file_path = "exchange_rates.json"
app_name = "Currency Converter"
app_author = "ZiglaCity"
cache_dir = user_cache_dir(app_name,app_author)
os.makedirs(cache_dir, exist_ok=True)

app_cache_path = os.path.join(cache_dir, json_file_path)


currency_and_country = {
    "SHP": "Saint Helena, Ascension and Tristan da Cunha", "XCD": "Anguilla", "CHF": "Liechtenstein",
    "SLL": "Sierra Leone", "HUF": "Hungary", "TWD": "Taiwan", "XPF": "New Caledonia", "BBD": "Barbados",
    "NZD": "New Zealand", "XOF": "Mali", "TND": "Tunisia", "EUR": "Belgium", "IDR": "Indonesia",
    "CVE": "Cape Verde", "LAK": "Laos", "USD": "American Samoa", "UGX": "Uganda", "BIF": "Burundi",
    "ZAR": "Lesotho", "LYD": "Libya", "MXN": "Mexico", "XAF": "Republic of the Congo", "MKD": "North Macedonia",
    "CNY": "China", "YER": "Yemen", "GBP": "Jersey", "GGP": "Guernsey", "SBD": "Solomon Islands",
    "NOK": "Norway", "DKK": "Denmark", "FOK": "Faroe Islands", "UZS": "Uzbekistan", "EGP": "Palestine",
    "LKR": "Sri Lanka", "ILS": "Israel", "JOD": "Jordan", "BDT": "Bangladesh", "PEN": "Peru",
    "SGD": "Brunei", "TRY": "Turkey", "AFN": "Afghanistan", "AWG": "Aruba", "ZMW": "Zambia",
    "AUD": "Kiribati", "AZN": "Azerbaijan", "DJF": "Djibouti", "MUR": "Mauritius", "COP": "Colombia",
    "MAD": "Western Sahara", "DZD": "Western Sahara", "SDG": "Sudan", "FJD": "Fiji", "NPR": "Nepal",
    "GEL": "Georgia", "PKR": "Pakistan", "BWP": "Botswana", "LBP": "Lebanon", "PGK": "Papua New Guinea",
    "DOP": "Dominican Republic", "QAR": "Qatar", "MGA": "Madagascar", "INR": "Bhutan", "SYP": "Syria",
    "SZL": "Eswatini", "PYG": "Paraguay", "UAH": "Ukraine", "IMP": "Isle of Man", "NAD": "Namibia",
    "AED": "United Arab Emirates", "BGN": "Bulgaria", "KHR": "Cambodia", "IQD": "Iraq", "SEK": "Sweden",
    "CUP": "Cuba", "KGS": "Kyrgyzstan", "RUB": "Russia", "MYR": "Malaysia", "STN": "São Tomé and Príncipe",
    "CAD": "Canada", "MWK": "Malawi", "SAR": "Saudi Arabia", "BAM": "Bosnia and Herzegovina", "ETB": "Ethiopia",
    "OMR": "Oman", "MOP": "Macau", "LSL": "Lesotho", "ANG": "Curaçao", "ISK": "Iceland", "ARS": "Argentina",
    "MRU": "Mauritania", "CRC": "Costa Rica", "THB": "Thailand", "HTG": "Haiti", "TVD": "Tuvalu",
    "HNL": "Honduras", "BYN": "Belarus", "PHP": "Philippines", "GIP": "Gibraltar", "GNF": "Guinea",
    "BHD": "Bahrain", "SRD": "Suriname", "CDF": "DR Congo", "SOS": "Somalia", "CZK": "Czechia",
    "VUV": "Vanuatu", "KES": "Kenya", "RWF": "Rwanda", "RON": "Romania", "TTD": "Trinidad and Tobago",
    "GYD": "Guyana", "VND": "Vietnam", "UYU": "Uruguay", "HKD": "Hong Kong", "TMT": "Turkmenistan",
    "MZN": "Mozambique", "PAB": "Panama", "ERN": "Eritrea", "TZS": "Tanzania", "KRW": "South Korea",
    "AOA": "Angola", "KZT": "Kazakhstan", "MDL": "Moldova", "FKP": "Falkland Islands", "AMD": "Armenia",
    "WST": "Samoa", "JEP": "Jersey", "JPY": "Japan", "BOB": "Bolivia", "CLP": "Chile", "BMD": "Bermuda",
    "SCR": "Seychelles", "GTQ": "Guatemala", "TJS": "Tajikistan", "GMD": "Gambia", "NGN": "Nigeria",
    "BSD": "Bahamas", "KWD": "Kuwait", "MVR": "Maldives", "SSP": "South Sudan", "IRR": "Iran",
    "ALL": "Albania", "BRL": "Brazil", "RSD": "Serbia", "BZD": "Belize", "MMK": "Myanmar", "BTN": "Bhutan",
    "VES": "Venezuela", "LRD": "Liberia", "JMD": "Jamaica", "PLN": "Poland", "KYD": "Cayman Islands",
    "BND": "Brunei", "KMF": "Comoros", "TOP": "Tonga", "KID": "Kiribati", "GHS": "Ghana", "ZWL": "Zimbabwe",
    "MNT": "Mongolia", "NIO": "Nicaragua"
}


#define a fixed style to be used for all the widgets
label_style = {
    "font": ("Arial", 14, "italic"),
    "bg": "#e6e6e6",
    "fg": "#2b2b2b",
    "padx": 8,
    "pady": 8
}

button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "#BBBBBB",
    "fg": "#333333",
    "bd": 3,
    "relief": "ridge"
}

entry_style = {
    "font": ("Times New Roman", 12),
    "bg": "#ffffff",
    "fg": "#000000",
    "bd": 2,
    "relief": "solid"
}
#DAA520
frame_style = {
    "bg": "#e0e0e0",
    "bd": 2,
    "relief": "sunken"
}
listbox_style = {
    'bg': '#f0f0f0',         # Background color
    'fg': '#333333',         # Text color
    'font': ('Arial', 12),   # Font type and size
    'highlightbackground': '#cccccc',  # Border color when the listbox is not in focus
    'highlightthickness': 1, # Border thickness
    'selectbackground': '#0078d4',  # Background color when an item is selected
    'selectforeground': '#ffffff',  # Text color when an item is selected
    'width': 100,             # Width of the listbox (number of characters)
    'height': 15  # Number of visible lines
}
scrollbar_style = {
    'bg': '#dddddd',         # Background color of the scrollbar
    'troughcolor': '#cccccc',# Color of the trough (the area the slider moves within)
    'width': 15              # Width of the scrollbar
}



#define a funciton which applies the styles to their respective widgets
def apply_styles(widget):
    #Apply styles to all Button, Label, Entry, and Frame widgets
    if isinstance(widget, tk.Button):
        widget.config(**button_style)
    elif isinstance(widget, tk.Label):
        widget.config(**label_style)
    elif isinstance(widget, tk.Entry):
        widget.config(**entry_style)
    elif isinstance(widget, tk.Frame):
        widget.config(**frame_style)
    elif isinstance(widget, tk.Listbox):
        widget.config(**listbox_style)
    elif isinstance(widget, tk.Scrollbar):
        widget.config(**scrollbar_style)

    # Recursively apply styles to all children
    for child in widget.winfo_children():
        apply_styles(child)



#create a function which updates the exchange rate when necessary
api_url = "https://api.exchangerate-api.com/v4/latest/USD" 
json_file_path = "exchange_rates.json"

def update_exchange_rate():

    try:
        # Fetch the current exchange rates from the API
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        api_response = response.json()
        exchange_rates = api_response.get('rates', {})
        
        try:
            # Attempt to save the new exchange rates to the JSON file in the app cache folder
            with open(app_cache_path, 'w') as json_file:
                global exchange_rate_offline_data
                json.dump(exchange_rates, json_file, indent=4)
                exchange_rate_offline_data = exchange_rates
                # print(f"Exchange rates successfully saved to {json_file_path}")
        
        except PermissionError as e:
        # Optionally, try saving to a different location or take alternative action
            fallback_path = os.path.join(os.path.expanduser("~"), "Documents", os.path.basename(json_file_path))
            try:
                with open(fallback_path, 'w') as json_file:
                    json.dump(exchange_rates, json_file, indent=4)
                    exchange_rate_offline_data = exchange_rates
                    # print("Exchange rate sent to Documents instead")
            except Exception as fallback_error:
                rates = rates
        
    except requests.RequestException as e:
        try:
            with open(app_cache_path, 'r') as file:
                offline_rate = json.load(file)
                if offline_rate:
                    exchange_rate_offline_data = offline_rate
                    # print(f"No Connction so this is the offline exchange rate {exchange_rate_offline_data}")
        except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
            # print("No Connection and File Not Found")
            return

 
def Refresh():
    update_exchange_rate()
    return 

#create a new function much convinient to check repeated when the user is either online or offline
def check_connection():
    global status_label
    try:
        # Make a request to a reliable site (like Google's DNS)
        response = requests.get('https://www.google.com', timeout=3)
        response.raise_for_status()

        if response.status_code == 200:
            status_label.config(text="Online", fg="green")
                    
        else:
            status_label.config(text="Offline", fg="red")

    except requests.exceptions.RequestException:
        status_label.config(text="Offline", fg="red")

    # Call this function periodically (e.g., every 5 seconds)
    root.after(5000, check_connection)



#define a function to convert the curries appropriately
def convert_currency():
    global entry_top, to_currency,answer, exchange_rate_offline_data, from_currency, entry_bottom, answer, app_cache_path 
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
                # print(f"this is the offline exchange rate {exchange_rate_offline_data}")
            else:
                # print("File Empty")
                rates = exchange_rate_offline_data
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
        # print("File Not Found while converting")
        rates = exchange_rate_offline_data

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


#use the various APIS to fetch the various currncies and country names and create a dictionary matching them
#since i have already run this function and generated the countries and capitals, its not really nededed in the program again, but for references so i'll keep it here for later refrences
def fetch_countries_and_currencies():
    # Fetch currencies and exchange rates
    exchange_api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    exchange_response = requests.get(exchange_api_url)
    exchange_data = exchange_response.json()
    usd_currencies = exchange_data['rates']

    # Fetch country names and their currency codes
    country_api_url = "https://restcountries.com/v3.1/all"
    country_response = requests.get(country_api_url)
    country_data = country_response.json()

    # Create a dictionary mapping currency codes to country names
    currency_to_country = {}
    for country in country_data:
        currencies = country.get('currencies', {}) #the 'currencies' is a key in the country (dictionary) data, which also returns or contains another dictionary as values
        for code, details in currencies.items(): #here i am trying to get each key and value pair of the currencies dictoinary data values. where code is the key and details is the values
            if code in usd_currencies:   #here if the codes we got above are also in our usd_currencies dictionary data, 
                currency_to_country[code] = country.get('name', {}).get('common', 'Unknown') # we then get the 'name' key values in our country and from the 'name' key it has a value stored in dictionary which also contains the country names with 'common' key; #now we set the country code as our key and get the country name as our value in our new country_to_currencies dictionary data

    return currency_to_country


#define a funcion to seach for a particulatar country or currency
def search():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)  # Clear existing items in the Listbox    
    for currency in currency_data:
        if query in " ".join(currency_data[currency][0:]).lower() or query in currency.lower():  # Case-insensitive search
            listbox.insert(tk.END, f"{" ".join(currency_data[currency][0:])}: {currency}")
    

#define functions for the buttons in the calculor phase
def clear_all():
    entry_top.delete(0, tk.END)
    entry_bottom.config(state='normal')
    entry_bottom.delete(0, tk.END)
    entry_bottom.config(state='readonly')


# A function that deletes last character
def delete_last():
    current_text = entry_top.get()
    if current_text:
        entry_top.delete(len(current_text) - 1, tk.END)


# A function that swaps both currencies
def swap_currencies():
    global top, down, from_, to_, amount, entry_bottom
    # Get the amount in the entry_from box
    top = entry_top.get()
    down = entry_bottom.get()

    #delete the button entry where the converted amount will be inputed to fix the new value
    entry_bottom.config(state= 'normal')
    entry_bottom.delete(0, tk.END)
    entry_bottom.config(state= 'readonly')

    from_ , to_ = to_, from_
    
    from_curr = convert_from.get()
    to_curr = convert_to.get()
    convert_from.set(to_curr)
    convert_to.set(from_curr)

    amount = top

    if amount:
        # Convert the amount based on the new currencies
        convert_currency()
        


#a function that appends the text value of the buttons to the entry field
def on_button_click(button_text, entry_top):
    current_text = entry_top.get()
    new_text = current_text + button_text
    entry_top.delete(0, tk.END)
    entry_top.insert(0, new_text)


# A function that evaluated the expression when the user clicks equal to
def evaluate_expression(entry_top):
    expression = entry_top.get()

    entry_bottom.config(state= 'normal')
    entry_bottom.delete(0, tk.END)
    entry_bottom.config(state= 'readonly')
    
    try:
        # Evaluate the expression
        result = eval(expression)
        print(result)
        # Update the entry with the result
        entry_top.delete(0, tk.END)
        entry_top.insert(0, (result))
        
        if result:
            convert_currency()

    except Exception as e:
        # Handle any errors (e.g., invalid expression)
        entry_top.delete(0, tk.END)
        entry_top.insert(0, "Error")
    


# Function to create a simple GUI with Tkinter
def create_gui():
    global root,status,status_label, answer, convert_from, convert_to, entry_top, entry_bottom
    root = tk.Tk()
    root.title("Currency Converter")

    # setting relative path for icon
    # def resource_path(relative_path):
    #     try:
    #         base_path = sys._MEIPASS
    #     except Exception:
    #         base_path = os.path.abspath(".")
    #     return os.path.join(base_path, relative_path)

    # root.iconbitmap(resource_path('icon.ico'))

    # windows title icon not working
    
    root.geometry(f"{fixed_width}x{fixed_height}")
    root.resizable(False, False)


    label = tk.Label(root, text="ZIGLA'S CURRENCY CONVERTER")
    label.pack()


    mode_frame = tk.Frame(root, width=20)
    mode_frame.pack()

    status_label = tk.Label(mode_frame, text="Checking...", font=('Helvetica', 12))
    status_label.pack(side="left")

    # # Start checking the connection
    check_connection()

    refresh_button = tk.Button(mode_frame, text="REFRESH", command=Refresh)
    refresh_button.pack(side='right')


    # Create a Frame to hold the entries, labels, and buttons
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    convert_from = tk.StringVar()
    convert_to = tk.StringVar()
    answer = tk.StringVar()
    convert_from.set(from_)
    convert_to.set(to_)

    # Create and place the label, button, and entry for the top entry
    label_top = tk.Label(frame, text="CONVERT FROM:")
    label_top.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Label at (0, 0)
    button_top = tk.Button(frame, textvariable=convert_from, command= to_convert_from)
    button_top.grid(row=0, column=1, padx=5, pady=5)  # Button at (0, 1)
    entry_top = tk.Entry(frame, width=30)
    entry_top.grid(row=0, column=2, padx=5, pady=5)  # Entry at (0, 2)

    # Create and place the label, button, and entry for the bottom entry
    label_bottom = tk.Label(frame, text="CONVERT TO:")
    label_bottom.grid(row=1, column=0, padx=5, pady=5, sticky="e")  # Label at (1, 0)
    button_bottom = tk.Button(frame, textvariable=convert_to, command=to_convert_to)
    button_bottom.grid(row=1, column=1, padx=5, pady=5)  # Button at (1, 1)
    entry_bottom = tk.Entry(frame, width=30, textvariable=answer, state="readonly")
    entry_bottom.grid(row=1, column=2, padx=5, pady=5)  # Entry at (1, 2)

    #create a button to convert
    convert_button = tk.Button(frame, text="CONVERT", command=convert_currency)
    convert_button.grid(row=3, column=2, padx=5, pady=5)

    # Create the bottom frame to hold the grid of buttons
    bottom_frame = tk.Frame(root, padx=10, pady=10)
    bottom_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create and place buttons in the bottom frame (4 columns x 5 rows) with individual commands
    clear_button = tk.Button(bottom_frame, text="CLEAR", width=10, height=2, command=clear_all)
    clear_button.grid(row=0, column=0, padx=5, pady=5)

    delete_button = tk.Button(bottom_frame, text="DELETE", width=10, height=2, command= delete_last)
    delete_button.grid(row=0, column=1, padx=5, pady=5)

    swap_button = tk.Button(bottom_frame, text="SWAP", width=10, height=2, command= swap_currencies)
    swap_button.grid(row=0, column=2, padx=5, pady=5)

    divide_button = tk.Button(bottom_frame, text="/", width=10, height=2, command=lambda: on_button_click("/", entry_top))
    divide_button.grid(row=0, column=3, padx=5, pady=5)

    # Repeat for other buttons, adjusting the row and column as needed
    button7 = tk.Button(bottom_frame, text="7", width=10, height=2, command=lambda: on_button_click("7", entry_top))
    button7.grid(row=1, column=0, padx=5, pady=5)

    button8 = tk.Button(bottom_frame, text="8", width=10, height=2, command=lambda: on_button_click("8", entry_top))
    button8.grid(row=1, column=1, padx=5, pady=5)

    button9 = tk.Button(bottom_frame, text="9", width=10, height=2, command=lambda: on_button_click("9", entry_top))
    button9.grid(row=1, column=2, padx=5, pady=5)

    multiply_button = tk.Button(bottom_frame, text="*", width=10, height=2, command=lambda: on_button_click("*", entry_top))
    multiply_button.grid(row=1, column=3, padx=5, pady=5)

    button4 = tk.Button(bottom_frame, text="4", width=10, height=2, command=lambda: on_button_click("4", entry_top))
    button4.grid(row=2, column=0, padx=5, pady=5)

    button5 = tk.Button(bottom_frame, text="5", width=10, height=2, command=lambda: on_button_click("5", entry_top))
    button5.grid(row=2, column=1, padx=5, pady=5)

    button6 = tk.Button(bottom_frame, text="6", width=10, height=2, command=lambda: on_button_click("6", entry_top))
    button6.grid(row=2, column=2, padx=5, pady=5)

    minus_button = tk.Button(bottom_frame, text="-", width=10, height=2, command=lambda: on_button_click("-", entry_top))
    minus_button.grid(row=2, column=3, padx=5, pady=5)

    button1 = tk.Button(bottom_frame, text="1", width=10, height=2, command=lambda: on_button_click("1", entry_top))
    button1.grid(row=3, column=0, padx=5, pady=5)

    button2 = tk.Button(bottom_frame, text="2", width=10, height=2, command=lambda: on_button_click("2", entry_top))
    button2.grid(row=3, column=1, padx=5, pady=5)

    button3 = tk.Button(bottom_frame, text="3", width=10, height=2,command=lambda: on_button_click("3", entry_top))
    button3.grid(row=3, column=2, padx=5, pady=5)

    add_button = tk.Button(bottom_frame, text="+", width=10, height=2, command=lambda: on_button_click("+", entry_top))
    add_button.grid(row=3, column=3, padx=5, pady=5)

    # Repeat for other buttons, adjusting the row and column as needed
    dot_button = tk.Button(bottom_frame, text=".", width=10, height=2, command=lambda: on_button_click(".", entry_top))
    dot_button.grid(row=4, column=0, padx=5, pady=5)

    button0 = tk.Button(bottom_frame, text="0", width=10, height=2, command=lambda: on_button_click("0", entry_top))
    button0.grid(row=4, column=1, padx=5, pady=5)

    button00 = tk.Button(bottom_frame, text="00", width=10, height=2, command=lambda: on_button_click("00", entry_top))
    button00.grid(row=4, column=2, padx=5, pady=5)

    equal_button = tk.Button(bottom_frame, text="=", width=10, height=2, command=lambda: evaluate_expression(entry_top))
    equal_button.grid(row=4, column=3, padx=5, pady=5)

    # Configure the frame's grid to center the widgets
    for i in range(5):
        bottom_frame.grid_rowconfigure(i, weight=1)

    for j in range(4): 
        bottom_frame.grid_columnconfigure(j, weight=1)

    apply_styles(root)


    root.mainloop()


    
def back_to_main_phase():
     # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    global status,status_label, answer, convert_from, convert_to, entry_top, entry_bottom

    root.title("Currency Converter")
    root.geometry(f"{fixed_width}x{fixed_height}")

    label = tk.Label(root, text="ZIGLA'S CURRENCY CONVERTER")
    label.pack()


    mode_frame = tk.Frame(root, width=20)
    mode_frame.pack()

    status_label = tk.Label(mode_frame, text="Checking...", font=('Helvetica', 12))
    status_label.pack(side="left")

    
    refresh_button = tk.Button(mode_frame, text="REFRESH", command=Refresh)
    refresh_button.pack(side='right')


    # Create a Frame to hold the entries, labels, and buttons
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    convert_from = tk.StringVar()
    convert_to = tk.StringVar()
    answer = tk.StringVar()
    convert_from.set(from_)
    convert_to.set(to_)

    # Create and place the label, button, and entry for the top entry
    label_top = tk.Label(frame, text="CONVERT FROM:")
    label_top.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Label at (0, 0)
    button_top = tk.Button(frame, textvariable=convert_from, command= to_convert_from)
    button_top.grid(row=0, column=1, padx=5, pady=5)  # Button at (0, 1)
    entry_top = tk.Entry(frame, width=30)
    entry_top.grid(row=0, column=2, padx=5, pady=5)  # Entry at (0, 2)

    # Create and place the label, button, and entry for the bottom entry
    label_bottom = tk.Label(frame, text="CONVERT TO:")
    label_bottom.grid(row=1, column=0, padx=5, pady=5, sticky="e")  # Label at (1, 0)
    button_bottom = tk.Button(frame, textvariable=convert_to, command=to_convert_to)
    button_bottom.grid(row=1, column=1, padx=5, pady=5)  # Button at (1, 1)
    entry_bottom = tk.Entry(frame, width=30, textvariable=answer, state="readonly")
    entry_bottom.grid(row=1, column=2, padx=5, pady=5)  # Entry at (1, 2)

    #create a button to convert
    convert_button = tk.Button(frame, text="CONVERT", command=convert_currency)
    convert_button.grid(row=3, column=2, padx=5, pady=5)

    # Create the bottom frame to hold the grid of buttons
    bottom_frame = tk.Frame(root, padx=10, pady=10)
    bottom_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create and place buttons in the bottom frame (4 columns x 5 rows) with individual commands
    clear_button = tk.Button(bottom_frame, text="CLEAR", width=10, height=2, command=clear_all)
    clear_button.grid(row=0, column=0, padx=5, pady=5)

    delete_button = tk.Button(bottom_frame, text="DELETE", width=10, height=2, command= delete_last)
    delete_button.grid(row=0, column=1, padx=5, pady=5)

    swap_button = tk.Button(bottom_frame, text="SWAP", width=10, height=2, command= swap_currencies)
    swap_button.grid(row=0, column=2, padx=5, pady=5)

    divide_button = tk.Button(bottom_frame, text="/", width=10, height=2, command=lambda: on_button_click("/", entry_top))
    divide_button.grid(row=0, column=3, padx=5, pady=5)

    # Repeat for other buttons, adjusting the row and column as needed
    button7 = tk.Button(bottom_frame, text="7", width=10, height=2, command=lambda: on_button_click("7", entry_top))
    button7.grid(row=1, column=0, padx=5, pady=5)

    button8 = tk.Button(bottom_frame, text="8", width=10, height=2, command=lambda: on_button_click("8", entry_top))
    button8.grid(row=1, column=1, padx=5, pady=5)

    button9 = tk.Button(bottom_frame, text="9", width=10, height=2, command=lambda: on_button_click("9", entry_top))
    button9.grid(row=1, column=2, padx=5, pady=5)

    multiply_button = tk.Button(bottom_frame, text="*", width=10, height=2, command=lambda: on_button_click("*", entry_top))
    multiply_button.grid(row=1, column=3, padx=5, pady=5)

    button4 = tk.Button(bottom_frame, text="4", width=10, height=2, command=lambda: on_button_click("4", entry_top))
    button4.grid(row=2, column=0, padx=5, pady=5)

    button5 = tk.Button(bottom_frame, text="5", width=10, height=2, command=lambda: on_button_click("5", entry_top))
    button5.grid(row=2, column=1, padx=5, pady=5)

    button6 = tk.Button(bottom_frame, text="6", width=10, height=2, command=lambda: on_button_click("6", entry_top))
    button6.grid(row=2, column=2, padx=5, pady=5)

    minus_button = tk.Button(bottom_frame, text="-", width=10, height=2, command=lambda: on_button_click("-", entry_top))
    minus_button.grid(row=2, column=3, padx=5, pady=5)

    button1 = tk.Button(bottom_frame, text="1", width=10, height=2, command=lambda: on_button_click("1", entry_top))
    button1.grid(row=3, column=0, padx=5, pady=5)

    button2 = tk.Button(bottom_frame, text="2", width=10, height=2, command=lambda: on_button_click("2", entry_top))
    button2.grid(row=3, column=1, padx=5, pady=5)

    button3 = tk.Button(bottom_frame, text="3", width=10, height=2,command=lambda: on_button_click("3", entry_top))
    button3.grid(row=3, column=2, padx=5, pady=5)

    add_button = tk.Button(bottom_frame, text="+", width=10, height=2, command=lambda: on_button_click("+", entry_top))
    add_button.grid(row=3, column=3, padx=5, pady=5)

    # Repeat for other buttons, adjusting the row and column as needed
    dot_button = tk.Button(bottom_frame, text=".", width=10, height=2, command=lambda: on_button_click(".", entry_top))
    dot_button.grid(row=4, column=0, padx=5, pady=5)

    button0 = tk.Button(bottom_frame, text="0", width=10, height=2, command=lambda: on_button_click("0", entry_top))
    button0.grid(row=4, column=1, padx=5, pady=5)

    button00 = tk.Button(bottom_frame, text="00", width=10, height=2, command=lambda: on_button_click("00", entry_top))
    button00.grid(row=4, column=2, padx=5, pady=5)

    equal_button = tk.Button(bottom_frame, text="=", width=10, height=2, command=lambda: evaluate_expression(entry_top))
    equal_button.grid(row=4, column=3, padx=5, pady=5)

    # Configure the frame's grid to center the widgets
    for i in range(5):  # 5 rows
        bottom_frame.grid_rowconfigure(i, weight=1)

    for j in range(4):  # 4 columns
        bottom_frame.grid_columnconfigure(j, weight=1)

    apply_styles(root)

    check_connection()





#create a duplicate of the show currency phase so that we handle different event in different button clicks
def to_convert_from():
    # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    global search_entry, search_button, listbox_frame, listbox, item_key, from_, to_

    # Create a title label
    title_label = tk.Label(root, text="Countries and Currencies", font=("Arial", 16))
    title_label.pack(pady=2)

    search_entry = tk.Entry(root, width=50)
    search_entry.pack()

    search_button = tk.Button(root, text="SEARCH", command=search)
    search_button.pack(pady=1)

    # Create a new frame for the currency phase
    currency_frame = tk.Frame(root, padx=10, pady=10)
    currency_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a canvas and scrollbar for scrolling
    canvas = tk.Canvas(currency_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a frame inside the canvas to hold the listbox
    listbox_frame = tk.Frame(canvas)
    listbox_frame.pack(pady=10)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(listbox_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    # Function to display key-value pairs
    def show_details(event):
        global item_key, from_, to_
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            item_display = listbox.get(index).strip()  # Get the displayed string
            item = item_display.split()  # Extract value and key from displayed string
            detail_label.config(text=f"Country: {item[0]}\nCurrency: {item[-1]}")
            from_ = item[-1]
        else:
            detail_label.config(text="No item selected.")
        
    # Add a listbox inside the frame
    listbox = tk.Listbox(listbox_frame, width=85, height=27, yscrollcommand=scrollbar.set)
    
    for currency in currency_data:
        listbox.insert(tk.END, f"{" ".join(currency_data[currency][0:])}: {currency}")

    listbox.pack(side=tk.LEFT)
    scrollbar.config(command=listbox.yview)

    #bind the listbox with an action
    # Bind the click event to the show_details function
    listbox.bind("<<ListboxSelect>>", show_details)

    # Label to display item details
    detail_label = tk.Label(canvas, text="", justify=tk.LEFT)
    detail_label.pack(pady=10, side="left")  

    # Add a back button to return to the main phase
    back_button = tk.Button(canvas, text="Back", command=back_to_main_phase)
    back_button.pack(side="right", padx = 20)

    apply_styles(root)




#create a duplicate of the show currency phase so that we handle different event in different button clicks
def to_convert_to():
    # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    global search_entry, search_button, listbox_frame, listbox, item_key

    # Create a title label
    title_label = tk.Label(root, text="Countries and Currencies", font=("Arial", 16))
    title_label.pack(pady=2)

    search_entry = tk.Entry(root, width=50)
    search_entry.pack()

    search_button = tk.Button(root, text="SEARCH", command=search)
    search_button.pack(pady=1)

    # Create a new frame for the currency phase
    currency_frame = tk.Frame(root, padx=10, pady=10)
    currency_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a canvas and scrollbar for scrolling
    canvas = tk.Canvas(currency_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a frame inside the canvas to hold the listbox
    listbox_frame = tk.Frame(canvas)
    listbox_frame.pack(pady=10)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(listbox_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    # Function to display key-value pairs
    def show_details(event):
        global item_key, from_, to_
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            item_display = listbox.get(index).strip()  # Get the displayed string
            item = item_display.split()  # Extract value and key from displayed string
            detail_label.config(text=f"Country: {item[0]}\nCurrency: {item[-1]}")
            to_ = item[-1]
        else:
            detail_label.config(text="No item selected.")
        
    # Add a listbox inside the frame
    listbox = tk.Listbox(listbox_frame, width=85, height=27, yscrollcommand=scrollbar.set)
        # Use the provided data dictionary
    for currency in currency_data:
        listbox.insert(tk.END, f"{" ".join(currency_data[currency][0:])}: {currency}")
    
    listbox.pack(side=tk.LEFT)
    scrollbar.config(command=listbox.yview)

    #bind the listbox with an action
    # Bind the click event to the show_details function
    listbox.bind("<<ListboxSelect>>", show_details)

    # Label to display item details
    detail_label = tk.Label(canvas, text="", justify=tk.LEFT)
    detail_label.pack(pady=10, side="left")  

    # Add a back button to return to the main phase
    back_button = tk.Button(canvas, text="Back", command=back_to_main_phase)
    back_button.pack(side="right", padx = 20)

    apply_styles(root)


# Start app by Creating GUI
create_gui()
