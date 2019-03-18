FROM jupyter/all-spark-notebook 
MAINTAINER ICGC <dcc-support@icgc.org>
RUN pip install --upgrade pip
RUN pip install --no-cache jupyterhub

# Make our python packages available inside the docker instance
RUN pip install icgc overture-song 

# Copy over our web customizations 
ENV notebook_path=/opt/conda/lib/python3.6/site-packages/notebook/
ADD ./www_custom/ /tmp/www_custom/
RUN cp -a /tmp/www_custom/* $notebook_path
