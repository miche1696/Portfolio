class Solution:

# Second solution, optimized
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        toReturn = set()
        p = []
        n = []
        z = []
        for x in nums:
            if(x>0):
                p.append(x)
            elif (x==0):
                z.append(x)
            else:
                n.append(x)

        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1*num in N:
                    toReturn.add((-1*num, 0, num))

        if (z):
            if len(z)>2:
                toReturn.add((0,0,0))


        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if -1*(p[i]+p[j]) in n:
                    toReturn.add(tuple(sorted([p[i],p[j],(-1*(p[i]+p[j]))])))

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if -1*(n[i]+n[j]) in p:
                    toReturn.add(tuple(sorted([n[i],n[j],(-1*(n[i]+n[j]))])))
        
        return toReturn


""" First Solution not optimized

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        toReturnVec = []
        toReturnVecSet = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for y in range(j+1,len(nums)):
                    if ((nums[i]+nums[j]+nums[y])==0):
                        # check if the triplet is already present
                        if({nums[i],nums[j],nums[y]} not in toReturnVecSet):
                            toReturnVec.append([nums[i],nums[j],nums[y]])
                            toReturnVecSet.append({nums[i],nums[j],nums[y]})
        return toReturnVec

i = 0 --> 3
j = 1 --> -1
y = 2 -->
[ 3,0,-2,-1, 1, 2]
[ 0,0, 0, 0, 1, 1]
"""


