from tljh.hooks import hookimpl
from tljh.user import ensure_group
import subprocess


@hookimpl
def tljh_config_post_install(config):
    """
    Set JupyterLab to be default
    """
    user_environment = config.get('user_environment', {})
    user_environment['default_app'] = user_environment.get('default_app', 'jupyterlab')

    config['user_environment'] = user_environment
 
@hookimpl
def tljh_post_install():
    """
    Install docker, docker spawner, and setup the datascience-notebook
    """
    # first we'll install docker on ubuntu 18.04
    # inspired by https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
    # and https://ideonate.com/DockerSpawner-in-TLJH/
    def install_docker():
        def use_packages_over_https():
            subprocess.call("sudo apt update && sudo apt install apt-transport-https ca-certificates curl software-properties-common", shell=True)
            add_gpg_key()

        def add_gpg_key():
            subprocess.call("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -", shell=True)
            add_docker_repo()

        def add_docker_repo():
            subprocess.call("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable'", shell=True)
            do_install()
            
        def do_install():
            subprocess.call("sudo apt update && sudo apt install -y docker-ce", shell=True)
            
        # ok, go!
        use_packages_over_https()
    
    # then we'll install docker spawner
    # inspired by https://ideonate.com/DockerSpawner-in-TLJH/
    def install_docker_spawner():
        subprocess.call("sudo /opt/tljh/hub/bin/python3 -m pip install dockerspawner jupyter_client", shell=True)
    
    # then'll we'll tell TLJH to use docker spawner 
    # and that the image to use is jupyter/datascience-notebook
    def tljh_use_docker_spawner():
        # create the config file
        def create_config_file():
            f = open("/opt/tljh/config/jupyterhub_config.d/dockerspawner_tljh_config.py", "w")
            
            contents = [
                "c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'",
                "c.DockerSpawner.image = 'jupyter/datascience-notebook:r-4.0.3'",
                "from jupyter_client.localinterfaces import public_ips",
                "c.JupyterHub.hub_ip = public_ips()[0]",
                "c.DockerSpawner.name_template = '{prefix}-{username}-{servername}'"
            ]
            
            for line in contents:
                f.write(line)
                f.write("\n")
                
            f.close()
            
        # ok, go!
        create_config_file()
        
    
    # finally we need to download the docker image so it's ready
    def get_docker_image():
        subprocess.call("sudo docker pull jupyter/datascience-notebook:r-4.0.3", shell=True)
   
    install_docker()
    install_docker_spawner()
    tljh_use_docker_spawner()
    get_docker_image()
    
