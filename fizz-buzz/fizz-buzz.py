class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
    
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                char = "FizzBuzz"
            elif i % 3 == 0:
                char = "Fizz"
            elif i % 5 == 0:
                char = "Buzz"
            else:
                char = str(i)
            result.append(char)
        
        return result
       