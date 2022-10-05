import markdownify
import os
from tkinter import Tk, END, Frame, SUNKEN, X, Text, BOTH
from tkinter import font, filedialog, Label, Button
from PIL import ImageTk, Image
import platform

cwd = os.path.dirname(os.path.realpath(__file__))
systemName = platform.system()


class AlHtmlToMarkdown():

    def __init__(self):
        root = Tk(className=" ALHTMLTOMARKDOWN ")
        root.geometry("400x200+1500+815")
        root.resizable(0, 0)
        iconPath = os.path.join(cwd+'\\UI\\icons',
                                'alhtmltomarkdown.ico')
        if systemName == 'Darwin':
            iconPath = iconPath.replace('\\','/')
        root.iconbitmap(iconPath)
        root.config(bg="#6a199b")
        root.overrideredirect(1)
        color = '#6a199b'

        def liftWindow():
            root.lift()
            root.after(1000, liftWindow)

        def callback(event):
            root.geometry("400x175+1500+840")

        def showScreen(event):
            root.deiconify()
            root.overrideredirect(1)

        def screenAppear(event):
            root.overrideredirect(1)

        def hideScreen():
            root.overrideredirect(0)
            root.iconify()

        def openHtml():
            fileTextEntry.delete(1.0, END)
            filename = filedialog.askopenfilename(filetypes=[('HTML Files',
                                                              '*.html')])
            fileTextEntry.insert(1.0, filename)

        def markdown():
            filepath = fileTextEntry.get("1.0", END)
            filepath = filepath.replace('/', '\\')[:-1]
            if systemName == 'Darwin':
                filepath = filepath.replace('\\','/')
            if os.path.exists(filepath):
                extension = os.path.splitext(filepath)[1]
                try:
                    if extension.lower() == ".html":
                        htmlFile = open(filepath, "r")
                        html = htmlFile.read()
                        htmlFile.close()
                        markDown = markdownify.markdownify(html,
                                                           heading_style="ATX")
                        markdownFileName = os.path.basename(filepath)
                        markdownFileName = markdownFileName.replace(extension,
                                                                    '.md')
                        markdownFilePath = os.path.join(cwd+'\\AlHtmlTo'
                                                        'Markdown\\Markdown',
                                                        markdownFileName)
                        if systemName == 'Darwin':
                            markdownFilePath = markdownFilePath.replace('\\',
                                                                        '/')
                        markdownFile = open(markdownFilePath, "w")
                        markdownFile.writelines(markDown)
                        markdownFile.close()
                        text.delete(1.0, END)
                        text.insert(1.0, markdownFileName + ' has been saved' +
                                    ' successfully in Markdown folder')
                except Exception as e:
                    text.delete(1.0, END)
                    print(str(e))
                    text.insert(1.0, 'Invalid document, please provide .html' +
                                ' extension files')
            else:
                text.delete(1.0, END)
                text.insert(1.0, 'Invalid file path')

        textHighlightFont = font.Font(family='OnePlus Sans Display', size=12)
        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12,
                                     weight='bold')

        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(iconPath)
        icon = icon.resize((30, 30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0, column=0, sticky="nsew")
        titleLabel = Label(titleBar, text='ALHTMLTOMARKDOWN', fg='#909090',
                           bg='#141414', font=appHighlightFont)
        titleLabel.grid(row=0, column=1, sticky="nsew")
        closeButton = Button(titleBar, text="x", bg='#141414', fg="#909090",
                             borderwidth=0, command=root.destroy,
                             font=appHighlightFont)
        closeButton.grid(row=0, column=3, sticky="nsew")
        minimizeButton = Button(titleBar, text="-", bg='#141414', fg="#909090",
                                borderwidth=0, command=hideScreen,
                                font=appHighlightFont)
        minimizeButton.grid(row=0, column=2, sticky="nsew")
        titleBar.grid_columnconfigure(0, weight=1)
        titleBar.grid_columnconfigure(1, weight=30)
        titleBar.grid_columnconfigure(2, weight=1)
        titleBar.grid_columnconfigure(3, weight=1)
        titleBar.pack(fill=X)

        fileText = Button(root, text="HTML FILE", borderwidth=0,
                          highlightthickness=3, command=openHtml)
        fileText.pack(fill=X)
        fileText.config(bg=color, fg="white", font=appHighlightFont)
        fileTextEntry = Text(root, bg="white", fg='#7a1da3',
                             highlightbackground=color, highlightcolor=color,
                             highlightthickness=3, bd=0,
                             font=textHighlightFont, height=1)
        fileTextEntry.pack(fill=BOTH, expand=True)

        convertToMarkdown = Button(root, borderwidth=0, highlightthickness=3,
                                   text="MARKDOWN", command=markdown)
        convertToMarkdown.config(bg=color, fg="white", font=appHighlightFont)
        convertToMarkdown.pack(fill=X)

        text = Text(root, font="sans-serif",  relief=SUNKEN,
                    highlightbackground=color, highlightcolor=color,
                    highlightthickness=5, bd=0)
        text.config(bg="white", fg='#7a1da3', height=2, font=textHighlightFont)
        text.pack(fill=BOTH, expand=True)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        if systemName == 'Windows':
            liftWindow()
        root.mainloop()


if __name__ == "__main__":
    AlHtmlToMarkdown()
