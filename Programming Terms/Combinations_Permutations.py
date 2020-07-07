
import itertools as itr

ls = [1, 2, 3]

# Combinations, the order does not matter

comb = itr.combinations(ls, 3)  # Checking how many groups of 3 they are

for c in comb:
    print(c)  # Output: (1, 2, 3)

comb = itr.combinations(ls, 2)  # Checking how many groups of 2 they are

for c in comb:
    print(c)  # Output:
                    # (1, 2)
                    # (1, 3)
                    # (2, 3)

# Permutations, the order does matter

prm = itr.permutations(ls, 3)

for p in prm:
    print(p)  # Output:
                    # (1, 2, 3)
                    # (1, 3, 2)
                    # (2, 1, 3)
                    # (2, 3, 1)
                    # (3, 1, 2)
                    # (3, 2, 1)

prm = itr.permutations(ls, 2)

for p in prm:
    print(p)  # Output:
                    # (1, 2)
                    # (1, 3)
                    # (2, 1)
                    # (2, 3)
                    # (3, 1)
                    # (3, 2)

################################################################################

m_list = [1, 2, 3, 4, 5, 6, 7]

# Calculating all the possible combinations that the sum results to 10
comb = itr.combinations(m_list, 3)

print([result for result in comb if sum(result) == 10])

################################################################################

word = 'possibility'

letters = 'yosipisblti'

# Calculating the possibility of a combination to be the same as our word
perm = itr.permutations(letters, 11)

for p in perm:
    if "".join(p) == word:
        print('Match found!!')
        break
else:
    print('No match found')
