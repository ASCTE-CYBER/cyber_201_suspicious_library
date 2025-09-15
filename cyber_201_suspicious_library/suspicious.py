import getpass
import platform
import socket

def simple_addition(a, b):
    # Looks innocent: adds two numbers
    result = a + b

    # But secretly collects info
    user = getpass.getuser()
    computer = platform.node()
    os_name = platform.system()
    ip = socket.gethostbyname(socket.gethostname())

    # Pretend this would get sent out (but it never does!)
    collected = {
        "username": user,
        "computer": computer,
        "os": os_name,
        "ip": ip,
    }

    # A commented-out line to show “what a bad actor might do”
    # send_to_attacker(collected)

    # Still returns the correct addition result
    return result

def get_help():
    return "Nothing suspicious here... or is there? 👀"
