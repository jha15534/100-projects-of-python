def calculate_love_score(name1, name2):
    # Convert both names to lowercase and combine them
    combined_names = (name1 + name2).lower()

    # Count the letters in "TRUE"
    t = combined_names.count('t')
    r = combined_names.count('r')
    u = combined_names.count('u')
    e = combined_names.count('e')
    true_score = t + r + u + e

    # Count the letters in "LOVE"
    l = combined_names.count('l')
    o = combined_names.count('o')
    v = combined_names.count('v')
    e2 = combined_names.count('e')  # Count again for love
    love_score = l + o + v + e2

    total_score = int(str(true_score) + str(love_score))

    print(total_score)

calculate_love_score("Shruti", "Ruby")
