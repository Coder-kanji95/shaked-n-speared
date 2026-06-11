#GUI Framework
import customtkinter as ctk
from tkinter import messagebox

#regex module - for better seperating the text, splitting up punctuation attached to words - something .split() can' do
import re

#file paths
import os
import sys

#Translations dictionary
from Translations import translations

#-----------------------Sub-programs--------------------------------------------------------------
    
#convert from modern English to shakespeare style English (create the window & allow user to input text to convert)
def reg2bard(icon):
    app.withdraw()

    translator = ctk.CTkToplevel(app)
    translator.title("Convert Normal English to Shakesperean English")
    translator.geometry("700x700")

    translator.iconbitmap(icon)

    frame = ctk.CTkFrame(translator)
    frame.pack(expand = True)

    inputLbl = ctk.CTkLabel(frame, text = "Enter your text to convert:", font = ("Comic Sans Ms", 14))
    inputLbl.grid(row = 0, column = 0, padx = 5, pady = 10)

    #use Textbox instead of Entry so input text gets wrapped
    inputEntry = ctk.CTkTextbox(frame, font = ("Comic Sans Ms", 14), width = 500, height = 250)
    inputEntry.grid(row = 1, column = 0, padx = 5, pady = 10)

    #insert placeholder text seperately cuz Textbox doesnt have it built-in
    inputEntry.insert("1.0", "Your text goes here...")

    submitBtn = ctk.CTkButton(frame, text = "Convert!", font = ("Comic Sans Ms", 16, "bold"), command = lambda: convert2bard(inputEntry.get("1.0", "end").strip(), frame, translator))
    submitBtn.grid(row = 2, column = 0, padx = 5, pady = 10)

#actual process of converting the text into shakespeare style
def convert2bard(text, frame, window):
    #validate the input
    if len(text) >= 2 and len(text) <= 500:
        valid = True
    else:
        messagebox.showerror("Input error", "Make sure your text is between 2 & 500 characters")
        valid = False
    
    if valid == True:
        #translating...
        words = re.findall(r"\w+|[^\w\s]", text.lower())

        newWords = []
        for word in words:
            if word in translations:
                newWords.append(translations[word])
            else:
                newWords.append(word)
        
        result = " ".join(newWords)
        
        #resize window
        window.geometry("700x500")

        #clear the input label & text entry widgets
        for widget in frame.winfo_children():
            widget.grid_forget()
        
        #rebuild the frame with output labels
        outputLbl = ctk.CTkLabel(frame, text = "Shaked & Speared Text -", font = ("Comic Sans Ms", 14))
        outputLbl.grid(row = 0, column = 0, padx = 5, pady = 10)

        outputBox = ctk.CTkTextbox(frame, font = ("Comic Sans Ms", 14), width = 500, height = 250, wrap = "word")
        outputBox.grid(row = 1, column = 0, padx = 5, pady = 10)

        outputBox.insert("1.0", result)
        outputBox.configure(state = "disabled")

        #button to convert more text
        convertBtn = ctk.CTkButton(frame, text = "Convert Another?", font = ("Comic Sans Ms", 16, "bold"), command = reg2bard(iconPath))
        convertBtn.grid(row = 2, column = 0, padx = 5, pady = 10)

    else:
        return

#convert from shakespeare style English to regular/modern English
def bard2reg(icon):
    messagebox.showinfo("Coming Soon...", "Coming soon in a future update")

def getFilePaths(icon):
    try:
        basePath = sys._MEIPASS #if all the code is bundled into an executable
    except Exception:
        basePath = os.path.abspath(".") #gives the folder where the main file is - which is main folder btw
    
    return os.path.join(basePath, icon)
#-----------------------Main Program--------------------------------------------------------------
iconPath = getFilePaths(os.path.join("shakednspeared.ico"))

#set the appearance mode & theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#create the main window
app = ctk.CTk()
app.title("Shaked'n'Speared")
app.geometry("500x200")

print(iconPath)
print(os.path.exists(iconPath))

app.iconbitmap(iconPath)

titleLbl = ctk.CTkLabel(app, text = "Shakespeare Text Converter", font = ("Comic Sans Ms", 22))
titleLbl.pack(pady = 10)

bardBtn = ctk.CTkButton(app, text = "Normal English → Bard English", font = ("Comic Sans Ms", 16, "bold"), command = lambda: reg2bard(iconPath))
bardBtn.pack(pady = 10)

regEngBtn = ctk.CTkButton(app, text = "Bard English → Normal English", font = ("Comic Sans Ms", 16, "bold"), command = lambda: bard2reg(iconPath))
regEngBtn.pack(pady = 10)

app.mainloop()