from setuptools import setup, find_packages

setup(
    name="MultilingualStemmer",
    version="0.1",
    packages=find_packages(include=['MultilingualStemmer', 'MultilingualStemmer.*']),
    install_requires=[
        "bangla-stemmer==1.0",
        "TurkishStemmer==1.3",
        "PersianStemmer==1.0.0"
        "nepali-stemmer==0.0.2"
        "importlib-resources==1.4.0"
    ],
)