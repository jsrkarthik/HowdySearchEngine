from Tkinter import *
import tkMessageBox
import tweepy

def helloCallBack(string,root):
   consumer_key = 'rcdbXbMyYAbaJ0DertwAjg'
   consumer_secret = 'JHcX2LVxxRZb9zgJi7J9j8my2Rvu6OHYbKM6HFjUKBI'
   access_key = '75150596-Y7hxPYCotMtrcBvXZ8sCsnGbLalgBBFJyS9PFDMR4'
   access_secret = 'Hi9LstuYQxR4sgfMfPyH4bqxnBkjVK2SSehyCnj2VKWmF'
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_key, access_secret)
   api = tweepy.API(auth)
   text = Text(root,height=250,width=250)
   i=0
   for tweet in api.search(q=string,count=1000,		
		                    result_type="recent",
		                    include_entities=True,
		                    lang="en"):
	    if i < 1000 :
	     text.insert(INSERT,i)
	     text.insert(INSERT, tweet.text.encode('utf-8'))
	     text.insert(INSERT,"\n")
	    else:
	     break
	    i+=1
   text.pack()
   #tkMessageBox.showinfo( "Hello Python", string)


def main():
	root=Tk()
	root.title("HOWDY")
	root.geometry("1000x1000")
	L1 = Label(root, text="HOWDY",fg='red')
	L1.pack( side = TOP)
	E1 = Entry(root, bd =5,textvariable=StringVar)
	E1.pack(side = TOP)
	B = Button(root, text ="Search", command = lambda: helloCallBack(E1.get(),root))
	B.pack()
	root.mainloop()
main()
	
