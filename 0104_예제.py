# 예제 1
list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")

"""
3 4 5 6 7 8
"""
"""
정답: 인덱스를 지정하지 않으면 .pop()은 리스트의 마지막 항목을 삭제하고 돌려준다.
2 3 4 5 7 8
"""


# 예제 2
for element in range(-2, 10, 2):
    print(element, end=" ")

"""
-2 0 2 4 6 8
"""


# 예제 3
a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1
    
    if number % 3 == 0:
        b = b + 1
    
    if number % 4 == 0:
        c = c + 1
    
    if number % 5 == 0:
        d = d + 1

print(a, b, c, d) # 5 2 0 1

# 정답: if 조건문들이 중첩 조건문으로 들여쓰기 되어 있는 것이 아니므로 모든 조건문을 거치며 카운팅된다.
# 5 4 3 2


# 예제 4
i = 0
while i <= 10:
    print(i)
    i = i + 1

"""
0
1
2
3
4
5
6
7
8
9
10
"""


# 예제 5
i = 0
while i <= 10:
    i = i + 1
    print(i)

"""
1
2
3
4
5
6
7
8
9
10
11
"""


# 예제 6
i = 0
while i <= 10:
    i = i + 2
    print(i)

"""
2
4
6
8
10
12
"""


# 예제 7
i = 0
while True:
    print(i)
    i = i + 1
    if i > 10:
        break

"""
0
1
2
3
4
5
6
7
8
9
10
"""


# 예제 8
i = 0
while True:
    print(i)
    if i > 10:
        break
    i = i + 1

"""
0
1
2
3
4
5
6
7
8
9
10
11
"""


# 예제 9
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable)) # 7


# 예제 10
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable)) # 21


# 예제 11
list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # -12