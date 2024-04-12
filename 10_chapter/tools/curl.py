from shlex import quote


def to_curl(request) -> str:
    """
    Request对象转curl命令
    :param request: request 对象
    """
    parts = [
        ('curl', None),
        ('-X', request.method),
    ]

    for key, value in sorted(request.headers.items()):
        parts += [('-H', f'{key}: {value}')]

    if request.body:
        body = request.body
        if isinstance(body, bytes):
            body = body.decode('utf-8')
        parts += [('-d', body)]

    parts += [(None, request.url)]

    flat_parts = []
    for key, value in parts:
        if key:
            flat_parts.append(quote(key))
        if value:
            flat_parts.append(quote(value))

    return ' '.join(flat_parts)
