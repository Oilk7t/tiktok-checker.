import requests
import random
import string
import time

TOKEN = '7306215437:AAHlnPRubepYAyEo-wOlsK662Q-HTnqekHw'
CHAT_ID = '6103417856'

def generate_username():
    length = random.choice([4, 5])
    characters = string.ascii_lowercase + string.digits + "._"
    return ''.join(random.choices(characters, k=length))

def check_username(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 404

def send_to_telegram(username):
    msg = f"يوزر متاح على تيك توك:\n@{username}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

while True:
    user = generate_username()
    print(f"جاري فحص: @{user}")
    try:
        if check_username(user):
            print(f"متاح: @{user}")
            send_to_telegram(user)
        else:
            print("مو متاح.")
    except Exception as e:
        print("خطأ:", e)
    time.sleep(2)
