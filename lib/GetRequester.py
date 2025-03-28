import requests
import json

class GetRequester:
    def __init__(self, url):
        """Initialize with a URL."""
        self.url = url

    def get_response_body(self):
        """Sends a GET request and returns the response body as bytes."""
        response = requests.get(self.url)
        return response.content  # Returns raw response as bytes

    def load_json(self):
        """Parses the JSON response and returns a Python dictionary or list."""
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))  # Convert bytes to string before loading JSON

# Example usage:
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    get_requester = GetRequester(url)

    print("\nRaw Response Body (Bytes):")
    print(get_requester.get_response_body())  # Should now match the test

    print("\nParsed JSON Data:")
    print(json.dumps(get_requester.load_json(), indent=4))  # Pretty-print JSON
