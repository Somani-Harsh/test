from setuptools import setup, find_packages


requirements = []
with open("requirements.txt","r") as f:
	for i in f:
		requirements.append(i)

setup(
	name = 'sample',
	version = '0.0.0',
	description = 'A sample Program',
	packages=find_packages(exclude=['contrib','docs','tests']),
	install_requires = requirements,
	classifiers = [
		"Programming Language :: Python :: 3.4"
	]
)


