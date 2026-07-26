class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=1:
            return False
        total_sum = 1
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                total_sum +=i
                if i!= num // i:
                    total_sum += num // i
        return total_sum == num

if __name__ == "__main__":
    sol = Solution()
    test_cases = [28, 6, 496, 8128, 2, 7]
    for num in test_cases:
        print(f"checkPerfectNumber({num}) = {sol.checkPerfectNumber(num)}")