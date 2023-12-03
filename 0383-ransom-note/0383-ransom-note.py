class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for char in magazine:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        for char in ransomNote:
            if char in counter:
                counter[char] -= 1
                if counter[char] < 0:
                    return False
            else:
                return False
        return True

        

# store and count each letter of magazing into a hashmap
# then for each letter in randomNote, decrement the hashmap
# if no value in hash found then return False
# if decrement is less than 0 then return False