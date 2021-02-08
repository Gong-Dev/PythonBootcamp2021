#autotranslate.py
#pip install googletrans==3.1.0a0
#pip install easyread
#pip install openpyxl

# from googletrans import Translator
from easyread.translator import Translate
from openpyxl import Workbook
from datetime import datetime
# result=trans.translate('cat',dest='th')
# print(result.text)

article=open('article.txt','r')
article=article.read()
article=article.split()

print ('count',len(article))

result=[]

for word in article:
	# print(word)
	res=Translate(word)
	if res != None:  #บางครั้ง
		# print(res['meaning'])
		result.append([word,res['meaning']])  #result.append['cat','แมว']
# print(result)

excelfile=Workbook()
sheet=excelfile.active

header=['Vocab','Translate']
sheet.append(header)

for r in result:
	sheet.append(r)

dt=datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save('Vocab-{}.xlsx'.format(dt))
