class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        res = False
        if len(A) != len(B):
            return False
        if A == B:
            if len(A) - len(set(A)) != 0:
                res = True
        else:
            n = 0
            arrA, arrB = [], []
            for i in range(len(A)):
                if A[i] != B[i]:
                    n += 1
                    arrA.append(A[i])
                    arrB.append(B[i])
            if n <=2 and set(arrA) == set(arrB):
                res = True
        return res
        