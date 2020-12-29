# tljh-datascience

This plugin installs Docker and DockerSpawner and then tells TLJH to use DockerSpawner to select the [jupyter/datascience-notebook](https://hub.docker.com/r/jupyter/datascience-notebook/tags?page=1&ordering=last_updated) image as the environment for each user. This makes it easy to include R and Julia Kernels for your JupyterHub users in addition to Python 3.

It also sets jupyterlab as the default IDE.

## Install

Include `--plugin tljh-datascience` in your TLJH install script. For example, here user `kschuler` with password `password` installs TLJH with `tljh-datascience`:
```
#!/bin/bash

curl https://raw.githubusercontent.com/jupyterhub/the-littlest-jupyterhub/master/bootstrap/bootstrap.py \
  | sudo python3 - \
    --admin kschuler:password --plugin git+https://github.com/pennchildlanglab/tljh-datascience
```

## Attribution

This plugin was inspired by [this Ideonate post](https://ideonate.com/DockerSpawner-in-TLJH/) and the [rxns Stack plugin](https://github.com/sustainable-processes/tljh-rxns)




