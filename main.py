ballanced = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']

unballanced = ['}{}', '{{[(])]}}', '[[{())}]']

vspom = {'(': ')', '[': ']', '{': '}'}


class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check_ballance(item):
    stack = Stack()
    for item_ in item:
        if item_ in vspom:
            stack.push(item_)
        elif item_ == vspom.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()


for item in ballanced + unballanced:
    value = check_ballance(item)
    if value == True:
        name = 'Сбалансированный'
    else:
        name = 'Не сбалансированный'
    print(f'{item}         {name}')
