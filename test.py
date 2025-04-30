from add import generate_captcha, verify_captcha

def test_generate_captcha_length():
    captcha = generate_captcha()
    assert len(captcha) == 6

def test_verify_captcha():
    captcha = "abc123"
    assert verify_captcha("abc123", captcha) == True
    assert verify_captcha("ABC123", captcha) == False  # case-sensitive
