
from setuptools import setup, find_packages

setup(
        name='data analysis',
        version= '0.0.1',
        url= 'www.github.com/Ingabireralice/data_analysis',
        license= 'BSD'
        author='Ralice',
        packages=find_packages(),
        install_requires=['pyqt5', 
                          'pandas' ,
                          'sqlalchemy' , 
                          'nltk' , 
                          'numpy' ,
                          'jupter',
                          'python-twitter']
        entry_points={},
        extra_require={'dev': ['flake8' ,]},
        )

