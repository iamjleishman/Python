from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class guiTime:

    def __init__(self, master):
        self.counter = 0
        self.all_instructions = []
        self.refined = []
        self.user_integers = []
        self.master = master

        master.title("UVSIM")

        self.label = Label(master, text="Welcome to UVSim")
        self.label.pack()

        self.exeButton = Button(master, text="Execute", command=self.refineEntries)
        self.exeButton.pack()

        self.addboxButton = Button(master, text="Add Instruction", fg="Blue", command=self.addBox)
        self.addboxButton.pack()

        self.addBox()

    def addBox(self):
        '''Adds new program counter text box and user entry'''

        frame = Frame(self.master)
        frame.pack()

        # Initialize Program Counter label
        if self.counter == 0:
            Label(frame, text="Program Counter").grid(row=0, column=0, sticky=W)

        # Create new text box that holds current program counter position
        t = Text(frame, height=1, width=10)
        t.grid(row=1, column=0, sticky=W, padx=4)

        # Format counter with leading zero if less than 10
        if self.counter < 10:
            temp = "0" + str(self.counter)
            t.insert(0.0, temp)
        else:
            t.insert(0.0, self.counter)
        t["state"] = DISABLED

        # Initialize Instruction label
        if self.counter == 0:
            Label(frame, text="Instruction").grid(row=0, column=1)

        # Increment Counter 
        self.counter += 1

        # Add new Instruction Entry
        ent1 = Entry(frame)
        ent1.grid(row=1, column=1)

        self.all_instructions.append(ent1)

    def refineEntries(self):
        '''Passes entries to main.py'''

        for number, ent1 in enumerate(self.all_instructions):
            if ent1.get() != '':
                instruct = ent1.get()
                self.refined.append((number, instruct))
                if instruct[1:3] == '10':  # Check for any Read opcodes
                    message = simpledialog.askinteger("Read", "Enter an integer",
                                        parent=self.master,
                                        minvalue=0, maxvalue=100)
                    self.user_integers.append(message)

            else:
                messagebox.showerror("Error", "Missing an instruction?")
                return
        # print([x for x in self.refined])
        self.master.destroy()

    def grabInstructions(self):
        return self.refined

    def grabInput(self):
        return self.user_integers

# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()