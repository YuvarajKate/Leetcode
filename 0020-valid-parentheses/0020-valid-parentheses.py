class Solution:
    def isValid(self, s: str) -> bool:
        l = list(s)

        parenthesis = {')': '(', '}': '{', ']': '['}
        check = []
        x = True  
        for i in l:
            # Pushing on Stack
            if i not in parenthesis:
                check.append(i)
            else:
                # If check is empty 
                if check == []:
                    x = False   
                    break
                
                top = check.pop()  
                #matching with the poped element 
                if parenthesis[i] != top:
                    x = False   
                    break

        # At end stack must be empty
        if check:
            x = False

        return x

