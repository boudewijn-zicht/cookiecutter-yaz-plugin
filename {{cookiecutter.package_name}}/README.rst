{{"=" * (cookiecutter.package_description|length)}}
{{cookiecutter.package_description}}
{{"=" * (cookiecutter.package_description|length)}}

TODO: Short description here


Installing
----------

    .. code-block:: bash

        pip3 install --upgrade {{cookiecutter.package_name}}

        # Call the installed script
        yaz-{{cookiecutter.app_name|lower}}


Developing
----------

    .. code-block:: bash

        # Get the code
        git clone {{cookiecutter.package_clone_url}}
        cd {{cookiecutter.package_name}}

        # Ensure you have python 3.5 or higher and yaz installed
        python3 --version
        pip3 install --upgrade yaz

        # Setup your virtual environment
        virtualenv --python=python3 env
        source env/bin/activate

        # Run tests
        python setup.py test

        # Or run nosetests directly (allows coverage report)
        nosetests --with-cover --cover-html --cover-package {{cookiecutter.package_name}}

        # Upload a new release to pypi
        python setup.py sdist upload --repository pypi

        # Once you are done... exit your virtual environment
        deactivate


Maintainer
----------

- {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>
