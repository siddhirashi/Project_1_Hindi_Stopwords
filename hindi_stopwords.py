"""
============================================================
Topic: Indic Language Stop Words for Natural Language Processing
============================================================
Author Name(s): [Enter Student Name(s)]
Short Description: This file contains a sample stop-word list of 24 Hindi
words (Devanagari script) for use in text preprocessing in Natural Language
Processing (NLP). The words are grouped by grammatical function
(conjunctions, pronouns, postpositions, auxiliary verbs and particles).
A small helper function at the bottom shows how the list is used to clean
a sentence.
Semester: Monsoon Semester 2026
Affiliation: [Enter Department and Institution Name]
Note:
These lists contain illustrative examples only. Please modify them
accordingly.
============================================================
"""

import re

# 1. Hindi Stop Words
# Language: Hindi
# Script: Devanagari
hindi_stopwords = [
    # conjunctions
    "और", "लेकिन", "या", "क्योंकि",
    # pronouns and demonstratives
    "मैं", "हम", "आप", "यह", "वह", "इस", "उस", "कुछ",
    # postpositions
    "का", "की", "के", "को", "से", "में", "पर",
    # auxiliary verbs
    "है", "हैं", "था",
    # particles and negation
    "भी", "नहीं",
]


# --------------------------------------------------------------
# Helper: tokenise a Hindi sentence and drop the stop words
# --------------------------------------------------------------
# The regex keeps Devanagari letters, vowel signs and the nukta, but
# leaves out the danda (।) and double danda (॥) so they don't stick to
# the last word of a sentence.
_DEVANAGARI_WORD = re.compile(r"[\u0900-\u0963\u0966-\u097F]+")
_stopword_set = set(hindi_stopwords)


def remove_stopwords(text):
    """Return the list of tokens in `text` that are not stop words."""
    tokens = _DEVANAGARI_WORD.findall(text)
    return [t for t in tokens if t not in _stopword_set]


if __name__ == "__main__":
    sample = "वह गाँव में रहता है और हर सुबह नदी के किनारे टहलने जाता है।"
    print("Stop words in list :", len(hindi_stopwords))
    print("Before             :", sample)
    print("After              :", " ".join(remove_stopwords(sample)))
