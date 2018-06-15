FROM jupyter/base-notebook:27ba57364579
USER root
RUN apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y libfuse-dev fuse curl wget software-properties-common
  
RUN apt-get install -y samtools man locate vim net-tools

# Add the contents of our sudo access file into our notebook
ADD sudo.access /tmp/sudo.access
RUN cat /tmp/sudo.access >> /etc/sudoers
RUN rm /tmp/sudo.access

# The default setup creates a a directory called 'work'
# We don't need it, and it might confuse our users, so we'll delete it
# Run 'true' so that we don't fail when the directory doesn't already exist
RUN test -d work && rmdir work; true

RUN echo 'function addPath { export PATH=$PATH:$1 ; }' >> ~jovyan/.bashrc
RUN echo 'umask 077' >> ~jovyan/.bashrc
RUN chown -R jovyan:users /home/jovyan
