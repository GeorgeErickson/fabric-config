import sys
from fabric.tasks import Task
from fabric.api import env

class GenericHostTask(Task):
    doc = "Sets env.host = %s"
    
    def __init__(self, host_name, host_url):
        self.name = "%s" % host_name
        self.__doc__ = self.doc % host_url
        self.host_url = host_url
    
    def run(self):
        env.hosts = [self.host_url]

def setup(config):
    module = sys.modules[__name__]
    
    for host_name, host_url in config['hosts'].items():
        generic_task = GenericHostTask(host_name, host_url)
        setattr(module, generic_task.name, generic_task)




        
