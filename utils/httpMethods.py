import allure
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
        with allure.step('GET'):
            Logger.add_request(url, method='GET')
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, data):
        with allure.step('POST'):
            Logger.add_request(url, method='POST')
            result = requests.post(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, data):
        with allure.step('PUT'):
            Logger.add_request(url, method='PUT')
            result = requests.put(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, data):
        with allure.step('DELETE'):
            Logger.add_request(url, method='DELETE')
            result = requests.delete(url, json=data, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result
