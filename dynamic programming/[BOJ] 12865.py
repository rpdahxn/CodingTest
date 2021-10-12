N, K = map(int, input().split())

dict = {}

for i in range (N):
    w, v = map(int, input().split())
    dict[w] = v

sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
#print(sorted_dict)
max_val = 0

for value in sorted_dict.values():
    K -= value
    if (K < 0):
        break
    max_val += value


print(max_val)

https://ssooyn.tistory.com/19        <-참고