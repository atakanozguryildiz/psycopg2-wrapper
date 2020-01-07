import setuptools

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md', 'r') as fh:
    long_description = fh.read()

version = '1.0'

setuptools.setup(
    name='psycopg2_wrapper',
    version=version,
    author='Atakan Ozgur Yildiz',
    author_email='atakanozguryildiz@gmail.com',
    description='Simple wrapper for executing commands and queries',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/atakanozguryildiz/psycopg2-wrapper',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
