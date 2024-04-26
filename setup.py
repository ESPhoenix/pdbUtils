from setuptools import setup

setup(name='pdbUtils',
      version='2024.0.0',
      description='A small python module that can parse PDB files as pandas DataFrames.',
      url='https://github.com/ESPhoenix/pdbUtils',
      download_url='placeholder',
      author='Eugene Shrimpton-Phoenix',
      author_email='eshrimpt@ed.ac.uk, e.s.phoenix@hotmail.co.uk',
      maintainer='Marta Chronowska',
      maintainer_email='mchrnwsk@gmail.com',
      packages=['pdbUtils'],
      install_requires = ['pandas'],
      license='GPLv3'
      )