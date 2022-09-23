import pytest
def Fizz_Buzz():
    output_string=''
    for i in range(1,37):
        if i%3==0 and i%5==0:
            output_string+='Fizz Buzz, '
        elif i%3==0:
            output_string+='Fizz, '
        elif i%5==0:
            output_string+='Buzz, '
        else:
            output_string+=str(i)+', '
    return(output_string+'...')
    
def test_Fizz_Buzz():
    assert Fizz_Buzz()== '1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...'
pytest.main()