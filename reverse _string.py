


string = input("Enter some string:")
def reverseSting(text):
    index = -1
    for i in range(len(text) - 1, int(len(text) / 2), -1):
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text

string = reverse . string(list(string))
print("output string:", "".join(string))
