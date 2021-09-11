def pig_it(text):
    pig = text.split()
    for i in range(len(pig)):
        if pig[i].isalpha():
            pig[i] = pig[i][1:] + pig[i][0] + "ay"
            
    pig = " ".join(pig)
    return pig