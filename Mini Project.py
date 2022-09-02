#!/usr/bin/env python
# coding: utf-8

# In[3]:


class onlinelibrary :
    def __init__(self) :
        print("welcome to online library")
        self._name=input("enter your name")
        self.__admine=int(input("please enter ur code"))
        self._email=input("please enter your e_mail")
        self._password=int(input("please enter your password"))
        self.__nameofbook=input("enter the name of the book, you need")
    def Displaybook(self) :
        name_book=input("enter ur book")
        if name_book==self._nameofbook :
            print("yes, we find it")
        else :
            print("ooops, we didnt find it")
    def lendbook(self) :
        Pass =int(input("please enter the password"))
        if Pass==self._password :
            lend=input("please enter the book , u want to lend")
            print("DONE ")
        else :
            print("oppos wrong password")
            
      
    def AddBook(self):
        test_code=int(input("enter ur code"))
        if test_code==self.__admine :
            newbook=input("enter the new book")
            print("DONE")
        else :
            print("the code is not valid")
    def retuernbook(self):
        passs=int(input("enter the code"))
        if passs==self._password :
            returnboook=input("enter the return book")
            print("DONE")
        else :
            print("errror ")
    


# In[4]:


a=onlinelibrary()


# In[5]:


class HarryLibrary(onlinelibrary ) :
    def passwordd(self) :
        self._ppp=int(input("enter the passs"))
        while self._ppp==self._password :
            select=int(input("enter ur number"))
            if select==1 :
                l=list() 
                l=["hebta", "yemmy"]
                print(l)
                   
            elif select==2 :
                print("welome, lend any book")
                lend_book=input("please enter the book, u want")
                print("the book is",lend_book)
            elif select==3 :
                print("welcome ,please return the book")
                return_book=input("enter the book ")
                print("return the book is",return_book)
            else :
                print("error ")


# In[6]:


a= HarryLibrary()


# In[ ]:


a.passwordd()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:




