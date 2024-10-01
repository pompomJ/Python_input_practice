# 入力された3つの整数のうち、最大値を表示
nums = []

for n in range(3):
    data = int(input("{}個目の整数を入力してください >>".format(n + 1)))
    nums.append(data)

print(max(nums))
