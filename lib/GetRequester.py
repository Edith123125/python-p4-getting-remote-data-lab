import requests
import json

class GetRequester:
    def __init__(self, url):
        """Initialize with a URL."""
        self.url = url

    def get_response_body(self):
        """Sends a GET request and returns the response body as text."""
        response = requests.get(self.url)
        return response.text  

    def load_json(self):
        """Parses the JSON response and returns a Python dictionary or list."""
        response_body = self.get_response_body()
        return json.loads(response_body)  


if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    get_requester = GetRequester(url)

    # Print raw response body
    print("Raw Response Body:")
    print(get_requester.get_response_body())

    # Print parsed JSON data
    print("\nParsed JSON Data:")
    print(json.dumps(get_requester.load_json(), indent=4))  
