def rand_strings_generator(length):
    import random
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),.<>?/"
    if length:
        randString = "".join(random.choice(chars) for _ in range(length))
        return randString
    else:
        return 