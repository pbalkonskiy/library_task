class FragmentSeeker:

    @staticmethod
    def check_file(filename: str, fragment: str) -> tuple[bool, str or None, int or None]:
        with open(f"library/{filename}", "r", encoding="windows-1251", errors="ignore") as file_obj:
            countline = 0
            while True:
                line = file_obj.readline()
                countline += 1
                if not line:
                    return False, None, None
                else:
                    if line.find(fragment) != -1:
                        return True, filename, countline
