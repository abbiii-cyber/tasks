#printing any 2 numbers in a list that add up to a given number enumerate assigns an index to each object
list = [10,2,8,5,7,1,15,-1,11]
sum = 10
for i, number in enumerate(list):
    diff = sum - number 
    if diff in list[i:]:
        print("numbers are: {} and {}". format(number, diff))
        break
    else:
        print("no numbers found")


        