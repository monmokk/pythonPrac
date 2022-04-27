import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for row in rows:
    gu_name = row['MSRSTE_NM']
    gu_mise = row['IDEX_MVL']
    if gu_mise < 100:
        print(gu_name, gu_mise)

a = 99
print(type(a))

str1 = 'codestates'
print(str1[2:4], str1[:4], str1[8:], str1[:-1], str1[:])

str2 = 'Welcome'
str3 = 'Hello'
print(str3 + str2 * 2)

print("code" in "codestates")

print(2 ** 3 * 3)

for i in range(2, 21):
    if i == 8:
        print()
        break
    print(i, end=' ')

list_a = [1,2,3,4]
list_b = [2,3,4,5]
result = []
for a in list_a:
    for b in list_b:
        if a == b:
            result.append(a)
print(result)

def remainder(param, num = 5, div = 2):
    return num % div

print(remainder(param=7))

s = [11,22,33,44,55]
print(s[0:1:3].index(11))

def sort(unsort_list):
    loop_number = len(unsort_list)

    for compare_index in range(loop_number):
        compare_value = unsort_list[compare_index]
        prev_position = compare_index -1

        if prev_position >= 0 and unsort_list[prev_position] >= compare_value:
            unsort_list[prev_position+1] = unsort_list[prev_position]

            prev_position = prev_position -1
    return unsort_list

test_arr = [5,3,1,6,7,13]
sort(test_arr)
print(test_arr)

str_data = {'A', 'B', 'C'}
joined_str = " and ".join(str_data)
print(joined_str)

dict = {}
dict['네이버'] = '[ㅓㅏㅋ처ㅣㅓㅏ]'
dict['다음'] = '[ㅇㅁㅇ;ㄴ암임ㄴ]'
dict['구글'] = '[구구]'
dict.pop('네이버')
print(dict)

test_data = 3
def func_1():
    global test_data
    test_data = 7
func_1()
print(test_data)

str_data='python programming'
cap_str_data = str_data.capitalize()
print(cap_str_data)

str_data = '{Hey} {Jude} {don"t be {{afraid'
pre_str_data1 = str_data.replace('{', '')
pre_str_data2 = pre_str_data1.replace('}', '')
print(pre_str_data2)

def value_list(list_1):
    result_value = list_1[0]
    resul_list_value = list_2[0]
    for list_test in list_1:
        if list_test < resul_list_value:
            result_value = list_test
    return resul_list_value

list_1 = [1,55,23,22]
list_2 = [4,24,78,6,21]

print("네?1", value_list(list_1))
print("네?@", value_list(list_2))