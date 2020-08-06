from heapq import nlargest
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
# Pkgs for Normalizing Text
# Import Heapq for Finding the Top N Sentences


def text_summarizer(raw_docx):
    raw_text = raw_docx

    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency
# word.text is tokenization in spacy
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [sentence for sentence in docx.sents]

    # Calculate Sentence Score and Ranking
    sentence_scores = {}
    for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Find N Largest
    summary_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [w.text for w in summary_sentences]
    summary = ' '.join(final_sentences)
    # print("Original Document\n")
    # print(raw_docx)
    # print("Total Length:", len(raw_docx))
    # print('\n\nSummarized Document\n')
    # print(summary)
    # print("Total Length:", len(summary))
    return summary


# document3 = """Grylls was born in London, England in 1974.[2] From a family with strong cricketing background, his grandfather Neville Ford and great-great-grandfather William Augustus Ford, were both first-class cricketers. He grew up in Donaghadee, Northern Ireland until the age of four, when his family moved to Bembridge on the Isle of Wight.[3][4]

# He is the son of Conservative politician Sir Michael Grylls and his wife Lady Sarah "Sally" (née Ford).[5] Grylls has one sibling, an elder sister, Lara Fawcett, who gave him the nickname 'Bear' when he was a week old.[6]

# From an early age, he learned to climb and sail with his father, who was a member of the prestigious Royal Yacht Squadron. As a teenager, he learned to skydive and earned a second dan black belt in Shotokan karate.[7] He speaks English, Spanish, and French.[8] He is Anglican,[9] and has described his faith as the "backbone" in his life.[10]

# Grylls married Shara Cannings Knight in 2000.[11][12] They have three sons named Jesse (born 2003), Marmaduke (born 2006) and Huckleberry (born 2009).[13][14]

# In August 2015, Grylls left his young son, Jesse, on Saint Tudwal's Island along the North Wales coast, as the tide approached, leaving him to be rescued by the Royal National Lifeboat Institution (RNLI) as part of their weekly practice missions. Jesse was unharmed, though the RNLI later criticised him for the stunt, saying its crew "had not appreciated" that a child would be involved.[15] """

# document1 = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""

# text_summarizer(document1)
