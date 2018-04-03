import accumulator
import memory
import gui
from tkinter import *

def main():
    #Pop up the gui
    root = Tk()
    my_gui = gui.guiTime(root)

    #Grab user entries
    user_entries = my_gui.grabInstructions()
    user_input = my_gui.grabInput()

    root.mainloop()
    
    sim = uvsim()
    
    #Pass user entries to uvsim
    sim.get_input(user_entries)

    #Pass user input for read function to simulation
    sim.run_simulation(user_input)

class uvsim:
    global accumulator, memory, instructionCounter, entryCount
    def __init__(self):
        self.accumulator = accumulator.accumulator()
        self.memory = memory.memory()
        self.entryCount = 0
        self.instructionCounter = 0
        self.inputCounter = 0
        
    # written by James Morris
    def get_input(self, user_entries):
        # this is where we will get the input from the user
        print("Welcome to UVSim!\n"
              "Please enter your program one instruction\n"
              "(or data word) at a time into the input\n"
              "text field. I will display the location. Enter\n"
              "-99999 to stop entering your program.\n")

        entries = user_entries # Sample data: [(0, '+1007'), (1, '+1008'), (2, '+2007'), (3, '+3008'), (4, '+2109'), (5, '+1109'), (6, '+4300'), (7, '+0000'), (8, '+0000'), (9, '+0000'), (10, '-99999')]
        self.entryCount = len(entries)

        for entry in entries:
            self.inputToken = entry[1]
            if self.inputToken[0] in ("+", "-"):
                opCode = self.inputToken[1:5]
                try:
                    int(opCode)
                    self.memory[entry[0]] = self.inputToken  # I think it maybe should be stored in memory as a string so it's easier to parse...
                    # ...out the opcodes during the program execution (if entryCount is a negative number, str(memory[xx]) results in '-0123' (length of 5) while
                    # ...if it's positive, str(memory[xx]) results in '0123' (length of 4) )
                    self.entryCount += 1
                except ValueError:
                    print("Invalid opcode!")
            if self.entryCount == 99:
                break

        print("Program loading completed")
        print("Beginning program execution...")

        return

    # written by Tasi Cluff
    def add(self, address):
        rho = int(self.memory[address])
        self.accumulator += rho
    
    # written by Tasi Cluff
    def subtract(self, address):
        rho = int(self.memory[address])
        self.accumulator -= rho

    # written by Tasi Cluff
    def store(self, address):
        global accumulator, instructionCounter, memory
        self.memory[address] = self.accumulator

    def halt(self):
        print("****** SIMULATION EXECUTION TERMINATED ******")
        self.memdump()
        exit()

    #written by Carter Davis
    def divide(self, address):
        rho = int(self.memory[address])
        self.accumulator /= rho
        int(self.accumulator)

    #written by Carter Davis
    def multiply(self, address):
        rho = int(self.memory[address])
        self.accumulator *= rho
        int(self.accumulator)

    #written by Carter Davis
    def memdump(self):
        print(str(self.memory))

    def read(self, address, user_input):
        getInput = user_input[self.inputCounter]
        if getInput > 5:
            print("Invalid input. Try again!")
        else:
            self.memory[address] = getInput
            self.inputCounter += 1
        # getInput = input("Enter an integer: ")
        # if len(getInput) > 5:
        #     print("Invalid input. Try again!")
        # else:
        #     self.memory[address] = getInput
    
    # written by James Morris
    def write(self, address):
        # store(address)
        print("The value stored at address  ", address, ": ", self.memory[address])

    # written by James Morris
    def load(self, address):
        self.accumulator = int(self.memory[address])
    
    #written by Jared Leishman
    def branch(self, address):
        if self.accumulator > 0:
            self.instructionCounter = address - 1
            
    #written by Jared Leishman
    def branchNeg(self, address):
        if self.accumulator < 0:
            self.instructionCounter = address - 1

    #written by Jared Leishman
    def branchZero(self, address):
        if self.accumulator == 0:
            self.instructionCounter = address - 1
    
    # written by James Morris
    def run_simulation(self, user_input):
        while self.instructionCounter <= self.entryCount:  # changed the expression to not be infinite
            # TODO: Handle instructions here
            self.currentInstruction = str(self.memory[self.instructionCounter])  # currentInstruction needs to be of type string for the next line of code to work

            # print('curr instr = ', self.currentInstruction)
            currentOpcode = int(self.currentInstruction[1:3])  # changed currentOpcode's type to int
            # print('curr opcode = ', currentOpcode)
            currentAddress = int(self.currentInstruction[3:5])  # parses out the address (operand) part of the instruction
            # print('curr address = ', currentAddress)
            # if currentOpcode == 10:         # Read
            #    print('instruction counter = ', instructionCounter) # helps with debugging branch
            #    print('accumulator = ', accumulator)                # helps with debugging branch
            #    print('\n------------------------------\n')

            if currentOpcode == 10:  # Read
                self.read(currentAddress, user_input)
            elif currentOpcode == 11:  # Write
                self.write(currentAddress)
            elif currentOpcode == 20:  # Load
                self.load(currentAddress)
            elif currentOpcode == 30:  # Add
                self.add(currentAddress)
            elif currentOpcode == 31:  # Subtract
                self.subtract(currentAddress)
            elif currentOpcode == 21:  # Store
                self.store(currentAddress)
            elif currentOpcode == 43:  # Halt
                self.halt()
            elif currentOpcode == 32:  # Divide
                self.divide(currentAddress)
            elif currentOpcode == 33:  # Multiply
                self.multiply(currentAddress)
            elif currentOpcode == 00:  # Memdump
                self.memdump()
            elif currentOpcode == 40:  # Branch
                self.branch(currentAddress)
            elif currentOpcode == 41:  # BranchNeg
                self.branchNeg(currentAddress)
            elif currentOpcode == 42:  # BranchZero
                self.branchZero(currentAddress)

            self.instructionCounter += 1  # We'll probably want to increment the instruction counter after all the work is done
        return

# call main function (good python practice)
if __name__ == "__main__":
    main()
