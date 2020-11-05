class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        initial = [0, 0]
        direction = {'N': [0, 1], 'S': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
        Ldirec = {'L': 'S', 'N': 'L', 'S': 'R', 'R': 'N'}
        Rdirec = {'L': 'N', 'N': 'R', 'S': 'L', 'R': 'S'}
        cur = 'N'
        for i in range(len(instructions)):
            if instructions[i] == 'G':
                initial[0] += direction[cur][0]
                initial[1] += direction[cur][1]
            else:
                print(initial)
                if instructions[i] == 'L':
                    cur = Ldirec[cur]
                else:
                    cur = Rdirec[cur]

        if not cur == 'N' or initial == [0, 0]:
            return True
        else:
            return False
