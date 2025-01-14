"""Run post-installation tasks."""

from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        
        install.run(self)
        
        # Run your post-install script
        subprocess.call(['echo', ''])
        subprocess.call(['echo', 'Running post-install script...'])
        subprocess.call(['echo', ''])
        # Add your custom post-install commands here
        # For example, you can run a shell script or a Python script
        # subprocess.call(['./your_script.sh'])
        subprocess.call(['python3', 'download_corpora.py']) 