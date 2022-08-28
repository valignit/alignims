from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alignims/__init__.py
from alignims import __version__ as version

setup(
	name="alignims",
	version=version,
	description="Investment Management Suite",
	author="Valignit",
	author_email="ghouseam@valignit.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
