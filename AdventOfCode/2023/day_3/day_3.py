from dataclasses import dataclass
from re import search


@dataclass
class Num():
    line_num: int
    start: int
    num: str
    is_valid: bool = False
    is_gear: bool = False
    
class Challenge:

    def retrieve_nums_by_line(self, line_text, line_num):
        prev_num = False
        new_Num = None
        nums = []
        for i in range(len(line_text)):
            if search(r"\d", line_text[i]):
                if prev_num:
                    new_Num.num += line_text[i]
                else:
                    # Need to close the
                    new_Num = Num(line_num, i, line_text[i])
                    prev_num = True
                    nums.append(new_Num)
            else:
                prev_num = False
        return nums

    def check_number_symbol(self, nums, symbol, x, y):

        gears = []

        for num in nums:
            num_end = num.start + len(num.num) - 1
            if num.line_num == x and y-1 >= num.start and y-1 <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            elif num.line_num == x and y+1 >= num.start and y+1 <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            elif num.line_num == x-1 and y >= num.start and y <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            elif num.line_num == x+1 and y >= num.start and y <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            elif num.line_num == x-1 and y-1 >= num.start and y-1 <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            elif num.line_num == x-1 and y+1 >= num.start and y+1 <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            elif num.line_num == x+1 and y-1 >= num.start and y-1 <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            elif num.line_num == x+1 and y+1 >= num.start and y+1 <= num_end:
                num.is_valid = True
                if search(r"\*", symbol):
                    gears.append(num.num)
            
        if len(gears) == 2:
            return gears
        else:
            return None 
            

        



    def challenge_1(self, file_name="AdventOfCode/2023/day_3/input_test.txt"):
        nums = []
        gear_total = 0
        with open(file_name, "r") as f:
            line_num = 0
            for line in f:
                num = self.retrieve_nums_by_line(line, line_num)
                nums += num
                line_num += 1
            
        with open(file_name, "r") as f:
            line_num = 0
            for line in f:
                for i in range(len(line.strip())):
                    if search(r"\d|\.", line[i]):
                        pass
                    else:
                        gear = self.check_number_symbol(nums, line[i], line_num, i)
                        if gear is not None and len(gear) == 2:
                            gear_total += int(gear[0]) * int(gear[1])
                line_num += 1
        
        count = 0
        for num in nums:
            if num.is_valid:
                count += int(num.num)        
        print(count)
        print(f"Gear total: {gear_total}")

        return nums
            

if __name__ == "__main__":
    challenge = Challenge()
    challenge.challenge_1("AdventOfCode/2023/day_3/input.txt")