# tljh-datascience

Tells TLJH to use [DockerSpawner](https://jupyterhub-dockerspawner.readthedocs.io/en/latest/) to spin up [jupyter/datascience-notebook](https://hub.docker.com/r/jupyter/datascience-notebook/tags?page=1&ordering=last_updated) containers for each user. This makes it easy to include R and Julia Kernels for your JupyterHub users. Read more about what's included in the `jupyter/datascience-notebook` [here](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook). 

The plugin also sets jupyterlab as the default interface. 

## Install

Include `--plugin tljh-datascience` in your TLJH install script. For example, here user `kschuler` with password `password` installs TLJH with `tljh-datascience`:
```
#!/bin/bash

curl https://raw.githubusercontent.com/jupyterhub/the-littlest-jupyterhub/master/bootstrap/bootstrap.py \
  | sudo python3 - \
    --admin kschuler:password --plugin git+https://github.com/pennchildlanglab/tljh-datascience
```

## Customize docker images

To add other or different images for your users to select, edit the dockerspawner config file (SSH into your server)

```
sudo nano /opt/tljh/config/jupyterhub_config.d/dockerspawner_tljh_config.py
```

The current list of available images is in `c.DockerSpawner.image_whitelist = ['jupyter/datascience-notebook:r-4.0.3', 'jupyter/datascience-notebook:r-3.6.6']`. You can edit this list include any docker images you want to make available to your users. Then reload the hub.

```
sudo tljh-config reload
```


## Attribution

This plugin was inspired by [this Ideonate post](https://ideonate.com/DockerSpawner-in-TLJH/) and the [Rxns stack plugin](https://github.com/sustainable-processes/tljh-rxns)

## To-do

- figure out how to include jupyterlab plugins (probably just a docker image based on the datascience-notebook is the easiest)


