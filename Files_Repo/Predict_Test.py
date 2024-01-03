import requests

# URL where the Flask app is hosted
url = 'http://localhost:9696/recommend'

# The title of the anime for which you want recommendations
anime_title = {"title": "Naruto"}

try:
    # Make a GET request to the Flask app
    response = requests.get(url, params=anime_title)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Try to parse the JSON response
            recommendations = response.json()
            print("Recommended Anime Titles:", recommendations)
        except ValueError:
            # Handle the case where response is not in JSON format
            print("Response is not in JSON format:", response.text)
    else:
        # Print the status code and response text if not successful
        print("Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    # Print any request exceptions that occur
    print("Request Exception:", e)
