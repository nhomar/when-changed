from setuptools import setup

setup(name='when-changed',
      version='0.2.1.1',
      description='Run a aws command (cp) when a file is changed',
      author='Johannes H. Jensen, Nhomar Hernandez',
      author_email='joh@pseudoberries.com, nhomar@vauxoo.com',
      url='https://github.com/nhomar/when-changed',
      packages=['whenchanged'],
      scripts=['when-changed'],
      install_requires=['pyinotify'],
      license='BSD'
      )
