import sys


def main(first_ip: str, second_ip: str):
    """
    Main function to control the script process
    :param first_ip: The first IP address
    :param second_ip: The second IP address
    :return:
    """
    if not validate_ip4v_address(first_ip):
        sys.exit()
    if not validate_ip4v_address(second_ip):
        sys.exit()
    if not compare_ipv4_address(first_ip, second_ip):
        sys.exit()

    print(f"Result: {second_ip} - {first_ip} = {difference_ipv4_address(first_ip, second_ip)}")


def validate_ip4v_address(ip):
    """
    Validates the IPv4 address
    :param ip: The IP address that should be validated
    :return: Returns True if valid, otherwise False
    :rtype: logical
    """
    parts = ip.split(".")

    if len(parts) == 4 and all(isinstance(int(part), int) and -1 < int(part) < 256 for part in parts):
        print(f"IPv4 address {ip} is valid")
        return True
    print(f"IPv4 address {ip} is not valid")
    return False


def compare_ipv4_address(ip_first, ip_second):
    """
    Compares two IP addresses, if the second one is bigger returns True, otherwise False
    :param ip_first: First IP address for compare
    :param ip_second: Second IP address for compare
    :return: Returns True if Second IP address is bigger, otherwise False
    :rtype: logical
    """
    first_ip_parts = ip_first.split(".")
    second_ip_parts = ip_second.split(".")

    if int(second_ip_parts[0]) > int(first_ip_parts[0]):
        return True
    elif int(second_ip_parts[0]) == int(first_ip_parts[0]):
        if int(second_ip_parts[1]) > int(first_ip_parts[1]):
            return True
        elif int(second_ip_parts[1]) == int(first_ip_parts[1]):
            if int(second_ip_parts[2]) > int(first_ip_parts[2]):
                return True
            elif int(second_ip_parts[2]) == int(first_ip_parts[2]):
                if int(second_ip_parts[3]) > int(first_ip_parts[3]):
                    return True
    print("Second IP address is not bigger than first IP address.")
    return False


def difference_ipv4_address(ip_first, ip_second):
    """
    Calculates the difference between two IP addresses
    :param ip_first: First IP address
    :param ip_second: Second IP address
    :return: Returns and integer that represents the difference of IP addresses
    :rtype: int
    """
    first_ip_parts = ip_first.split(".")
    second_ip_parts = ip_second.split(".")

    first_part = (int(second_ip_parts[0]) - int(first_ip_parts[0])) * 256 * 256 * 256
    second_part = (int(second_ip_parts[1]) - int(first_ip_parts[1])) * 256 * 256
    third_part = (int(second_ip_parts[2]) - int(first_ip_parts[2])) * 256
    fourth_part = int(second_ip_parts[3]) - int(first_ip_parts[3])

    return first_part + second_part + third_part + fourth_part


if __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2])
    except ValueError:
        print("Incorrect format of IP address")
    except IndexError:
        print("Please specify the IP addresses")
