def palindrome(s,start,end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return palindrome(s,start+1,end-1)

s = "NITIN"
print(palindrome(s,0,len(s)-1))