fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for fruit in fruits:
    print(fruit)

for person in people:
    if person['age'] > 20:
        print(person['name'])

def sum(a, b):
    return a+b
result = sum(1,2)
print(result)

def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년입니다')

is_adult(30)