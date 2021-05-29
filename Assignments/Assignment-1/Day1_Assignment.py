import math


def greater(a, b, c):  # Q1 greater no.
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def armstrong(num):  # Q2 armstrong
    result = 0
    temp_num = n = num
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    while num != 0:
        temp = num % 10
        result = result + temp ** cnt
        num = num // 10
    if result == temp_num:
        return 'yes'
    else:
        return 'no'


def result(num):  # Q3 reverse and sum
    sum = 0
    rev = 0
    n = num
    while num != 0:
        rem = num % 10
        sum += rem
        rev = rev * 10 + rem
        num //= 10
    return 'reverse is', rev, 'sum is', sum


def hcf(a, b):  # Q4 HCF
    if b == 0:
        return a
    return hcf(b, a % b)


def checkHCF(x, y):  # calling function for hcf
    if hcf(x, y):
        return hcf(x, y)
    else:
        return 'not found'


def lcm(a, b):  # Q5 LCM
    lar = max(a, b)
    small = min(a, b)
    i = lar
    while 1:
        if i % small == 0:
            return i
        i += lar


def leap(year):  # Q6 Leap year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'yes'
    else:
        return 'no'


def typeOfTriangle(a, b, c):  # Q7 Type of triangle
    temp_list = [a, b, c]
    temp_list.sort()
    a1 = temp_list[0]
    b1 = temp_list[1]
    c1 = temp_list[2]
    if a == b and b == c:
        return "equilateral triangle"
    elif c1 * c1 == a1 * a1 + b1 * b1:
        return "right angle triangle"
    elif a == b or b == c or c == a:
        return "isosceles triangle"
    else:
        return "Scalene triangle"


def equationRoots(a, b, c):  # Q8 quadratic equations
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    if dis > 0:
        return 'real and different roots', (-b + sqrt_val) / (2 * a), '&', (-b - sqrt_val) / (2 * a)
    elif dis == 0:
        return 'real and same roots', -b / (2 * a)
    else:
        return "Complex Roots", - b / (2 * a), "+ i", sqrt_val, '&', - b / (2 * a), "- i", sqrt_val


def findQuadrant(x, y):  # Q9 Quadrant
    if x > 0 and y > 0:
        return "first quadrant"
    elif x < 0 and y > 0:
        return "second quadrant"
    elif x < 0 and y < 0:
        return "third quadrant"
    elif x > 0 and y < 0:
        return "fourth quadrant"
    elif x == 0 and y == 0:
        return "center"
    else:
        return "on line"


def arithmetic(a, b):
    addition(a, b)
    subtraction(a, b)
    multiplication(a, b)
    division(a, b)
    floorDivision(a, b)
    modulus(a, b)
    power(a, b)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def floorDivision(a, b):
    return a // b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def fibonacci(n):  # Q11 fibonacci series
    a = 0
    b = 1
    res = 0
    fibo_list = [0, 1]
    count = 1
    while count <= n - 2:
        res = a + b
        fibo_list.append(res)
        a = b
        b = res
        count += 1
    return fibo_list


def tribonacci(n):  # Q11 tribonacci series
    a = 0
    b = 0
    c = 1
    res = 0
    tribo_list = [0, 0, 1]
    count = 1
    while count <= n - 3:
        res = a + b + c
        tribo_list.append(res)
        a = b
        b = c
        c = res
        count += 1
    return tribo_list


def factorial(num):  # Q12 factorial
    fact = 1
    while num != 0:
        fact *= num
        num -= 1
    return fact


def sumOfFactors(num):  # Q13 sum of factors
    result = 0
    i = 1
    while i < num:
        if num % i == 0:
            result += i
        i += 1
    return result


def vowelCheck(ch):  # Q14 vowel or consonant check
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return 'vowel'
    else:
        return 'consonant'


def digitalRoot(num):  # Q15 Digital root
    result = 0
    while num != 0:
        result += num % 10
        num //= 10
    if result > 9:
        return digitalRoot(result)
    else:
        return result


def prime(start, end):  # Q16 prime no in given range
    prime_list = []
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


def sumOfTriangularNo(num):  # Q17 sum of triangular number
    result = 0
    for i in range(num + 1):
        for j in range(i + 1):
            result += j
    return result


def maxNumber(n):  # Q18 maximum number after deleting one digit
    ans = 0
    i = 1
    while n // i > 0:
        temp = (n // (i * 10)) * i + (n % i)
        i *= 10
        if temp > ans:
            ans = temp
    n = ans
    return ans


def SieveOfEratosthenes(n, isPrime):  # Q19 super prime
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True
    for p in range(2, n + 1):
        if p * p <= n and isPrime[p] == True:
            for i in range(p * 2, n + 1, p):
                isPrime[i] = False
                p += 1


def superPrimes(n):  # calling function for super prime
    isPrime = [1 for i in range(n + 1)]
    SieveOfEratosthenes(n, isPrime)
    primes = [0 for i in range(2, n + 1)]
    j = 0
    for p in range(2, n + 1):
        if isPrime[p]:
            primes[j] = p
            j += 1
    super_prime = []
    for k in range(j):
        if isPrime[k + 1]:
            super_prime.append(primes[k])

    return super_prime


def noOfMatch(n):  # Q20 No of matches for n teams
    return n * (n - 1) // 2


def pascalTriangle(n):  # Q21 pascal's triangle
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(' ', end='')

        c = 1
        for j in range(1, i + 1):
            print(' ', c, sep='', end='')
            c = c * (i - j) // j
        print()


def pyramidTriangle(n):  # Q21 Pyramid triangle
    p = 1
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(p, end=" ")
            p += 1
        print("\r")


print(greater(34, 89, 12))   # Q1
print(armstrong(153))   # Q2
print(result(34652))   # Q3
print(hcf(6, 2))   # Q4
print(lcm(15, 3))   # Q5
print(leap(2019))   # Q6
print(typeOfTriangle(3, 4, 3))   # Q7
print(equationRoots(3, 5, 2))   # Q8
print(findQuadrant(5, -6))   # Q9
print(arithmetic(7, 3))   # Q10
print(fibonacci(10))   # Q11
print(tribonacci(10))   # Q11
print(factorial(7))   # Q12
print(sumOfFactors(30))   # Q13
print(vowelCheck('Y'))   # Q14
print(digitalRoot(7895))   # Q15
print(prime(3, 8))   # Q16
print(sumOfTriangularNo(4))   # Q17
print(maxNumber(98567))   # Q18
print(superPrimes(241))   # Q19
print(noOfMatch(10))   # Q20
print(pascalTriangle(5))   # Q21
print(pyramidTriangle(5))   # Q21
