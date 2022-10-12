"""
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

Note:
    all strings appear to only be capital letters
    you can get letter score by subtracting ord('A') - 1
"""


# determine name value
def name_value(name):
    letter_list = [ord(c) for c in name]
    letter_score = [c - ord("A") + 1 for c in letter_list]
    return sum(letter_score)



# import txt file
with open(file="p022_names.txt", mode="r") as f:
    contents = f.read()
    name_list = contents.replace('"', '')
    name_list = name_list.split(",")
    # sort alphabetically
    name_list.sort()


tot_score = 0
for count, name in enumerate(name_list):
    # determine list position
    pos = count + 1
    # determine score
    score = pos * name_value(name)
    # add scores
    tot_score += score

print(tot_score)
