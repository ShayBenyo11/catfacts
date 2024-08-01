import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    while True:
        # Make a request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            fact_text = data.get("fact", "")
            fact_length = data.get("length", 0)
            
            # Check if the length of the fact is higher than 200
            if fact_length > 200:
                break
            else:
                print(fact_text)
               # print(" Length:" + str(fact_length))
        else:
            print(f"Error: Unable to fetch data (status code: {response.status_code})")

get_cat_fact()
