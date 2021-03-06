'''
https://stepik.org/lesson/24469/step/6?unit=6775
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s﻿.
Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a, либо же определить, что это невозможно.
Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a.
Если после применения любого числа операций в строке s останутся вхождения строки a, выведите Impossible.
Sample Input 1:
ababa
a
b
Sample Output 1:
1
Sample Input 2:
ababa
b
a
Sample Output 2:
1
Sample Input 3:
ababa
c
c
Sample Output 3:
0
Sample Input 4:
ababac
c
c
Sample Output 4:
Impossible
'''
s, a, b = input(), input(), input()
count = 0
zz = 0
while True:
    if a in s:
        s = s.replace(a, b)
        count += 1
    else:
        break
    zz += 1
    if zz == 1000:
        count = "Impossible"
        break
print(count)
