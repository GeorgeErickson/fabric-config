import sys, os, yaml

sys.path.insert(0, os.path.dirname(__file__))

DEFAULTS = {
    'config_name': 'fabric_config.yaml',
}


def setup(namespaces=['hosts']):
    """
    Takes all modules named in namespaces and imports them into the fabfile.
    
    """
    config_path = os.path.join(os.getcwd(), DEFAULTS['config_name'])
    
    #convert config_file to dict
    with open(config_path) as config_file:
        config = yaml.load(config_file.read())
    
    for namespace in namespaces:
        ns_module = __import__(namespace)
        ns_module.setup(config)
    
    fab_module = sys.modules['fabfile']
    setattr(fab_module, namespace, ns_module)
    
