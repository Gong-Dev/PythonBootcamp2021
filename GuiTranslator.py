#GuiTranslator.py
from tkinter import * #จากไลบราลี่ชื่อ tkinter โดย * คือให้ดึงความสามารถเฉพาะเมนหลักมาทั้งหมด
from tkinter import ttk #เลือกใช้ธีมที่ชื่อttk
from googletrans import Translator # ใช้google translator
translator = Translator()

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #ขนาด กว้างxสูง
GUI.title('โปรแกรมแปลภาษา by GONGGANG') #สร้างไตเติ้ล
#------- config-----------
FONT = ('ThsarabunPSK',18)
FONT2 = ('ThsarabunPSK',24)
FONT3 = ('ThsarabunPSK',26)
#------Label---------
L = ttk.Label(GUI,text='กรุณาใส่คำศัพท์ที่ต้องการ',font=FONT)
L.pack(pady=10) #แสดงlabel ด้วยการเว้นบน-ล่าง 10 pt
# -------Entry (ช่องกรอก)-------
v_vocab = StringVar() #กล่องเก็บช้อความ  กำหนด v_vocab คือ ตัวแปรString 
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT2,width=20) #สร้างช่องกรอกขึ้นมาโดยใช้ธีมttk และเก็บค่าเช้ากล่อง
E1.pack(pady=20) #แสดงช่องกรอก
# -------Button (ปุ่มแปล)-------
def Translate():
    vocab = v_vocab.get() #.get คือคำสั่งที่ทำให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    meni = vocab +' : '+meaning.text
    print(meni) #meaningต้อง .text เนื่องจากมาจากtranslateจึงต้องระบุ
    print(meaning.pronunciation)
    v_result.set(meaning.text)

B1 = ttk.Button(GUI,text='แปลคำศัพท์',command=Translate) #สร้างปุ่มขึ้นมาโดยใช้ธีมttk และใช้ฟังก์ชั่นTranslate
B1.pack(ipadx=20,ipady=10) #แสดงปุ่มขึ้นมาวางจากบนลงล่าง (กำหนดขนาดของปุ่ม)
#------Label2---------
L = ttk.Label(GUI,text='ความหมาย',font=FONT)
L.pack(pady=10) #แสดงlabel ด้วยการเว้นบน-ล่าง 10 pt
#-----Result-------
v_result = StringVar() #กล่องเก็บคำแปล ต้องเป็นSใหญ่และVใหญ่
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT3,foreground='green') #สร้างเลเบลที่แสดงความหมาย textvariableคือข้อความที่เปลี่ยนแปลงได้
R1.pack() #แสดงบนGUIด้วนคำสั่งpack

GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด (บรรทัดสุดท้าย)
