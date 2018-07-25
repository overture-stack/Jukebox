FROM jupyterhub/jupyterhub
ARG JUPYTERHUB_VERSION 
ARG USE_OAUTH 
ARG USE_CERTBOT
ARG SERVICE_DIR
ARG SSL_DIR
ARG KEY
ARG CERT
ARG PYTHON_LIB
ARG HUB_DIR

# Environment variables 
ENV SSL=$SERVICE_DIR/ssl \
TEMPLATE_DIR=$SERVICE_DIR/www_custom/hub/templates/

RUN pip install --upgrade pip
RUN pip install dockerspawner
RUN pip install jupyterhub-dummyauthenticator
RUN [ "${USE_OAUTH}" = "False" ] || pip install oauthenticator requests-oauthlib

# symbolic link to the web page customization section of the juptyterhub module 
RUN set -x; ln -s $HUB_DIR $SERVICE_DIR/www

# Copy contents of the SSL directory we were given
RUN mkdir $SSL
ADD ${SSL_DIR}/ $SSL

ADD ./jupyterhub_config.py $SERVICE_DIR/

# Copy in our daco authentication code over into the oauthenticator module
COPY ./auth_daco/* $PYTHON_LIB/oauthenticator/

# symbolic link to the web page customization section of the juptyterhub module
RUN ln -s $HUB_DIR $SERVICE_DIR/www

# Copy in all of our custom files (add to / replace existing files in www)
COPY ./www_custom/ $SERVICE_DIR/www_custom/

RUN [ "${USE_OAUTH}" = "True" ] || echo "*** :Deactivating custom login.html template***"

# Rename our login file to disable it
RUN [ "${USE_OAUTH}" = "True" ] || mv ${TEMPLATE_DIR}/login.html ${TEMPLATE_DIR}/deactivated_login.html

# Copy over all of the custom files over top of the jupyterhub web directory we've symlinked to
RUN cp -a $SERVICE_DIR/www_custom/* $SERVICE_DIR/www/

# If we need to create ssl certs, do it here 
RUN [ "${USE_CERTBOT}" = "True" ] || openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout $SSL/$KEY -out $SSL/$CERT -days 3650 -subj '/CN=localhost' 
