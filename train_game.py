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

def main():
    nums = input("Print nums, space separated: ").split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    d = int(nums[3])
    generate(a, b, c, d)

if __name__=="__main__":
    main()
