"""
============================================================
Topic: Indic Language Stop Words for Natural Language Processing
============================================================
Author Name(s): [Enter Student Name(s)]
Short Description: This file contains a stop-word list of 200 Hindi
words (Devanagari script) for use in text preprocessing in Natural Language
Processing (NLP). The words are grouped by grammatical function
(conjunctions, pronouns, postpositions, auxiliary verbs, particles, etc.).
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
    # conjunctions (19)
    "और", "लेकिन", "या", "क्योंकि", "किंतु", "परंतु", "मगर", "तथा", "एवं",
    "अथवा", "कि", "जबकि", "इसलिए", "ताकि", "यानी", "बल्कि", "अगर", "यदि",
    "वरना",
    # personal pronouns (16)
    "मैं", "हम", "आप", "तुम", "तू", "यह", "वह", "ये", "वे", "मुझे", "हमें",
    "तुम्हें", "उसे", "इसे", "उन्हें", "इन्हें",
    # demonstratives and determiners (12)
    "इस", "उस", "इन", "उन", "कुछ", "कोई", "किसी", "सब", "सभी", "हर", "अन्य",
    "कई",
    # possessive pronouns (26)
    "मेरा", "मेरी", "मेरे", "हमारा", "हमारी", "हमारे", "तुम्हारा",
    "तुम्हारी", "तुम्हारे", "आपका", "आपकी", "आपके", "उसका", "उसकी", "उसके",
    "इसका", "इसकी", "इसके", "उनका", "उनकी", "उनके", "अपना", "अपनी", "अपने",
    "खुद", "स्वयं",
    # relative and interrogative words (15)
    "जो", "जिस", "जिन", "जिसे", "जिसका", "जिसके", "कौन", "किस", "किन",
    "क्या", "क्यों", "कैसे", "कहाँ", "कब", "कितना",
    # postpositions (22)
    "का", "की", "के", "को", "से", "में", "पर", "तक", "ने", "द्वारा", "लिए",
    "साथ", "बाद", "पहले", "ऊपर", "नीचे", "बीच", "अंदर", "बाहर", "पास",
    "बिना", "सामने",
    # adverbs of place and time (14)
    "यहाँ", "वहाँ", "यहां", "वहां", "जब", "तब", "अब", "तभी", "अभी", "फिर",
    "कभी", "हमेशा", "अक्सर", "जहाँ",
    # auxiliary verbs (24)
    "है", "हैं", "था", "थी", "थे", "हो", "हूँ", "हूं", "होता", "होती",
    "होते", "हुआ", "हुई", "हुए", "होगा", "होगी", "होंगे", "रहा", "रही",
    "रहे", "सकता", "सकती", "सकते", "चाहिए",
    # light and common verbs (17)
    "गया", "गई", "गए", "गये", "जाए", "पड़ा", "पड़ी", "लगा", "लगी", "लगे",
    "करना", "करने", "करके", "किया", "कर", "दिया", "लिया",
    # degree, manner and quantity (21)
    "बहुत", "ज्यादा", "अधिक", "थोड़ा", "कम", "इतना", "इतनी", "इतने", "उतना",
    "उतने", "जैसा", "जैसी", "जैसे", "वैसा", "वैसे", "ऐसा", "ऐसी", "ऐसे",
    "सा", "सी", "एक",
    # particles, negation and fillers (14)
    "भी", "नहीं", "ही", "तो", "न", "मत", "केवल", "सिर्फ", "बस", "हाँ", "जरा",
    "वाला", "वाली", "वाले",
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
