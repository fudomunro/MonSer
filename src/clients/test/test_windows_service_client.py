'''
Created on 2011-11-21

@author: Alec
'''
from unittest.case import TestCase
import clients.windows_service_client as mut
import mock

SAMPLE_SERVICE = "Widgit factory"
SAMPLE_MACHINE = "Grandma"
SAMPLE_ADDR = mut.ADDR_TMPL.format(SAMPLE_MACHINE)

class TestWindowsServiceClient(TestCase):
    
    @mock.patch("subprocess.Popen")
    def test_start(self, m_Popen):
        """Start a service."""
        client = mut.WindowsServiceClient(SAMPLE_MACHINE)
        client.start_service(service_name=SAMPLE_SERVICE)
        m_Popen.assert_called_with([mut.SERVICE_CMD, SAMPLE_ADDR, mut.START_CMD, 
                                    SAMPLE_SERVICE])
        
    
    @mock.patch("subprocess.Popen")
    def test_stop(self, m_Popen):
        """Stop a service."""
        client = mut.WindowsServiceClient(SAMPLE_MACHINE)
        client.stop_service(service_name=SAMPLE_SERVICE)
        m_Popen.assert_called_with([mut.SERVICE_CMD, SAMPLE_ADDR, mut.STOP_CMD, 
                                    SAMPLE_SERVICE])
        
