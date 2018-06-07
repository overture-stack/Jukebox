# How to configure Jukebox for your Openstack system
1. Create a secrets directory to store all of the passwords, private keys, and
other secret data that ansible will use to configure your system.
eg. % mkdir ~/secrets

2. Run create_templates.sh.  

3. Go into your secrets directory, and create enter your private keys and password settings into the ansible_secrets.yml and jupyterhub_oath.env files. 

```    
# Google OAuth Settings
# To use Google's Single Sign on mechanism, we need a valid email address,
# and we need to get a client_id and a client secret from them.
#
# We can generate these credentials by using Google's web API at
# https://console.developers.google.com/apis
oauth_client_id: <id>
oauth_client_secret: <secret>
    
# DACO Settings
# These need to be valid credentials that allow a user
# application (such as jupyterhub) to query our
# DACO authorization service.
daco_base_url: 'https://icgc.org/ud_oauth/1/search'
daco_client_key: <secret>
daco_client_secret: <secret>
daco_token: <secret>
daco_token_secret: <secret>
    
# OpenStack Settings
# These need to be valid credentials to create 
# virtual machines on the OpenStack system 
login_username: < valid openstack user >
login_password: < openstack user's password > 

# This must be the name of a SSH keypair that you've
# uploaded to your OpenStack account; it should
# also be the same name as the key file name in your
# .ssh home directory
keypair_name: <keypair name>
    
# Ansible Settings
# This needs to be the name of a user with ssh
# access to openstack; it might be the same as the
# openstack login_username field.
openstack_ssh_user: <ssh user >
```

2. Open a terminal window. Use **cd** to go into the same directory where you found this README file.

3. Edit the file './vars/main.yml', and  change the setting of the 
'secrets_file' to match the pathname of the secrets file you just created.  

4. Edit the file './config/hosts', and set the hostname of the host on your openstack instance that you want to create. 

4. Type: ansible-playbook deploy-jukebox.yml 
