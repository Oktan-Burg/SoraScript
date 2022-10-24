numbers = "0123456789"
odd_characters = "()-"
char = "abcdefghijklmnopqrstuvwxyz"
# error
class Error:
    def __init__(self, error = "", start_pos = 0, data="", segmentData = 0):
        self.error = error
        self.start_pos = start_pos
        someinfo = data[start_pos:].split(" ")
        self.end_pos = len(someinfo)
        self.errorsection = someinfo[0]
        self.segmentData = segmentData
class UnknownPrefixError(Error):
    def __init__(self, error, start_pos, data, segmentData):
        super().__init__(error, start_pos, data, segmentData)
        
    def __str__(self) -> str:
        return f"ERROR: {self.error}, Segment: '{self.errorsection}, Command_Pos: {self.segmentData}, Char: {self.start_pos} - {self.end_pos}'"
# lexer 


class Lexer:
    def __init__(self, data):
        self.data = data.replace("\n","")
        self.commandSegments = self.data.split(";")
        self.SegmentIndex = 0
    def functionTokenHandler(self, segment):
        commands = ["echo", "exit", "print", "input", "def", "advanced", "import"]
        if not commands[segment.prefix]:
            # UnknownPrefixError
            return False, UnknownPrefixError("UnknownPrefixError", segment.prefix[0], self.commandSegments[self.SegmentIndex], self.SegmentIndex)
        else: return segment, False
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
                self.functionTokenHandler({"args": segment[1:], "prefix": prefix, "commandSeg": self.SegmentIndex})
            self.SegmentIndex += 1
# execute
def run(data):
    lexer = Lexer(data)
    return lexer.segmentTokenCommissioner()