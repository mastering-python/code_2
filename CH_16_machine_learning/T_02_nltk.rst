>>> import nltk

>>> from nltk import sentiment

>>> nltk.download('vader_lexicon')
True

>>> sentences = [
...     'Python is a wonderful programming language',
...     'Weak-typed languages are prone to errors',
...     'I love programming in Python and I hate YAML',
... ]

>>> si = sentiment.SentimentIntensityAnalyzer()
>>> for sentence in sentences:
...     scores = si.polarity_scores(sentence)
...     print(sentence)
...     print('negative: {neg}, positive: {pos}'.format(**scores))
Python is a wonderful programming language
negative: 0.0, positive: 0.481
Weak-typed languages are prone to errors
negative: 0.324, positive: 0.0
I love programming in Python and I hate YAML
negative: 0.287, positive: 0.326
