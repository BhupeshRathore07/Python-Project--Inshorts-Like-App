import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

class newsApp:

    def __init__(self):
        #fetch Data
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=970cd3f766ee4ec796e563e8cf89993f").json()

        # initialise GUI load
        self.load_gui()

        # load 1st news item
        self.loadNewsItem(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.title('Inshorts Copy')
        self.root.configure(background = "white")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def loadNewsItem(self,index):

        #clear screen for new news item
        self.clear()

        #image
        try:
            imgUrl = self.data['articles'][index]['urlToImage']
            rawImg = urlopen(imgUrl).read()
            img = Image.open(io.BytesIO(rawImg)).resize((340,260))
            photo = ImageTk.PhotoImage(img)

        except:
            imgUrl = 'http://i.gyazo.com/059b6cd618ca6e81a1167f89cb825f40.png'
            rawImg = urlopen(imgUrl).read()
            img = Image.open(io.BytesIO(rawImg)).resize((340, 260))
            photo = ImageTk.PhotoImage(img)

        label = Label(self.root, image = photo)
        label.pack()


        # Displaying Content
        #Heading
        heading = Label(self.root, text = self.data['articles'][index]['title'], bg = 'white',
                        fg = 'black', wraplength=350, justify= 'center')
        heading.pack(pady=(10,20))
        heading.config(font=('cambria', 15))

        #Details
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='white',
                        fg='black', wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('calibri', 12))

        #frame for Butons
        frame = Frame(self.root, bg = "white")
        frame.pack(side=BOTTOM, expand= True, fill = BOTH)

        # Previous Buttton
        if index != 0:
            prev = Button(frame, text = "Prev", width=16, height=3,
                          command= lambda :self.loadNewsItem(index-1))
            prev.pack(side=LEFT)

        # Read More Buttton
        read = Button(frame, text="Read More", width=16, height=3,
                      command= lambda :self.openLink(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        # Next Buttton
        if index != len(self.data['articles']) - 1:
            next = Button(frame, text="Next", width=16, height=3,
                          command= lambda :self.loadNewsItem(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def openLink(self, url):
        webbrowser.open(url)

#Object
obj = newsApp()
