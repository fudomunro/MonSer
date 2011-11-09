'''
Created on 8 Nov 2011

@author: alec
'''
from util import DictTemplate
import requests

DEFAULT_HOST = "http://staging.cxserver.lb/balancer-manager"
DEFAULT_NAME = "staging-cxserver-icg"
    
LB_PARAMS = DictTemplate(
    base = {'nonce': 'd4b7e1ee-9798-f345-a483-ef814ad600c9', 
            'rr': '', 'ls': '0', 'wr': ''},
    required = ('b', 'w', "dw"))


class ModProxyBalancerClient(object):
    """A simple network client to facilitate access to a mod_proxy_balancer
    interface.
    
    Primarily intended to enable or disable worker nodes."""
    
    def __init__(self, url, name):
        self.url = url
        self.name = name
        
        
    def make_request(self, worker, action):
        params = LB_PARAMS(b=self.name, w=worker, dw=action)
        print("Making request")
        requests.get(self.url, params=params)
        
    
    def enable(self, worker):
        """Enable the node at address *worker*."""
        self.make_request(worker=worker, action="enable")
        
    
    def disable(self, worker):
        """Disable the node at address *worker*."""
        self.make_request(worker=worker, action="disable")
    
    
if __name__ == "__main__":
    import sys
    try:
        action = sys.argv[1]
        worker = sys.argv[2]
        client = ModProxyBalancerClient(url="http://127.0.0.1:8000/", name=DEFAULT_NAME)
        if action == "enable":
            print("Enabling")
            client.enable(worker)
    except IndexError:
        print("Expects at least two arguments: action and host.")
    
    