"""
sample_script.py
A tiny example script created by GitHub Copilot.
"""

def greet(name: str) -> str:
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"


def main() -> None:
    name = input("Your name: ")
    print(greet(name))


if __name__ == "__main__":
    main()
