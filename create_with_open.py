"""
create_with_open.py
Example showing how to create a file using Python's open() function.
"""

def create_file(path: str, content: str) -> None:
    """Create or overwrite `path` with `content` using open()."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> None:
    out_path = "created_by_open.txt"
    text = (
        "This file was created using Python open() from create_with_open.py\n"
        "Feel free to modify the script to change the filename or content.\n"
    )
    create_file(out_path, text)
    print(f"Created file: {out_path}")


if __name__ == "__main__":
    main()
