'''
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([4, 30, 50])
Output:
    12,1

Input:
solution.solution([4, 17, 50])
Output:
    -1,-1

'''

from fractions import Fraction
pegs1 = [4, 30, 50]
pegs2 = [4, 17, 50]


def solution(pegs):
    n = len(pegs)

    '''
    # No empty array is being passed as a test case.
    # Number of pegs (n) is also always greater than 1,
    # as mentioned in the question.
    # Hence, the following if statement can be commented 
    # out.
    '''
    # if ((not pegs) or n == 1):
    #     return [-1,-1]

    total = pegs[0] + ((-1)**(n-1)) * pegs[n-1]
    frac = (-2.) / (3.)**((n-1) % 2)

    if n > 2:
        for i in range(1, n-1):
            sign = ((-1)**i)
            total += sign * 2 * pegs[i]

    # -------------------------------------------

    # limits denominator to 1000000
    r0 = Fraction(frac * total).limit_denominator()

    # radius of input gear has to be at least 2
    if r0 < 2:
        return [-1, -1]

    # -------------------------------------------

    curr_r = r0
    for i in range(0, n-1):
        # according to r0 + r1 = pegs[1] - pegs[0],
        rx = (pegs[i+1] - pegs[i]) - curr_r

        # radius of gear has to be at least 1
        if curr_r < 1 or rx < 1:
            return [-1, -1]
        else:
            curr_r = rx

    return [r0.numerator, r0.denominator]


print(not [])  # Outputs True
print(not pegs1)  # Outputs False
print(solution(pegs1))
print(solution(pegs2))
