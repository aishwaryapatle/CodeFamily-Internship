# Question: You have to given a String and you have to swap that String In Other words Convert all the lowercase letter into Uppercase letter vice versa

# Sample Input :
# Hello Code Family

# Constraint :
# 0<=len(s)<=1000

# Sample Output ;
# hELLO cODE fAMILY

oldStr = input('Enter an input string : ')
newStr = "";  

for i in range(0, len(oldStr)):  
    if oldStr[i].islower():  
        newStr += oldStr[i].upper();  
    elif oldStr[i].isupper():  
        newStr += oldStr[i].lower();      
    else:  
        newStr += oldStr[i];          
print("String after case conversion : " +  newStr);  
