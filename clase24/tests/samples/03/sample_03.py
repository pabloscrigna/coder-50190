import requests


def get_url(url: str):
    r = requests.get(url)

    if r.status_code == 200:
        return r.status_code, r.text
    
    return r.status_code, None

if __name__ == "__main__":
    response = get_url('https://www.clarin.com')

    print(response[1])