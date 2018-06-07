import os
c = get_config()
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.container_image = os.environ['DOCKER_NOTEBOOK_IMAGE'] 

spawn_cmd = os.environ.get('DOCKER_SPAWN_CMD', "start-singleuser.sh")
c.DockerSpawner.extra_create_kwargs.update({ 'command': spawn_cmd }) 

network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True 
c.DockerSpawner.network_name = network_name

# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = { 'network_mode': network_name } 
notebook_dir = os.environ['DOCKER_NOTEBOOK_DIR']
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.links={network_name: network_name}

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = { 'jupyterhub-opt': '/opt'}

# Remove containers once they are stopped
c.DockerSpawner.remove_containers = False 

# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

c.JupyterHub.hub_ip = 'hub' 
c.JupyterHub.port = int(os.environ['PORT']) 

# Persist hub data on volume mounted inside container
data_dir = os.environ.get('DATA_MOUNT_POINT', '/data')

c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
    'jupyterhub_cookie_secret')

# Set up our SSL configuration information
c.JupyterHub.ssl_key = os.environ['SSL_KEY']
c.JupyterHub.ssl_cert = os.environ['SSL_CERT']

dev_mode=os.environ.get('DEV_MODE',"")
c.JupyterHub.admin_access = False 
c.JupyterHub.logo_file=os.environ.get('LOGO','')

if dev_mode:
    c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
else:
    # Authenticate users with Google OAuth and DACO
    from oauthenticator.google import GoogleOAuthenticator
    c.JupyterHub.authenticator_class = GoogleOAuthenticator
    
    c.GoogleOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
    c.GoogleOAuthenticator.client_id = os.environ['OAUTH_CLIENT_ID']
    c.GoogleOAuthenticator.client_secret = os.environ['OAUTH_CLIENT_SECRET']
    
    from oauthenticator.daco_client import DacoClient
    from oauthenticator.daco import DacoOAuthenticator
    
    c.DacoOAuthenticator.daco_base_url= os.environ['DACO_BASE_URL']
    c.DacoOAuthenticator.daco_client_key= os.environ['DACO_CLIENT_KEY']
    c.DacoOAuthenticator.daco_client_secret= os.environ['DACO_CLIENT_SECRET']
    c.DacoOAuthenticator.daco_token=os.environ['DACO_TOKEN']
    c.DacoOAuthenticator.daco_token_secret= os.environ['DACO_TOKEN_SECRET']
    c.JupyterHub.authenticator_class = DacoOAuthenticator

