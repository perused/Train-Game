from num import Num

def generate(a, b, c, d):
    item = Num(a, b, c, d)
    solutions = item.get_solutions()
    i = 0
    if len(solutions) == 0:
        print("No solutions found.")
    else:
        while i < len(solutions):
            print(f"Solution {i+1}: {solutions[i]}")
            i += 1

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

    return a, b, c, d 
    

def main():
    done_parsing = False
    while not done_parsing:
        nums = input("Enter four numbers: ")
        done_parsing, a, b, c, d = parse(nums)
        if not done_parsing:
            print("\nInvalid arguments. Please try again.\n")

    print(f"Nums are {a}, {b}, {c}, {d}")
    #generate(a, b, c, d)

if __name__=="__main__":
    main()
