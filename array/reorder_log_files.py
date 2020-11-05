class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
       l = []
       n = []
       for i in logs:
            splitted = i.split()
            if splitted[1].isnumeric():
                n.append(i)
            else:
                l.append(i)
        return sorted(l, key=lambda x: [' '.join(x.split()[1:]), x.split()[0]]) + n
