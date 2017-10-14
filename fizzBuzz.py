def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [str(x) if (x % 3 != 0 and x % 5 != 0) else (('Fizz' * (x % 3 == 0)) + ('Buzz' * (x % 5 == 0))) for x in range(1,n+1)]

print(fizzBuzz(15))
