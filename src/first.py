'''
Created on 8 Nov 2011

@author: alec
'''
import requests

params = {'nonce': 'd4b7e1ee-9798-f345-a483-ef814ad600c9', 'b': 'staging-cxserver-icg', 'rr': '', 'ls': '0', 'w': 'http://172.17.100.75:4000', 'dw': 'Enable', 'wr': ''}

requests.get("http://127.0.0.1:8000/", params=params)
