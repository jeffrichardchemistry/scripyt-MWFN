from setuptools import setup, find_packages

with open("README.md", 'r') as fr:
	description = fr.read()

setup(
    name='scripyt-MWFN',
    version='1.0.1',
    url='https://github.com/jeffrichardchemistry/scripyt-MWFN',
    license='GNU GPL',
    author='Jefferson Richard',
    author_email='jrichardquimica@gmail.com',
    keywords='Cheminformatics, Chemistry, Multiwfn, quantum-chemistry',
    description='A package for Cheminformatics.',
    long_description = description,
    long_description_content_type = "text/markdown",
    packages=['scripyt-MWFN'],
    install_requires=['pandas'],
	scripts=['scripyt-MWFN/scripyt-MWFN'],
	classifiers = [
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Chemistry',
		'Topic :: Scientific/Engineering :: Physics',
		'Topic :: Scientific/Engineering :: Bio-Informatics',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9']
)
