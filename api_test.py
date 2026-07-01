import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# Проверяваме дали сървърът ни е отговорил с 200 OK (Успех)
if response.status_code == 200:
    data = response.json()
    print(data[0]["name"])
else:
    print(f"Грешка при връзка със сървъра. Код: {response.status_code}")