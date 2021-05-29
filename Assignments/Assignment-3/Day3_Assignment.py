import ipaddress


def formatting_time(time_str):   # Q1 formatting malformed time string
    time_list = time_str.split(':')
    hh = int(time_list[0])
    mm = int(time_list[1])
    ss = int(time_list[2])

    while ss > 59:
        if ss == 60:
            ss = 0
            mm += 1
        elif ss > 60:
            ss = ss - 60
            mm += 1
    while mm > 59:
        if mm == 60:
            mm = 0
            hh += 1
        elif mm > 60:
            mm = mm - 60
            hh += 1
    corrected_time = str(hh) + ':' + str(mm) + ':' + str(ss)
    return corrected_time


def formatting_date(date_str):   # Q2 formatting malformed date string
    date_list = date_str.split('/')
    dd = int(date_list[0])
    mm = int(date_list[1])
    yyyy = int(date_list[2])

    while dd > 28:
        if mm == 2:
            dd -= 28
            mm += 1
        elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
            dd -= 31
            mm += 1
        else:
            dd -= 30
            mm += 1
    if dd == 0:
        dd += 1
    while mm > 12:
        mm -= 12
        yyyy += 1
    return str(dd) + '/' + str(mm) + '/' + str(yyyy)


def is_isogram(strng):   # Q3 string is isogram or not
    lower_str = strng.lower()
    letter_list = []
    for letter in lower_str:
        if letter.isalpha():
            if letter in letter_list:
                return 'no'
            letter_list.append(letter)
    return 'yes'


def ip_address_to_integer(ip_str):   # Q4 ip address to integer format
    return int(ipaddress.ip_address(ip_str))


def integer_to_ip_address(ip_int):   # Q4 integer to ip address
    return str(ipaddress.ip_address(ip_int))


def mexican_wave(user_str):   # Q5 find mexican wave
    new_str = []
    for i, val in enumerate(user_str[:]):
        up = user_str[i].upper()
        c = user_str[:i] + up + user_str[i + 1:]
        new_str.append(c)
    return new_str


def maxNumber_after_one_deletion(n):   # Q6 largest number by deleting single digit
    ans = 0
    i = 1
    while n // i > 0:
        temp = (n // (i * 10)) * i + (n % i)
        i *= 10
        if temp > ans:
            ans = temp
    n = ans
    return ans


def maxNumber_after_shuffling(num):   # Q7 largest number by shuffling the digits
    count = [0 for x in range(10)]
    string = str(num)
    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] + 1
    result = 0
    multiplier = 1
    for i in range(10):
        while count[i] > 0:
            result += i * multiplier
            count[i] = count[i] - 1
            multiplier = multiplier * 10
    return result


def frequency_of_given_word(user_str, word):   # Q8 word frequency in given message
    return user_str.count(word)


def decToHexa(n):   # Q9 RGB to Hex conversion
    hexaDeciNum = ['0'] * 100
    i = 0
    while n != 0:
        temp = 0
        temp = n % 16
        if temp < 10:
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)

    hexCode = ""
    if i == 2:
        hexCode = hexCode + hexaDeciNum[0]
        hexCode = hexCode + hexaDeciNum[1]

    elif i == 1:
        hexCode = "0"
        hexCode = hexCode + hexaDeciNum[0]

    elif i == 0:
        hexCode = "00"

    return hexCode


def convertRGBtoHex(R, G, B):   # calling function for RGB to Hex
    if ((0 <= R <= 255) and
            (0 <= G <= 255) and
            (0 <= B <= 255)):
        hexCode = "#"
        hexCode = hexCode + decToHexa(R)
        hexCode = hexCode + decToHexa(G)
        hexCode = hexCode + decToHexa(B)
        return hexCode
    else:
        return "-1"


def accumulated_string(user_str):   # Q10 accumulated strings
    count = 1
    newList = []
    for i in user_str:
        newList.append(i * count)
        count += 1
    temp_str = ''
    for i in range(len(newList)):
        temp_str = newList[i][0].upper() + str(newList[i][1:])
        newList[i] = temp_str + '-'
    res_str = ''
    return res_str.join(newList)[:-1]


print(formatting_time('5:70:65'))   # Q1
print(formatting_date('45/8/2018'))   # Q2
print(is_isogram('python'))   # Q3
print(ip_address_to_integer('255.0.11.255'))   # Q4
print(integer_to_ip_address(438349270))   # Q4
print(mexican_wave('shahin'))   # Q5
print(maxNumber_after_one_deletion(98567))   # Q6
print(maxNumber_after_shuffling(4582309))   # Q7
print(frequency_of_given_word('python is object oriented programming language python is interpreted language', 'python'))   # Q8
print(convertRGBtoHex(25, 56, 123))   # Q9
print(accumulated_string('abcde'))   # Q10
