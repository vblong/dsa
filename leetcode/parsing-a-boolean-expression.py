class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for char in expression:
            if char == '(':
                st.append(char)
            elif char == ',':
                continue
            elif char == 'f' or char == 't':
                st.append(True if char == 't' else False)
            elif char == ')':
                components = []
                while st:
                    last = st.pop()
                    if last == '(':
                        break
                    components.append(last)
                logic = st.pop()
                print('do logic', logic, 'on', components)
                value = components[0]
                if logic == '!': 
                    value = not components[0]
                for val in components:
                    if logic == '|':
                        value = value | val
                    elif logic == '&':
                        value = value & val
                print('results:', value)
                st.append(value)
                print('now st is', st)
            else:
                st.append(char)
        return st[0]


expression = "&(|(f))" # False
# expression = "|(f,f,f,t)" # True
expression = "!(&(f,t))" # True
print(Solution().parseBoolExpr(expression))