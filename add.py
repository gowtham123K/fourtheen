import random
import string

def generate_captcha(length=6):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

def verify_captcha(actual_captcha, user_input):
    return actual_captcha == user_input
