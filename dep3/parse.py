


def get_headers(fileobj):
    data = {}
    last = None

    for line in fileobj.readlines():
        if line.startswith(b"diff"):
            break

        line = line.rstrip()
        if line == b"":
            break

        if line.rstrip() == b" .":
            data[last] += b"\n"
            continue

        if line.startswith(b" "):
            data[last] += line.strip() + b"\n"
            continue

        last, value = line.split(b":", 1)
        value = value.strip()
        data[last] = value
    return data
