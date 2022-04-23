import qrcode
from tkinter import simpledialog
from tkinter import messagebox
import sys
import os.path

def inputtext():
    outputstr = simpledialog.askstring("QR CODE","Enter a text:")

    if outputstr is not None:
        if len(outputstr) > 0:
            img = qrcode.make(outputstr)
            img.save("QR_code.png")
            print("DONE!")
            messagebox.showinfo("SUCCESS", "QR code was successfully created.")
        else:
            messagebox.showerror("ERROR!","Input text is empty!")
            inputtext()
    else:
        sys.exit()  

def main():
    try:
        png_exists = os.path.exists('QR_code.png')
        if png_exists == True: #checking old QR code image file exists
            
            result = messagebox.askquestion("WARNING!", "An old QR code was found. Do you want to replace it?", icon='warning')
            if result == 'yes':

                inputtext()         
        else:
            inputtext()
    except Exception as e:
        messagebox.showerror("ERROR!",e)
        sys.exit()        
if __name__ == '__main__':
    main()
 


