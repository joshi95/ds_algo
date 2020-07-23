def F(str, idx, res):

    if idx == len(str):
        print(res)
        return  
    F(str, idx + 1, res) #skipping the character
    F(str, idx + 1, res + str[idx]) # taking the character

if __name__ == '__main__':
    F("ABC", 0, "")

