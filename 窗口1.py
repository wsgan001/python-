# -*- coding: cp936 -*-
from Tkinter import *  #����ģ��
#resize�����������ı����ִ�С�ģ����������ı�ʱ����
def resize(ev=None):
 label.config(font='Helvetica -%d bold'%scale.get())
#config��������ͨ����������Ĳ������ı�����ģ�����ı����font�����С
top=Tk()   #�����������������ڵĳ�ʼ��С600x400
top.geometry('600x400')  #
label=Label(top,text='Hello world!',font='Helvetica -12 bold')     #���ñ�ǩ����ĳ�ʼ��С
label.pack(fill=Y,expand=1)
#scale����������������
scale=Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)  #������ʼλ��
scale.pack(fill=X,expand=1)
quit = Button(top,text='QUIT',command=top.quit,activeforeground='white',
activebackground='red')
quit.pack()
mainloop()
