import socket
import threading

import tkinter as tk
from tkinter import font
from tkinter import ttk



PORT = 5001 # why not 5000?
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDRESS)

class GUI:
    def __init__(self):
        self.Window = tk.Tk()
        self.Window.withdraw()
        
        self.login = tk.Toplevel()
        self.login.title("LOGIN")

        self.login.resizable(width = False, height = False)
        self.login.configure(width = 400, height = 300)
        
        self.welcome = tk.Label(self.login,
                                text = "Press login to continue",
                                justify = tk.CENTER,
                                font = "Helvetica 14 bold")
        
        self.go = tk.Button(self.login,
                            text = "login",
                            font = "Helvetica 14 bold",
                            #command = lambda: self.goAhead(self.entryName.get()))
                            command = lambda: self.goAhead("test"))
        
        self.go.place(relx = 0.4,
                      rely = 0.55)
        
        self.Window.mainloop()
        
        
    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)
        
        rcv = threading.Thread(target = self.receive)
        rcv.start()
        
        
    def layout(self, name):
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("GOBLIN BOT 3.0")
        self.Window.resizable(width = False,
                              height = False)
        self.Window.configure(width = 680,
                              height = 550)#,
                              #bg = "#17202A")
        # self.labelHead = tk.Label(self.Window,
        #                      bg = "#17202A", 
        #                       fg = "#EAECEE",
        #                       text = self.name ,
        #                        font = "Helvetica 13 bold",
        #                        pady = 5)
          
        # self.labelHead.place(relwidth = 1)
        # self.line = tk.Label(self.Window,
        #                   width = 450,
        #                   bg = "#ABB2B9")
          
        # self.line.place(relwidth = 1,
        #                 rely = 0.07,
        #                 relheight = 0.012)
          
        # self.textCons = tk.Text(self.Window,
        #                      width = 20, 
        #                      height = 2,
        #                      bg = "#17202A",
        #                      fg = "#EAECEE",
        #                      font = "Helvetica 14", 
        #                      padx = 5,
        #                      pady = 5)
          
        # self.textCons.place(relheight = 0.745,
        #                     relwidth = 1, 
        #                     rely = 0.08)
        
        self.button_flip = tk.Button(self.Window, text="flip")
        self.button_flip.pack()
        
        self.button_d4 = tk.Button(self.Window, text="d4")
        self.button_d4.pack()
        
        self.button_d6 = tk.Button(self.Window, text="d6")
        self.button_d6.pack()
        
        self.button_d8 = tk.Button(self.Window, text="d8")
        self.button_d8.pack()
        
        self.button_d10 = tk.Button(self.Window, text="d10")
        self.button_d10.pack()
        
        self.button_d12 = tk.Button(self.Window, text="d12")
        self.button_d12.pack()
        
        self.button_d20 = tk.Button(self.Window, text="d20")
        self.button_d20.pack()
        
        self.button_d20 = tk.Button(self.Window, text="d100")
        self.button_d20.pack()
        
        
        self.labelBottom = tk.Label(self.Window,
                                 bg = "#ABB2B9",
                                 height = 80)
          
        #self.labelBottom.place(relwidth = 1,
        #                       rely = 0.95)
        self.labelBottom.pack()
          
        self.entryMsg = tk.Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
          
        # place the given widget
        # into the gui window
        # self.entryMsg.place(relwidth = 0.74,
        #                     relheight = 0.06,
        #                     rely = 0.008,
        #                     relx = 0.011)
		
        self.entryMsg.pack()
          
        self.entryMsg.focus()
          
        # create a Send Button
        self.buttonMsg = tk.Button(self.labelBottom,
                                text = "Send",
                                font = "Helvetica 10 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
          
        # self.buttonMsg.place(relx = 0.77,
        #                      rely = 0.008,
        #                      relheight = 0.06, 
        #                      relwidth = 0.22)
        self.buttonMsg.pack()
        
          
        # self.textCons.config(cursor = "arrow")
          
        # # create a scroll bar
        # scrollbar = tk.Scrollbar(self.textCons)
          
        # # place the scroll bar 
        # # into the gui window
        # scrollbar.place(relheight = 1,
        #                 relx = 0.974)
          
        # scrollbar.config(command = self.textCons.yview)
          
        # self.textCons.config(state = tk.DISABLED)
        
        
    def sendButton(self, msg):
        #self.textCons.config(state = tk.DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, tk.END)
        snd = threading.Thread(target = self.sendMessage)
        snd.start()
    
    
    # function to receive messages
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                  
                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    # insert messages to text box
                    #self.textCons.config(state = NORMAL)
                    #self.textCons.insert(END,
                    #                    message+"\n\n")
                    pass
                    #self.textCons.config(state = DISABLED)
                    #self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client.close()
                break 
    
    # function to send messages 
    def sendMessage(self):
        #self.textCons.config(state=tk.DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))    
            break
        
    def formatDiceString(self, dice):
        #flip doesn't quite work yet
        pass
                
g = GUI()
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        