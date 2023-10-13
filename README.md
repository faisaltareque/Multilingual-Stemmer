# Multilingual-Stemmer

*This is a python package for stemming words in different languages. It contains stemmers for 15+ languages. It is a wrapper around different stemmers. It is very easy to use. You just need to pass the word and the language of the word to the stemmer. It will return the stemmed word.*

### Available Languages

- [x] [Gujarati](/MultilingualStemmer/Languages/Gujarati/README.md)
- [x] [Hindi](/MultilingualStemmer/Languages/Hindi/README.md)
- [x] [Marathi](/MultilingualStemmer/Languages/Marathi/README.md)
- [x] [Punjabi](/MultilingualStemmer/Languages/Punjabi/README.md)
- [x] [Urdu](/MultilingualStemmer/Languages/Urdu/README.md)
- [x] [Bengali](/MultilingualStemmer/Languages/Bengali/README.md)
- [X] [Turkish](/MultilingualStemmer/Languages/Turkish/README.md)
- [x] [Ukrainian](/MultilingualStemmer/Languages/Ukrainian/README.md)
- [X] [Telugu](/MultilingualStemmer/Languages/Telugu/README.md)
- [x] [Portuguese](/MultilingualStemmer/Languages/Portuguese/README.md)
- [x] [Spanish](/MultilingualStemmer/Languages/Spanish/README.md)
- [x] [Nepali](/MultilingualStemmer/Languages/Nepali/README.md)
- [x] [Arabic](/MultilingualStemmer/Languages/Arabic/README.md)
- [x] [Russian](/MultilingualStemmer/Languages/Russian/README.md)
- [X] [Persian](/MultilingualStemmer/Languages/Persian/README.md)
- [x] [English](/MultilingualStemmer/Languages/English/README.md)
- [X] [Tamil](/MultilingualStemmer/Languages/Tamil/README.md)
- [x] [French](/MultilingualStemmer/Languages/French/README.md)
- [x] [Indonesian](/MultilingualStemmer/Languages/Indonesian/README.md)

## Installation

```bash
pip install git+https://github.com/faisaltareque/Multilingual-Stemmer.git
```

## Usage

```python
from MultilingualStemmer import Stemmer
print(Stemmer.stem("walking", language="english"))
```

### Disclaimer
I have made this package for my personal use. None of these stemmers are developed by me. I just collected them from different sources and made them available in a single package. I am not responsible for any kind of error in the stemmers. If you find any error, please report it to the respective developer. I have mentioned the source of each stemmer in the respective language folder. If you are the developer of any of these stemmers and you don't want your stemmer to be included in this package, please contact me. I will remove it immediately.

If you want to add any stemmer to this package, please contact me. I will add it to the package.

If you find this package useful, please feel free to use it in your project. If you want to contribute to this package, please contact me. I will add you as a contributor.

## License
As this package is just a wrapper around different stemmers, the license of each stemmer is applicable to this package. Please check the license of each stemmer before using it.

