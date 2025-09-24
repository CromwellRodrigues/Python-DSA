# Given the first 2 terms A1 and A2 of an arithmetic progression, and a number N,
# find the Nth term of the series.

def find_nth_term(A1, A2, N):
    diff = A2 - A1  # Common difference
    nTerm = A1 + (N - 1) * diff
    return nTerm 


print(find_nth_term(2, 4, 5))  # 10
print(find_nth_term(5, 6, 7))  # 11