# Importing Packages
import pyautogui as py
import pause


# Defining function
def cvs():
    
    # Tries to recognize an image for 2 seconds
    def loc(pic):
        x = None
        y=1
        while x == None and y < 2:
            pause.seconds(1)
            y=y+1
            x = py.locateCenterOnScreen(pic,confidence=0.95,grayscale=False)
        return(x)
    
    # Looks for image to add to card
    # If item is not on card it adds it
    # If does not see image to add to card, it will scroll down
    # This will repeat until all items are added to card, and the end is reached
    p = loc(r'C:\Users\Personal\Personal Projects\CVS\Bot pics\SendToCard.PNG')
    q = loc(r'C:\Users\Personal\Personal Projects\CVS\Bot pics\End.PNG')
    while q == None:
        p = loc(r'C:\Users\Personal\Personal Projects\CVS\Bot pics\SendToCard.PNG')
        q = loc(r'C:\Users\Personal\Personal Projects\CVS\Bot pics\End.PNG')
        pause.seconds(1)
        py.click(p)
        pause.seconds(1)
        while q == None and p == None:
            pause.seconds(1)
            py.scroll(-300)
            pause.seconds(1)
            p = loc(r'C:\Users\Personal\Personal Projects\CVS\Bot pics\SendToCard.PNG')
            q = loc(r'C:\Users\Personal\Personal Projects\CVS\Bot pics\End.PNG')
    print('Process end')
    
    
# Calling function
cvs()
