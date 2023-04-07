class Solution:
    def numberOfSteps(self, num: int) -> int:
        x,y=0,0
        while num: 
          x+=num%2
          y+=1
          num//=2
        return x+y-1 if x+y>0 else 0
       