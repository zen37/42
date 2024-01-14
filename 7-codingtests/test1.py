
dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}

numbers  = [1, 2, 3, 4, 5]

def solution(D, S):

    if D not in numbers:
        return f"Error: {D} is not in {numbers}"

    if S not in dict:
        return f"Error: {S} is not in {dict}"

    return D * dict[S]



result = solution(1, "five")
print(result)