import argparse

from alphabet_filelist.filelist import (
    list_files,
    print_extensions,
    print_filepaths,
    print_folderpath,
    validate_extensions,
    validate_folderpath,
)

FILTER_EXTENSIONS = [
    ".otf",
    ".ttf",
    ".woff",
    ".woff2",
    ".ufo",
]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folderpath",
        nargs="?",
        default=".",
        help="Folder Path",
    )
    parser.add_argument(
        "-e",
        "--extensions",
        nargs="*",
        default=FILTER_EXTENSIONS,
        help="File Extensions. Default: %(default)s",
    )
    args = parser.parse_args()

    return args


def main():
    args = parse_arguments()
    folderpath = args.folderpath
    extensions = args.extensions
    valid_folderpath = validate_folderpath(folderpath)
    valid_extensions = validate_extensions(extensions)
    if valid_folderpath and valid_extensions:
        filelist = list_files(valid_folderpath, valid_extensions)
        print_extensions(valid_extensions)
        print_folderpath(valid_folderpath)
        print_filepaths(filelist)


if __name__ == "__main__":
    main()
