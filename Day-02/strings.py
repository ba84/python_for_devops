number = "322"
word2 = "I am 32 years old"

def text(number,word2):
    if number in word2:
        return "The digits are in the text"
    else:
        return "WRONG WRONG WRONG!"
print(text(number,word2))