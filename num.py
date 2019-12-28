import math

class Num:
    def __init__(self, a, b, c, d):
        self.nums = [b, c, d]
        self.solutions = []
        self.generate(a, self.nums, str(a)) # always starts with "a"
        # self.generate(self.parenthesize(), str(a))

    # works out solutions with parentheses
    def parenthesize(self):

        # a (b c) d
        # a b (c d)
        # (a b) (c d)

        # x (y z)

        return

    # works out solutions
    # to do the ones that dont use the next value, simply delete the number after they have used it because theyve changed the value and thats what matters
    def generate(self, value, nums, path):

        # if no more nums left to evaluate
        if len(nums) == 0:

            if value == 10:
                # solution found
                self.solutions.append(path)

            else:
                # no solution found
                return

        else:
            div = False
            fac = False

            v1 = value + nums[0]
            v2 = value - nums[0]
            v3 = value * nums[0]
            if nums[0] != 0:
                v4 = value / nums[0]
            #     v5 = value // nums[0]
            #     v6 = math.ceil(value / nums[0])
            #     v7 = value**(1/float(nums[0])) # nth root
            #     div = True
            # v8 = value ** nums[0]

            # because these solutions don't use the next value, they will recur forever. I think its silly (and should be against the rules) to have something do !! or root(root(... so I stop their recursion after one usage of these ops.
            # if it > 0:
            #     # ops that don't use the next value
            #     v9 = math.sqrt(value)
            #     if type(value) == int:
            #         v10 = math.factorial(value)
            #         fac = True
            #     v11 = abs(value)
            #     v12 = math.ceil(value)
            #     v13 = math.floor(value)
            #
            #     self.generate(v9, nums, path+"^(1/2)", it+1)
            #     if fac:
            #         self.generate(v10, nums, path+"!", it+1)
            #     self.generate(v11, nums, path[:len(path)-1]+"abs("+str(nums[0])+")", it+1)
            #     self.generate(v12, nums, path[:len(path)-1]+"ceil("+str(nums[0])+")", it+1)
            #     self.generate(v13, nums, path[:len(path)-1]+"floor("+str(nums[0])+")", it+1)

            self.generate(v1, nums[1:], path+" + "+str(nums[0]))
            self.generate(v2, nums[1:], path+" - "+str(nums[0]))
            self.generate(v3, nums[1:], path+" x "+str(nums[0]))
            if div:
                self.generate(v4, nums[1:], path+" / "+str(nums[0]))
            #     self.generate(v5, nums, path+" // "+str(n), 0)
            #     self.generate(v6, nums, path+" ceil/ "+str(n), 0)
            #     self.generate(v7, nums, path+"^(1/"+str(n)+") ", 0)
            # self.generate(v8, nums, path+"**"+str(n), 0)


    def get_solutions(self):
        return self.solutions
