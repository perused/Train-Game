from num import Num

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

    sitch_a([a, b, c, d])

    return

# a . b . c . d
def sitch_a(nums):
   
     

    return 

def combine(x, y):

    return x + y

# a . (b . c) . d
#def sitch_b(a, b, c, d):

def main():
    done_parsing = False
    while not done_parsing:
        nums = input("Enter four numbers: ")
        done_parsing, a, b, c, d = parse(nums)
        if not done_parsing:
            print("\nInvalid arguments. Please try again.\n")

    solve(a, b, c, d)

if __name__=="__main__":
    main()
