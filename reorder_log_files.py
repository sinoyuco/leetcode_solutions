class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        i = count = j = 0
        while i <= len(logs) and j <= len(logs)-1:
            splitted = logs[i].split()
            if splitted[1].isalpha():
                count+=1
                a = logs[i]
                del logs[i]
                logs.insert(0,a)
                i-=1
                j-=1
            i+=1
            j+=1
        return sorted(logs[:count], key=lambda x: x[5:])+logs[count:]
