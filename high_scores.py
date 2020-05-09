import heapq

def check_ints(scores):
    """Helper function to check that list values are all integers"""
    if all(isinstance(x, int) for x in scores):
        return True
    else:
        return False

def latest(scores):
    """Takes list of scores and returns the last added score"""
    if check_ints(scores) == False or len(scores) == 0:
        raise Exception("Please enter valid integer scores.")
    elif check_ints(scores)==True:
        return (scores[len(scores) - 1])


def personal_best(scores):
    """Takes list of scores and returns the top score"""
    if check_ints(scores) == False or len(scores) == 0:
        raise Exception("Please enter valid integer scores.")
    elif check_ints(scores)==True:
        return max(scores)

def personal_top_three(scores):
    """Takes list of scores and returns the three highest scores"""
    if check_ints(scores) == False or len(scores) == 0:
        raise Exception("Please enter valid integer scores.")
    elif check_ints(scores)==True:
        return heapq.nlargest(3, scores)


# Test Cases:

# "normal input"
# print(check_ints([54, 64, 76]))
# print(latest([54, 64, 76]))
# print(personal_best([54, 64, 76, 65, 78]))
# print(personal_top_three([54, 64, 76, 65, 78]))

# "bad input"
# print(check_ints([54, 64, "a"]))
# print(latest([54, 64, "a"]))
# print(personal_top_three([54, 64, "a", 78, 65]))
# print(personal_best([54, 64, "a", 78, 65]))

# "edge case tests"
# print(latest([]))
# print(personal_best([]))
# print(personal_top_three([]))






