a = input()
b = input()
count = 0
i = 0
while i < len(a):
  if a[i:i+len(b)] == b:
    count += 1
    i += len(b)  # 찾았으므로 단어의 뒤 인덱스부터 다시 찾음
  else:
    i += 1
print(count)