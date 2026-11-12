import json
import socket
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

def fetch_profile(login):
    if not login:
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + login
    req = Request(url, headers={"User-Agent": "python-course"})
    with urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
        if "login" not in data:
            raise ValueError("Ответ не похож на профиль")
        return data

def main():
    try:
        login = input("Введите логин GitHub: ")
        data = fetch_profile(login)
        with open("profile.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Профиль сохранен:", data["login"])
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
