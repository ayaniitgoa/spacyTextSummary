import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()


def readingTime(mytext):
	total_words = len([ token.text for token in nlp(mytext)])
	estimatedTime = total_words/200.0
	return estimatedTime
