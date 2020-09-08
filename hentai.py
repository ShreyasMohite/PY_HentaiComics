from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from PIL import ImageTk
from PIL import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests,re     
import os
import random



class hentai:
     def __init__(self,root):
          self.root=root
          self.root.title("HENTAIBOY ;)")
          self.root.geometry("500x300")
          self.root.resizable(0,0)
          self.root.iconbitmap("com.ico")

          sites=StringVar()
          comb=StringVar()




#==================================functions=====================================================
          def on_enter1(e):
            But_down['background']="black"
            But_down['foreground']="cyan"
  
          def on_leave1(e):
                 But_down['background']="SystemButtonFace"
                 But_down['foreground']="SystemButtonText"

          def on_enter2(e):
                 But_clear['background']="black"
                 But_clear['foreground']="cyan"
       
          def on_leave2(e):
                 But_clear['background']="SystemButtonFace"
                 But_clear['foreground']="SystemButtonText"



          def clear():
               sites.set("")



          
          def getsite():
           self.root.update()
           sitename=comb.get()
           entres=sites.get()
           if sitename=="select" and entres=="":
               tkinter.messagebox.askretrycancel("Info","please select the site name first / And write the site url",icon="info")

           elif not entres:
                tkinter.messagebox.askretrycancel("Info","please select the correct site name and url",icon="info")
                

           elif sitename=="select" or entres=="":
               tkinter.messagebox.askretrycancel("Info","please select the site name first / And write the site url",icon="info")
           elif sitename=="select":
               tkinter.messagebox.askretrycancel("Info","please select the site name first",icon="info")

           elif sitename=="ilikecomix.com":
               try:
                    parent="C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Hentaiboy"
                    num=random.randint(1,100)
                    dirs="ilikecomix{}".format(num)
                    path=os.path.join(parent,dirs)
                    os.mkdir(path)

                    site=sites.get()
                    response=requests.get(site)

                    Soup=BeautifulSoup(response.text,"html.parser")
                    gather=Soup.findAll("a")
                    urls=[images["href"] for images in gather]
                    for url in urls:
                        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
                        if not filename:
                             Lab.config(text="Regex didn't match with the url: {}".format(url))
                             continue
                        with open(path+"\\"+filename.group(1), 'wb') as f:
                            if 'http' not in url:
                                # sometimes an image source can be relative 
                                # if it is provide the base url which also happens 
                                # to be the site variable atm. 
                                url = '{}{}'.format(site, url)
                                
                            response = requests.get(url)
                            
                            f.write(response.content)

               except:
                     tkinter.messagebox.askretrycancel("Info","please check the url / Network error",icon="info")

           elif sitename=="porncomics.one":
               try:
                    parent="C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Hentaiboy"
                    num=random.randint(1,100)
                    dirs="porncomics.one{}".format(num)
                    path=os.path.join(parent,dirs)
                    os.mkdir(path)

                    site=sites.get()
                    response=requests.get(site)

                    Soup=BeautifulSoup(response.text,"html.parser")
                    gather=Soup.findAll("a")
                    urls=[images["href"] for images in gather]
                    for url in urls:
                        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
                        if not filename:
                             Lab.config(text="Regex didn't match with the url: {}".format(url))
                             continue
                        with open(path+"\\"+filename.group(1), 'wb') as f:
                            if 'http' not in url:
                                # sometimes an image source can be relative 
                                # if it is provide the base url which also happens 
                                # to be the site variable atm. 
                                url = '{}{}'.format(site, url)
                                
                            response = requests.get(url)                     
                            f.write(response.content)

               except:
                     tkinter.messagebox.askretrycancel("Info","please check the url / Network error",icon="info")
                                      
           else:
                tkinter.messagebox.askretrycancel("Info","please check the url or internal error",icon="info")
               
        

#=================================  FRAME====================================#
         
          MainFrame=Frame(self.root,width=500,height=300,relief="sunken",bd=3)
          MainFrame.place(x=0,y=0)


          self.original1 = Image.open ("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Hentaiboy\\unnamed.jpg")
          resized1 = self.original1.resize((495, 300),Image.ANTIALIAS)
          self.image1 = ImageTk.PhotoImage(resized1)
          bglab1=Label(MainFrame,image=self.image1,bd=1).place(x=0,y=0)

          #Labframe=LabelFrame(MainFrame,width=495,height=295,text="HENTAI_MANGA_PComics")
          #Labframe.place(x=1,y=0)

#===================================LABELS===========================================
          Lab=Label(MainFrame,width=20,bd=4,text="PASTE YOUR URL :>",bg="black",fg="cyan")
          Lab.place(x=180,y=90)


          Labofsite=Label(MainFrame,width=20,bd=4,text="SELECT YOUR SITE :>",bg="black",fg="cyan")
          Labofsite.place(x=280,y=180)

#===================================COMBOBOX==========================================
          Sites_list=["ilikecomix.com","porncomics.one"]
          Sites_combo=Combobox(MainFrame,values=Sites_list,font=('arial',10),width=14,state="readonly",textvariable=comb)
          Sites_combo.set("select")
          Sites_combo.place(x=300,y=220)

#================================== ENTRY=============================================
          Ent=Entry(MainFrame,width=55,bd=4,relief="sunken",font=("times new roman","12","bold"),bg="#dbfbf8",textvariable=sites)
          Ent.place(x=20,y=120)



#=====================================================================================
          But_down=Button(MainFrame,text="Dowloade comics",width=15,command=getsite,cursor="hand2",font=("times new roman",12,"bold"))
          But_down.place(x=70,y=190)
          But_down.bind("<Enter>",on_enter1)
          But_down.bind("<Leave>",on_leave1)


          But_clear=Button(MainFrame,text="Clear",width=15,command=clear,cursor="hand2",font=("times new roman",12,"bold"))
          But_clear.place(x=70,y=240)
          But_clear.bind("<Enter>",on_enter2)
          But_clear.bind("<Leave>",on_leave2)







          
          






#=====================================================================#

if __name__ == "__main__":
    root=Tk()
    app=hentai(root)
    root.mainloop()

