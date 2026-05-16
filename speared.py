#GUI Framework
import customtkinter as ctk
from tkinter import messagebox

#regex module - for better seperating the text, splitting up punctuation attached to words - something .split() can' do
import re

#Translations dictionary
from Translations import translations

#-----------------------Sub-programs--------------------------------------------------------------
    
#convert from modern English to shakespeare style English (create the window & allow user to input text to convert)
def reg2bard():
    app.withdraw()

    translator = ctk.CTkToplevel(app)
    translator.title("Convert Normal English to Shakesperean English")
    translator.geometry("700x700")

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
        convertBtn = ctk.CTkButton(frame, text = "Convert Another?", font = ("Comic Sans Ms", 16, "bold"), command = reg2bard)
        convertBtn.grid(row = 2, column = 0, padx = 5, pady = 10)

    else:
        return

#convert from shakespeare style English to regular/modern English
def bard2reg():
    messagebox.showinfo("Coming Soon...", "Coming soon in a future update")
#-----------------------Main Program--------------------------------------------------------------

#set the appearance mode & theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#create the main window
app = ctk.CTk()
app.title("Shaked'n'Speared")
app.geometry("500x200")

titleLbl = ctk.CTkLabel(app, text = "Shakespeare Text Converter", font = ("Comic Sans Ms", 22))
titleLbl.pack(pady = 10)

bardBtn = ctk.CTkButton(app, text = "Normal English → Bard English", font = ("Comic Sans Ms", 16, "bold"), command = reg2bard)
bardBtn.pack(pady = 10)

regEngBtn = ctk.CTkButton(app, text = "Bard English → Normal English", font = ("Comic Sans Ms", 16, "bold"), command = bard2reg)
regEngBtn.pack(pady = 10)

app.mainloop()