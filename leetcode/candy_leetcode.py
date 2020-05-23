# leetcode problem # 1431 ids with the Greatest number of candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

candies = [2, 3, 5, 1, 3]
extra_candies = 3
greatest_amount_of_candies = candies[0]
kid_with_most_candy = None
greatest_amount_of_candies_boolean = []

# determine which kid has the greatest amount of candies
for h, i in enumerate(candies):
    # assign kid[h] with the greatest_amount_candy title
    if i > greatest_amount_of_candies:
        greatest_amount_of_candies = i
        kid_with_most_candy = h

    # if each kid where given 3 extra pieces of candy would they have the most candy or be tied for the most
    if i + extra_candies >= greatest_amount_of_candies:
        print(f"If kid {h} receives Extra Candy he could have the most candy")
        greatest_amount_of_candies_boolean.append(True)
    else:
        greatest_amount_of_candies_boolean.append(False)

print(f"Kid {kid_with_most_candy} has {greatest_amount_of_candies} pieces of candy which is the most .")
print(greatest_amount_of_candies_boolean)








