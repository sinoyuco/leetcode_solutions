class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # i = 0
        # while i < len(asteroids)-1:
        #     if asteroids[i] > 0 and asteroids[i+1]<0:
        #         if abs(asteroids[i])>abs(asteroids[i+1]):
        #             asteroids.pop(i+1)
        #             i=max(0,i-1)
        #         elif abs(asteroids[i])<abs(asteroids[i+1]):
        #             asteroids.pop(i)
        #             i=max(0,i-1)
        #         else:
        #             asteroids = asteroids[:i]+asteroids[i+2:]
        #             i= max(0, i-2)
        #     else:
        #         i+=1
        # return asteroids
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                curr = stack.pop()
                if abs(a) == abs(curr):
                    break
                a = (curr + a) // abs(curr + a) * max(abs(curr), abs(a))
            else:
                stack.append(a)
        return stack
