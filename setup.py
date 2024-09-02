from setuptools import setup, find_packages

setup(
    name='ctgenerics',
    version='0.1',
    packages=find_packages(),
    description='A utility package for my STST projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Callum Thickett',
    author_email='callum.thickett@stepstone.com',
    url='https://stash.stepstone.com/users/callum.thickett/repos/ctgenerics',
    install_requires=[
        'numpy',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
