
def Subsequence (arrayA, arrayB):
    {
    int startIndexB = 0:
        foreach (int n in arrayA) 
        {
            int next = indexOf(arrayB, startIndexB , n);
            if (next == NOT_FOUND)
            {
                return false;
            }
            startIndexB = next+1;
        }
        return true:
    }


