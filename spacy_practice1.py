import spacy
nlp=spacy.load("en")
docx=nlp("Spacy is cool tool")
print(docx)
docx1=nlp(u"Spacy is cool tool like NLTK")
print(docx1)
myfile=nlp(open("C:/Users/Vidya/Desktop/mangoes.txt").read())
print(myfile)
for num, sentence in enumerate(myfile.sents):
    print(f'{num}:{sentence}')
for token in docx:
    print(token.text)
print([token.text for token in docx])
print(docx)
for word in docx:
    print(word.text,word.shape_)
exdoc=nlp("Hello hello HELLO HeLLO")
for word in exdoc:
    print("Token=>",word.text,"shape",word.shape_,word.is_alpha,word.is_stop)