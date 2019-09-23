'''
This program will print students their final grade
>  90% student gets an A
>= 80% student gets a B
>= 70% student gets a C
>= 60% student gets a D
<  60% student gets an F

'''

# creating a variable score and converting it to an integer
score = int(input('Enter you Score: '))


if score < 0 or score >100:
    print('error')
elif score >= 90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
elif score >= 60:
    print('D')
elif score < 60:
    print('F')
