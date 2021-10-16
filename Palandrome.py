#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class palanExample:
    def __init__(self):
        pass
    
    def palaChecker(self):
        
        name_input2 = input("Enter any word:  ")
        
        name_input2_reversed = name_input2[::-1]
        
        if name_input2 == name_input2_reversed:
            print("Its a palandrome")
            
        else:
            print("Its not a palandrome")

