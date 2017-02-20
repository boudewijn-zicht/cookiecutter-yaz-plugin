from setuptools import setup

setup(name='{{cookiecutter.package_name}}',
      version='1.0.0b1',
      description='{{cookiecutter.package_description}}',
      author='{{cookiecutter.author_name}}',
      author_email='{{cookiecutter.author_email}}',
      license='MIT',
      packages=['{{cookiecutter.package_name}}'],
      install_requires=['yaz'],
      zip_safe=False)
