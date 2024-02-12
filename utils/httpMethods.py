import requests

from utils.logger import Logger


class HttpMethods:
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    cookie = ''

    @staticmethod
    def get(url):
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, data):
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, data):
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, data):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result
