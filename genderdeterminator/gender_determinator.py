import pkg_resources
import csv
import codecs
from enum import Enum


class Case(Enum):
    NOMINATIVE = 1,
    GENITIVE = 2,
    DATIVE = 3,
    ACCUSATIVE = 4


def _append(word, noun):
    if word is None:
        return noun
    else:
        return "{} {}".format(word, noun)


cases = {
    "singular": {
        Case.NOMINATIVE: dict(
            m="der",
            f="die",
            n="das"
        ),
        Case.ACCUSATIVE: dict(
            m="den",
            f="die",
            n="das"
        ),
        Case.DATIVE: dict(
            m="dem",
            f="der",
            n="dem"
        ),
        Case.GENITIVE: dict(
            m="des",
            f="der",
            n="des"
        )
    },
    "plural": {
        Case.NOMINATIVE: dict(
            m="die",
            f="die",
            n="die"
        ),
        Case.ACCUSATIVE: dict(
            m="die",
            f="die",
            n="die"
        ),
        Case.DATIVE: dict(
            m="den",
            f="den",
            n="den"
        ),
        Case.GENITIVE: dict(
            m="die",
            f="die",
            n="die"
        )
    }
}


class GenderDeterminator:
    def __init__(self):
        with pkg_resources.resource_stream(__name__, "words.csv") as csv_file:
            utf8_reader = codecs.getreader('utf-8')
            reader = csv.reader(utf8_reader(csv_file))
            self.words = [tuple(row) for row in reader]

    def get_gender(self, noun):
        noun_lowered = noun.lower()

        for (word, gender) in self.words:
            if noun_lowered.endswith(word):
                return gender.split(';')[0]

        return None

    def get(self, noun, case, plural=False, append=True):
        gender = self.get_gender(noun)

        if gender is None:
            return noun if append else None

        ps = "plural" if plural else "singular"
        word = cases[ps][case][gender]

        return _append(word, noun) if append else word
