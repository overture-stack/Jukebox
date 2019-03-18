import os
c = get_config()
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = "{{ notebook_image }}"

spawn_cmd = "{{ docker_spawn_cmd }}"
c.DockerSpawner.extra_create_kwargs.update({ 'command': spawn_cmd }) 

# This is the address of the docker container that runs the 'hub' service
# on the internal docker network we've created for jupyterhub and it's
# notebooks.
c.JupyterHub.hub_ip = 'hub' 
c.DockerSpawner.use_internal_ip = True 

network_name = "{{ docker_network_name }}" 
c.DockerSpawner.network_name = network_name

# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config.update({ 'network_mode': network_name, 'devices': ['/dev/fuse:/dev/fuse:rwm'], 'cap_add': ['SYS_ADMIN'], 'security_opt': ['apparmor=unconfined'] })
c.DockerSpawner.links={network_name: network_name}

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
opt_volume = "{{ opt_volume }}"
opt_mount = "{{ opt_mount }}" 

c.DockerSpawner.volumes = { opt_volume: opt_mount }

# Don't remove containers once they are stopped; let people log back in again
# later on!
c.DockerSpawner.remove_containers = False 

# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

c.JupyterHub.port = int("{{ jupyterhub_port }}") 

# Persist hub data on volume mounted inside container
data_dir = "{{ data_mount_point }}"

c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
    'jupyterhub_cookie_secret')

# Set up our SSL configuration information
c.JupyterHub.ssl_key = "{{ config_mount }}/{{ ssl_key }}"
c.JupyterHub.ssl_cert = "{{ config_mount }}/{{ ssl_cert }}"

use_oauth="{{ use_oauth }}"
c.JupyterHub.admin_access = False 
c.JupyterHub.logo_file="{{ logo_path }}"

# Authenticate users with Google OAuth and DACO
if use_oauth.lower() == 'true':
    from oauthenticator.google import GoogleOAuthenticator
    c.JupyterHub.authenticator_class = GoogleOAuthenticator
    
    c.GoogleOAuthenticator.oauth_callback_url = "{{ oauth_callback_url }}"
    c.GoogleOAuthenticator.client_id = "{{ oauth_client_id }}"
    c.GoogleOAuthenticator.client_secret = "{{ oauth_client_secret }}"

# Use DACO only with OAuth
use_daco="{{ use_daco }}"
if use_daco.lower() == 'true':
    from oauthenticator.daco_client import DacoClient
    from oauthenticator.daco import DacoOAuthenticator

    c.DacoOAuthenticator.daco_base_url = "{{ daco_base_url }}"
    c.DacoOAuthenticator.daco_client_key = "{{ daco_client_key }}"
    c.DacoOAuthenticator.daco_client_secret = "{{ daco_client_secret }}"
    c.DacoOAuthenticator.daco_token = "{{ daco_token }}"
    c.DacoOAuthenticator.daco_token_secret = "{{ daco_token_secret }}"
    c.JupyterHub.authenticator_class = DacoOAuthenticator

else:
    c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
