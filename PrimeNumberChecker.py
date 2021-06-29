# inputされた数字が素数かどうか調べる
import math

def isPrime(x):
	#整数xが素数かどうかを判定する
	if x < 2: return False #2未満に素数はないため
	if x == 2 or x == 3 or x == 5 :return True #2,3,5は素数
	if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 : return False # 2,3,5 の倍数は合成数

	# 試し割り : 疑似素数(2,3,5 でも割り切れない数字)で割っていく
	prime = 7
	step = 4
	while prime <= math.sqrt(x):
		if x % prime == 0: return False
		prime += step
		step = 6 - step
	return True

inputNumber = input('値を入力 : ')

if isPrime(int(inputNumber)):
	print( inputNumber + 'は素数です')
else:
	print(inputNumber + "は素数ではありません")