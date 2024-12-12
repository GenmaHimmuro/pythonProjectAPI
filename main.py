import requests


def main():
    places = ['аэропорт Шереметьево', 'Лондон', "Череповец"]
    payload = {'lang=ru':'','M':'','n':'','q':'','T':''}
    for place in places:
        url = 'https://wttr.in/{}'.format(place)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()