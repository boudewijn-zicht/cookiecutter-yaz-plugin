import os
import setuptools
import sys

with open("{{cookiecutter.package_name}}/version.py") as file:
    globals = {}
    exec(file.read(), globals)
    version = globals["__version__"]

if sys.argv[-1] == "tag":
    os.system("git tag -a {} -m \"Release {}\"".format(version, version))
    os.system("git push origin {}".format(version))
    sys.exit()

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

setuptools.setup(
    name="{{cookiecutter.package_name}}",
    packages=["{{cookiecutter.package_name}}"],
    version=version,
    description="{{cookiecutter.package_description}}",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="{{cookiecutter.package_github_url}}",
    license="MIT",
    zip_safe=False,
    install_requires=["yaz"],
    scripts=["bin/yaz-{{cookiecutter.app_name|lower}}"],
    test_suite="nose.collector",
    tests_require=["nose", "coverage"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ])
