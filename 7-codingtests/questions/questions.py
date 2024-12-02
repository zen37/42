
def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
    x = ""
    for i in range(N):
        y = "B" if C[i] == "A" else "A"
        x += y

    return x


n = 3
c = "ABA"

result = getWrongAnswers(n, c)
print(result)