import random
import countinv
import naive_countinv
import sys
import time

class Tester():
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def run(self):
		while (self.a < self.b):
			A = []
			while (len(A) < self.a):
				A.append(random.randint(0, self.c))
			self.a += 1

			# print A
			start_time = time.time()
			r1 = naive_countinv.naive_count_inv(A)
			naive_total_time = time.time() - start_time

			start_time = time.time()
			r2 = countinv.count_inv(A)
			total_time = time.time() - start_time
			values = [self.a, naive_total_time, total_time]

			# print A
			# print(r1, r2)
			if (r1 != r2):
				print('FML!')
				return

			print('\t'.join(map(str, values)))

if __name__ == '__main__':
	test = Tester(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
	test.run()
