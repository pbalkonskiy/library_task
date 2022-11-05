from FileFinder import FileFinder


def call_menu() -> str:
    string_to_find = input("Enter the text fragment:\n> ")
    print("Fragment entered:")
    print(string_to_find, end="\n\n")
    return string_to_find


if __name__ == "__main__":
    fragment = call_menu()

    finder = FileFinder(fragment)
    files, lines, amount = finder.go_through_lib()
    list_of_matches = list(zip(files, lines))

    print(f"Found {amount} coincidences.")
    for filename, line in list_of_matches:
        print(filename, f"- in line {line}")
