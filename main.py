ip = input().strip()
parts = ip.split(".")
if len(parts) != 4:
    print("Invalid IP address")
else:
    valid = True
    for p in parts:
        if not p.isdigit():
            valid = False
            break
        num = int(p)
        if num < 0 or num > 255:
            valid = False
            break
    if valid:
        print("Valid IP address")
    else:
        print("Invalid IP address")
