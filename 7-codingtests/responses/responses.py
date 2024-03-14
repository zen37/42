
def getWrongAnswers(N: int, C: str) -> str:
    answers = ""
    for i in range(N):
        answer = "B" if C[i] == "A" else "A"
        answers += answer

    return answers


n = 3
c = "ABA"

result = getWrongAnswers(n, c)
print(result)