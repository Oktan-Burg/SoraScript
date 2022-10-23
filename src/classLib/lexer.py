numbers = "0123456789"
odd_characters = "()"
char = "abcdefghijklmnopqrstuvwxyz"
# error
class Error:
    def __init__(self, error, start_pos, data):
        self.error = error
        self.start_pos = start_pos
        
# lexer 


class Lexer:
    def __init__(self, data):
        self.data = data.replace("\n","")
        self.commandSegments = self.data.split(";")
    
    def functionTokenHandler(self, segment):
        commands = ["echo", "exit", "print", "input", "def", "advanced", "import"]
        if not segment.prefix in commands:
            # UnknownPrefixError
            return  
    def segmentTokenCommissioner(self):
        for segment in self.commandSegments:
            prefix = None
            segmentType = None
            subSegment = segment.split(" ")
            if subSegment[0] in numbers or odd_characters :
                segmentType = "Equation"
            elif subSegment[0] in char and subSegment[0][1] in char and not "=*$%#&^/\-+|'" in subSegment[0] and not '"' in subSegment[0] and not "`" in subSegment[0]:
                segmentType = "Function"
                prefix = subSegment[0]
                self.functionTokenHandler({"args": segment[1:], "prefix": prefix})
            
            
            