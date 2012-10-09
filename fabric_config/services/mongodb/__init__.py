from fabric.api import task, sudo, run
from fabric.contrib.files import upload_template
from os.path import dirname, join

HERE = dirname(__file__)

@task
def install():
    """
    Installs MongoDB on the host.
    """
    #Add the yum repo
    upload_template(join(HERE, 'templates/10gen.repo-x86_64'), '/etc/yum.repos.d/10gen.repo', use_sudo=True)
    sudo('yum install mongo-10gen mongo-10gen-server')
    sudo('chkconfig mongod on')

@task
def stop():
    sudo('service mongod stop')

@task
def start():
    sudo('service mongod start')

@task
def restart():
    sudo('service mongod restart')

@task
def shell():
    run('mongo')