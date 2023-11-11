import os
import markdown

class Console:
    def __init__(self):
        self.name = 'markdown'

    def isAvailable(self, userInput):
        if len(userInput) != 4: return False
        if userInput[1] != 'markdown': return False
        if not os.path.isfile(userInput[2]): return False
        if userInput[2] == userInput[3]: return False

        return True
    
    def parseInput(self, userInput):
        if not self.isAvailable(userInput):
            print("your command is not available.")
            return
        
        input = userInput[2]
        output = userInput[3]
        contents = ""

        with open(input, "r") as f:
            contents = f.read()

        with open(output, 'w') as f:
            conversion = markdown.markdown(contents, extensions=['extra', 'sane_lists'])
            f.write(conversion)


