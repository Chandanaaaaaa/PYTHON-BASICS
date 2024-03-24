#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BMI = (weight in poundsx703)/(height in inchesx height in inches)


# In[11]:


name=input("Enter your name: ")

weight=int(input("Enter your weight in pounds: "))

height=int(input("enter your height in inches :"))

BMI = (weight*703)/(height*height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name+",you are underweight")
    elif(BMI<=24.9):
        print(name+",you are normalweight")
    elif(BMI<29.9):
        print(name+",you are overweight")
    elif(BMI<34.9):
        print(name+",you are obese")
    elif(BMI<39.9):
        print(name+",you are severely obese")
    else:
        print(name+",you are morbidly obese")
else:
    print("enter valid input")


# In[ ]:



        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




