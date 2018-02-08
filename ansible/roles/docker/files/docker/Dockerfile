FROM jupyter/all-spark-notebook 
MAINTAINER ICGC <dcc-support@icgc.org>

# Make our python packages available inside the docker instance
RUN pip install icgc overture-song 

# Their default user for jupyter; a pun on the word 'jovian'
USER jovyan

ENV notebook_path=/opt/conda/lib/python3.6/site-packages/notebook/

# The 'all-spark-notebook' setup creates a a directory called 'work' 
# We don't need it, and it might confuse our users, so we'll delete it 
# Run 'true' so that we don't fail when the directory doesn't already exist
RUN test -d work && rmdir work; true

# Automatically install a demo notebook, so that people have a clue about
# what jupyter notebooks are, and what they can do... 
ADD --chown=jovyan:users demo.ipynb .

# Copy over our icgc favicon
COPY --chown=jovyan:users favicon.ico $notebook_path/static
# Copy over our new tree and other template modifications
COPY --chown=jovyan:users tree.html $notebook_path/templates/tree.html 
COPY --chown=jovyan:users page.html $notebook_path/templates/page.html 
