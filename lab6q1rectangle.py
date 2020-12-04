from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='white',height=250,width=300)
canvas.create_rectangle(10,10,200,150,fill='blue',outline='black')
canvas.create_text(100,100,text='Au Tsz Yui')
canvas.create_line(70,110,150,110)
canvas.pack()
frame.mainloop()

