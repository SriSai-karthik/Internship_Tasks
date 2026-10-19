# Q1. Find the Frequency of Each Word in a Sentence

def word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency



# Q2. Find the Frequency of Each Character in a Word

def character_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency




# Q3. Find the First Non-Repeating Character in a Word

def first_non_repeating(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in word:
        if frequency[char] == 1:
            return char

    return None




# Q4. Check Whether Two Strings Are Anagrams

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    frequency = {}

    for char in s1:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in s2:
        if char in frequency:
            frequency[char] -= 1
        else:
            return False

    for count in frequency.values():
        if count != 0:
            return False

    return True



# Q5. Find the First Repeating Character in a String

def first_repeating_char(word):
    seen = set()

    for char in word:
        if char in seen:
            return char
        seen.add(char)

    return None


# Q6. Move All Zeros to the End of a List

def move_zeros(nums):
    result = []

    for num in nums:
        if num != 0:
            result.append(num)

    zero_count = len(nums) - len(result)
    result.extend([0] * zero_count)

    return result



# Q7. Find the Second Highest Distinct Number in a List

def second_highest(nums):
    unique_nums = []

    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)

    if len(unique_nums) < 2:
        return None

    unique_nums.sort(reverse=True)

    return unique_nums[1]



# Q8. Remove Duplicates Without Changing the Original Order

def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result



# Q9. Find the Missing Number from 1 to N

def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum



# Q10. Find Two Numbers Whose Sum Equals a Target

def find_pair(nums, target):
    for j in range(1, len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []



# Q11. Find the Number Closest to Zero

def closest_to_zero(nums):
    return min(nums, key=lambda num: (abs(num), -num))



# Q12. Find Common Elements Between Two Lists

def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result



# Q13. Rotate a List to the Right by K Positions

def rotate_right(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    if k == 0:
        return nums[:]

    return nums[-k:] + nums[:-k]



# Q14. Find the Maximum Sum of Two Consecutive Elements

def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum



# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def all_pairs_target(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in pairs:
                    pairs.append(pair)

    pairs.sort()
    return pairs