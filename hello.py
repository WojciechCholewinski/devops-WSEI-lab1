import redis
import os

# Pobranie adresu hosta Redis z zmiennej środowiskowej
redis_host = os.getenv("REDIS_HOST", "localhost")

# Łączenie z Redisem
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# Zwiększ licznik uruchomień
r.incr('counter')

# Pobierz wartość countera
count = r.get('counter')

print(f"Hello World! This script has been run {count} times")
