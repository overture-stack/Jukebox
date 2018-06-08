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

# symbolic link to the web page customization section of the juptyterhub module 
RUN set -x; ln -s $HUB_DIR $SERVICE_DIR/www

# Copy in all of our custom files (add to / replace existing files in www)
ADD ./www_custom/ $SERVICE_DIR/www_custom/

# Copy contents of the SSL directory we were given
RUN mkdir $SSL
ADD ${SSL_DIR}/ $SSL

# Our custom login template only works on a production machine; 
# so we automatically disable it when we're in dev mode, and tell people we've done it.
RUN echo USE_OAUTH is ${USE_OAUTH}
RUN [ "${USE_OAUTH}" = "True" ] || echo "***Development mode:Deactivating custom login.html template***"

# Rename our login file to disable it
RUN [ "${USE_OAUTH}" = "True" ] || mv ${TEMPLATE_DIR}/login.html ${TEMPLATE_DIR}/deactivated_login.html

# Copy over all of the custom files over top of the jupyterhub web directory we've symlinked to
RUN set -x; cp -a $SERVICE_DIR/www_custom/* $SERVICE_DIR/www/ 

# Overwrite any jupyterhub_config.py with this version
ADD ./jupyterhub_config.py $SERVICE_DIR/

# If we need to create ssl certs, do it here 
RUN [ "${USE_CERTBOT}" = "True" ] || openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout $SSL/$KEY -out $SSL/$CERT -days 3650 -subj '/CN=localhost' 
