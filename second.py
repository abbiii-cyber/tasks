def Numbers(list, n, sum):
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if list[i] + list[j] + list[k] == sum:
                    print("the three numbers are", list[i], ",", list[j], ",", list[k])
                    break
               
                else:
                    print("no three numbers add up to sum")

list = [-1, -10,2,-5,7,8,21,9,12,3,20,0]
sum = 10
n = len(list)
Numbers(list, n, sum)




