from tkinter import *
from typing import Counter


def toArr(string):
    arr = []
    for c in string:
        if c.isalpha():
            arr.append(c)
    return arr

def retFlames(list1, list2):
    arr = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    list1 = list1.lower()
    list2 = list2.lower()

    curDic = {}

    list1 = toArr(list1)
    list2 = toArr(list2)
    visit = set()

    #ini dict curDic with list1 chars
    for c in list1:
        curDic[c] = 1 + curDic.get(c, 0)

    #finding the common ele b/w the names
    for c in list2:
        if c in curDic:
            visit.add(c)
    
    #if common elements found
    if visit:
        visitList = list(visit)

        for c in visitList:
            del curDic[c]
        
        tmp = []
        for c in list2:
            if c not in visit:
                tmp.append(c)
        list2 = tmp


    #finalizing dict
    for c in list2:
        curDic[c] = 1 + curDic.get(c, 0)
    

    #number for calculating flames
    count = 0

    for i in curDic.values():
        count += i
    
    count %= 6
    return arr[count - 1]

def tell_status() :
    # take a 1st player name from Player1_field entry box 
    p1 = Player1_field.get()

    # take a 2nd player name from Player2_field entry box
    p2 = Player2_field.get()

    Status_field.insert(10, retFlames(p1, p2))


def clear_all() : 
    Player1_field.delete(0, END)  
    Player2_field.delete(0, END)
    Status_field.delete(0, END)
   
    # set focus on the Player1_field entry box 
    Player1_field.focus_set() 
 
 
if __name__ == "__main__" :
   
    root = Tk()
   
    root.configure(background = "#0c4a60")
   
    root.geometry("360x200")
   
    # set the name of tkinter GUI window
    root.title("Flames Game") 
       
    #labels   
    label1 = Label(root, text = "Player 1 Name: ",
                   fg = '#759cb7', bg = '#136581')
   
    label2 = Label(root, text = "Player 2 Name: ",
                   fg = '#759cb7', bg = '#136581')
       
    label3 = Label(root, text = "Relationship Status: ",
                   fg = '#a3bdcf', bg = '#195a87')

    blanklabel = Label(root, text="",
                        bg="#0c4a60")
    
    blanklabel1 = Label(root, text="",
                        bg="#0c4a60")
    
    blanklabel2 = Label(root, text="",
                        bg="#0c4a60")
 
    #placing labels with padding
    label1.grid(row = 1, column = 0, sticky ="E") 
    label2.grid(row = 2, column = 0, sticky ="E") 
    label3.grid(row = 6, column = 0, sticky ="E")
    blanklabel1.grid(row = 3, column = 0)
    blanklabel.grid(row = 5, column = 0)
 
    #input
    Player1_field = Entry(root) 
    Player2_field = Entry(root) 
    Status_field = Entry(root)
  
    Player1_field.grid(row = 1, column = 1, ipadx ="50") 
    Player2_field.grid(row = 2, column = 1, ipadx ="50") 
    Status_field.grid(row = 6, column = 1, ipadx ="50") 
 
    #submit button 
    button1 = Button(root, text = "Submit", bg = "#148c7a", 
                     fg = "#8cadc3", command = tell_status)
   
    #clear button 
    button2 = Button(root, text = "Clear", bg = "#071b28", 
                     fg = "#759cb7", command = clear_all)
 
    #buttons with padding . 
    button1.grid(row = 4, column = 1)
    blanklabel2.grid(row = 7)
    button2.grid(row = 8, column = 1)
  
    root.mainloop()
