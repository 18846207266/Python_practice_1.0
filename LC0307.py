class Solution:
    def twoSum(self,nums,target):
        global i,j
        """
        :type nums: List[int]

        :type target: int

        :rtype: List[int]

        """
        for i in range(0,len(nums)-1):
            
            for j in range(i+1,len(nums)):
                if int(nums[i])+int(nums[j]) ==int(target):
                    return [i,j]

n=input()
num=n.strip('[]')
nums=num.split(',')
target=input()
final = Solution()#注意这里的空括号

print(final.twoSum(nums,target))#注意这里的（）要写入变量


