class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to a set for O(1) lookup
        wordSet = set(wordList)
        
        # If endWord is not in wordList, return 0 since it's impossible to transform
        if endWord not in wordSet:
            return 0
        
        # BFS initialization
        queue = deque([(beginWord, 1)])  # Queue contains pairs of (current_word, current_depth)
        
        while queue:
            current_word, depth = queue.popleft()
            
            # Check if we've reached the endWord
            if current_word == endWord:
                return depth
            
            # Try changing each character in the current word
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':  # Try all possible lowercase letters
                    new_word = current_word[:i] + c + current_word[i+1:]
                    
                    # If the new word is in the wordSet, add it to the queue and remove it from the set
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, depth + 1))
        
        # If we exhaust the queue without finding endWord, return 0
        return 0 