string = "()(()"
stack = []
index = 0
for i in range(len(string)):
    if string[i] == '(':
        if len(stack) <= 0:
            index = i
        stack.append(string[i])
    if string[i] == ')':
        if len(stack) <= 0:
            index = i
            stack.append(')')
            break
        stack.pop()
if len(stack) > 0:
    print("Индекс выпадающего элемента =", index)
else:
    print("Всё ок")