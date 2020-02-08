from tkinter import *
import webbrowser
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.geometry("890x450")
l1=["اهلا","مرحبا","هل من الممكن مساعدتي"]
l2=["طباعه","متغير","شرط","تكرار"]
response = ["مرحبا","اهل", "بالتاكيد ماذا تريد ان تتعلم🤔 "]
r2=["System.out.print(هنا يوضع النص المراد طباعته );","انواع المتغيرات :نص ، عدد عشري ، عدد صحيح ، حرف ، نص","for(نوع المتغير ورمزه );(عدد التكرار);(مقدار الزياده)","if (الشرط المراد )"]
names = ['d.gif'.format(i) for i in range(20)]
photo=PhotoImage(file="jva.png")
lbl=Label(window,image=photo)
lbl.place(x=0,y=0)


def callback(url):
    webbrowser.open_new(url)

name=Entry(window,bd = 3,width=40)
name.place(x=250,y=350)
lbl2 = Label(window)

lbl6=Label(window, text="sorry i can't know you Q")
lbl = Label(window)




def Click():
    q=name.get()
    lbl2.configure(text="")
    lbl.configure(text="")
    if q in l1 or "مساعدة" in q:
        if q =="اهلا":
            lbl2.configure(text="مرحبا♥")
            lbl2.place(x=400, y=390)
        elif q =="مرحبا":
            lbl2.configure(text="✭اهلا✭")
            lbl2.place(x=400, y=390)
        elif 'مساعدة' in q:

            lbl2.configure(text="✭بالتاكيد ماذا تريد ان تتعلم✭")
            lbl2.place(x=350, y=390)

    elif 'طباعه'in q:
        link1 = Label(window, text="شرح للطباعة", fg="blue", cursor="hand2")
        link5 = Label(window, text="مقطع يوتيوب", fg="blue", cursor="hand2")
        link1.bind("<Button-1>", lambda e: callback("https://www.geeksforgeeks.org/system-out-println-in-java/"))
        link5.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=_neD2Rs8GwM"))
        link1.place(x=480, y=415)
        link5.place(x=350, y=415)
        lbl.configure(text=r2[0])
        lbl.place(x=400, y=390)
    elif "متغير"in q:
        link2 = Label(window, text="شرح للمتغيرات", fg="blue", cursor="hand2")
        link2.bind("<Button-1>", lambda e: callback("https://www.geeksforgeeks.org/variables-in-java/"))
        link6 = Label(window, text="مقطع يوتيوب", fg="blue", cursor="hand2")
        link6.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=JcW34UKdzSk"))

        link2.place(x=480, y=415)
        link6.place(x=350, y=415)
        lbl.configure(text=r2[1])
        lbl.place(x=300, y=390)
    elif "شرط"in q:
        link3 = Label(window, text="شرح للشرط", fg="blue", cursor="hand2")
        link7 = Label(window, text="مقطع يوتيوب ", fg="blue", cursor="hand2")
        link3.bind("<Button-1>", lambda e: callback("https://www.geeksforgeeks.org/java-if-statement-with-examples/"))
        link7.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=FG7-8gAJ-5k"))
        link3.place(x=480, y=415)
        link7.place(x=350, y=415)
        lbl.configure(text=r2[3])
        lbl.place(x=400, y=390)
    elif "تكرار"in q:
        link4 = Label(window, text="شرح للتكرار", fg="blue", cursor="hand2")
        link8 = Label(window, text="مقطع يوتيوب شرح", fg="blue", cursor="hand2")
        link4.bind("<Button-1>", lambda e: callback("https://www.geeksforgeeks.org/loops-in-java/"))
        link8.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=XM4hlBuVlAQ"))
        link4.place(x=480, y=415)
        link8.place(x=350, y=415)
        lbl.configure(text=r2[2])
        lbl.place(x=300, y=390)
    else:
        lbl6.configure(text="عذرا لا استطيع التعرف على سؤالك ولكن قوقيل يستطسع مساعدتك :)")
        link1 = Label(window, text="عمنا قوقيل", fg="blue", cursor="hand2")
        link1.bind("<Button-1>", lambda e: callback("https://www.google.com/?client=safari&channel=iphone_bm"))
        link1.place(x=400, y=415)
        lbl6.place(x=250, y=390)

icon2=PhotoImage(file="se.png")
bu=Button(window,text="Enter",image=icon2, height = 25, width = 25,command=Click)
bu.place(x=630,y=350)
window.mainloop()