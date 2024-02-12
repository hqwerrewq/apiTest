import requests


class HttpMethods:
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    cookie = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url, data):
        result = requests.post(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def put(url, data):
        result = requests.put(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def delete(url, data):
        result = requests.delete(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
