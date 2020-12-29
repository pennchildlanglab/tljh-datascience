from tljh.hooks import hookimpl
from tljh.user import ensure_group
import sh

@hookimpl
def tljh_extra_user_conda_packages():
    """
    Return list of extra conda packages to install in user environment.
    """
    return [
        'r-base', 
        'r-essentials', 
        'r-irkernel',
        'julia'
    ]

# @hookimpl
# def tljh_extra_apt_packages():
#   return ['julia']

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
    Configure /srv/scratch and change configs/mods
    """
    ### mkdir -p /opt/tljh/user/lib/R
    ### sudo chown  root:jupyterhub-users /srv/scratch
    ### sudo chmod 777 /srv/scratch
    ### sudo chmod g+s /srv/scratch
    ### sudo ln -s /srv/scratch /etc/skel/scratch
    #sh.mkdir('/opt/tljh/user/lib/R', '-p')
    # jupyterhub-users doesn't get created until a user logs in
    # make sure it's created before changing permissions on directory
    ensure_group('jupyterhub-users') 
    sh.chown('root:jupyterhub-users', '/opt/tljh/user/lib/R')
    # sh.chmod('777', '/srv/scratch')
    # sh.chmod('g+s', '/srv/scratch')
    # sh.ln('-s', '/srv/scratch', '/etc/skel/scratch')

    
