def arithmetic_arranger(problems, state = False):
    
    # if length of the problems more than 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # if wrong operator
    if wrongOp(problems) is True:
        return "Error: Operator must be '+' or '-'."

    # if wrong digit
    if wrongDigit(problems) is True:
        return "Error: Numbers must only contain digits."
    
 

    # split numbers, operators and get answers 
    first_number, second_number, operations, answers = splitOperations(problems)

    # Check numbers length
    for i in range(len(first_number)):
        if len(first_number[i]) > 4 or len(second_number[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Get the problem format 
    lines = getFormat(first_number, second_number, operations, answers)
    
    # Combine lines
    arranged_problems = lines[0] + '\n' + lines[1] + '\n' + lines[2]
    if state is True:
        arranged_problems += '\n' + lines[3]

    return arranged_problems


def wrongOp(problems):
    # Check for '*' and '/' in all strings
    for problem in problems:
        for char in problem:
            if char == '*' or char == '/':
                return True


def wrongDigit(problems):
    # check if the number is not numeric, '+' or '-'
    for problem in problems:
        for char in problem:
            if not(char.isnumeric() or char == '+' or char == '-' or char == ' '):
                return True


def splitOperations(problems):
    first_number = []
    second_number = []
    operations =  []
    answers = []

    for problem in problems:
        num1 = ""
        num2 = ""
        op = ""
        getOp = False

        for x in problem:
            if x != " ":
                if getOp is True:
                    num2 += x
                else:
                    if x == '+' or x == '-':
                        op = x
                        getOp = True
                    else:
                        num1 += x


        first_number.append(num1)
        second_number.append(num2)
        operations.append(op)
        answer = 0

        if op == '+':
            answer = int(num1) + int(num2)
        else:
            answer = int(num1) - int(num2)
        
        answers.append(str(answer))

    return first_number, second_number, operations, answers


def getFormat(first_number, second_number, operations, answers):
    f_str = ""
    s_str = ""
    d_str = ""
    a_str = ""

    for i in range(len(first_number)):
        
        l = max(len(first_number[i]), len(second_number[i])) + 2
        f_str += " " * (l - len(first_number[i])) + first_number[i]
        s_str += operations[i] + " " * (l - len(second_number[i]) - 1) + second_number[i]
        d_str += "-" * l
        a_str += " " * (l - len(answers[i])) + answers[i]

        if i < len(first_number) - 1:
            f_str += ' ' * 4
            s_str += ' ' * 4
            d_str += ' ' * 4
            a_str += ' ' * 4

    return f_str, s_str, d_str, a_str