# 예제 1
number1 = 1
number2 = number1 + 1
print(number1, number2) # 1, 2 
# 정답 1 2 (콤마 없어야 함)


# 예제 2
number1 = 10
number2 = 5
number3 = str(number1) + str(number2)
number4 = number1 + number2

print(number1, number2, number3, number4) # 10, 5, 105, 15
# 정답 10 5 105 15 (콤마 없어야 함)


# 예제 3
string1 = "Hello"
string2 = string1
string3 = "World" + "!"

print(string2, "?", string3) # Hello ? World !
# 정답 Hello ? World! (문자열 결합시 띄어쓰기 없음)


# 예제 4
string = "Hello?"
n = 5

print(string * n) # Hello? Hello? Hello? Hello? Hello?
# 정답 Hello?Hello?Hello?Hello?Hello? (문자열 결합시 띄어쓰기 없음)


# 예제 5
string = "abc hello def"
sub_string1 = string[4:10]
sub_string2 = string[1:4]
sub_string3 = string[-1]

print(sub_string1) # hello 
print(sub_string2) # bc 
print(sub_string3) # f


# 예제 6
number1 = 5
number2 = 10.0 + number1
number1 - 5
number3 = number1 * (number2 + 10)

print(number1, number2, number3) # 5 15.0 125.0


# 예제 7
list_variable = [1, 2, 3, [1, 2, 3]]
sub_list = list_variable[3][-1]

print(sub_list) # 3


# 예제 8
list_variable = []
list_variable.append(1)
list_variable.append("a")
list_variable[0] = 0

print(list_variable) # 0, 'a'
# 정답 [0, 'a'] (대괄호([])를 이용하여 리스트 형식 표현)


# 예제 9
name = input("너의 이름은?")

print(name) # 입력한 값 ex) 김규리


# 예제 10
age = int(input("너의 나이는?"))

print("올해 나이 : ", age) # 올해 나이 : 입력한 값 ex) 올해 나이 : 30
print("내년 나이 : ", age + 1) # 내년 나이 : 입력한 값 + 1 ex) 내년 나이 : 31