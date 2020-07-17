import math

# BETTER IDEA: HAVE AN OPERATIONS ARRAY THAT I ITERATE THROUGH

# negatives out the front

def parse(nums):

    if "," in nums:
        nums.replace(" ", "")
        nums = nums.split(",")
    else:
        nums = nums.split()

    # args given like "1234", so split would be ["1234"]
    if len(nums) == 1:
        if len(nums[0]) != 4:
            return False, 0, 0, 0, 0
        else:
            try:
                return True, int(nums[0][0]), int(nums[0][1]), int(nums[0][2]), int(nums[0][3])
            except:
                return False, 0, 0, 0, 0

    elif len(nums) == 4:
        try:
            return True, int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])
        except:
            return False, 0, 0, 0, 0

    else:
        return False, 0, 0, 0, 0

def solve(a, b, c, d):

    # a . b . c . d
    sitch_a(None, [a, b, c, d], None)

    # a . (b . c) . d
    sitch_b(None, [a, (b+c), d], "(" + str(b) + " + " + str(c) + ")")
    sitch_b(None, [a, (b*c), d], "(" + str(b) + " x " + str(c) + ")")
    sitch_b(None, [a, (b-c), d], "(" + str(b) + " - " + str(c) + ")")
    if c != 0:
        sitch_b(None, [a, (b/c), d], "(" + str(b) + " / " + str(c) + ")")

    # a . b . (c . d)
    sitch_c(None, [a, b, (c+d)], "",  "(" + str(c) + " + " + str(d) + ")")
    sitch_c(None, [a, b, (c*d)], "", "(" + str(c) + " x " + str(d) + ")")
    sitch_c(None, [a, b, (c-d)], "", "(" + str(c) + " - " + str(d) + ")")
    # if c != 0:
    #     sitch_c(None, [a, (b/c), d], "(" + str(b) + " / " + str(c) + ")")

    # a . ((b . c) . d)
    sitch_d(None, [a, (b+c), d], "(" + str(b) + " + " + str(c) + ")")
    sitch_d(None, [a, (b*c), d], "(" + str(b) + " x " + str(c) + ")")
    sitch_d(None, [a, (b-c), d], "(" + str(b) + " - " + str(c) + ")")
    # if c != 0:
    #     sitch_d(None, [a, (b/c), d], "(" + str(b) + " / " + str(c) + ")")

    return

# a . b . c . d
def sitch_a(ans, nums, string):

    if len(nums) == 0:
        if ans == 10:
            print("Solution a: " + string)

    elif len(nums) == 4:
        sitch_a(nums[0]+nums[1], nums[2:], str(nums[0]) + " + " + str(nums[1]))
        sitch_a(nums[0]*nums[1], nums[2:], str(nums[0]) + " x " + str(nums[1]))
        sitch_a(nums[0]-nums[1], nums[2:], str(nums[0]) + " - " + str(nums[1]))

        if nums[1] != 0:
            sitch_a(nums[0]/nums[1], nums[2:], str(nums[0]) + " / " + str(nums[1]))

    else:
        sitch_a(ans+nums[0], nums[1:], string + " + " + str(nums[0]))
        sitch_a(ans*nums[0], nums[1:], string + " x " + str(nums[0]))
        sitch_a(ans-nums[0], nums[1:], string + " - " + str(nums[0]))

        if nums[0] != 0:
            sitch_a(ans/nums[0], nums[1:], string + " / " + str(nums[0]))


# a . (b . c) . d
def sitch_b(ans, nums, string):

    if len(nums) == 0:
        if ans == 10:
            print("Solution b: " + string)

    elif len(nums) == 3:
        sitch_b(nums[0]+nums[1], nums[2:], str(nums[0]) + " + " + string)
        sitch_b(nums[0]*nums[1], nums[2:], str(nums[0]) + " x " + string)
        sitch_b(nums[0]-nums[1], nums[2:], str(nums[0]) + " - " + string)

        if nums[1] != 0:
            sitch_b(nums[0]/nums[1], nums[2:], str(nums[0]) + " / " + str(nums[1]))

    else:
        sitch_b(ans+nums[0], [], string + " + " + str(nums[0]))
        sitch_b(ans*nums[0], [], string + " x " + str(nums[0]))
        sitch_b(ans-nums[0], [], string + " - " + str(nums[0]))

        if nums[0] != 0:
            sitch_b(ans/nums[0], [], string + " / " + str(nums[0]))

# a . b . (c . d)
def sitch_c(ans, nums, beg_string, end_string):

    if len(nums) == 0:
        if ans == 10:
            print("Solution c: " + end_string)

    elif len(nums) == 3:
        sitch_c(nums[0]+nums[1], nums[2:], str(nums[0]) + " + " + str(nums[1]), end_string)
        sitch_c(nums[0]*nums[1], nums[2:], str(nums[0]) + " x " + str(nums[1]), end_string)
        sitch_c(nums[0]-nums[1], nums[2:], str(nums[0]) + " - " + str(nums[1]), end_string)

    else:
        sitch_c(ans+nums[0], nums[1:], "", beg_string + " + " + end_string)
        sitch_c(ans*nums[0], nums[1:], "", beg_string + " x " + end_string)
        sitch_c(ans-nums[0], nums[1:], "", beg_string + " - " + end_string)

# a . ((b . c) . d)
def sitch_d(ans, nums, string):

    if len(nums) == 0:
        if ans == 10:
            print("Solution d: " + string)

    elif len(nums) == 3:
        sitch_d(nums[1]+nums[2], nums[:2], "(" + string + " + " + str(nums[2]) + ")")
        sitch_d(nums[1]*nums[2], nums[:2], "(" + string + " x " + str(nums[2]) + ")")
        sitch_d(nums[1]-nums[2], nums[:2], "(" + string + " - " + str(nums[2]) + ")")

    else:
        sitch_d(ans+nums[0], [], str(nums[0]) + " + " + string)
        sitch_d(ans*nums[0], [], str(nums[0]) + " x " + string)
        sitch_d(ans-nums[0], [], str(nums[0]) + " - " + string)


def main():
    print("""Operators in use:
    + = addition
    x = multiplication
    - = subtraction
    / = division
    ^ = to the power of (a^b = a to the power of b)
    """)
    # // = floor division
    # \\\\ = ceiling division
    # a^1/b = the bth root of a
    # """)
    done_parsing = False
    while not done_parsing:
        nums = input("Enter four numbers: ")
        done_parsing, a, b, c, d = parse(nums)
        if not done_parsing:
            print("\nInvalid arguments. Please try again.\n")

    print()
    solve(a, b, c, d)

if __name__=="__main__":
    main()
