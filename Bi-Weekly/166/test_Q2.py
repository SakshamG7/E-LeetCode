from Q2_2 import Solution

sol = Solution()

def test_1():
    case = sol.climbStairs(4, [1, 2, 3, 4])
    return case == 13, case

def test_2():
    case = sol.climbStairs(23, [5,22,27,7,7,3,21,20,27,21,20,4,11,16,18,16,4,26,15,3,15,6,17])
    return case == 149, case

def test_3():
    case = sol.climbStairs(32, [18,25,3,5,8,7,24,26,8,2,3,19,37,4,6,31,14,12,17,4,24,14,37,3,20,23,16,29,6,31,8,20])
    return case == 190, case

def main():
    print(test_1())
    print(test_2())
    print(test_3())

if __name__ == "__main__":
    main()