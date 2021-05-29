def odd_one_out(l1):   # Q1 odd man out
    for i in range(len(l1)):
        freq = 0
        for j in range(len(l1)):
            if l1[i] == l1[j]:
                freq += 1
        if freq == 1:
            return l1[i]

    return -1


def closest_to_mean(lst):   # Q2 closest to mean
    mean = sum(lst)/len(lst)
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - mean))]


def find_speed(distance, time):   # Q3 find speed when distance and time are given
    speed = []
    for i in range(len(time)):
        speed.append(distance[i]/time[i])
    return speed


def missing_no(original, modified):   # Q4 missing no when original and modified lists are given
    for i in range(len(original)):
        if original[i] not in modified:
            return original[i]


def difference_between_two_lowest(lst):   # Q5 difference between two lowest number of list
    lst.sort()
    return lst[1] - lst[0]


def count_smaller_than_mean(lst):   # Q6 count no of elements smaller than mean
    mean = sum(lst)/len(lst)
    count = 0
    for i in range(len(lst)):
        if lst[i] < mean:
            count += 1
    return count


print(odd_one_out([5, 6, 5, 5, 5]))   # Q1
print(closest_to_mean([34, 56, -12, 90, 71]))   # Q2
print(find_speed([70, 65, 45, 95, 120], [5, 5, 3, 7, 4]))   # Q3
print(missing_no([12, 56, 73, 90, 85], [73, 85, 12, 56]))   # Q4
print(difference_between_two_lowest([12, 45, 76, 3, 15]))   # Q5
print(count_smaller_than_mean([89, 34, 65, 13, -47]))   # Q6
