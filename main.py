import requests


def main(place):
    url = 'https://wttr.in/{}?lang=ru&M&n&q&T'.format(place)
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    print(main('Лондон'), main('аэропорт Шереметьево'), main('Череповец'))