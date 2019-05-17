# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:23:54 2019

@author: Chenyu
"""
import numpy as np
import math
#There are n^2-n possible (x,y) pairs, we have to exclude most of them based on the answers.

#Every time we deal with the latter layer, the conditions of all former layers must be satisfied.

#n is the maximal possible number(from 1 to n).


#process the information derived from the first answer: xy is not a prime number.
def layer1(a,n): #a=xy, so 1<=a<=n^2, this function recognizes the possible prime number a.
    j = 0 #indicator 
    if a <= n**2:
        for i in range(2, math.floor(a)):
            if a%i == 0:
                j=1
                break
    return j # j=0 implies that j is a prime number or 1 while j=1 implies that j is not a prime number.
  
#process the information derived from the second answer: the property of x+y          
def layer2(b,n): 
    j = 0 #indicator
    count = 0
    if b >= 4 and b<= 2*n:
        if b%2 == 0:
            for i in range(1, int((b+2)/2)):
                x = i
                y = b-i
                a = x*y
                if layer1(a,n) == 1:
                    count += 1
        else:
            for i in range(1, int((b+1)/2)):
                x = i
                y = b-i
                a = x*y
                if layer1(a,n) == 1:
                    count += 1
    if count >= 2:
        j = 1
    return j # j=1 implies that such b:=x+y satisfies the second answer and the first answer while j=0 doesn't.

#process the information derived from the third answer: the property of a = xy
def layer3(a,n):
    j = 0 #indicator
    count = 0
    if layer1(a,n)==1:
        if np.sqrt(a)%1 == 0:
            for i in range(1, int(np.sqrt(a)+1)):
                if a%i == 0:
                    x = i
                    y = a/i
                    b = x+y
                    if layer2(b,n) == 1:
                        count += 1
        else:
            for i in range(1, math.ceil(np.sqrt(a))):
                if a%i == 0:
                    x = i
                    y = a/i
                    b = x+y
                    if layer2(b,n) == 1:
                        count += 1
    if count == 1:
        j = 1
    return j # j=1 implies that such a:= xy satisfies the first three answers while j=0 doesn't.

# process the information derived from the last answer: the property of b = x+y
def layer4(b,n):
    j = 0 #indicator
    count = 0
    if layer2(b,n) == 1:
        if b%2 == 0:
            for i in range(1, int((b+2)/2)):
                x = i
                y = b-i
                a = x*y 
                if layer3(a,n) == 1:
                    count += 1
        else:
            for i in range(1, int((b+1)/2)):
                x = i
                y = b-i
                a = x*y 
                if layer3(a,n) == 1:
                    count += 1
    if count == 1:
        j = 1
    return j # j=1 implies that all the four answers are satisfied while j=0 doesn't.        
    
# n is the maximal possible number(from 1 to n).
# verify whether (x, y) satisfies all the conditions from n^2-n possible pairs.
# Actually the pair (x,y) is disordered. So we regulate that x <= y.
def search(n):
    answers = []
    for x in range(1, n+1):
        for y in range(x, n+1):
            answer = []
            a = x*y
            b = x+y
            if layer3(a,n) == 1 and layer4(b,n) == 1:
                answer.append(x)
                answer.append(y)
                answers.append(answer)
    return answers
    
print(search(30))
              
            
            
        
    

       
                
        
        
        

