import re


class Challenge_1:
    
    def textToNum(self, text):
        text = text.lower()
        newText = ""
        i = 0
        prevNum = False

        while i < len(text):
            if text[i : i + 3] == "one":
                newText += "1"
                i += 2
                prevNum = True
            elif text[i : i + 3] == "two":
                newText += "2"
                i += 2
                prevNum = True
            elif text[i : i + 5] == "three":
                newText += "3"
                i += 4
                prevNum = True
            elif text[i : i + 4] == "four":
                newText += "4"
                i += 3
                prevNum = True
                prevNum = True
            elif text[i : i + 4] == "five":
                newText += "5"
                i += 3
                prevNum = True
            elif text[i : i + 3] == "six":
                newText += "6"
                i += 2
                prevNum = True
            elif text[i : i + 5] == "seven":
                newText += "7"
                i += 4
                prevNum = True
            elif text[i : i + 5] == "eight":
                newText += "8"
                i += 4
                prevNum = True
            elif text[i : i + 4] == "nine":
                newText += "9"
                i += 3
                prevNum = True
            else:
                if prevNum is False:
                    newText += text[i] 
                else:
                    prevNum = False
                i += 1

        return newText
    
    def removeLetters(self, text):
        sub = re.sub(r"[a-zA-Z]", "", text)
        first = sub[0]
        last = sub[-1]
        num = int(f"{first}{last}")
        return num
    

    def challenge_1(self, fileName="input_1.txt"):
        counter = 0
        with open(fileName, "r") as f:
            for line in f:
                line = line.strip()
                first = None
                last = None
                if line:
                    sub = re.sub(r"[a-zA-Z]", "", line)
                    first = sub[0]
                    last = sub[-1]
                    num = int(f"{first}{last}")
                    print(f"{line} - {sub} = {num}")
                    counter += num
        print("counter: ", counter)
        return counter

    def challenge_2(self, fileName="AdventOfCode/2023/inputs/input_1.txt"):
        counter = 0
        with open(fileName, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    convertedString = self.textToNum(line)
                    num = self.removeLetters(convertedString)
                    print(f"{line} -> {convertedString} = {num}")
                    counter += num
        return counter


if __name__ == "__main__":
    challenge = Challenge_1()

    # challenge.challenge_1()
    counter_2 = challenge.challenge_2()
    print("counter 2: ", counter_2)
