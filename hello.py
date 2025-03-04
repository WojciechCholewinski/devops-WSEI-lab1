import redis

# Łączenie z Redisem
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# Zwiększ licznik uruchomień
r.incr('counter')

# Pobierz wartość countera
count = r.get('counter')

print(f"Hello World! This script has been run {count} times")
