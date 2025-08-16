# BT1

"""stack = "MindX"

def is_epmty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
    

def output(stack):
    new_stack = []
    new_string = ""

    for i in stack:
        new_stack.append(i)

    
    while new_stack:
        new_string += new_stack.pop()

    return new_string

result = output(stack)
print(result)

# --------------------------------------------------CHỮA----------------------------------------------------- #

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)

    result = []
    while stack:
        # result.append(stack.pop())
        result += stack.pop()

    # return "".join(result) # "": string rỗng
    return result

print(reverse_string("MindX"))"""

#BT2

"""def is_valid_bracket_pairs(s):
    stack = []
    openning_brackets = '([{'
    closing_brackets = ')]}'
    bracket_pairs = {')' : '(', ']' : '[', '}' : '{'}

    for char in s:
        if char in openning_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
            
    return len(stack) == 0

print(is_valid_bracket_pairs("{[()]}"))
print(is_valid_bracket_pairs("{[(]]}"))"""


# BT3

from collections import deque
def ban_ve(ticket_stack, customer_queue):

    while ticket_stack and customer_queue:
        ticket_stack.pop()
        customer_queue.popleft()

    return len(ticket_stack), len(customer_queue)

tickets = ["A1", "A2", "A3"]
customers = deque(["An", "Khang", "Nam", "Minh", "Sơn", "Tuấn"])

ve_con, khach_con = ban_ve(tickets, customers)
print(f"Số vé còn lại là: {ve_con}")
print(f"Số khách còn lại : {khach_con}")