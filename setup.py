from setuptools import find_packages, setup

setup ( 
    name = 'OneClassTextCollectionsLibrary', 
    packages = find_packages(), 
    version = '0.2.0', 
    description = 'Library to use one-class text collections in which the texts are news from GEDELT project and each collection are based on the taxonomy of IPTC', 
    author = 'Marcos P. S. Gôlo',  
    install_requires = ['gdown', 'pandas']
)
