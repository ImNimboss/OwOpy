from setuptools import setup, find_packages

with open('README.md') as readme: readme = readme.read()

setup(
    name = 'owopy',
    version = '0.0.1',
    description = 'An easy to use module to OwOify your text - turn it into furry Japanese Baby Babblespeak!',
    long_description = readme,
    url = 'https://github.com/Nimboss2411/OwOpy',
    author = 'Nimit Grover',
    author_email = 'nimbossthegreat@gmail.com',
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Other Audience',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
    keywords = 'owo owoify',
    packages = ['owopy'],
    install_requires = []
)
