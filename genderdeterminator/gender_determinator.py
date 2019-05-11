import pkg_resources
import csv
import codecs

DEFINITE_ARTICLES = dict(
    m="der",
    f="die",
    n="das"
)

INDEFINITE_ARTICLES = dict(
    m="ein",
    f="eine",
    n="ein"
)

LOCAL_PREPOSITION_INSIDE = dict(
    m="im",
    f="in der",
    n="im"
)


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

    def get_definite_article(self, noun):
        gender = self.get_gender(noun)

        if gender is None:
            return None

        return DEFINITE_ARTICLES[gender]

    def get_indefinite_article(self, noun):
        gender = self.get_gender(noun)

        if gender is None:
            return None

        return INDEFINITE_ARTICLES[gender]

    def get_local_preposition_for_inside(self, noun):
        gender = self.get_gender(noun)

        if gender is None:
            return None

        return LOCAL_PREPOSITION_INSIDE[gender]
