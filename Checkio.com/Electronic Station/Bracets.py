def checkio(expression):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = []
    for i in expression:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                print(False)
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else: 
                print(False)
    if len(stack) == 0:
        print(True)
    else:
        print(False)
    

checkio("(({[(((1)-2)+3)-3]/3}-3)")