


def get_headers(fileobj):
    data = {}
    last = None

    for line in fileobj.readlines():
        if line.startswith("diff"):
            break

        line = line.rstrip()
        if line == "":
            break

        if line.rstrip() == " .":
            data[last] += "\n"
            continue

        if line.startswith(" "):
            data[last] += line.strip() + "\n"
            continue

        last, value = line.split(":", 1)
        value = value.strip()
        data[last] = value
    return data
