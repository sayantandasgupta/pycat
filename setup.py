from setuptools import setup, find_packages

setup(
    name='pycat',
    version='0.1.0',
    author='Sayantan Dasgupta',
    author_email='sayantan.dasgupta21@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        pycat=pycat.pycat:main
'''
)