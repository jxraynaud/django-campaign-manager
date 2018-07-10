import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-campaign-manager',
    version='alpha-0.1',
    packages=['django-campaign-manager'],
    description='Tool to manage advertising campaigns',
    long_description=README,
    author='Jean-Xavier Raynaud',
    author_email='jx@pixelforest.com',
    url='https://github.com/jxraynaud/django-campaign-manager',
    license='MIT',
    install_requires=[
        'Django>=2.0',
    ]
)
