import shutil
import os

def hcenter(text: str) -> str:
    width = shutil.get_terminal_size().columns
    return text.center(width)

def hcenter_block(lines: list[str]) -> list[str]:
    width = shutil.get_terminal_size().columns
    return [line.center(width) for line in lines]

def main():
    menu = [
        "[ tasks ]  [ finance ]  [ diary ]",
        "",
        "[ stats ]  [ workout ]  [ about ]",
        "",
        "[ q ] quit"
    ]

    os.system("clear")

    for line in hcenter_block(menu):
        print(line)

    choice = input("> ").strip().lower()

if __name__ == "__main__":
    main()

