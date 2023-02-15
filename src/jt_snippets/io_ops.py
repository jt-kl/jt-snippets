import hashlib
from collections.abc import Iterator
from datetime import datetime
from pathlib import Path
from typing import Optional, Union
from zipfile import ZIP_DEFLATED, ZipFile

# region: Validators


def validate_file_hash(
    _hash: str,
    path: Path,
    algorithm: str = "md5",
) -> bool:
    """
    Helper method to validate a file hash

    Args:
        hash: Hash value to validate against
        path: Source file path to generate hash
        algorithM: Hashing algorithm to use. Example: "md5", "sha256"
    """
    return _hash == generate_file_hash(path, algorithm)


def validate_path_exists(
    path: Path,
):
    """
    Validates path exists

    Args:
        path: Path to be validated
    """
    if not path.exists():
        raise Exception(f"Path doesn't exists.")


def validate_is_directory(
    path: Path,
):
    """
    Validates path is directory

    Args:
        path: Path to be validated
    """
    if not path.is_dir():
        raise Exception(f"Path is not a directory.")


def validate_is_file(
    path: Path,
):
    """
    Validates path is file

    Args:
        path: Path to be validated
    """
    if not path.is_file():
        raise Exception(f"Path is not a file.")


def validate_file_size(
    path: Path,
    lower_bound: int,
    upper_bound: int,
) -> bool:
    """
    Helper method to validate file size between specified ranges

    Args:
        path: Source file path to be validated
        lower_bound: Acceptable lower bound range of file size in bytes
        upper_bound: Acceptable upper bound range of file size in bytes
    """
    validate_is_file(path)

    if lower_bound >= upper_bound:
        raise ValueError(
            f"Value of lower bound range cannot be greater " f"than or equal to value of upper bound range"
        )

    return lower_bound < path.stat().st_size < upper_bound


# endregion: Validators


def create_directories(
    paths: list[Path],
    **kwargs,
):
    """
    Helper method to create a collection of directories

    Args:
        paths: Collection of directory paths to be created
    """
    [
        path.mkdir(
            parents=True,
            exist_ok=True,
            **kwargs,
        )
        for path in paths
    ]


def delete_directory(
    path: Path,
    recursive: bool = False,
):
    """
    Helper method to delete directory and its contents

    Args:
        path: Directory path to be deleted
        recursive: Recursively deletes child directories and its contents
    """
    # Deletes the only directory in the current directory
    if all(
        (
            path.is_dir(),
            not recursive,
            not len(list(path.iterdir())),
        ),
    ):
        path.rmdir()

        return

    # Deletes only files in the current directory
    if all(
        (
            path.is_dir(),
            not recursive,
            len(list(path.iterdir())),
        ),
    ):
        [_path.unlink(missing_ok=True) for _path in path.iterdir() if _path.is_file()]

        return

    # Deletes both files and directory in the current directory recursivley
    if all(
        (
            path.is_dir(),
            recursive,
            len(list(path.iterdir())),
        )
    ):
        for _path in path.glob("**"):
            if _path.is_file():
                _path.unlink(missing_ok=True)

            elif _path.is_dir():
                delete_directory(_path, recursive)


def list_directory(
    path: Path,
    is_file: Optional[bool] = None,
) -> Iterator:
    """
    Helper method to list contents of a directory

    Args:
        path: Directory path to be iterated
        is_file: Return files, directories or both in results
    """
    for item in path.iterdir():
        if is_file is not None:
            if is_file and item.is_file():
                yield item
            if not is_file and item.is_dir():
                yield item
        else:
            yield item


def generate_file_hash(
    path: Path,
    algorithm: str = "md5",
) -> str:
    """
    Generate a unique hash value from a given file path

    Args:
        path: Source file path to generate hash
        algorithM: Hashing algorithm to use. Example: "md5", "sha256"
    """
    if algorithm not in ["md5", "sha256"]:
        raise Exception(f"Unsupported hash algorithm")

    hasher = hashlib.new(algorithm)

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def archive_items(
    source: Path,
    destination: Path,
    validate: bool = True,
):
    """
    Archive items into a ZIP file

    Args:
        source: Source item to archive (Directory/File)
        destination: Destination to output archive file
    """
    paths = list()

    if source.is_file():
        paths.append(source)

    if source.is_dir():
        paths = [i for i in sorted(source.rglob("*"))]

    with ZipFile(destination, "w") as archive:
        for i in paths:
            archive.write(
                filename=i,
                arcname=i.relative_to(source.parent),
                compress_type=ZIP_DEFLATED,
            )

    if validate:
        with ZipFile(destination, "r") as archive:
            if archive.testzip():
                raise Exception(f"Invalid archive")
