# written by kschuler
FROM jupyter/datascience-notebook
ARG JUPYTERHUB_VERSION=0.8.0
RUN pip3 install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION
