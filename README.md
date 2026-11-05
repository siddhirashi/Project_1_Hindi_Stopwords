# Hindi Stop Words for NLP

**Assignment 1 · Indic stop words · Monsoon Semester 2026**
Author: Siddhi Rashi 25MA0012 · Digital Humanities and Social Sciences

**Abstract.** Stop words are the small grammatical words (और, है, का) that carry almost no topic information and are usually removed before text is analysed. For this assignment I wrote a list of 24 Hindi stop words in Devanagari, grouped by grammatical role, plus a short helper that uses the list to clean a sentence. The word list is in [`hindi_stopwords.py`](hindi_stopwords.py).

---

## What is in this repository

| File | What it is |
|---|---|
| [`hindi_stopwords.py`](hindi_stopwords.py) | The stop-word list and the `remove_stopwords()` helper |
| `README.md` | This page |

The file name follows the pattern in the assignment sheet (`<language>_stopwords.py`) and the header block (topic, author, description, semester, affiliation) is copied from the sheet's template.

## What I did, step by step

1. **Started from the sample.** The assignment sheet gives five Hindi words as an example (और, लेकिन, या, यह, वह) and says to modify the list. I kept those five and extended the list.
2. **Picked words by reading Hindi text.** I went through a few ordinary Hindi paragraphs and marked the small words that do grammatical work but say nothing about the subject.
3. **Grouped them by grammatical role** so the list is easy to check and extend:

| Group | Words |
|---|---|
| Conjunctions | और, लेकिन, या, क्योंकि |
| Pronouns and demonstratives | मैं, हम, आप, यह, वह, इस, उस, कुछ |
| Postpositions | का, की, के, को, से, में, पर |
| Auxiliary verbs | है, हैं, था |
| Particles and negation | भी, नहीं |

That makes 24 words in total.

4. **Wrote a small tokeniser and filter.** The function `remove_stopwords(text)` finds the Devanagari words with a regular expression and returns the ones that are not in the list. The regular expression keeps letters, vowel signs and the nukta, but leaves out the danda (।) and double danda (॥), so that a full stop does not stick to the last word of a sentence. The list is turned into a `set` once so that look-ups are fast.
5. **Ran it on a sentence** to see whether it behaves.

## Output

Running `python hindi_stopwords.py` prints:

```
Stop words in list : 24
Before             : वह गाँव में रहता है और हर सुबह नदी के किनारे टहलने जाता है।
After              : गाँव रहता हर सुबह नदी किनारे टहलने जाता
```

Six of the fourteen words were removed (वह, में, है, और, के, है), and what is left is the part that says what happens and where: the village, the river, the morning walk. The danda at the end is dropped by the tokeniser.

Using it from another script:

```python
from hindi_stopwords import hindi_stopwords, remove_stopwords

remove_stopwords("यह एक छोटी सी कहानी है")
# ['एक', 'छोटी', 'सी', 'कहानी']
```

## Limits I noticed

- **A short list leaves things behind.** In the example above, "रहता" and "हर" survive because they are not in my 24 words. For heavier cleaning the list should be longer.
- **Stop words depend on the task.** For topic modelling, "नहीं" is noise. For sentiment analysis it flips the meaning of a sentence, so it should be taken out of the list.
- **No stemming.** "है" and "हैं" are listed separately because the code does exact matching only. Hindi has many inflected forms that a stemmer or lemmatiser would handle better.

## Link for the website

Replace `USERNAME` and `REPOSITORY` with the real names before submitting.

| File | URL |
|---|---|
| hindi_stopwords.py | https://github.com/USERNAME/REPOSITORY/blob/main/hindi_stopwords.py |
