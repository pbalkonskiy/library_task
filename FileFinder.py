import os
from FragmentSeeker import FragmentSeeker


class FileFinder:
    def __init__(self, fragment: str) -> None:
        self.__PATH = "/home/pbalkonskiy/Projects/python/library_repo/library"
        self.__fragment = fragment
        self.__files_counter = 0
        self.__set_of_files = set()
        self.__list_of_lines = list()

    def go_through_lib(self) -> tuple[list, list, int]:
        files = sorted(sorted(os.listdir(self.__PATH)))
        for file in files:
            if file:
                is_equal, filename, linenum = FragmentSeeker.check_file(file, self.__fragment)
                if is_equal:
                    self.__files_counter += 1
                    self.__set_of_files.add(filename)
                    self.__list_of_lines.append(linenum)

        return list(self.__set_of_files), self.__list_of_lines, self.__files_counter
