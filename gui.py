import tkinter as tk
import random
import string

class Gui:
    #constructor
    def __init__(self,root):
        self.root = root
        self.constructMain()

    #handles construction of main gui
    def constructMain(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.frame.option_add("*Font","Helvetica")

        self.lbl_title = tk.Label(self.frame, text="Password Generator", font=("Helvetica",24))
        self.lbl_title.grid(row=0,columnspan=5)

        self.btn_select_customPassword = tk.Button(self.frame,text="Create\nCustom Password",command=self.customPassword)
        self.btn_select_customPassword.grid(row=1,column=0,padx=5,pady=15)
        self.btn_select_randomPassword = tk.Button(self.frame,text="Create\nRandom Password",command=self.randomPassword)
        self.btn_select_randomPassword.grid(row=1,column=1,padx=5,pady=15)

    #contains logic for random password window
    def randomPassword(self):
        self.addRandomPasswordWindow = tk.Toplevel(self.frame)
        self.addRandomPasswordWindow.title("Create Random")
        self.addRandomPasswordWindow.geometry("300x250")
        self.addRandomPasswordWindow.resizable(False,False)

        self.lbl_rInputType = tk.Label(self.addRandomPasswordWindow,text="How many characters?")
        self.lbl_rInputType.pack(pady=10)
        self.scale_howmanychar = tk.Scale(self.addRandomPasswordWindow,from_=5,to=20,orient="horizontal")
        self.scale_howmanychar.pack()
        self.scale_howmanychar.set(8)
        self.lbl_recommended = tk.Label(self.addRandomPasswordWindow,text="Recommended is 8(eight)")
        self.lbl_recommended.pack()

        self.entry_randomPassword = tk.Entry(self.addRandomPasswordWindow,width=25)
        self.entry_randomPassword.pack()

        self.btn_createRandomPassword = tk.Button(self.addRandomPasswordWindow,text="Create",command=self.createRandomPassword)
        self.btn_createRandomPassword.pack(pady=10)


    #contains logic for custom password window
    def customPassword(self):
        self.addCustomPasswordWindow = tk.Toplevel(self.frame)
        self.addCustomPasswordWindow.title("Create Custom")
        self.addCustomPasswordWindow.geometry("300x250")
        self.addCustomPasswordWindow.resizable(False,False)

        self.lbl_cInputType = tk.Label(self.addCustomPasswordWindow,text="Type a word or symbols in the first box,\n adding hashes(#) to signify\nrandom characters. Then\npress 'Create'")
        self.lbl_cInputType.pack()

        self.entry_customSelection = tk.Entry(self.addCustomPasswordWindow,width=25)
        self.entry_customSelection.pack(pady=10)

        self.entry_customPassword = tk.Entry(self.addCustomPasswordWindow,width=25)
        self.entry_customPassword.pack(pady=10)

        self.btn_createCustomPassword = tk.Button(self.addCustomPasswordWindow,text="Create",command=self.createCustomPassword)
        self.btn_createCustomPassword.pack(pady=10)

    #puts together a random password with a length based on the slider and sends it to gui
    def createRandomPassword(self):
        howmanychar = self.scale_howmanychar.get()
        newpassword = ""

        #calls createRandomChar and appends it to newpassword variable
        for x in range(howmanychar):
            newpassword+=self.createRandomChar()


        #erase old password and add new password to entry box "entry_randompassword"
        self.entry_randomPassword.delete(0,tk.END)
        self.entry_randomPassword.insert(0,newpassword)
        
    #creates a random uppercase, lowercase, number, or symbol and returns it
    def createRandomChar(self):
        upperCase = list(string.ascii_uppercase)
        lowerCase = list(string.ascii_lowercase)
        numbers = ["1","2","3","4","5","6","7","8","9","0"]
        symbols = ['!','@','#','$','%','^','&','*','-','_']

        selection = random.randint(0,3)

        randLetters = random.randint(0,25)
        randNumbersSymbols = random.randint(0,9)

        if selection == 0:
            return upperCase[randLetters]
        elif selection == 1:
            return lowerCase[randLetters]
        elif selection == 2:
            return numbers[randNumbersSymbols]
        elif selection == 3:
            return symbols[randNumbersSymbols]

        return "create random char error"
        
    #puts together a custom password and sends it to gui
    def createCustomPassword(self):
        selection = self.entry_customSelection.get()
        newpassword = ""

        for letter in selection:
            if letter != "#":
                newpassword += letter
            if letter == "#":
                newpassword += self.createRandomChar()

        self.entry_customPassword.delete(0,tk.END)
        self.entry_customPassword.insert(0,newpassword)