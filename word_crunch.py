def word_crunch(str):

    if len(str) < 3:
        return str
    
    i = 0
    while i < len(str)-2:
        if str[i] == str[i+1] == str[i+2]:
            j = i
            while (j+1)<len(str) and str[j] == str[j+1]:
                j+=1
            str = str[:i]+str[(j+1):]

            if i-2 >= 0 and str[i-2]==str[i-1]:
                i = max(0, i-2)
            else:
                i = max(0, i-1) 
        else:
            i+=1
    return str


print(word_crunch('kabbbaa'))
print(word_crunch('abbbaa'))
print(word_crunch('abnnnnke'))
print(word_crunch('deeedbbcccbdaa'))

