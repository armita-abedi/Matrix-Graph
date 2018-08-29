import nltk
# >>> nltk.download()   # Download all books
from nltk.book import *

# >>> text1
# >>> text3


# A concordance view shows us every occurrence of a given word, together with some context.
text1.concordance("monstrous")



# We can determine the location of a word in the text: how many words from the beginning it appears.
# This positional information can be displayed using a dispersion plot. Each stripe represents an instance of a word, and each row represents the entire text.
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])


# To get the number of words (or tokens) in a next
len(text3)
sorted(set(text3))
len(set(text3)) # to get the number of unique tokens


# We can count how often a word occurs in a text, and compute what percentage of the text is taken up by a specific word
def lexical_diversity(text):
    return len(set(text))/len(text)


def percentage(count, total):
    return 100 * count / total


# Adding two lists	
['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail']




# To join the words of a list to make a single string, or split a string into a list
' '.join(['Monty', 'Python'])   # result: 'Monty Python'
'Monty Python'.split()          # result: ['Monty', 'Python']



# frequency distribution tells us the frequency of each vocabulary item in the text.
# Let's use a  FreqDist to find the 50 most frequent words of text 1

fdist1 = FreqDist(text1)
fdist1.most_common(50)    # return a tuple of (word, frequency)
fdist1['whale']

# To generate a cumulative frequency plot for these words
# Graph shows these 50 words account for nearly half the book!
fdist1.plot(50, cumulative=True)


# If the frequent words don't help us, how about the words that occur once only?
fdist1.hapaxes()
# It seems that there are too many rare words, and without seeing the context we probably can't guess what half of the hapaxes mean in any case!
# Since neither frequent nor infrequent words help, we need to try something else.

# To find the words with length greater than 15;
V = set(text1)
long_words = [w for w in V if len(w) > 15]


# Notice that the long words in text4 reflect its national focus — constitutionally, transcontinental —
# whereas those in text5 reflect its informal content: boooooooooooglyyyyyy and yuuuuuuuuuuuummmmmmmmmmmm.
# These very long words are often hapaxes (i.e., unique) and perhaps it would be better to find frequently occurring long words.
# This seems promising since it eliminates frequent short words (e.g., the) and infrequent long words (e.g. antiphilosophists).
# Here are all words from the chat corpus that are longer than seven characters, that occur more than seven times;
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

# A collocation is a sequence of words that occur together unusually often.
list(bigram(["wine", "wine", "white", "maroon"])

# Collocations are essentially just frequent bigrams in the text.
# The collocations that emerge are very specific to the genre of the texts. 
text4.collocations()
text8.collocations()


# a FreqDist out of a long list of numbers, where each number is the length of the corresponding word in the text
[len(w) for w in text1]    # result: [1, 4, 4, 2, 6, 8, 4, 1, 9, 1, 1, 8, 2, 1, 4, 11, 5, 2, 1, 7, 6, 1, 3, 4, 5, 2, ...]
fdist = FreqDist(len(w) for w in text1)  [2]
fdist    # result: FreqDist({3: 50223, 1: 47933, 4: 42345, 2: 38513, 5: 26597, 6: 17111, 7: 14399,
                           # 8: 9966, 9: 6428, 10: 3528, ...})
fdist.most_common()        # [(3, 50223), (1, 47933), (4, 42345), (2, 38513), (5, 26597), (6, 17111), (7, 14399),
                           #  (8, 9966), (9, 6428), (10, 3528), (11, 1873), (12, 1053), (13, 567), (14, 177),
                           #  (15, 70), (16, 22), (17, 12), (18, 1), (20, 1)]
fdist.max() # result: 3
fdist[3]    # result: 50223
fdist.freq(3)   # result: 0.19255882431878046
# Further analysis of word length might help us understand differences between authors, genres, or languages.


# Functions Defined for NLTK's Frequency Distributions
fdist = FreqDist(samples)	 # create a frequency distribution containing the given samples
fdist[sample] += 1	         # increment the count for this sample
fdist['monstrous']	         # count of the number of times a given sample occurred
fdist.freq('monstrous')	         # frequency of a given sample
fdist.N()	                 # total number of samples
fdist.most_common(n)	         # the n most common samples and their frequencies
for sample in fdist:	         # iterate over the samples
fdist.max()	                 # sample with the greatest count
fdist.tabulate()	         # tabulate the frequency distribution
fdist.plot()	                 # graphical plot of the frequency distribution
fdist.plot(cumulative=True)	 # cumulative plot of the frequency distribution
fdist1 |= fdist2	         # update fdist1 with counts from fdist2
fdist1 < fdist2	                 # test if samples in fdist1 occur less frequently than in fdist2

# Some Word Comparison Operators
s.startswith(t)	# test if s starts with t
s.endswith(t)	# test if s ends with t
t in s	        # test if t is a substring of s
s.islower()	# test if s contains cased characters and all are lowercase
s.isupper()	# test if s contains cased characters and all are uppercase
s.isalpha()	# test if s is non-empty and all characters in s are alphabetic
s.isalnum()	# test if s is non-empty and all characters in s are alphanumeric
s.isdigit()	# test if s is non-empty and all characters in s are digits
s.istitle()	# test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)


	
[w for w in set(text1) if w.endswith('ableness')]      # ['comfortableness', 'honourableness', 'immutableness', 'indispensableness', ...]
[term for term in set(text4) if 'gnt' in term]         # ['Sovereignty', 'sovereignties', 'sovereignty']
sorted(item for item in set(text6) if item.istitle()   # ['A', 'Aaaaaaaaah', 'Aaaaaaaah', 'Aaaaaah', 'Aaaah', 'Aaaaugh', 'Aaagh', ...]
sorted(item for item in set(sent7) if item.isdigit())  # ['29', '61']


# we are not double-counting words like This and this
# we also eliminate numbers and punctuation from the vocabulary count by filtering out any non-alphabetic items
len(set(word.lower() for word in text1 if word.isalpha()))



# The thieves stole the paintings. They were subsequently found.
# To find the antecedent of the pronoun they, either thieves or paintings.
# anaphora resolution — identifying what a pronoun or noun phrase refers to —
# semantic role labeling — identifying how a noun phrase relates to the verb (as agent, patient, instrument, and so on).
       

# Accessing Text Corpora
from nltk.corpus import gutenberg
gutenberg.fileids()  # ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', ...]
emma = gutenberg.words('austen-emma.txt')

# For a compact output display, we will round each number to the nearest integer, using round().
# To displays three statistics for each text: average word length, average sentence length, and the number of times each vocabulary item appears in the text on average (our lexical diversity score).
# By contrast average sentence length and lexical diversity appear to be characteristics of particular authors.
       
for fileid in gutenberg.fileids():
       num_chars = len(gutenberg.raw(fileid))   # returns how many letters occur in the text, including the spaces between words.
       num_words = len(gutenberg.words(fileid))
       num_sents = len(gutenberg.sents(fileid))
       num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
       print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)



# The Brown Corpus is a convenient resource for studying systematic differences between genres, a kind of linguistic inquiry known as stylistics.
# To compare genres in their usage of modal verbs. The first step is to produce the counts for a particular genre.
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end=' ')

 	
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
#                  can could  may might must will
#            news   93   86   66   38   50  389
#        religion   82   59   78   12   54   71
#         hobbies  268   58  131   22   83  264
# science_fiction   16   49    4   12    8   16
#         romance   74  193   11   51   45   43
#           humor   16   30    8    8    9   13


# Observe that the most frequent modal in the news genre is will, while the most frequent modal in the romance genre is could.


from nltk.corpus import inaugural
inaugural.fileids()                                   # ['1789-Washington.txt', '1793-Washington.txt', '1797-Adams.txt', ...]
[fileid[:4] for fileid in inaugural.fileids()]        #['1789', '1793', '1797', '1801', '1805', '1809', '1813', '1817', '1821', ...]
# Notice that the year of each text appears in its filename. To get the year out of the filename, we extracted the first four characters, using fileid[:4].

# Let's look at how the words America and citizen are used over time.
# The following code converts the words in the Inaugural corpus to lowercase using w.lower().
# Then checks if they start with either of the "targets" america or citizen using startswith().
# Thus it will count words like American's and Citizens. 
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
cfd.plot()


# FreqDist(mylist) would compute the number of occurrences of each item in the list. 
# When the texts of a corpus are divided into several categories, by genre, topic, author, etc, we can maintain separate frequency distributions for each category.
# A conditional frequency distribution is a collection of frequency distributions, each one for a different "condition". The condition will often be the category of the text.

# A frequency distribution counts observable events, such as the appearance of words in a text.
text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
       
# A conditional frequency distribution needs to pair each event with a condition. So instead of processing a sequence of words, we have to process a sequence of pairs.
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...]      


genre_word = [(genre, word) for genre in ['news', 'romance'] for word in brown.words(categories=genre)]
cfd = nltk.ConditionalFreqDist(genre_word)
cfd.conditions()      # ['news', 'romance']
print(cfd['news'])    # <FreqDist with 14394 samples and 100554 outcomes>
print(cfd['romance']) # <FreqDist with 8452 samples and 70022 outcomes>
cfd['romance'].most_common(20)
#[(',', 3899), ('.', 3736), ('the', 2758), ('and', 1776), ('to', 1502),
#('a', 1335), ('of', 1186), ('``', 1045), ("''", 1044), ('was', 993),
#('I', 951), ('in', 875), ('he', 702), ('had', 692), ('?', 690),
#('her', 651), ('that', 583), ('it', 573), ('his', 559), ('she', 496)]
cfd['romance']['could']   # 193



# The bigrams() function takes a list of words and builds a list of consecutive word pairs.
sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven','and', 'the', 'earth', '.']
list(nltk.bigrams(sent))
#[('In', 'the'), ('the', 'beginning'), ('beginning', 'God'), ('God', 'created'),
#('created', 'the'), ('the', 'heaven'), ('heaven', 'and'), ('and', 'the'),
#('the', 'earth'), ('earth', '.')]


# NLTK's Conditional Frequency Distributions
cfdist = ConditionalFreqDist(pairs)	     # create a conditional frequency distribution from a list of pairs
cfdist.conditions()	                     # the conditions
cfdist[condition]	                     # the frequency distribution for this condition
cfdist[condition][sample]	             # frequency for the given sample for this condition
cfdist.tabulate()	                     # tabulate the conditional frequency distribution
cfdist.tabulate(samples, conditions)	     # tabulation limited to the specified samples and conditions
cfdist.plot()	                             # graphical plot of the conditional frequency distribution
cfdist.plot(samples, conditions)	     # graphical plot limited to the specified samples and conditions
cfdist1 < cfdist2	                     # test if samples in cfdist1 occur less frequently than in cfdist2



# A collection of variable and function definitions in a file is called a Python module.
# A collection of related modules is called a package.


# A lexicon, or lexical resource, is a collection of words and/or phrases along with associated information such as part of speech and sense definitions.
# A lexical entry consists of a headword (also known as a lemma) along with additional information such as the part of speech and the sense definition.
# Two distinct words having the same spelling are called homonyms.


# NLTK includes some corpora that are nothing more than wordlists. We can use it to find unusual or mis-spelt words in a text corpus.

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
#['abbeyland', 'abhorred', 'abilities', 'abounded', 'abridgement', 'abused', 'abuses',
#'accents', 'accepting', 'accommodations', 'accompanied', 'accounted', 'accounts',
#'accustomary', 'aches', 'acknowledging', 'acknowledgment', 'acknowledgments', ...]
unusual_words(nltk.corpus.nps_chat.words())
#['aaaaaaaaaaaaaaaaa', 'aaahhhh', 'abortions', 'abou', 'abourted', 'abs', 'ack',
#'acros', 'actualy', 'adams', 'adds', 'adduser', 'adjusts', 'adoted', 'adreniline',
#'ads', 'adults', 'afe', 'affairs', 'affari', 'affects', 'afk', 'agaibn', 'ages', ...]


# There is also a corpus of stopwords, that is, high-frequency words like the, to and also that we sometimes want to filter out of a document before further processing.
# Stopwords usually have little lexical content, and their presence in a text fails to distinguish it from other texts.
from nltk.corpus import stopwords
def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

content_fraction(nltk.corpus.reuters.words())    #0.7364374824583169
# With the help of stopwords we filter out over a quarter of the words of the text.

# How many words with six letter or more can you make that contains 'r' and 5 or more letters from a puzzle list
# It is trickier to check that candidate solutions only use combinations of the supplied letters, especially since some of the supplied letters appear twice in the puzzle list.
# The FreqDist comparison method permits us to check that the frequency of each letter in the candidate word is less than or equal to the frequency of the corresponding letter in the puzzle list.
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
[w for w in wordlist if len(w) >= 6 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters] 
#['glover', 'gorlin', 'govern', 'grovel', 'ignore', 'involver', 'lienor',
#'linger', 'longer', 'lovering', 'noiler', 'overling', 'region', 'renvoi',
#'revolving', 'ringle', 'roving', 'violer', 'virole']


# One more wordlist corpus is the Names corpus, containing 8,000 first names categorized by gender.
# The male and female names are stored in separate files. Let's find names which appear in both files, i.e. names that are ambiguous for gender:
names = nltk.corpus.names
names.fileids()   # ['female.txt', 'male.txt']
male_names = names.words('male.txt')
female_names = names.words('female.txt')
[w for w in male_names if w in female_names]
#['Abbey', 'Abbie', 'Abby', 'Addie', 'Adrian', 'Adrien', 'Ajay', 'Alex', 'Alexis',
#'Alfie', 'Ali', 'Alix', 'Allie', 'Allyn', 'Andie', 'Andrea', 'Andy', 'Angel',
#'Angie', 'Ariel', 'Ashley', 'Aubrey', 'Augustine', 'Austin', 'Averil', ...]

#It is well known that names ending in the letter a are almost always female.
names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])   # name[-1] is the last letter of  name.
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()




# a word can have multiple synsets (synonym set). Here 'motorcar' has one synset only.  	
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')   # [Synset('car.n.01')]

# The entity car.n.01 is called a synset, or "synonym set", a collection of synonymous words (or "lemmas")
wn.synset('car.n.01').lemma_names()           #['car', 'auto', 'automobile', 'machine', 'motorcar']

wn.synset('car.n.01').definition()       # 'a motor vehicle with four wheels; usually propelled by an internal combustion engine'
wn.synset('car.n.01').examples()         # ['he needs a car to get to work']
wn.synset('car.n.01').lemmas()           # [Lemma('car.n.01.car'), Lemma('car.n.01.auto'), Lemma('car.n.01.automobile'),
                                         # Lemma('car.n.01.machine'), Lemma('car.n.01.motorcar')]
wn.lemma('car.n.01.automobile')          # Lemma('car.n.01.automobile')
wn.lemma('car.n.01.automobile').synset() # Synset('car.n.01')
wn.lemma('car.n.01.automobile').name()   # 'automobile'


       
 	
wn.synsets('car')   # [Synset('car.n.01'), Synset('car.n.02'), Synset('car.n.03'), Synset('car.n.04'), Synset('cable_car.n.01')]
for synset in wn.synsets('car'):
    print(synset.lemma_names())
#['car', 'auto', 'automobile', 'machine', 'motorcar']
#['car', 'railcar', 'railway_car', 'railroad_car']
#['car', 'gondola']
#['car', 'elevator_car']
#['cable_car', 'car']

wn.lemmas('car')    # [Lemma('car.n.01.car'), Lemma('car.n.02.car'), Lemma('car.n.03.car'), Lemma('car.n.04.car'), Lemma('cable_car.n.01.car')]


# Given a concept like motorcar, we can look at the concepts that are more specific; the (immediate) hyponyms.
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[0]         # Synset('ambulance.n.01')
sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())
""" ['Model_T', 'S.U.V.', 'SUV', 'Stanley_Steamer', 'ambulance', 'beach_waggon',
'beach_wagon', 'bus', 'cab', 'compact', 'compact_car', 'convertible',
'coupe', 'cruiser', 'electric', 'electric_automobile', 'electric_car',
'estate_car', 'gas_guzzler', 'hack', 'hardtop', 'hatchback', 'heap',
'horseless_carriage', 'hot-rod', 'hot_rod', 'jalopy', 'jeep', 'landrover',
'limo', 'limousine', 'loaner', 'minicar', 'minivan', 'pace_car', 'patrol_car',
'phaeton', 'police_car', 'police_cruiser', 'prowl_car', 'race_car', 'racer',
'racing_car', 'roadster', 'runabout', 'saloon', 'secondhand_car', 'sedan',
'sport_car', 'sport_utility', 'sport_utility_vehicle', 'sports_car', 'squad_car',
'station_waggon', 'station_wagon', 'stock_car', 'subcompact', 'subcompact_car',
'taxi', 'taxicab', 'tourer', 'touring_car', 'two-seater', 'used-car', 'waggon',
'wagon'] """


# We can also navigate up the hierarchy by visiting hypernyms. Some words have multiple paths, because they can be classified in more than one way.
# There are two paths between car.n.01 and entity.n.01 because wheeled_vehicle.n.01 can be classified as both a vehicle and a container.
motorcar.hypernyms()    # [Synset('motor_vehicle.n.01')]
paths = motorcar.hypernym_paths()



# A text corpus is a large, structured collection of texts. NLTK comes with many corpora, e.g., the Brown Corpus, nltk.corpus.brown.
# Some text corpora are categorized, e.g., by genre or topic; sometimes the categories of a corpus overlap each other.
# A conditional frequency distribution is a collection of frequency distributions, each one for a different condition. They can be used for counting word frequencies, given a context or a genre.
# WordNet is a semantically-oriented dictionary of English, consisting of synonym sets — or synsets — and organized into a network.


from urllib import request
url = "http://www.gutenberg.org/files/12345/12345.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw)    # <class 'str'>   # it is just simple text
len(raw)     # 281780
raw[:75]     # 'The Project Gutenberg EBook of Friday, the Thirteenth, by Thomas W. Lawson\r'


# tokenization: to produce a list of words and punctuation.
from nltk import word_tokenize
tokens = word_tokenize(raw)
type(tokens)   # <class 'list'>
len(tokens)    # 58388


# Notice that NLTK was needed for tokenization, but not for any of the earlier tasks of opening a URL and reading it into a string.
# If we now take the further step of creating an NLTK text from this list, we can carry out all of the other linguistic processing we saw previously.

import nltk
text = nltk.Text(tokens)
type(text)       # <class 'nltk.text.Text'>
text[1024:1062]  # ['of', 'which', 'I', 'of', 'all', 'men', 'best', 'knew', 'the', 'meaning', '.', 'The', 'big', 'brown', 'eyes', 'were', 'set', 'on', 'space', ';', 'the', 'outer', 'corners', 'of', 'the', 'handsome', 'mouth', 'were', 'drawn', 'hard', 'and', 'tense', 'as', 'though', 'weighted', '.', 'As', 'I']
text.collocations()
#Barry Conant; Project Gutenberg-tm; Beulah Sands; Wall Street; Stock
#Exchange; Project Gutenberg; New York; Bob Brownley; Miss Sands;
#Literary Archive; United States; Mr. Brownley; Gutenberg-tm
#electronic; electronic works; Archive Foundation; Gutenberg Literary;
#Dear Sir; 'the Street; Mr. Randolph; 'Standard Oil    


url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
html[:60]   # '<!doctype html public "-//W3C//DTD HTML 4.0 Transitional//EN'
# You can type print(html) to see the HTML content in all its glory, including meta tags, an image map, JavaScript, forms, and tables.

#To get text out of HTML we will use a Python library called BeautifulSoup
from bs4 import BeautifulSoup
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)

# This still contains unwanted material concerning site navigation and related stories.
# With some trial and error you can find the start and end indexes of the content and select the tokens of interest, and initialize a text as before.
tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')
#Displaying 5 of 5 matches:
#hey say too few people now carry the gene for blondes to last beyond the next
#blonde hair is caused by a recessive gene . In order for a child to have blond
#have blonde hair , it must have the gene on both sides of the family in the g
#ere is a disadvantage of having that gene or by chance . They do n't disappear
#des would disappear is if having the gene was a disadvantage and I do not thin


# Reading local files:
f = open('document.txt')
raw = f.read()

# To examine the content of current directory from within Python
import os
os.listdir('C:\ARMITA\Code Practice')


f = open('document.txt', 'r')  # Open the file for reading
for line in f:
       print(line.strip())

#Time flies like an arrow.
#Fruit flies like a banana.
# Here we use the strip() method to remove the newline character at the end of the input line.

 	
s = input("Enter some text: ")
Enter some text: On an exceptionally hot evening early in July
print("You typed", len(word_tokenize(s)), "words.")   #You typed 8 words.


s.find(t)	 # index of first instance of string t inside s (-1 if not found)
s.rfind(t)	 # index of last instance of string t inside s (-1 if not found)
s.index(t)	 # like s.find(t) except it raises ValueError if not found
s.rindex(t)	 # like s.rfind(t) except it raises ValueError if not found
s.join(text)	 # combine the words of the text into a string using s as the glue
s.split(t)	 # split s into a list wherever a t is found (whitespace by default)
s.splitlines()	 # split s into a list of strings, one per line
s.lower()	 # a lowercased version of the string s
s.upper()	 # an uppercased version of the string s
s.title()	 # a titlecased version of the string s
s.strip()	 # a copy of s without leading or trailing whitespace
s.replace(t, u)	 # replace instances of t with u inside s


# To use regular expressions in Python we need to import the re library using: import re.
import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

# words that ends with ed
[w for w in wordlist if re.search('ed$', w)]          # ['abaissed', 'abandoned', 'abased', 'abashed', 'abatised', 'abed', 'aborted', ...]

# 8-letter word with j as its third letter and t as its sixth letter.
[w for w in wordlist if re.search('^..j..t..$', w)]   # ['abjectly', 'adjuster', 'dejected', 'dejectly', 'injector', 'majestic', ...]

# «^e-?mail$» will match both email and e-mail. We could count the total number of occurrences of this word (in either spelling) in a text using sum:
sum(1 for w in text if re.search('^e-?mail$', w))s


# words generated pressing the sequence 4653 on a phone. 
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
['gold', 'golf', 'hold', 'hole']


chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
[w for w in chat_words if re.search('^m+i+n+e+$', w)]  # ['miiiiiiiiiiiiinnnnnnnnnnneeeeeeeeee', 'miiiiiinnnnnnnnnneeeeeeee', 'mine', 'mmmmmmmmiiiiiiiiinnnnnnnnneeeeeeee']
[w for w in chat_words if re.search('^[ha]+$', w)]     # ['a', 'aaaaaaaaaaaaaaaaa', 'aaahhhh', 'ah', 'ahah', 'ahahah', 'ahh', 'ahhahahaha', 'ahhh', 'ahhhh', 'ahhhhhh', 'ahhhhhhhhhhhhhh', 'h', 'ha', 'haaa', 'hah', 'haha', 'hahaaa', 'hahah', 'hahaha', 'hahahaa', 'hahahah', 'hahahaha', ...]


# The ^ operator has another function when it appears as the first character inside square brackets.
# For example «[^aeiouAEIOU]» matches any character other than a vowel.


wsj = sorted(set(nltk.corpus.treebank.words()))
[w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)]      # ['0.0085', '0.05', '0.1', '0.16', '0.2', '0.25', '0.28', '0.3', '0.4', '0.5', '0.50', '0.54', '0.56', '0.60', '0.7', '0.82', '0.84', '0.9', '0.95', '0.99', '1.01', '1.1', '1.125', '1.14', '1.1650', '1.17', '1.18', '1.19', '1.2', ...]
[w for w in wsj if re.search('^[A-Z]+\$$', w)]            # ['C$', 'US$']
[w for w in wsj if re.search('^[0-9]{4}$', w)]            # ['1614', '1637', '1787', '1901', '1903', '1917', '1925', '1929', '1933', ...]
[w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]   # ['10-day', '10-lap', '10-year', '100-share', '12-point', '12-year', ...]
[w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)] # ['black-and-white', 'bread-and-butter', 'father-in-law', 'machine-gun-toting','savings-and-loan']
[w for w in wsj if re.search('(ed|ing)$', w)]  # ['62%-owned', 'Absorbed', 'According', 'Adopting', 'Advanced', 'Advancing', ...]
       
.	    # Wildcard, matches any character
^abc	    # Matches some pattern abc at the start of a string
abc$	    # Matches some pattern abc at the end of a string
[abc]	    # Matches one of a set of characters
[A-Z0-9]    # Matches one of a range of characters
ed|ing|s    # Matches one of the specified strings (disjunction)
*	    # Zero or more of previous item, e.g. a*, [a-z]* (also known as Kleene Closure)
+	    # One or more of previous item, e.g. a+, [a-z]+
?	    # Zero or one of the previous item (i.e. optional), e.g. a?, [a-z]?
{n}	    # Exactly n repeats where n is a non-negative integer
{n,}	    # At least n repeats
{,n}	    # No more than n repeats
{m,n}	    # At least m and no more than n repeats
a(b|c)+	    # Parentheses that indicate the scope of the operators
\.          # .
\$          # $



# The re.findall() ("find all") method finds all (non-overlapping) matches of the given regular expression.
# Let's find all the vowels in a word, then count them
word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]', word)       # ['u', 'e', 'a', 'i', 'a', 'i', 'i', 'i', 'e', 'i', 'a', 'i', 'o', 'i', 'o', 'u']
len(re.findall(r'[aeiou]', word))  # 16


# Let's look for all sequences of two or more vowels in some text, and determine their relative frequency:
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
fd.most_common(12)   # [('io', 549), ('ea', 476), ('ie', 331), ('ou', 329), ('ai', 261), ('ia', 253),
                     #  ('ee', 217), ('oo', 174), ('ua', 109), ('au', 106), ('ue', 105), ('ui', 95)]


from nltk.corpus import gutenberg, nps_chat
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
# In the following example, <.*> will match any single token, and enclose it in parentheses so only the matched word (e.g. monied) and not the matched phrase (e.g. a monied man) is produced.    
moby.findall(r"<a> (<.*>) <man>") # monied; nervous; dangerous; white; white; white; pious; queer; good; mature; white; Cape; great; wise; wise; butterless; white; fiendish;
chat = nltk.Text(nps_chat.words())
chat.findall(r"<.*> <.*> <bro>") # you rule bro; telling you bro; u twizted bro

chat.findall(r"<l.*>{3,}") # lol lol lol; lmao lol lol; lol lol lol; la la la la la; la la la; lala la; lovely lol lol love; lol lol lol.; la la la; la la la
	
from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")  # speed and other activities; water and other liquids; tomb and other landmarks; Statues and other monuments; pearls and other jewels; charts and other items; roads and other features; figures and other objects; military and other areas; demands and other factors;



 	
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)

#Observe that the Porter stemmer correctly handles the word lying (mapping it to lie), while the Lancaster stemmer does not.
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
[porter.stem(t) for t in tokens]
['DENNI', ':', 'Listen', ',', 'strang', 'women', 'lie', 'in', 'pond',
'distribut', 'sword', 'is', 'no', 'basi', 'for', 'a', 'system', 'of', 'govern',
'.', 'Suprem', 'execut', 'power', 'deriv', 'from', 'a', 'mandat', 'from',
'the', 'mass', ',', 'not', 'from', 'some', 'farcic', 'aquat', 'ceremoni', '.']
[lancaster.stem(t) for t in tokens]
['den', ':', 'list', ',', 'strange', 'wom', 'lying', 'in', 'pond', 'distribut',
'sword', 'is', 'no', 'bas', 'for', 'a', 'system', 'of', 'govern', '.', 'suprem',
'execut', 'pow', 'der', 'from', 'a', 'mand', 'from', 'the', 'mass', ',', 'not',
'from', 'som', 'farc', 'aqu', 'ceremony', '.']

       
# The WordNet lemmatizer only removes affixes if the resulting word is in its dictionary.
# This additional checking process makes the lemmatizer slower than the above stemmers. Notice that it doesn't handle lying, but it converts women to woman.
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]
['DENNIS', ':', 'Listen', ',', 'strange', 'woman', 'lying', 'in', 'pond',
'distributing', 'sword', 'is', 'no', 'basis', 'for', 'a', 'system', 'of',
'government', '.', 'Supreme', 'executive', 'power', 'derives', 'from', 'a',
'mandate', 'from', 'the', 'mass', ',', 'not', 'from', 'some', 'farcical',
'aquatic', 'ceremony', '.']


\b	# Word boundary (zero width)
\d	# Any decimal digit (equivalent to [0-9])
\D	# Any non-digit character (equivalent to [^0-9])
\s	# Any whitespace character (equivalent to [ \t\n\r\f\v])
\S	# Any non-whitespace character (equivalent to [^ \t\n\r\f\v])
\w	# Any alphanumeric character (equivalent to [a-zA-Z0-9_])
\W	# Any non-alphanumeric character (equivalent to  [^a-zA-Z0-9_])
\t	# The tab character
\n	# The newline character



text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = nltk.sent_tokenize(text)

'{} wants a {} {}'.format ('Lee', 'sandwich', 'for lunch')  #'Lee wants a sandwich for lunch'

'I want a {} right now'.format('coffee')  #'I want a coffee right now'

'from {1} to {0}'.format('A', 'B')  # 'from B to A'


sent = ['No', 'good', 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '.']
all(len(w) > 4 for w in sent)       # False
any(len(w) > 4 for w in sent)       # True
