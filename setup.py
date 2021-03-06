from setuptools import setup

setup(name='RaspberryPi Manager',
      version='1.0',
      description='Controls the raspberry in combination with the grovepi',
      author='Hiz',
      author_email='0893430@hr.nl',
      url='https://github.com/Jehizkia',
      packages=['raspberry'],
      install_requires=['requests', 'socketIO-client-nexus', 'grovepi', 'PyInstaller']
     )

