#!/usr/bin/env python
# coding: utf-8

# # types

# In[2]:


type(12345)


# In[3]:


type(12.3)


# In[6]:


type(5+2j)


# In[7]:


type([1,2,3,4])


# In[8]:


type({1:"one", 2:"two"})


# In[9]:


type((1,2,3,4))


# In[10]:


type("sumbul")


# In[11]:


type("Ture")


# In[12]:


type(True)


# # statments

# In[11]:


num =int(input("Enter a number: "))
if(num % 2) ==0:
    print("{0} is Even Number".format(num))
else:
    print("{0} is odd Number".format(num))

        


# # notes

# In[25]:


total=0;  
amt= 890;
total=int(amt/500)
print("{} notes of 500".format(total))
amt=amt-(total*500); 
total=int(amt/100);
print("{} note of 100".format(total))
amt=amt-(total*100); 
total=int(amt/50);
print("{} note of 50".format(total))
amt=amt-(total*50); 
total=int(amt/20);
print("{} note of 20".format(total))
amt=amt-(total*20); 
total=int(amt/10);
print("{} note of 10".format(total))
amt=amt-(total*10);
total=int(amt/5);
print("{} note of 5".format(total))
amt=amt-(total*5); 
      
      


# In[ ]:





# In[ ]:




