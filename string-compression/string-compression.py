class Solution(object):
    def compress(self, chars):
        if not chars:
            return []
        
        if len(chars) == 1:
            return 1
        
        i = 0
        j = 0
        count = 1
        
        while j < len(chars) - 1:
            if chars[j] == chars[j+1]:
                count += 1
            else:
                # Important to handle ["a","a","a","b","b","a","a"] 
                # or else the output ["a","2","a","2","b","2"] which is incorrect
                # replacing j with i
                chars[i] = chars[j]
                i += 1
                if count > 1:
                    for char in str(count):
                        chars[i] = char
                        i += 1
                    count = 1    
            j += 1
            
        chars[i] = chars[j]
        i += 1
        if count > 1:
            for char in str(count):
                chars[i] = char
                i += 1
            count = 1

        return i
        