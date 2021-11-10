n = input("Please enter the number of participants: ")
n = int(n)

scores = input()
scores = scores.split(" ")
scores = scores[0:n]

for i in range(n):
    scores[i] = int(scores[i])

unique_scores = set(scores)
unique_scores = list(unique_scores)
unique_scores.sort(reverse=True)
print(f"Runner up score: {unique_scores[1]}")


