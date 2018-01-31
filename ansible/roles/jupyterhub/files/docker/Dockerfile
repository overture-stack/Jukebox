FROM jupyter/all-spark-notebook 
MAINTAINER ICGC <dcc-support@icgc.org>

# Make our python packages available inside the docker instance
RUN pip install icgc overture-song 

# Their default user for jupyter; a pun on the word 'jovian'
USER jovyan

# The 'all-spark-notebook' setup creates a a directory called 'work' 
# We don't need it, and it might confuse our users, so we'll delete it 
RUN rmdir work

# Automatically install a demo notebook, so that people have a clue about
# what jupyter notebooks are, and what they can do... 
ADD demo.ipynb .
