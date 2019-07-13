from pathlib import Path
import pickle

class GooglePhotos:
    """"""

    # redundance naming
    cache = authentic_cache = credential = None

    def __init__(self, client_secret=None):
        self.authenticated = False
        self._client_secret = client_secret
    
    def try2find_client_secret(self):
        if self._client_secret:
            return
            
        # search current dir
        for client_secret_file in Path.cwd().glob('client_secret*.json'):
            self._client_secret = client_secret_file.absolute()

    def authenticate(self):
        self.try2find_client_secret()

    @classmethod
    def readPickledCache(cls, cache):
        creds = pickle.loads(cache)
        from google_auth_httplib2 import Request

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
    
    @classmethod
    def readFromDataStore(cls, key=None):
        from google.cloud import datastore

        client = datastore.Client()

        if key is None:
            key = ('googlephoto.py', 'credential')

        key2creds = client.key(*key)
        dsCreds = client.get(key2creds)
        if dsCreds:
            return cls.readPickledCache(dsCreds['PickledCache'])

        else:
            raise Exception('Fail to read creditial cache from Google DataStore')
    
    @property
    def authenticated(self):
        try:
            _ = self.service
        except NameError:
            return False

        return True