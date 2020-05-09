import heapq

def check_ints(scores):
    if all(isinstance(x, int) for x in scores):
        return True
    else:
        return False

def latest(scores):
    if check_ints(scores) == False or len(scores) == 0:
        raise Exception("Please enter valid integer scores.")
    elif check_ints(scores)==True:
        return (scores[len(scores) - 1])


def personal_best(scores):
    if check_ints(scores) == False or len(scores) == 0:
        raise Exception("Please enter valid integer scores.")
    elif check_ints(scores)==True:
        return max(scores)

def personal_top_three(scores):
    if check_ints(scores) == False or len(scores) == 0:
        raise Exception("Please enter valid integer scores.")
    elif check_ints(scores)==True:
        return heapq.nlargest(3, scores)


# Test Cases:
# "normal input"
# print(check_ints([54, 64, 76]))
# "non-integer input"
# print(check_ints([54, 64, "a"]))
# "normal input"
# print(latest([54, 64, 76]))
# "empty list"
# print(latest([]))
# "non-integer input"
# print(latest([54, 64, "a"]))
# "normal input"
# print(personal_top_three([54, 64, 76, 65, 78]))
# print(personal_top_three([]))
# "non-integer input"
# print(personal_top_three([54, 64, "a", 78, 65]))
# "normal input"
# print(personal_best([54, 64, 76, 65, 78]))
# "non-integer input"
# print(personal_best([54, 64, "a", 78, 65]))
# "empty list"
# print(personal_best([]))



