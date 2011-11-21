'''
Created on 2011-11-21

@author: Alec
'''
from unittest.case import TestCase
import clients.windows_service_client as mut

SAMPLE_SERVICE = "Widgit factory"

class TestWindowsServiceClient(TestCase):
    
    def test_start(self):
        client = mut.WindowsServiceClient()
        client.start_service(service_name=SAMPLE_SERVICE)