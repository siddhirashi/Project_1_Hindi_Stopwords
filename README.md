# Hindi Stop Words for NLP

**Assignment 1 · Indic stop words · Monsoon Semester 2026**
Author: Siddhi Rashi 25MA0012 · Digital Humanities and Social Sciences

**Abstract.** Stop words are the small grammatical words (और, है, का) that carry almost no topic information and are usually removed before text is analysed. For this assignment I wrote a list of 200 Hindi stop words in Devanagari, grouped by grammatical role, plus a short helper that uses the list to clean a sentence. The word list is in [`hindi_stopwords.py`](hindi_stopwords.py).

---

## What is in this repository

| File | What it is |
|---|---|
| [`hindi_stopwords.py`](hindi_stopwords.py) | The stop-word list and the `remove_stopwords()` helper |
| `README.md` | This page |

The file name follows the pattern in the assignment sheet (`<language>_stopwords.py`) and the header block (topic, author, description, semester, affiliation) is copied from the sheet's template.

## What I did, step by step

1. **Started from the sample.** The assignment sheet gives five Hindi words as an example (और, लेकिन, या, यह, वह) and says to modify the list. I kept those five and extended the list to 200 words.
2. **Picked words by reading Hindi text.** I went through a few ordinary Hindi paragraphs and marked the small words that do grammatical work but say nothing about the subject.
3. **Grouped them by grammatical role** so the list is easy to check and extend:

| Group | Words |
|---|---|
| Conjunctions | और, लेकिन, या, क्योंकि, किंतु, परंतु, मगर, तथा, एवं, अथवा, कि, जबकि, इसलिए, ताकि, यानी, बल्कि, अगर, यदि, वरना |
| Personal pronouns | मैं, हम, आप, तुम, तू, यह, वह, ये, वे, मुझे, हमें, तुम्हें, उसे, इसे, उन्हें, इन्हें |
| Demonstratives and determiners | इस, उस, इन, उन, कुछ, कोई, किसी, सब, सभी, हर, अन्य, कई |
| Possessive pronouns | मेरा, मेरी, मेरे, हमारा, हमारी, हमारे, तुम्हारा, तुम्हारी, तुम्हारे, आपका, आपकी, आपके, उसका, उसकी, उसके, इसका, इसकी, इसके, उनका, उनकी, उनके, अपना, अपनी, अपने, खुद, स्वयं |
| Relative and interrogative words | जो, जिस, जिन, जिसे, जिसका, जिसके, कौन, किस, किन, क्या, क्यों, कैसे, कहाँ, कब, कितना |
| Postpositions | का, की, के, को, से, में, पर, तक, ने, द्वारा, लिए, साथ, बाद, पहले, ऊपर, नीचे, बीच, अंदर, बाहर, पास, बिना, सामने |
| Adverbs of place and time | यहाँ, वहाँ, यहां, वहां, जब, तब, अब, तभी, अभी, फिर, कभी, हमेशा, अक्सर, जहाँ |
| Auxiliary verbs | है, हैं, था, थी, थे, हो, हूँ, हूं, होता, होती, होते, हुआ, हुई, हुए, होगा, होगी, होंगे, रहा, रही, रहे, सकता, सकती, सकते, चाहिए |
| Light and common verbs | गया, गई, गए, गये, जाए, पड़ा, पड़ी, लगा, लगी, लगे, करना, करने, करके, किया, कर, दिया, लिया |
| Degree, manner and quantity | बहुत, ज्यादा, अधिक, थोड़ा, कम, इतना, इतनी, इतने, उतना, उतने, जैसा, जैसी, जैसे, वैसा, वैसे, ऐसा, ऐसी, ऐसे, सा, सी, एक |
| Particles, negation and fillers | भी, नहीं, ही, तो, न, मत, केवल, सिर्फ, बस, हाँ, जरा, वाला, वाली, वाले |

That makes 200 words in total.

4. **Wrote a small tokeniser and filter.** The function `remove_stopwords(text)` finds the Devanagari words with a regular expression and returns the ones that are not in the list. The regular expression keeps letters, vowel signs and the nukta, but leaves out the danda (।) and double danda (॥), so that a full stop does not stick to the last word of a sentence. The list is turned into a `set` once so that look-ups are fast.
5. **Ran it on a sentence** to see whether it behaves.

## Output

Running `python hindi_stopwords.py` prints:

```
Stop words in list : 200
Before             : वह गाँव में रहता है और हर सुबह नदी के किनारे टहलने जाता है।
After              : गाँव रहता सुबह नदी किनारे टहलने जाता
```

Seven of the fourteen words were removed (वह, में, है, और, हर, के, है), and what is left is the part that says what happens and where: the village, the river, the morning walk. The danda at the end is dropped by the tokeniser.

Using it from another script:

```python
from hindi_stopwords import hindi_stopwords, remove_stopwords

remove_stopwords("यह एक छोटी सी कहानी है")
# ['एक', 'छोटी', 'सी', 'कहानी']
```

## Limits I noticed

- **Some words still survive.** In the example above, "रहता" and "जाता" are kept because they are full verbs, not just grammatical helpers. Even a 200-word list cannot cover every inflected form.
- **Stop words depend on the task.** For topic modelling, "नहीं" is noise. For sentiment analysis it flips the meaning of a sentence, so it should be taken out of the list.
- **No stemming.** "है" and "हैं" are listed separately because the code does exact matching only (so both forms, and spelling variants such as यहाँ / यहां, are listed). Hindi has many inflected forms that a stemmer or lemmatiser would handle better.

## Link for the website

Replace `USERNAME` and `REPOSITORY` with the real names before submitting.

| File | URL |
|---|---|
| hindi_stopwords.py | [https://github.com/siddhirashi/Project_1_Hindi_Stopwords/hindi_stopwords.py](https://github.com/siddhirashi/Project_1_Hindi_Stopwords/blob/main/hindi_stopwords.py) |
