import os
import json

settings = None

class Settings(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'testsettings.json')) as f:
            settings = json.load(f)
            self.browser = settings['browser']
            self.portal_url = settings['portal_url']
            self.portal_env = settings['portal_env']
            
settings = Settings()