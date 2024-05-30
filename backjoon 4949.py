while(True):
    str_ = input()
    
    stack = []
    
    if str_ == '.':
        break 

    for i in str_:
        if i=='(' or i=='[': 
            stack.append(i)
        elif i==')': 
            if stack and stack[-1]=='(': 
                stack.pop()
            else: 
                stack.append(i)
                break
        elif i==']': 
            if stack and stack[-1]=='[': 
                stack.pop()
            else:
                stack.append(i)
                break

    if stack:
        print('no')
    else: 
        print('yes')
