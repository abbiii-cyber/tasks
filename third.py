#function to check if an array is a subsequence of a given array where i is the index of first array x is its length and j and y for second array
def Subsequence (arrayA, arrayB, x, y):
    i = 0; j = 0;
    while(i<x and j<y):
        if(arrayA[i] == arrayB[j]):
            i += 1;
            j+= 1;
            if (j==y):
                return True
            else:
                    i=i-j+1;
                    j=0;
        return False


arrayA = [1, 2, 3, 8, 9, -1, 0]
arrayB = [2, 8, 9, 10]
x = len(arrayA);
y = len(arrayB);
if (Subsequence(arrayA, arrayB, x, y)):
    print("True")
else:
    print("False")