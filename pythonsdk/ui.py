from Tkinter import *
import tkMessageBox
import tweepy
import MySQLdb as mdb
import querying as query
import staticRanking as sR
import re;
import tkFont
import tkHyperlinkManager
from PIL import ImageTk, Image
import webbrowser

def get_position(event):
	"""get the line and column number of the text insertion point"""
	line, column = text.index('insert').split('.')
	s = "line=%s column=%s" % (line, column)
	print "Karthik",
	print s

def callback(url):    
    webbrowser.open('http://'+url)
    
def helloCallBack(string,text):
   temp = sR.staticRanking(string)		
   list = []
   text.delete(1.0,END)   
   if(len(temp) == 0 ) :
	text.insert(INSERT,"No, results found for the query")
	return 	
   if(len(temp) == 1 and temp[0] == -1) :
	text.insert(INSERT,"No, results found for the query")
	return	
   for item in temp :
	tempList = re.split('_',item[0]);
       	list.append(tempList[1])
   con = mdb.connect('localhost', 'root', 'javar', 'nkj255-db1');
   with con: 
           #cur = con.cursor()      
           cur = con.cursor(mdb.cursors.DictCursor)
           j = 0	
           AUTHOR_URL=[]
           for postid in list:
               if j<50:
                  cur.execute("SELECT * FROM PostInfo WHERE postID=%s ORDER BY date ASC",(postid))
                  row = cur.fetchone()                  
                  if not row :
			continue	
                  cur.execute("SELECT pageName FROM PageInfo WHERE pageID=%s",(row['pageID']))
                  row2=cur.fetchone()
                  AUTHOR_URL.append('www.facebook.com/'+row['pageID'])
                  if int(row['isPage'])==1:
                     POST_URL='www.facebook.com/'+row['pageID']+'/posts'+row['postID']
                     PAGE_URL='www.facebook.com/'+row['pageID']                     
                     if row2:
                       AUTHOR_NAME=row2['pageName']
                     else:
                       AUTHOR_NAME='John David'
                  else:
                     POST_URL='www.facebook.com/groups/'+row['pageID']+'/permalink'+row['postID']
                     PAGE_URL='www.facebook.com/groups/'+row['pageID']                     
                     auth=row['author'].split('_')
                     if auth:
                       AUTHOR_NAME=auth[1]
                     else:
                       AUTHOR_NAME=' '
                  hyperlink = tkHyperlinkManager.HyperlinkManager(text)
                  Font = tkFont.Font(size=14,weight='bold')
                  text.tag_configure("Normal",font=Font)
                  text.tag_add("Normal",1.0,END)
                  text.insert(INSERT,str(j+1))
                  text.insert(INSERT,".      ")
                  """text.insert(INSERT,row['postID']+" ")
                  text.insert(INSERT,row['pageID']+" ")
                  text.insert(INSERT,row['likes'])
                  text.insert(INSERT," ")
                  text.insert(INSERT,row['shares'])
                  text.insert(INSERT," ")
                  text.insert(INSERT,row['date'])
                  text.insert(INSERT," ")
                  text.insert(INSERT,row['objectID'])
                  text.insert(INSERT," ")"""
                  text.insert(INSERT,row['post'])
                  text.insert(INSERT," ")
                  text.insert(INSERT,"\n")
                  text.insert(INSERT,'Dated  ')
                  text.insert(INSERT,row['date'])
                  text.insert(INSERT,'            ')
                  Font1 = tkFont.Font(size=14,weight='bold')
                  text.tag_configure("datefont",foreground="dark green",underline=False,font=Font1)
                  highlighttext(text,'Dated',"datefont")
                  highlighttext(text,row['date'],"datefont")
                  text.insert(INSERT, AUTHOR_NAME, hyperlink.add(lambda:callback(AUTHOR_URL[j-1])))
                  text.insert(INSERT,"\n\n\n")
                  Font = tkFont.Font(family='Helvetica',size=19, weight='bold')
                  text.tag_configure("highlightfont",foreground="red",underline=False,font=Font)
                  highlighttext(text,string,"highlightfont")
                  j=j+1
                  text.pack()

def highlighttext(text,pattern,Font,start="1.0",end="end",regexp=False):
    words=pattern.split()    
    for word in words:
	    start=text.index(start)
	    end=text.index(end)
	    text.mark_set("matchStart",start)
	    text.mark_set("matchEnd",start)
	    text.mark_set("searchLimit", end)
	    countvar= IntVar()
	    while True:
		     index = text.search(word, "matchEnd","searchLimit",regexp=regexp,count=countvar,nocase=1)
		     if index == "": 
		        break
		     text.mark_set("matchStart", index)
		     text.mark_set("matchEnd", "%s+%sc" % (index,countvar.get()))
		     text.tag_add(Font, "matchStart","matchEnd")
		     
def main():
	root=Tk()
	text = Text(root,height=250,width=250)	
	text.bind("<KeyRelease>", get_position)
	text.focus()
	root.title("HOWDY")
	root.geometry("1000x1000")
	background_image=ImageTk.PhotoImage(Image.open("howdy1.jpg"))
	background_label = Label(root, image=background_image)
	background_label.place(x=0, y=0, relwidth=1, relheight=0.3)
	#L1 = Label(root, text="HOWDY",fg='red')
	#L1.pack( side = TOP)
	img = Image.open("howdy.jpg")
	resized = img.resize((200, 200),Image.ANTIALIAS)
	resized_image = ImageTk.PhotoImage(resized)
	panel = Label(root, image = resized_image,height=200,width=200)
	panel.pack(side = TOP)
	E1 = Entry(root, bd =5,textvariable=StringVar,width=1000)
	E1.pack(side = TOP)
	B = Button(root, text ="Search", command = lambda: helloCallBack(E1.get(),text))
	B.pack()
	root.mainloop()
main()
	
