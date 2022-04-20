from ipaddress import ip_address
import platform


def find_ips(start, end):
    start = ip_address(start)
    end = ip_address(end)
    result = []
    while start <= end:
        result.append(str(start))
        start += 1
    return result


def get_ping_cmd():
    oper = platform.system()
    if (oper == "Windows"):
        return "ping -n 1 "
    elif (oper == "Linux"):
        return "ping -c 1 "
    else:
        return "ping -c 1 "
