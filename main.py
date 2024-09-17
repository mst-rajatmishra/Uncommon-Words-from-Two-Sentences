from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Count occurrences of each word in both sentences
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        # Find uncommon words
        uncommon_words = []
        
        # Check words in s1
        for word in count1:
            if count1[word] == 1 and word not in count2:
                uncommon_words.append(word)
        
        # Check words in s2
        for word in count2:
            if count2[word] == 1 and word not in count1:
                uncommon_words.append(word)
        
        return uncommon_words
