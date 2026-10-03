"""Greet tool — SHS-Agent E2E (v4.4.0)."""


def greet(name):
    """Return a greeting string for the given name."""
    return f'Hello, {name} from SHS-Agent!'


if __name__ == '__main__':
    print(greet('world'))
