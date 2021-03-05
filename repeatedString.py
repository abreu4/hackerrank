# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):

    ss_n = len(s)
    ss_as = 0
    total_as = 0
    a_indexes = []
    
    # as in ONE substring
    ss_as = s.count("a")
    
    # total as in regular substrings
    full_sss = n // ss_n
    total_as += ss_as * full_sss
    
    # total + as in final substring
    total_as += s[:n - (full_sss * ss_n)].count("a")

    return total_as

s = "aba"
n = 10

print(repeatedString(s, n))