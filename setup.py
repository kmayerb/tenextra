from setuptools import setup, find_packages
PACKAGES = find_packages()

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

opts = dict(name='tcrdist3',
            maintainer='Koshlan Mayer-Blackwell',
            maintainer_email='kmayerbl@fredhutch.org',
            description='get most likly VDJ receptor pairs from single cells',
            long_description=long_description,
            long_description_content_type='text/markdown',
            url='https://github.com/kmayerb/tenextra',
            license='MIT',
            author='Koshlan Mayer-Blackwell',
            author_email='kmayerbl@fredhutch.org',
            version='0.0.1',
            packages=PACKAGES,
            package_data={"": ["*.csv","*.tsv","*.txt"]},
           )

install_reqs = [
      'pandas>=0.24.2',
      'numpy>=1.16.4']

if __name__ == "__main__":
      setup(**opts, install_requires=install_reqs)