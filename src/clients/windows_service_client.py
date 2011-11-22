'''
Created on 2011-11-21

@author: Alec
'''
import subprocess

SERVICE_CMD = "sc"
START_CMD = "start"
STOP_CMD = "stop"
ADDR_TMPL = r"\\{0}"

class WindowsServiceClient(object):
    
    
    def __init__(self, machine):
        self.machine = ADDR_TMPL.format(machine)
    
    
    def start_service(self, service_name):
        subprocess.Popen([SERVICE_CMD, self.machine, 
                          START_CMD, service_name])
        
    def stop_service(self, service_name):
        subprocess.Popen([SERVICE_CMD, self.machine, 
                          STOP_CMD, service_name])
        
        
if __name__ == "__main__":
    WindowsServiceClient("arcvm").start_service("Alerter")
    
    



