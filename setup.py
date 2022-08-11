from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cafeteria_app/__init__.py
from cafeteria_app import __version__ as version

setup(
	name="cafeteria_app",
	version=version,
	description="sistema",
	author="Orlando",
	author_email="edwin_orlando83@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
