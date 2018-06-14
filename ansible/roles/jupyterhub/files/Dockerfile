FROM jupyterhub/jupyterhub
ARG JUPYTERHUB_VERSION 
ARG USE_OAUTH 
ARG USE_CERTBOT
ARG SERVICE_DIR
ARG SSL_DIR
ARG KEY
ARG CERT

# Environment variables 
ENV PYTHON_LIB=/opt/conda/lib/python3.5/site-packages \
HUB_DIR=/opt/conda/share/jupyterhub/  \
SSL=$SERVICE_DIR/ssl \
TEMPLATE_DIR=$SERVICE_DIR/www_custom/hub/templates/

RUN pip install --upgrade pip
RUN pip install dockerspawner
RUN pip install jupyterhub-dummyauthenticator
RUN [ "${USE_OAUTH}" = "False" ] || pip install oauthenticator 

# symbolic link to the web page customization section of the juptyterhub module 
RUN set -x; ln -s $HUB_DIR $SERVICE_DIR/www

# Copy contents of the SSL directory we were given
RUN mkdir $SSL
ADD ${SSL_DIR}/ $SSL

ADD ./jupyterhub_config.py $SERVICE_DIR/

# If we need to create ssl certs, do it here 
RUN [ "${USE_CERTBOT}" = "True" ] || openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout $SSL/$KEY -out $SSL/$CERT -days 3650 -subj '/CN=localhost' 
