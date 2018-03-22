def fizzbuzz():
	answer = ""
	for num in range(100):
		if(num % 3 == 0 and num % 5 == 0):
			answer + "FizzBuzz"
			print(num,"FizzBuzz")
		elif num % 3 == 0:
			answer + "Fizz"
			print (num,"Fizz")
		elif num % 5 == 0:
			print (num,"Buzz")
			answer + "Buzz"
	return answer

def main():
	answer = fizzbuzz()
	print (answer)

if __name__ == '__main__': main()
