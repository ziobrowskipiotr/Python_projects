#import moduls
from langdetect import detect
import tkinter as tk
import iso639

#writing function for creating window Tkinter
def detect_lang():
   window = tk.Tk()
   window.title('My Language Detector')
   window.geometry('600x400')
   head = tk.Label(window, text='Language Detector', font=('Calibri 15'), anchor='center')
   window.configure(background='#5dc2be')
   head.pack(pady=10) #space between the header and the window

   def check_language():
       new_text = text.get()
       lang_code = detect(new_text)
       lang_name = iso639.to_name(lang_code) #full expression
       result_label.configure(text=lang_name)

   text = tk.StringVar() #user-entered text
   entry = tk.Entry(window, textvariable=text, font=('Calibri 15')) #text input field
   entry.place(relx=0.5, rely=0.5, anchor='center')
   button = tk.Button(window, text='Check Language', command=check_language, font=('Calibri 15'))
   button.place(relx=0.5, rely=0.6, anchor='center')
   result_label = tk.Label(window, text='', font=('Calibri 15'))
   result_label.place(relx=0.5, rely=0.7, anchor='center') #results of searching language

   window.mainloop() #keeping the window in a loop and handling user events

detect_lang()