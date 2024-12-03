# 성적이 낮은 순서로 학생 출력하기

N = int(input())
student = []
for _ in range(N):
    name, score = input().split()
    student.append((name,score))
student.sort(key=lambda x : x[1])

for i in range(N):
    print(student[i][0],end=' ')