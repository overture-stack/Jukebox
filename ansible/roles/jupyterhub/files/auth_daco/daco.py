import json
import subprocess
from traitlets import Unicode
from tornado import gen
from oauthenticator.daco_client import DacoClient, DacoException
from tornado.web import HTTPError
from oauthenticator.google import GoogleOAuthenticator
def log(msg, *args):
    subprocess.run(['logger',msg.format(*args)])

class DacoOAuthenticator(GoogleOAuthenticator):
    daco_base_url = Unicode(config=True)
    daco_client_key = Unicode(config=True)
    daco_client_secret = Unicode(config=True)
    daco_token = Unicode(config=True)
    daco_token_secret = Unicode(config=True)

    @gen.coroutine
    def authenticate(self, handler, data=None):
        # Google authentication either succeeds or throws an exception
        auth= yield super().authenticate(handler, data)

        # Confirm that they have DACO access, and return our
        # Google authentication credentials
        email = auth['name']
        self.daco_client = DacoClient(
            base_url=self.daco_base_url,
            client_key=self.daco_client_key,
            client_secret=self.daco_client_secret, 
            token=self.daco_token, 
            token_secret=self.daco_token_secret)
        try:
            self.daco_client.get_daco_status(email)
        except DacoException as e:
            raise HTTPError(403, "User '{}' does not have DACO authorization".format(email))
        log("Returning auth='{}'", auth)
        return auth 
