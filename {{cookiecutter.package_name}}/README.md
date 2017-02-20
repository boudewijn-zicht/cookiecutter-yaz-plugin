# {{cookiecutter.package_description}}
TODO: Short description here

# Installing
## From a package
```sh
pip3 install {{cookiecutter.package_name}}
```

## From source
```sh
git clone git@github.com:boudewijn-zicht/{{cookiecutter.package_name}}.git
cd {{cookiecutter.package_name}}
python3 setup.py install
```

## From source (for development, with virtualenv)
```sh
# skip this step if you have a python3.5 (or higher) environment
sudo apt-get install libssl-dev
cd $HOME/local
git clone https://github.com/python/cpython.git
cd cpython
./configure --prefix=$HOME/local
make install

# get yaz
git clone git@github.com:boudewijn-zicht/{{cookiecutter.package_name}}.git
cd {{cookiecutter.package_name}}

# skip this step if you have a python3.5 (or higher) environment
# create and activate your python3.5 (or higher) virtual env
virtualenv --python=python3.5 env
source env/bin/activate
# run deactivate to exit the virtualenv

# run tests
make test
```

# Maintainer(s)
- {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>