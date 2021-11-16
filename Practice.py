a = [9, 13, 1, 8, 12, 4, 0, 5]

b = [3, 17, 4, 14, 6,]

t = 20

def close_sum (list1, list2, target) :
    i = 0
    j = 0

    while i < len(list1) :
        num1 = list1[i]

        while j < len(list2) :
            num2 = list2[j]

            if (num1 + num2 == target + 1) or (num1 + num2 == target -1) :
                print([num1, num2])
                j += 1

            else :
                j += 1

        j = 0        
        i += 1


close_sum(a, b, t)