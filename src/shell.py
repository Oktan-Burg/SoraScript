from classLib import lexer
while True:
    line = input("sora: ")
    tokens, error = lexer.run(line)
    if error:
        print(error)
    else: print("worked")