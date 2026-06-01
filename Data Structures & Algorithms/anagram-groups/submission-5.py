class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         maps = {}
         from string import ascii_lowercase
         for s in strs:
            alphabet_map = [0 for i in ascii_lowercase]
            for letter in s:
                index = ascii_lowercase.index(letter)
                alphabet_map[index]+=1     
            alphabet_map_key = tuple(alphabet_map)           
            if alphabet_map_key in maps:        
                maps[alphabet_map_key].append(s) 
            else:
                maps[alphabet_map_key] = [s]
         print(maps)      
         return list(maps.values())   