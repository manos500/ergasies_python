from sympy import re


with open('randomText.txt','r') as f:
    data = f.read()
    sum_zugwn = 0
    sum_dibBy3 = 0
    sum_dibBy5 = 0
    sum_dibBy7 = 0
    akolouthia = ''

    #find the first and last two bits of evert letter
    for letter in data:
       binary_number = bin(ord(letter))
       last_two = binary_number[-2:]
       if ord(letter) >= 64:                    
           first_two =  binary_number[2:4]
       elif ord(letter) >= 32:
           first_two = '0' + binary_number[2]
       else:
           first_two = '00'
       akolouthia = akolouthia + first_two + last_two
    

    #split akolouthia in parts of 16 bits
    A = 16
    result = []
    for i in range(0, len(akolouthia), A):
        result.append(akolouthia[i : i + A])
    
    #remove the last part of the list if the bits are less than 16
    if len(str(result[-1])) < 15:
        result.remove(result[-1])   
    
    for number in result:
        dec_number = int(number,2)
        
        if dec_number % 2 == 0:
            sum_zugwn = sum_zugwn + dec_number
        if dec_number % 3 == 0:  
            sum_dibBy3 = sum_dibBy3 + dec_number 
        if dec_number % 5 == 0:  
            sum_dibBy5 = sum_dibBy5 + dec_number 
        if dec_number % 7 == 0:  
            sum_dibBy7 = sum_dibBy7 + dec_number

    total_sum = sum_zugwn + sum_dibBy3 + sum_dibBy5 + sum_dibBy7 

    pososto_zugwn = int(sum_zugwn/total_sum*100)
    pososto_divBy3 = int(sum_dibBy3/total_sum*100)
    pososto_divBy5 = int(sum_dibBy5/total_sum*100)
    pososto_dibBy7 = int(sum_dibBy7/total_sum*100)

    print('Το ποσοστό των ζυγών αριθμών είναι: ' + str(pososto_zugwn) + '%')
    print('Το ποσοστό των αριθμών που διαιρούνται ακριβώς με το 3 είναι: ' + str(pososto_divBy3) + '%')
    print('Το ποσοστό των αριθμών που διαιρούνται ακριβώς με το 5 είναι: ' + str(pososto_divBy5) + '%')
    print('Το ποσοστό των αριθμών που διαιρούνται ακριβώς με το 7 είναι: ' + str(pososto_dibBy7) + '%')
           


        
       
    
