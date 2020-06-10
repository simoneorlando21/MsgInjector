def inject_msg(path, message):
    file = open(path, "ab")
    file.write(message)
