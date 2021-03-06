from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

#creating root or parent window

root=Tk()
root.title("PYTHON PROJECT")
root.resizable(width = FALSE , height = FALSE )
root.config(bg = "gray")


#creating send function consists of commands and responses

def send():
   send = " ME := " + e.get()
   txt.insert(END,"\n\n"+ send)
   
   if(e.get()=="hello" or e.get()=="hi" or e.get()=="HI" or e.get()=="HELLO"):
       txt.insert(END,"\n\n"+" MOBBY := Hi ,BOSS.")

   elif(e.get() =="i am fine too"or e.get()=="i am also fine"):
        txt.insert(END,"\n\n"+" MOBBY := That's cool ,BOSS")
        
   elif(e.get() =="how are you"):
        txt.insert(END,"\n\n"+" MOBBY :=  I am fine BOSS , what about you.")
        
   elif(e.get() =="i am also fine . tell me something about you"or e.get() =="tell me about yourself" or e.get() =="tell me something about yourself" or e.get() =="tell me something about you"):
        txt.insert(END,"\n\n"+" MOBBY :=  That's good BOSS , \n\n I am MOBBY chatbot.  I am here to provide information and aware people about CORONAVIRUS/COVID-19.")

   elif(e.get()=="tell me about coronavirus" or e.get()=="ok tell me about coronavirus"or e.get()==" ok tell me about covid-19 " or e.get()=="what is coronavirus" or e.get()=="what is COVID-19"):
        txt.insert(END,"\n\n"+" MOBBY := coronavirus disease(COVID-19) is a infectious disease caused by newly discovered coronavirus also known as SARS-CoV-2 .")
        txt.insert(END,"\n"+"This new virus and disease were unknown before the outbreak began in WUHAN , CHINA in December 2019 ")

   elif(e.get()== " what are the symptoms of coronavirus" or e.get() =="symptoms of coronavirus"):
        txt.insert(END,"\n"+" MOBBY := The most common symptoms are fever,tiredness and dry cough.Some patients may have aches and pains , nasal congestion,runny nose , sore throat or diarrhoea.")
        txt.insert(END,"\n"+"Most people(about 80%)recover from the disease without needing special treatment.Around 1 out of 6 people who gets COVID-19 gets seriously ill and")
        txt.insert(END,"\n"+"develops difficulty breathing.Older people with other medical problems like blood pressure,diabetes etc are more likely to develop serious illness")
   
   elif(e.get()=="i wanted to know about coronavirus" or e.get() ==  "let me ask you something" or e.get()=="i wanted to know something"):
        txt.insert(END,"\n\n"+" MOBBY := Sure BOSS . Ask whatever you want to know . I will try to answer  most of the qns . ")

   elif(e.get()=="how does coronavirus spread"):
        txt.insert(END,"\n\n"+" MOBBY := People can catch coronavirus from others who have the virus.They can catch virus by touching the infected person or infected object/surface.")
        txt.insert(END,"\n"+" Also it can spread from person to person through droplets from the mouth or nose of infected person whenever he coughs or exhales .")
        txt.insert(END,"\n"+" This is why it is important to stay more than 1 meter(3 feet) away from a perso who is sick")

   elif(e.get()=="precautions and preventions" or e.get()=="precautions" or e.get()=="preventions" or e.get()=="precautions of coronavirus"or e.get()=="preventions of coronavirus"):
        txt.insert(END,"\n\n"+" MOBBY := precautions of conoavirus are : 1.Regularly and throughly clean your hands with an alcohol-based handrub or wash them with soap and water")
        txt.insert(END,"\n\n"+" 2. Avoid touching eyes , nose and mouth.Hands touch many surfaces and can pick up viruses and touching nose , mouth will transfer the virus inside our body")
        txt.insert(END,"\n\n"+" 3.Follow respiratory hygiene. Cover you mouth and nose with mask when going outside.After use dispose of the used mask")
        txt.insert(END,"\n\n"+"4.Stay home if you feel unwell.If you have fever,cough and difficulty breathing seek medical help immediately.Follow the directions of local health authority")
        txt.insert(END,"\n"+" 5.Avoid travelling to places.Keep up to date on the latest COVID-19 situation and hotspots.")

   elif(e.get()=="incubation period of coronavirus" or e.get()=="incubation peiod"):
        txt.insert(END,"\n\n"+" MOBBY := Incubation period is 1-14 days,most commonly around 5 days.These estimates will be updated as more data become available")

   elif(e.get()=="what is incubation period"):
        txt.insert(END,"\n\n"+" MOBBY := The incubation period means the time between catching the virus and beginning to have symptoms of the disease ")

   elif(e.get()=="is there anything else i should not do " or e.get()=="is there anything i should not do"):
        txt.insert(END,"\n\n"+" MOBBY := Following are not effective against COVID-19 and can be harmful :  1. Smoking. 2. Wearing multiple masks.  3. Taking antibiotics.")

   elif(e.get()=="country with highest corona cases and death"):
        txt.insert(END,"\n\n"+" MOBBY := USA with cases close to 9M(8,882,818) and deaths = 230,477")


   elif(e.get()=="corona cases and deaths in world"):
        txt.insert(END,"\n\n"+" MOBBY := cases = 42,441,532 and deaths = 1,148,517 and  both are increasing rapidly")

   elif(e.get()=="treatment of coronavirus" or e.get()=="vaccine of coronavirus" or e.get()=="treatmet" or e.get()=="vaccine"):
        txt.insert(END,"\n\n"+" MOBBY := There is no treatment or vaccine for coronavirus yet.Possible vaccines and some specific drug treatments are under investigation and being tested")
        txt.insert(END,"\n"+"through clinical trials.Currently the type of treatment may involve : 1. fluids to reduce the risk of dehydration  2.medication to reduce a fever ")
        txt.insert(END,"\n"+"3. supplemental oxygen in more severe cases .")

   elif(e.get() == "who is your boss"):
        txt.insert(END,"\n\n"+" MOBBY := My BOSS is His Highness SHAHARIA ZAMAN CHOUDHURY")
        
   else:
        txt.insert(END,"\n\n"+" MOBBY := Sorry , I dont know about this BOSS. Next question .If you don't have one then Thank you  :) . ")
   e.delete(0,END)


#creating menu bar

main_menu = Menu(root)

file1_menu = Menu(root)
file2_menu = Menu(root)

file1_menu.add_command(label = "Feedback")

file2_menu.add_command(label = "Simple chatbot(MOBBY) created using python GUI(tkinter library)by Shaharia Zaman Choudhury")
file2_menu.add_command(label = "along with Kakimoni Gokul and Sakshi Poddar ")
file2_menu.add_command(label = "Thank you")

main_menu.add_cascade( label="About",menu = file2_menu)
main_menu.add_cascade( label="Help", menu = file1_menu)
main_menu.add_command( label="Exit")

root.config(menu = main_menu)
   

#creating top , middle and bottom frames

topFrame = Frame(root,bg = "gray")
topFrame.pack()

middleFrame = Frame(root,bg = "gray")
middleFrame.pack()

bottomFrame = Frame(root,bg = "gray")
bottomFrame.pack(side=BOTTOM)

#inserting image 

image1 = Image.open("C:/New folder/mahi1.jpeg")
resize1 = image1.resize((100,100),Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(resize1)

label1 = Label(topFrame,image = photo1,bg="cyan")
label1.pack(side=LEFT)



#header

theLabel = Label(topFrame , text = "CORONA CHATBOT" , fg = "black",bg = "cyan",width = "15",height = 2,font = ("Verdana",20))
theLabel.pack(side = LEFT)

image = Image.open("C:/New folder/mahi1.jpeg")
resize = image.resize((100,100),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resize)

label = Label(topFrame,image = photo,bg="cyan")
label.pack(side = LEFT)



#creating scroll bar

scrollbar = Scrollbar(middleFrame,orient = VERTICAL)
scrollbar.pack(side = RIGHT,fill = "y")

#creating the notepad or text area

txt=Text(middleFrame,font = ("Verdana",10),fg = "blue",width = 120,height = 30)
txt.pack(fill = BOTH,padx = 2)

Fact= """\n\n                                                              WELCOME . I AM MOBBY AND HOW MAY I HELP YOU               """

scrollbar.config(command = txt.yview)
txt.config(yscrollcommand = scrollbar.set)
txt.insert(tk.END,Fact)

# entry field

e = Entry(middleFrame,width = 140,fg="blue")
e.pack(expand = TRUE)

#send button

button1 = Button (middleFrame , text = "SEND",width = "12", height = 1 ,font = ("Verdana",15),fg= "black", command = send,bg="cyan")
button1.pack()





root.mainloop()


