a = '735+*3-*'

def is_operand(i):
    b = (i=='0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i== '7' or i =='8' or i =='9')
    if b:
        return True
    else:
        return False


def is_operator(i):
    return i == '+' or i == '-' or i == '/' or i == '*'


def create_expression(a):
    expression = []
    need_operand = True # if true, need operand, if false, need operator
    for i in a:
        if need_operand == True:
            if is_operand(i):
                expression.append(i)
                need_operand = False
        elif need_operand == False:
            if is_operator(i):
                expression.append(i)
                need_operand=True
    if is_operator(a[-1]):
        del expression[-1]
    expression = ''.join(expression)
    return expression


print(a)
print(create_expression(a))



def get_3_items(expression):
    eval3 = []
    eval3.append(expression[0:3])
    x = eval[(eval3[0])
    print x

def get_2_items(expression):
    eval2 = []
    for n in range(3, len(expression), 2):
        eval2.append(expression[n:n+2])
    return eval2


def evaluate_expression(expression):
    evaluate_list = get_3_items(expression) + get_2_items(expression)
    
    return evaluate_list

expression = create_expression(a)
get_3_items(expression)