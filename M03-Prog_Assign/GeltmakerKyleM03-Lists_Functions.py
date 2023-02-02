# 7.4 - Create "things" list.
print("----7.4----")
things = ["mozzarella", "cinderella", "salmonella"]
print(things)
# 7.5 - Capitalize human name in list.
print("----7.5----")
things[1] = things[1].capitalize()
print(things)
# 7.6 - Uppercase word relate to cheese.
print("----7.6----")
things[0] = things[0].upper()
print(things)
# 7.7 - Remove disease variable and add "Nobel Prize" variable
print("----7.7----")
things.pop(2)
things.insert(2, "Nobel Prize")
print(things)
# 9.1 - Create function called "good".
print("----9.1----")
def good():
    student_list = ["Harry", "Ron", "Hermione"]
    print(student_list)

good()
# 9.2 - Create function called "get_odds".
print("----9.2----")
def get_odds():
    list = []
    for i in range(10):
        if i % 2 == 1:
            list.append(i)
    print(list[2])

get_odds()


