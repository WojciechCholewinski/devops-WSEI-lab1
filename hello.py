import redis
import os
import time

# Pobranie adresu hosta Redis z zmiennej środowiskowej
redis_host = os.getenv("REDIS_HOST", "127.0.0.1")

# Łączenie z Redisem
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

while True:

	# Zwiększ licznik uruchomień
	r.incr('counter')

	# Pobierz wartość countera
	count = r.get('counter')

	print(f"Hello World! This script has been run {count} times")

	time.sleep(5)
