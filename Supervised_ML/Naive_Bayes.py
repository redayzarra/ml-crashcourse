"""
Naive Bayes classifiers are essentially machine learning models that accept text as
input and generate a probabiltity to classify the data. We could write it as:
                  P(spam | message)
The expression above basically asks what is the probability of spam given a certain
message. 

Stemming is removing the suffixes -ing's, -ed's, etc. from a word and reassigning
it to the same word. Essentially getting rid of all suffixes. Cheaper option.

Lemmatization is when you group together forms of the same word. So all the similar
words with and without suffixes will just be mapped together. More expensive.
"""