import requests

params = {
    "amount": 10,
    "category": 18,
    "difficulty": "easy",
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
response = response.json()
quiz_list = response["results"]