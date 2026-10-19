from solutions import word_frequency

# Q1. Find the Frequency of Each Word in a Sentence

# Q1 - Given test case
result1 = word_frequency("python is easy and python is powerful")
print("Q1 - Given test case:", result1)

# Q1 - Additional test case
result2 = word_frequency("cat dog cat")
print("Q1 - Additional test case:", result2)




# Q2. Find the Frequency of Each Character in a Word

from solutions import character_frequency

# Given test case
result1 = character_frequency("banana")
print("Q2 - Given test case:", result1)

# Additional test case
result2 = character_frequency("hello")
print("Q2 - Additional test case:", result2)




# Q3. Find the First Non-Repeating Character in a Word

from solutions import first_non_repeating

# Given test case
result1 = first_non_repeating("swiss")
print("Q3 - Given test case:", result1)

# Additional test case
result2 = first_non_repeating("aabb")
print("Q3 - Additional test case:", result2)




# Q4. Check Whether Two Strings Are Anagrams

from solutions import are_anagrams

# Given test case
result1 = are_anagrams("listen", "silent")
print("Q4 - Given test case:", result1)

# Additional test case
result2 = are_anagrams("hello", "world")
print("Q4 - Additional test case:", result2)



# Q5. Find the First Repeating Character in a String

from solutions import first_repeating_char

# Given test case
result1 = first_repeating_char("programming")
print("Q5 - Given test case:", result1)

# Additional test case
result2 = first_repeating_char("abcd")
print("Q5 - Additional test case:", result2)



# Q6. Move All Zeros to the End of a List

from solutions import move_zeros

# Given test case
result1 = move_zeros([0, 3, 0, 1, 2, 0, 4])
print("Q6 - Given test case:", result1)

# Additional test case
result2 = move_zeros([0, 5, 0, 2])
print("Q6 - Additional test case:", result2)



# Q7. Find the Second Highest Distinct Number in a List

from solutions import second_highest

# Given test case
result1 = second_highest([10, 20, 40, 30, 40, 20])
print("Q7 - Given test case:", result1)

# Additional test case
result2 = second_highest([5, 5, 3])
print("Q7 - Additional test case:", result2)



# Q8. Remove Duplicates Without Changing the Original Order

# Q8. Remove Duplicates Without Changing the Original Order

from solutions import remove_duplicates

# Given test case
result1 = remove_duplicates([4, 2, 4, 5, 2, 7, 5])
print("Q8 - Given test case:", result1)

# Additional test case
result2 = remove_duplicates([1, 1, 2, 3, 2])
print("Q8 - Additional test case:", result2)



# Q9. Find the Missing Number from 1 to N

from solutions import find_missing_number

# Given test case
result1 = find_missing_number([1, 2, 4, 5, 6], 6)
print("Q9 - Given test case:", result1)

# Additional test case
result2 = find_missing_number([1, 3, 4, 5], 5)
print("Q9 - Additional test case:", result2)



# Q10. Find Two Numbers Whose Sum Equals a Target

from solutions import find_pair

# Given test case
result1 = find_pair([2, 7, 11, 15], 9)
print("Q10 - Given test case:", result1)

# Additional test case
result2 = find_pair([1, 4, 6, 8], 10)
print("Q10 - Additional test case:", result2)



# Q11. Find the Number Closest to Zero

from solutions import closest_to_zero

# Given test case
result1 = closest_to_zero([-8, -3, 2, 5, -2])
print("Q11 - Given test case:", result1)

# Additional test case
result2 = closest_to_zero([-4, 4, -7])
print("Q11 - Additional test case:", result2)



# Q12. Find Common Elements Between Two Lists

from solutions import common_elements

# Given test case
result1 = common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
print("Q12 - Given test case:", result1)

# Additional test case
result2 = common_elements([4, 2, 4, 1], [1, 4, 5])
print("Q12 - Additional test case:", result2)



# Q13. Rotate a List to the Right by K Positions

from solutions import rotate_right

# Given test case
result1 = rotate_right([1, 2, 3, 4, 5], 2)
print("Q13 - Given test case:", result1)

# Additional test case
result2 = rotate_right([1, 2, 3], 1)
print("Q13 - Additional test case:", result2)



# Q14. Find the Maximum Sum of Two Consecutive Elements

from solutions import max_consecutive_sum

# Given test case
result1 = max_consecutive_sum([4, 7, 2, 9, 5])
print("Q14 - Given test case:", result1)

# Additional test case
result2 = max_consecutive_sum([1, 5, 2])
print("Q14 - Additional test case:", result2)



# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

from solutions import all_pairs_target

# Given test case
result1 = all_pairs_target([2, 4, 3, 5, 7, 8, 1], 9)
print("Q15 - Given test case:", result1)

# Additional test case
result2 = all_pairs_target([1, 2, 3, 4, 5], 6)
print("Q15 - Additional test case:", result2)
