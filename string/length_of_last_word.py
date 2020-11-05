def lengthOfLastWord(s):
      a = s.split(' ')
       if len(a) < 1:
            return 0
        else:
            for i in range(len(a)-1, -1, -1):
                if len(a[i]) > 0:
                    return len(a[i])
            return 0
