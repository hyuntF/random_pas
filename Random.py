import random
import string

def generate_random_password(length=8):
    """Генерирует случайный пароль заданной длины"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Генерация случайного пароля длиной 10 символов
random_password = generate_random_password(10)
print("Случайный пароль:", random_password)
