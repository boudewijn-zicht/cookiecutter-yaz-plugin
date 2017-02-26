from setuptools import setup

setup(name='{{cookiecutter.package_name}}',
      packages=['{{cookiecutter.package_name}}'],
      version='{{cookiecutter.package_version}}',
      description='{{cookiecutter.package_description}}',
      author='{{cookiecutter.author_name}}',
      author_email='{{cookiecutter.author_email}}',
      url="{{cookiecutter.package_url}}",
      license='MIT',
      zip_safe=False,
      install_requires=['yaz'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6"
      ])
