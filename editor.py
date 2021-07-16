from tkinter import *

root=Tk()
root.title("myeditor")
root.iconbitmap("")
root.geometry("1200x660")
myframe = Frame(root)
myframe.pack(pady= 5)

textscroll= Scrollbar(myframe)

textscroll.pack(side= RIGHT,fill=Y)

mytext = Text(myframe,width= 99,height= 30,font=("Lucida Calligraphy", 16),selectbackground="BLUE", selectforeground="white", undo= True, yscrollcommand= textscroll.set)
mytext.pack()
textscroll.config(command=mytext.yview)
# file menu
my_menu =Menu(root)
root.config(menu=my_menu)
# add file menu
file_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu,)
file_menu.add_command(label= "New")
file_menu.add_command(label= "open")
file_menu.add_command(label= "Save")
file_menu.add_command(label= "Save As")
file_menu.add_separator()
file_menu.add_command(label ="Exit", command=root.quit)
# edit menu

Edit_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit", menu=Edit_menu)
Edit_menu.add_command(label= "Cut")
Edit_menu.add_command(label= "Copy")
Edit_menu.add_command(label= "Undo")
Edit_menu.add_command(label ="Redo")

# staus bar
status_bar = Label(root,text= 'Ready  ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=6)
#


root.mainloop()