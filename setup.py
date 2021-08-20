import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='temp-mail',
    version='0.2',
    license='MIT',
    description='Wrapper for online service which provides '
                'temporary email address: https://www.1secmail.com/api/',
    long_description=read('README.md'),
    keywords='temporary temp mail email address wrapper api anon '
             'anonymous secure free disposable',
    url='https://github.com/leirons/TempMail',
    author='Ivan Grechka',
    author_email='grecigor11@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['requests'],
    py_modules=['tempmail'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',

        'Topic :: Internet :: WWW/HTTP'
    ],
)