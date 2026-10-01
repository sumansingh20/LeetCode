class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        
        for x in s:
            if x=='(' or x=='[' or x=='{':
                a.append(x)
            else:
                if not a:
                    return False
                y=a.pop()
                if x==')' and y!='(':
                    return False
                if x==']' and y!='[':
                    return False
                if x=='}' and y!='{':
                    return False
        
        return len(a)==0