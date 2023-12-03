class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
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
# rather than using 2 for loop to tally up the characters then iterate through the other string
# you can tally up a string by just using Counter(magazine)