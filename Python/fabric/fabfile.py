from fabric.api import sudo

def UpdateServer():
	sudo("yum -y upgrade", pty=True)
