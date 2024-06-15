import io
from setuptools import setup

setup(
    name='feffery_dash_utils',
    version='0.1.0',
    author_email='fefferypzy@gmail.com',
    homepage='https://github.com/CNFeffery/feffery-dash-utils',
    author='CNFeffery <fefferypzy@gmail.com>',
    packages=['feffery_dash_utils'],
    license='MIT',
    description='A series of tool functions to assist Dash application development.',
    long_description=io.open(
        'README.md', encoding='utf-8'
    ).read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Framework :: Dash',
    ],
    url='https://github.com/CNFeffery/feffery-dash-utils',
)
