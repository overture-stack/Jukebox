FROM jupyterhub/jupyterhub
ARG JUPYTERHUB_VERSION=0.8 
ARG SERVICE_DIR=/srv/jupyterhub
ARG SSL_DIR=/srv/jupyterhub/ssl
ARG PYTHON_LIB=/opt/conda/lib/python3.6/site-packages
ARG HUB_DIR=/opt/conda/share/jupyterhub/

# Environment variables 
ENV SSL=$SERVICE_DIR/ssl \
TEMPLATE_DIR=$SERVICE_DIR/www_custom/hub/templates/

RUN pip install --upgrade pip
RUN pip install dockerspawner
RUN pip install jupyterhub-dummyauthenticator
RUN pip install oauthenticator requests-oauthlib

# symbolic link to the web page customization section of the juptyterhub module 
RUN set -x; ln -s $HUB_DIR $SERVICE_DIR/www

# Copy contents of the SSL directory we were given
RUN mkdir $SSL

#ADD ${SSL_DIR}/ $SSL
#ADD ./jupyterhub_config.py $SERVICE_DIR/

# Copy in our daco authentication code over into the oauthenticator module
COPY ./auth_daco/* $PYTHON_LIB/oauthenticator/

# Copy in all of our custom files (add to / replace existing files in www)
COPY ./www_custom/ $SERVICE_DIR/www_custom/

# Copy over all of the custom files over top of the jupyterhub web directory we've symlinked to
RUN cp -a $SERVICE_DIR/www_custom/* $SERVICE_DIR/www/
