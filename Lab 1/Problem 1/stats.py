"""
Problem: 

Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. The median is the number that
would appear at the midpoint of a list if it were sorted. The mode is the number that appears most frequently in the list. Define 
these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. 
Each function expects a list of numbers as an argument and returns a single number.
"""

def mean(nums): 
    """
    Returns the average of a set of numbers
    """
    try:
        return sum(nums) / len(nums)
    except Exception as e:
        print("Exception in Mean:", e)
        return None
    
def median(nums):
    """
    Returns the numbers at the midpoint of a sorted list
    """
    try:
        nums = sorted(nums)
        if len(nums) % 2 == 0: # Even number of items
            left = nums[(len(nums) // 2) - 1]     
            right = nums[len(nums) // 2]
            return (left + right) / 2
        elif len(nums) % 2 != 0: # Odd number of items
            return nums[len(nums) // 2] 
    except Exception as e:
        print("Exception in Median:",e)
        return None

def mode(nums):
    """
    Returns the number that appears most frequently in the list.
    """
    try:
        count_dic = {}
        for i in nums:
            count_dic[i] = count_dic.get(i,0) + 1 # add 1 to x's count in dictionary
        modes = []
        for num,count in count_dic.items():
            if count == max(count_dic.values()):
                modes.append(num)
        if len(modes) == len(nums):
            return []
        else:
            return modes
    except Exception as e:
        print("Exception in Mode",e)
        return None


