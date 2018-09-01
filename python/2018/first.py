from collections import Counter
sentence ='Hi this is kamesh.this article is about kerala floods.'

list_sentence = sentence.split()
list_variable = Counter(list_sentence)
print(list_variable.most_common())

final=' '.join(list_sentence)
print(final)