#!/usr/bin/python3
""" Pythonn script that fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://aluswe.com/projects') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
