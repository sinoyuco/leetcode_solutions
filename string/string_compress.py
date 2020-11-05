from datetime import datetime
def string_compress(word):
    m = datetime.now()
    result = []
    # str2= ''
    i = 0
    while i < len(word):
        j = i+1
        while j < len(word) and word[i]==word[j]:
            j+=1
        result.append(word[i])
        result.append(str(j-i))
        # str2 += word[i] + str(j-i)
        i = j

    print(datetime.now() - m)
    return ''.join([i for i in result])
    # return str2


# print(string_compress('aabcccccaaa'))
# print(string_compress('aabcccccaaahhhhhhkkkkkkkaajjdddmnnskkkffdnnndddllvbbj'))
