#matrix terminal python app

import curses #module used for terminal cursor handling
import random #module to generat random values

def matrix(window):
    curses.start_color() #allow for color manipulation routines
    curses.use_default_colors() #use the terminals default colors
    curses.curs_set(0)
    window.clear() #clear the terminal
    window.refresh() #refresh the terminal

    height, width = window.getmaxyx() #get the hieght and width of the terminal

    characters = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{};:,<>./?   " #list of characters to use (extra space chars to be chosen more frequently)

    #perform action until interupt (CNTR + C)
    while(True):
        for row in reversed(range(height-1)): #iterate through the matrix in reverse to shift items down the terminal
            for column in reversed(range(width)):
                if row == 0: #when we are at the top of the terminal
                    string = window.instr(row+1,column,1) #collect the item below the cursor
                    window.addstr(0,width-1," ") #append a comparison byte string to the terminal
                    comparison = window.instr(0,width-1,1) #collect the comparison byte string
                    window.move(row,column) #reset the cursor to the current row,column
                    if string == comparison: #check to see if we have a " " below where we are more likely to append another
                        if random.randint(0,15) == 0: #if " " was found, unlikely chance we would get soemthing other than " "
                            window.addstr(row,column,random.choice(characters)) #append a new random char
                        else:
                            window.addstr(row,column,string) #append another " "
                    else:
                        window.addstr(row,column,random.choice(characters)) #if " " is not found, append a new random character
                else: #when we are not at the top of the terminal
                    string = window.instr(row-1,column,1) #collect the item to shift down
                    window.move(row,column) #reset the cursor to the current row,column
                    window.addstr(row,column,string) #shift the item down

        curses.napms(50) #wait for visual appeal
        window.refresh() #refresh the termianl to update display



#main function to call matrix method using curses wrapper for clean up
def main():
    curses.wrapper(matrix) #call to main function with curses wrapper for clean handling

if __name__ == '__main__':
    main() #run main
