class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash = {}
        for c in magazine:
            magazine_hash[c] = 1 + magazine_hash.get(c,0)
        for c in ransomNote:
            if c not in magazine_hash or magazine_hash[c] <=0:
                return False
            magazine_hash[c]-=1
        return True
    
