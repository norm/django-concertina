from setuptools import setup

PACKAGE = 'django-concertina'
VERSION = '1.0'

setup(
    name=PACKAGE,
    version=VERSION,
    description="Django template tag to provide concertina pagination.",
    packages=[
        'concertina',
        'concertina.templatetags',
    ],
    include_package_data=True,
    license='MIT',
    author='Mark Norman Francis',
    author_email='norm@201created.com',
    install_requires=[
        'Django>=1.6.0',
    ],
    url = 'https://github.com/norm/django-concertina',
    classifiers = [
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
