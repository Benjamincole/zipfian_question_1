zipfian_question_1
==================

#Write a program that counts the numbers from 3 to 117. 
#But for multiples of three add 3 instead #of 1 and for 
#the multiples of five add 5 instead of 1. For numbers 
#which are multiples of both #three and five add 15 instead of 1. 
#Ex: If we are looking at numbers 5 to 15 (inclusive), the #program would output 39 *



def totalcount(a,b):
    count = 0
    x = range(a,b)
    for n in x:
        if n % 3 == 0 and n % 5 == 0:
            count += 15
        elif n % 3 == 0:
            count += 3
        elif n % 5 == 0:
            count += 5
        else:
            count += 1
    return count 


print totalcount(5,16)


