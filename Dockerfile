# Używamy oficjalnego obrazu Pythona jako bazy
FROM python:3.9

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Kopiowanie pliku hello.py do katalogu /app w kontenerze
COPY hello.py /app/

# Przejście do katalogu roboczego
WORKDIR /app

# Komenda uruchamiająca skrypt Pythona
CMD ["python", "hello.py"]
