# Always prefer setuptools over distutils
from setuptools import setup, find_packages

reqs = ['numpy==1.15.4',
        'pandas==0.25.1',
        'python-dotenv==0.13.0',
        'psutil==5.7.0',
        'setuptools>=38.6.0', 
        'ipython==7.15.0', 
        'pytest-runner==5.2'
         ]

setup(
    name='abraxas',
    version='0.0.0',
    description='Python Algorithms an utilities',
    url='',
    author='Carlos Arias',
    author_email='carlos.arias@ucsp.edu.pe, carias@utec.edu.pe',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='Algorithms',
    packages=find_packages(exclude=[]),
    setup_requires=reqs,
    tests_require=['pytest'], 
    install_requires=reqs

)
