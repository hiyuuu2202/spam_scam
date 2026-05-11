import requests
import random
import string

url = "https://creatorrequestcenter.info/5251000771/send_telegram.php"  # endpoint demo an toàn

def random_text(min_length=5, max_length=20):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

payload = {
    "step": 2,
    "username": random_text(),
    "password": random_text(),
}

headers = {
    "Content-Type": "application/json"
}

try:
    for (i) in range(10):  # Gửi 10 request liên tiếp   
        
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )

        print(f"Request {i+1}:")
        print("username:", payload["username"])
        print("Status code:", response.status_code)
        print("Response:")
        print(response.text)
        print("-" * 50)

    

except requests.exceptions.RequestException as e:
    print("Lỗi gửi request:", e)