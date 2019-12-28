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

# if numbers are going to be factorialed on their own before being added, they need this to be done in a separate situation. If the result of two numbers is going to be factorialed, this is done inside the existing situations. 
def solve(a, b, c, d):

    sitch_a(None, [a, b, c, d], None)
    sitch_b(None, [a, (b+c), d], "(" + str(b) + " + " + str(c) + ")")
    sitch_b(None, [a, (b*c), d], "(" + str(b) + " x " + str(c) + ")")
    sitch_b(None, [a, (b-c), d], "(" + str(b) + " - " + str(c) + ")")

    return

# a . b . c . d
# doesn't do division yet
def sitch_a(ans, nums, string):

    if len(nums) == 0:
        if ans == 10:
            print("Solution: " + string)

    elif len(nums) == 4:
        sitch_a(nums[0]+nums[1], nums[2:], str(nums[0]) + " + " + str(nums[1]))
        sitch_a(nums[0]*nums[1], nums[2:], str(nums[0]) + " x " + str(nums[1]))
        sitch_a(nums[0]-nums[1], nums[2:], str(nums[0]) + " - " + str(nums[1]))

    else:
        sitch_a(ans+nums[0], nums[1:], string + " + " + str(nums[0]))
        sitch_a(ans*nums[0], nums[1:], string + " x " + str(nums[0]))
        sitch_a(ans-nums[0], nums[1:], string + " - " + str(nums[0]))

# a . (b . c) . d
def sitch_b(ans, nums, string):

    if len(nums) == 0:
        if ans == 10:
            print("Solution: " + string)

    elif len(nums) == 3:
        sitch_b(nums[0]+nums[1], nums[2:], str(nums[0]) + " + " + string)
        sitch_b(nums[0]*nums[1], nums[2:], str(nums[0]) + " x " + string)
        sitch_b(nums[0]-nums[1], nums[2:], str(nums[0]) + " - " + string)

    else:
        sitch_b(ans+nums[0], nums[1:], string + " + " + str(nums[0]))
        sitch_b(ans*nums[0], nums[1:], string + " x " + str(nums[0]))
        sitch_b(ans-nums[0], nums[1:], string + " - " + str(nums[0]))


# a . b . (c . d)
def sitch_c(ans, nums, string):
    pass

def main():
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
