import os
import hvac

""" Class for initializing, configuring, and handling the Vault client. """
class client:

    """ Initialize the client class. """
    def __init__(self, url='https://localhost:8200', vault_online = True, client=hvac.Client()):
        self.url = url
        self.vault_online = vault_online
        self.client = client

    def start_server(self):
        #gonna have to hunt for path to vault and start the server
        #once the server is started, do the following
        if not self.client.is_initialized():
            new_server = self.client.initialize(5, 3)
            root_tok = result['root_token']
            seal_keys = result['keys']

    def stop_server():
        #stop server here

    def unseal_vault():
        #unseal vault here

    def seal_vault():
        #seal vault here

    def create_secret():
        #create secret here

    def read_secret():
        #read secret here

    def update_secret():
        #update secret here

    def delete_secret():
        #delete secret here
