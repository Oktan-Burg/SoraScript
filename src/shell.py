from classLib import lexer
while True:
    line = input("sora: ")
    lexerResult = lexer.run(line)
    if lexerResult.error:
        print(lexerResult)
    else: print("worked")