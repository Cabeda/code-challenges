def getIndexOfCode(unique_length: int) -> int:
    is_first = True
    for index in range(0, len(chars) - unique_length):
        if len(set(chars[index : index + unique_length])) == unique_length and is_first:

            print(chars[index : index + unique_length])
            print(index + unique_length)
            is_first = False


start_msg_code = 4
msg_code = 14
with open("input_6.txt", "r") as f:
    line = f.readlines()[0]

    chars = [*line.strip()]

    # getIndexOfCode(start_msg_code)
    getIndexOfCode(msg_code)