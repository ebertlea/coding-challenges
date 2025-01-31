class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_dict = Counter(s)
        n = len(count_dict)
        pal_len = 0
        for key,val in count_dict.items():
            if val%2==0:
                pal_len+=val
                n=n-1
            if val%2==1 and val>1:
                pal_len+=(val-1)
                n=n+1
        if n>0:
            pal_len+=1
        return pal_len
