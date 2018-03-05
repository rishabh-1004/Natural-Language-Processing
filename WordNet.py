from nltk.corpus import wordnet
syns= wordnet.synsets("program")


synonyms = []
antonyms = []


print (syns)

"""
Output

[Synset('plan.n.01'), Synset('program.n.02'), Synset('broadcast.n.02'), Synset('platform.n.02'), Synset('program.n.05'), Synset('course_of_study.n.01'), Synset('program.n.07'), Synset('program.n.08'), Synset('program.v.01'), Synset('program.v.02')]

"""

#synset
print (syns[0].name())
# output - Synset('plan.n.01')

#just the word
print (syns[0].lemmas()[0].name())
#output - plan

#defination
print(syns[0].definition())
# Output- a series of steps to be carried out or goals to be accomplished

#examples
print(syns[0].examples())
['they drew up a six-step plan', 'they discussed plans for a new bond issue']


for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())

print (synonyms)
print (antonyms)

"""
Output

[u'they drew up a six-step plan', u'they discussed plans for a new bond issue']
[u'good', u'good', u'goodness', u'good', u'goodness', u'commodity', u'trade_good', u'good', u'good', u'full', u'good', u'good', u'estimable', u'good', u'honorable', u'respectable', u'beneficial', u'good', u'good', u'good', u'just', u'upright', u'adept', u'expert', u'good', u'practiced', u'proficient', u'skillful', u'skilful', u'good', u'dear', u'good', u'near', u'dependable', u'good', u'safe', u'secure', u'good', u'right', u'ripe', u'good', u'well', u'effective', u'good', u'in_effect', u'in_force', u'good', u'good', u'serious', u'good', u'sound', u'good', u'salutary', u'good', u'honest', u'good', u'undecomposed', u'unspoiled', u'unspoilt', u'good', u'well', u'good', u'thoroughly', u'soundly', u'good']
[u'evil', u'evilness', u'bad', u'badness', u'bad', u'evil', u'ill']

"""


w1 = wordnet.synset("ship.n.01") 
w2 = wordnet.synset("boat.n.01")
print (w1.wup_similarity(w2))

#Output
#0.9090909090909091

w1 = wordnet.synset("ship.n.01") 
w2 = wordnet.synset("car.n.01")
print (w1.wup_similarity(w2))

#Output
#0.695652173913


w1 = wordnet.synset("ship.n.01") 
w2 = wordnet.synset("cat.n.01")
print (w1.wup_similarity(w2))

#Output
#0.32

