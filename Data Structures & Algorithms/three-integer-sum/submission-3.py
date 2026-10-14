class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i,j=(0,len(nums)-1)
        tri=[]
        for i in range (len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            r=len(nums)-1
            j=i+1
            while j<r:
                sum=nums[i]+nums[j]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    j+=1
                else:
                    tri.append([nums[i],nums[j],nums[r]])
                    r-=1
                    j+=1
                    while j<r and nums[j]==nums[j-1]:
                        j+=1
                    while j<r and nums[r]==nums[r+1]:
                        r-=1
        return tri             
        