def Fizz_Buzz(number_of_rounds):
    output_string=''
    for i in range(1,number_of_rounds):
        if i%3==0 and i%5==0:
            output_string+='Fizz Buzz, '
            print('Fizz Buzz')
        elif i%3==0:
            output_string+='Fizz, '
            print('Fizz')
        elif i%5==0:
            output_string+='Buzz, '
            print('Buzz')
        else:
            output_string+=str(i)+', '
            print(str(i))
    print('Printing finished')