#autotranslate.py
#pip install googletrans==3.1.0a0

from googletrans import Translator

trans=Translator()
# result=trans.translate('cat',dest='th')
# print(result.text)

article=open('article.txt','r')
article=article.read()
article=article.split()

print ('count',len(article))

result={}

for word in article:
	# print(word)
	res=trans.translate(word,dest='th')
	print(res.text)