# string formatting

name='john'
age=21

print('%s is %d years old' %(name,age))
print('{} is{} years old'.format(name,age))
print(f'{name}is {age} years old')

bags=3
apples_in_bag=12
print(f'There are total of {bags* apples_in_bag}apples')