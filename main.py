#by Mathéo Lambay
import tkinter as tk
from tkinter import ttk
import json

with open('data.json', 'r') as f:
    data = json.load(f)


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("table thermodynamique")
        # self.geometry("1400x800")

        self.win = tk.Canvas(self)

        self.entryTable = tk.Entry(self.win)
        self.entryTable.bind("<Button-1>", lambda event:self.listTable('nom'))
        self.entryTable.pack()
        
        self.entryElement = tk.Entry(self.win)
        self.entryElement.bind("<Button-1>", lambda event:self.listTable('element'))
        self.entryElement.pack()
        
        self.win.pack()

        self.buttonSend = tk.Button(self.win,text="Chercher",command=self.researchData)
        self.buttonSend.pack()

    def on_click(self,name):
        
        curItem = self.table.item(self.table.focus())
        
        if name == 'Table':
            self.entryTable.delete(0,"end")
            self.entryTable.insert(0,curItem['values'])
        else:
            self.entryElement.delete(0,"end")
            self.entryElement.insert(0,curItem['values'])
        
    def listTable(self,table):
        try:
            self.table.destroy()
        except:
            pass
        if table == 'nom':
            name = "Table"
            result = data
        else:
            tablename = self.entryTable.get()
            name = "Element"
            result = data[tablename][0]
        
        self.table = ttk.Treeview(self,columns="#1",show='headings')
        self.table.bind("<ButtonRelease-1>", lambda event: self.on_click(name))
        self.table.pack()

        self.table.heading('#1',text=name)
        self.table.column('#1',width=320)

        for i in result:
           self.table.insert("",'end',values=i)

    def researchData(self):

        try:
            self.table.destroy()
        except:
            pass

        tab = []
        tablename = self.entryTable.get()
        elementname = self.entryElement.get()
        
        result = data[tablename][0][elementname][0]
        
        self.table = ttk.Treeview(self,columns=(),show='headings', selectmode="browse")
        self.table.pack()

        for i in range(len(result)):
            tab.append("#%i"%(i+1)) #le i+1 permet de d'éviter un décallage des données du tableaux par rapport au collonne à cause d'une colonne id ajouté de base par tkinter
        self.table.config(columns=tab)
        
        
        tabdata=[]
        tab=[]
        
        for i,j in enumerate(result): 
            
            self.table.heading('#%i'%(i+1),text=j)#idem i+1
            
            tabdata.append(result[j])

        x=0
        for i in tabdata:
           if len(i) > x:
               x = len(i)
               
        for i in range(x):
            
            for j in range(len(tabdata)):
                try:
                    tab.append(tabdata[j][i])
                except:
                    tab.append('')
                           
            self.table.insert("",'end',values=(tab))
            tab = []
            
                
app = Application()
app.mainloop()


