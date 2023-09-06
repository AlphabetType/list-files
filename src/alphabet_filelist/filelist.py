from pathlib import Path


def list_files(folderpath: Path, extensions):
    filelist = []
    for path in folderpath.iterdir():
        if path.is_file() and path.suffix in extensions:
            filelist.append(path)

    return filelist


def validate_folderpath(path_as_string):
    fp = Path(path_as_string)
    if fp.is_dir():
        return fp
    else:
        print(f"Folderpath not found: {path_as_string}")
        return None


def validate_extensions(extensions):
    valid_extensions = []
    for extension in extensions:
        if not extension.startswith("."):
            print(f"Ignoring extension: {extension} -- Doesn't start with a dot (.)")
        else:
            valid_extensions.append(extension)
    return valid_extensions


def print_filepaths(filelist):
    if len(filelist) == 0:
        print("No files found with the provided extension.")
    else:
        for fp in filelist:
            print(fp)


def print_extensions(extensions):
    print(f"Looking for files with extension: {', '.join(extensions)}")


def print_folderpath(fp):
    print(f"Looking in path: {fp.resolve()}")
