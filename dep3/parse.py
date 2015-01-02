


def get_headers(fileobj):
    data = {}
    last = None

    for line in fileobj.readlines():
        line = line.decode('utf-8')

        if line.startswith("diff"):
            break

        line = line.rstrip()
        if line == "":
            break

        if line.rstrip() == " .":
            data[last] += "\n"
            continue

        if line.startswith(" "):
            if last is None:
                break

            data[last] += line.strip() + "\n"
            continue

        if ":" not in line:
            break

        last, value = line.split(":", 1)
        value = value.strip()
        data[last] = value

    if None in data:
        data.pop(None)
    return data
