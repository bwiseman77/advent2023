file = open('./input').read().splitlines()
sum = 0
word_bank = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine": "9"}

for line in file: 
    print("-----------------")
    print(line)
    first_word = ""
    last_word = ""
    first_digit = None
    last_digit = None
    length = len(line)
    for i in range(length):
        if(first_digit == None):
            if(first_digit!=None):
                break
            else:
                for key in word_bank:
                    if ((key in first_word)):
                        print(word_bank[key])
                        first_digit = word_bank[key]
                        break
                if (line[i].isdigit() and first_digit==None):
                    first_digit = line[i]
                    break
                if(first_digit == None):
                    first_word += line[i]
    for i in range(length):
        if(last_digit!=None):
            break
        else:
            for key in word_bank:
                if (key in last_word):
                    last_digit = word_bank[key]
                    break
            if (line[length-1-i].isdigit() and last_digit==None):
                last_digit = line[length-1-i]
                break
            if(last_digit == None):
                last_word = line[length-1-i] + last_word
                continue
    print("digits: ",first_digit, last_digit)
    sum+= int(first_digit+last_digit)
    print(sum)

print("sum: ",sum)
