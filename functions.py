import requests

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
