known_primes = []

for candidate in range(2, 100):

	is_prime = True
	for d in known_primes:
		if candidate % d == 0:
			is_prime = False
			break
		if d > candidate**0.5:
			break

	if is_prime:
		print(candidate)
		known_primes.append(candidate)
