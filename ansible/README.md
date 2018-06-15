# How to configure Jukebox for your Openstack system

1. Make a file with your openstack secrets in it, say '~/secrets/openstack_secrets'. In it create a file called openstack_secrets.yml, and copy the in the section below, filling in the values with your 
secret information.
```
# OpenStack Settings
# These need to be valid credentials to create 
# virtual machines on the OpenStack system 
login_username: *< valid openstack user >*
login_password: *< openstack user's password >* 

# This must be the name of a SSH keypair that you've
# uploaded to your OpenStack account; it should
# also be the same name as a key file name in your
# .ssh home directory
keypair_name: *<keypair name>*
```    
2. Edit ~/vars/openstack.yml, and make sure the first line is set to the name of your openstack secrets file. 
3. Fill in the rest of the information in openstack.yml with the correct 
information for your openstack system.
4. Get credentials from Google to use for their single sign on mechanism. 
You can generate these credentials by using Google's web API at  https://console.developers.google.com/apis.
5. Create a file for your oauth credentials, eg. ~/secrets/oauth_secrets.yml,
with the contents below. Fill in the appropriate settings with the credentials you got from google. 
``` 
# Google OAuth Settings
# To use Google's Single Sign on mechanism, we need a valid email address,
# and we need to get a client_id and a client secret from them.
oauth_client_id: <id>
oauth_client_secret: <secret>
```
6. Edit the file /vars/oauth.yml, and make sure the first line is set to the name of your oauth secrets file. 

7. Edit the file './config/hosts', and set the hostname of the host on your openstack instance that you want to create. 

9. Edit the file /vars/certbot.yml, and enter your email address.

10. Type: ansible-playbook deploy-jukebox.yml 

Note: If you have shade installed (use 'pip2 install shade'), and you still get the error message: 'shade not installed', it may be because there is both an
python module called 'openstack' (which shade installs), and an ansible module called 'openstack' (which ansible installs).

In that case, you can work around the issue by setting your PYTHON_PATH environment variable to directory where your ansible modules have been installed. 

`. fix_openstack_fix` does this for MacOS/X. 
