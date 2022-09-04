import collections.abc
import hashlib
import pathlib
import typing


def create_directories(
    directories: list[pathlib.Path],
):
    """
    Helper method to create a collection of directories

    Args:
        directories: Collection of directories to be created
    """
    [directory.mkdir(parents=True, exist_ok=True) for directory in directories]


def delete_directory(
    directory: pathlib.Path,
    recursive: bool = False,
):
    """
    Delete directory and its contents

    Args:
        directory: Directory path to be deleted
        recursive: Recursively deletes child directories
    """
    assert directory.exists(), f"Invalid directory path"
    assert directory.is_dir(), f"Invalid directory path"

    if not recursive:
        directory.unlink()

        return

    for item in directory.iterdir():
        if item and item.is_dir():
            delete_directory(item, recursive)
        else:
            item.unlink(missing_ok=True)


def list_directory(
    directory: pathlib.Path,
    is_file: typing.Union[bool, None] = None,
) -> collections.abc.Iterator:
    """
    List contents of directory

    Args:
        directory: Directory path to be iterated
        is_file: Return files, directories or both in results
    """
    assert directory.exists(), f"Invalid directory path"
    assert directory.is_dir(), f"Invalid directory path"

    for item in directory.iterdir():
        if is_file is not None:
            if is_file and item.is_file():
                yield item
            if not is_file and item.is_dir():
                yield item
        else:
            yield item


def validate_file_size(
    source: pathlib.Path,
    lower_bound: int,
    upper_bound: int,
) -> bool:
    """
    Validate file size is between specified ranges

    Args:
        source: Source file path to be validated
        lower_bound: Acceptable lower bound range of file size in bytes
        upper_bound: Acceptable upper bound range of file size in bytes
    """
    assert not lower_bound >= upper_bound, (
        f"Value of lower bound range cannot be greater "
        f"than or equal to value of upper bound range"
    )
    assert source.is_file(), (
        f"Source path is referring to a directory, please "
        f"provide a source path that leads to a file"
    )

    return lower_bound < source.stat().st_size < upper_bound


def generate_file_hash(
    source: pathlib.Path,
    algorithm: str = "md5",
) -> str:
    """
    Generate a unique hash value from a given file path

    Args:
        source: Source file path to generate hash
        algorithM: Hashing algorithm to use. Example: "md5", "sha256"
    """
    assert source.is_file(), f"Invalid source path"
    assert algorithm in ["md5", "sha256"], f"Unsupported hash algorithm"

    hasher = hashlib.new(algorithm)

    with open(source, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def validate_file_hash(
    _hash: str,
    source: pathlib.Path,
    algorithm: str = "md5",
) -> bool:
    """
    Validate hash of a file

    Args:
        hash: Hash value to validate against
        source: Source file path to generate hash
        algorithM: Hashing algorithm to use. Example: "md5", "sha256"
    """
    return _hash == generate_file_hash(source, algorithm)
