# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

def log(msg, level):
    print("[", level, "]", msg)


def debug(msg):
    log(msg, "DEBUG")


def info(msg):
    log(msg, "INFO")



info("Start")