import collections.abc
import datetime
import pathlib
import unittest.mock

import pytest
from src.io_ops import (
    create_directories,
    delete_directory,
    generate_file_hash,
    list_directory,
    validate_file_hash,
    validate_file_size,
)

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources


def mock_directory(
    exist: bool = True, childrens: collections.abc.Iterator = iter(())
) -> unittest.mock.Mock:
    mock = unittest.mock.Mock(spec=pathlib.Path)
    mock.exists.return_value = exist
    mock.is_dir.return_value = True
    mock.is_file.return_value = False
    mock.iterdir.return_value = childrens

    return mock


def mock_directories(total: int = 1, **kwargs) -> list[unittest.mock.Mock]:
    mocks = [mock_directory(**kwargs) for i in range(total)]

    return mocks


def mock_file(exist: bool = True, st_size: int = 1024) -> unittest.mock.Mock:
    mock = unittest.mock.Mock(spec=pathlib.Path)
    mock.exists.return_value = exist
    mock.is_dir.return_value = False
    mock.is_file.return_value = True
    mock.stat.return_value.st_size = st_size

    return mock


def mock_files(total: int = 1, **kwargs) -> list[unittest.mock.Mock]:
    mocks = [mock_file(**kwargs) for i in range(total)]

    return mocks


def _childrens():
    yield from [
        mock_directory(),
        mock_file(),
        mock_file(),
        mock_directory(),
        mock_file(),
    ]


# endregion: Mocked resources

# region: PyTest parametrized variables
create_directories_happy = [(dict(directories=mock_directories(3)))]

delete_directory_happy = [
    (dict(directory=mock_directory(), recursive=True)),
    (dict(directory=mock_directory(), recursive=False)),
    (dict(directory=mock_directory())),
]
delete_directory_sad = [
    (
        dict(directory=mock_directory(False), recursive=True),
        dict(
            exception_type=AssertionError,
            exception_message=f"Invalid directory path",
        ),
    ),
    (
        dict(directory=mock_file(True), recursive=True),
        dict(
            exception_type=AssertionError,
            exception_message=f"Invalid directory path",
        ),
    ),
]

list_directory_happy = [
    (
        dict(
            directory=mock_directory(childrens=_childrens()),
            is_file=True,
        )
    ),
    (
        dict(
            directory=mock_directory(childrens=_childrens()),
            is_file=False,
        )
    ),
    (
        dict(
            directory=mock_directory(childrens=_childrens()),
        )
    ),
]
list_directory_sad = [
    (
        dict(
            directory=mock_directory(False),
            is_file=True,
        ),
        dict(
            exception_type=AssertionError,
            exception_message=f"Invalid directory path",
        ),
    ),
    (
        dict(
            directory=mock_file(True),
            is_file=True,
        ),
        dict(
            exception_type=AssertionError,
            exception_message=f"Invalid directory path",
        ),
    ),
]

validate_file_size_happy = [
    (
        dict(
            source=mock_file(),
            lower_bound=512,
            upper_bound=2048,
        ),
        dict(result=True),
    ),
    (
        dict(
            source=mock_file(),
            lower_bound=2048,
            upper_bound=4096,
        ),
        dict(result=False),
    ),
]
validate_file_size_sad = [
    (
        dict(
            source=mock_file(),
            lower_bound=4096,
            upper_bound=256,
        ),
        dict(
            exception_type=AssertionError,
            exception_message=(
                f"Value of lower bound range cannot be greater "
                f"than or equal to value of upper bound range"
            ),
        ),
    ),
    (
        dict(
            source=mock_directory(),
            lower_bound=128,
            upper_bound=256,
        ),
        dict(
            exception_type=AssertionError,
            exception_message=(
                f"Source path is referring to a directory, please "
                f"provide a source path that leads to a file"
            ),
        ),
    ),
]

generate_file_hash_happy = [
    (
        dict(
            source=mock_file(),
            algorithm="md5",
            text="J92mcMpESqWbiP$F",
        ),
        dict(result="91777a7557772d0cda0cb772961198aa"),
    ),
    (
        dict(
            source=mock_file(),
            algorithm="sha256",
            text="5dTsbUXM9KpvY~$^",
        ),
        dict(result="c93b9390d897dc1f5ef3b0950311a96ae22c9185402b509d0aab5d9551346882"),
    ),
]
generate_file_hash_sad = [
    (
        dict(
            source=mock_file(),
            algorithm="sha512",
            text="mu5q3$5HE#h#qmQj",
        ),
        dict(
            result="da2794cc681ad27d7325045c0a48941d36fe0bd94d8d6747404d4990d5c9d96d045e16dc253a1496be375781c858b0f051c78b931880d4ae4084eb8bfeecd9ac",
            exception_type=AssertionError,
            exception_message=f"Unsupported hash algorithm",
        ),
    ),
    (
        dict(
            source=mock_directory(),
            algorithm="sha256",
            text="@zn@Fo`V2CVT%K3S",
        ),
        dict(
            result="ceb9fb9796b0d7c7bb822039a312cd0ebdefbf53ab12097f77a16000adb4d0a5",
            exception_type=AssertionError,
            exception_message=f"Invalid source path",
        ),
    ),
]

validate_file_hash_happy = [
    (
        dict(
            _hash="d67d458aa1460d49f3ea15f0c5574234acdbdbaae774dceda8d0dd8602becc61",
            source=mock_file(),
            algorithm="sha256",
            text="h@7szVAUpf9^b@ES",
        ),
        dict(result=True),
    ),
    (
        dict(
            _hash="cb5e8b5409fb353fde644017fd694959",
            source=mock_file(),
            algorithm="md5",
            text="S9ftQaVPjTz&7YN5",
        ),
        dict(
            result=True,
        ),
    ),
    (
        dict(
            _hash="ceac42abcd46db4aee968d74427c3d69e27cb879e5f1351d5df7c49342a4a02c",
            source=mock_file(),
            algorithm="sha256",
            text="x&DhYR~3u4d`vnLK",
        ),
        dict(result=False),
    ),
]


# endregion: PyTest parametrized variables


class TestIOOps:
    @pytest.mark.parametrize("payload", create_directories_happy)
    def test_happy_create_directories(self, payload):
        create_directories(**payload)

        [directory.mkdir.assert_called() for directory in payload["directories"]]

    @pytest.mark.parametrize("payload", delete_directory_happy)
    def test_happy_delete_directory(self, payload):
        delete_directory(**payload)

        payload["directory"].exists.assert_called_once()
        payload["directory"].is_dir.assert_called_once()

        if payload.get("recursive") == True:
            payload["directory"].iterdir.assert_called_once()
        else:
            payload["directory"].unlink.assert_called()

    @pytest.mark.parametrize("payload, expect", delete_directory_sad)
    def test_sad_delete_directory(self, payload, expect):
        with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
            delete_directory(**payload)

    @pytest.mark.parametrize("payload", list_directory_happy)
    def test_happy_list_directory(self, payload):
        results = list_directory(**payload)

        assert isinstance(results, collections.abc.Iterator)

        results = list(results)

        if payload.get("is_file") == True:
            for item in results:
                assert item.is_file()

        elif payload.get("is_file") == False:
            for item in results:
                assert item.is_dir()

        else:
            for item in results:
                assert item.is_file() or item.is_dir()

    @pytest.mark.parametrize("payload, expect", list_directory_sad)
    def test_sad_list_directory(self, payload, expect):
        with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
            results = list_directory(**payload)

            results = list(results)

    @pytest.mark.parametrize("payload, expect", validate_file_size_happy)
    def test_happy_validate_file_size(self, payload, expect):
        results = validate_file_size(**payload)

        assert results == expect["result"]

    @pytest.mark.parametrize("payload, expect", validate_file_size_sad)
    def test_sad_validate_file_size(self, payload, expect):
        with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
            results = validate_file_size(**payload)

    @pytest.mark.parametrize("payload, expect", generate_file_hash_happy)
    def test_happy_generate_file_hash(self, payload, expect):
        text = payload.pop("text").encode("utf-8")

        with unittest.mock.patch(
            "builtins.open", unittest.mock.mock_open(read_data=text)
        ) as mocked_file:
            result = generate_file_hash(**payload)

            assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", generate_file_hash_sad)
    def test_sad_generate_file_hash(self, payload, expect):
        text = payload.pop("text").encode("utf-8")

        with unittest.mock.patch(
            "builtins.open", unittest.mock.mock_open(read_data=text)
        ) as mocked_file:
            with pytest.raises(
                expect["exception_type"], match=expect["exception_message"]
            ):
                result = generate_file_hash(**payload)

    @pytest.mark.parametrize("payload, expect", validate_file_hash_happy)
    def test_happy_validate_file_hash(self, payload, expect):
        text = payload.pop("text").encode("utf-8")

        with unittest.mock.patch(
            "builtins.open", unittest.mock.mock_open(read_data=text)
        ) as mocked_file:
            result = validate_file_hash(**payload)

            assert result == expect["result"]
