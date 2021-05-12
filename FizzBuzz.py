# FizzBuzz問題のPythonの解法例
"""
1から100までの数をプリントするプログラム

ただし3の倍数のときは数の代わりに「Fizz」と、

5の倍数のときは「Buzz」とプリントし、

3と5両方の倍数のときは「FizzBuzz」とプリントすること
"""
count = 0
for i in range(100):
	count += 1
	if (count % 3 == 0) and (count % 5 == 0):
		print("FizzBuzz")
		continue
	if count % 3 == 0:
		print("Fizz")
		continue
	if count % 5 == 0:
		print("Buzz")
		continue
	else:
		print(count)