def arithmetic_arranger(problems, show_answers=False): 
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # ✅ Formatting goes here (not inside validation!)
        width = max(len(operand1), len(operand2)) + 2

        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers.append(answer.rjust(width))

    # ✅ After the loop is finished, join everything
    arranged = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )

    if show_answers:
        arranged += '\n' + '    '.join(answers)

    return arranged

# Example run
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
