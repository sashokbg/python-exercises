def dtb(decimal):
    
    finished = False
    result = ''

    while not finished:
        quotient = decimal // 2
        reminder = decimal % 2

        print('q {} r {}'.format(quotient, reminder))

        if quotient == 0:
            finished = True

        result = str(reminder)+result
        decimal = quotient

    print('Result {}'.format(result))

    return result

