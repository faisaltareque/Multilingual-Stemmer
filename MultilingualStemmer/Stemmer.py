from .Languages.config import AVAILABLE_LANGUAGES_MAP
from .Languages.Arabic.ArabicStemmer import ArabicStemmer
from .Languages.Bengali.BengaliStemmer import BengaliStemmer
from .Languages.English.EnglishStemmer import EnglishStemmer
from .Languages.French.FrenchStemmer import FrenchStemmer
from .Languages.Gujarati.GujaratiStemmer import GujaratiStemmer
from .Languages.Hindi.HindiStemmer import HindiStemmer
from .Languages.Indonesian.IndonesianStemmer import IndonesianStemmer
from .Languages.Marathi.MarathiStemmer import MarathiStemmer
from .Languages.Nepali.NepaliStemmer import NepaliStemmer
from .Languages.Persian.PersianStemmer import PersianStemmer
from .Languages.Portuguese.PortugueseStemmer import PortugueseStemmer
from .Languages.Punjabi.PunjabiStemmer import PunjabiStemmer
from .Languages.Russian.RussianStemmer import RussianStemmer
from .Languages.Spanish.SpanishStemmer import SpanishStemmer
from .Languages.Tamil.TamilStemmer import TamilStemmer
from .Languages.Telugu import TeluguStemmer
from .Languages.Turkish.TurkishStemmer import TurkishStemmer
from .Languages.Ukrainian.UkrainianStemmer import UkrainianStemmer
from .Languages.Urdu.UrduStemmer import UrduStemmer

def stem(word, language):
    language = language.lower()
    if language not in AVAILABLE_LANGUAGES_MAP:
        raise ValueError('Language not supported')
    stemmer = None 
    if AVAILABLE_LANGUAGES_MAP[language] == 'arabic':
        stemmer = ArabicStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'bengali':
        stemmer = BengaliStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'english':
        stemmer = EnglishStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'french':
        stemmer = FrenchStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'gujarati':
        stemmer = GujaratiStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'hindi':
        stemmer = HindiStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'indonesian':
        stemmer = IndonesianStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'marathi':
        stemmer = MarathiStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'nepali':
        stemmer = NepaliStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'persian':
        stemmer = PersianStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'portuguese':
        stemmer = PortugueseStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'punjabi':
        stemmer = PunjabiStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'russian':
        stemmer = RussianStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'spanish':
        stemmer = SpanishStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'tamil':
        stemmer = TamilStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'telugu':
        stemmer = TeluguStemmer
    elif AVAILABLE_LANGUAGES_MAP[language] == 'turkish':
        stemmer = TurkishStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'ukrainian':
        stemmer = UkrainianStemmer()
    elif AVAILABLE_LANGUAGES_MAP[language] == 'urdu':
        stemmer = UrduStemmer()
    return stemmer.stem(word)
