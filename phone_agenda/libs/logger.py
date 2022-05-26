# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

from black import main


def log(msg, level):
    print("[", level, "]", msg)


def debug(msg):
    log(msg, "DEBUG")


def info(msg):
    log(msg, "INFO")


def warning(msg):
    log(msg, "WARNING")


def error(msg):
    log(msg, "ERROR")


def critical(msg):
    log(msg, "CRITICAL")

if __name__ == "__main__":
    print("From MODULE!!!!")