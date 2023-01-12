from collections.abc import Iterator
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional
from unittest.mock import Mock, mock_open, patch

import pytest

import jt_snippets.io_ops
from jt_snippets.io_ops import (
    create_directories,
    delete_directory,
    generate_file_hash,
    list_directory,
    suffix_datetime,
    validate_file_hash,
    validate_file_size,
)

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources


def mock_directory(
    exist: bool = True,
    childrens: Iterator = iter(()),
    side_effect: Optional[Callable] = None,
) -> Mock:
    mock = Mock(spec=Path)
    mock.exists.return_value = exist
    mock.is_dir.return_value = True
    mock.is_file.return_value = False
    mock.iterdir.return_value = childrens
    # mock.side_effect = side_effect() if side_effect else side_effect

    return mock


def mock_directories(
    total: int = 1,
    **kwargs,
) -> list[Mock]:
    mocks = [mock_directory(**kwargs) for i in range(total)]

    return mocks


def mock_file(
    exist: bool = True,
    st_size: int = 1024,
    side_effect: Optional[Callable] = None,
) -> Mock:
    mock = Mock(spec=Path)
    mock.exists.return_value = exist
    mock.is_dir.return_value = False
    mock.is_file.return_value = True
    mock.stat.return_value.st_size = st_size
    # mock.side_effect = side_effect() if side_effect else side_effect

    return mock


def mock_files(
    total: int = 1,
    **kwargs,
) -> list[Mock]:
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
create_directories_happy = [(dict(paths=mock_directories(3)))]

delete_directory_happy = [
    (dict(path=mock_directory(), recursive=True)),
    (dict(path=mock_directory(), recursive=False)),
    (dict(path=mock_directory())),
]
delete_directory_sad = [
    (
        dict(path=mock_directory(False), recursive=True),
        dict(
            exception_type=Exception,
            exception_message=(f"Path doesn't exists."),
        ),
    ),
    (
        dict(path=mock_file(True), recursive=True),
        dict(
            exception_type=Exception,
            exception_message=(f"Path is not a directory"),
        ),
    ),
]

list_directory_happy = [
    (
        dict(
            path=mock_directory(childrens=_childrens()),
            is_file=True,
        )
    ),
    (
        dict(
            path=mock_directory(childrens=_childrens()),
            is_file=False,
        )
    ),
    (
        dict(
            path=mock_directory(childrens=_childrens()),
        )
    ),
]
list_directory_sad = [
    (
        dict(
            path=mock_directory(False),
            is_file=False,
        ),
        dict(
            exception_type=FileNotFoundError,
            exception_message="",
        ),
    ),
    (
        dict(
            path=mock_file(True),
            is_file=True,
        ),
        dict(
            exception_type=Exception,
            exception_message=(f"Path is not a directory."),
        ),
    ),
    (
        dict(
            path=mock_file(True),
            is_file=True,
        ),
        dict(
            exception_type=Exception,
            exception_message=(f"Path is not a directory."),
        ),
    ),
]

validate_file_size_happy = [
    (
        dict(
            path=mock_file(),
            lower_bound=512,
            upper_bound=2048,
        ),
        dict(result=True),
    ),
    (
        dict(
            path=mock_file(),
            lower_bound=2048,
            upper_bound=4096,
        ),
        dict(result=False),
    ),
]
validate_file_size_sad = [
    (
        dict(
            path=mock_file(),
            lower_bound=4096,
            upper_bound=256,
        ),
        dict(
            exception_type=Exception,
            exception_message=(
                f"Value of lower bound range cannot be greater " f"than or equal to value of upper bound range"
            ),
        ),
    ),
    (
        dict(
            path=mock_directory(),
            lower_bound=128,
            upper_bound=256,
        ),
        dict(
            exception_type=Exception,
            exception_message=(f"Path is not a file."),
        ),
    ),
]

generate_file_hash_happy = [
    (
        dict(
            path=mock_file(),
            algorithm="md5",
            text="J92mcMpESqWbiP$F",
        ),
        dict(result="91777a7557772d0cda0cb772961198aa"),
    ),
    (
        dict(
            path=mock_file(),
            algorithm="sha256",
            text="5dTsbUXM9KpvY~$^",
        ),
        dict(result="c93b9390d897dc1f5ef3b0950311a96ae22c9185402b509d0aab5d9551346882"),
    ),
]
generate_file_hash_sad = [
    (
        dict(
            path=mock_file(),
            algorithm="sha512",
            text="mu5q3$5HE#h#qmQj",
        ),
        dict(
            result="da2794cc681ad27d7325045c0a48941d36fe0bd94d8d6747404d4990d5c9d96d045e16dc253a1496be375781c858b0f051c78b931880d4ae4084eb8bfeecd9ac",
            exception_type=Exception,
            exception_message=f"Unsupported hash algorithm",
        ),
    ),
    (
        dict(
            path=mock_directory(),
            algorithm="sha256",
            text="",
        ),
        dict(
            result="ceb9fb9796b0d7c7bb822039a312cd0ebdefbf53ab12097f77a16000adb4d0a5",
            exception_type=IsADirectoryError,
            exception_message="",
        ),
    ),
]

validate_file_hash_happy = [
    (
        dict(
            _hash="d67d458aa1460d49f3ea15f0c5574234acdbdbaae774dceda8d0dd8602becc61",
            path=mock_file(),
            algorithm="sha256",
            text="h@7szVAUpf9^b@ES",
        ),
        dict(result=True),
    ),
    (
        dict(
            _hash="cb5e8b5409fb353fde644017fd694959",
            path=mock_file(),
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
            path=mock_file(),
            algorithm="sha256",
            text="x&DhYR~3u4d`vnLK",
        ),
        dict(result=False),
    ),
]

suffix_datetime_happy = [
    (
        dict(path=Path("/srv/work/test_document_01.pdf")),
        dict(name="test_document_01_20230108_154025.pdf"),
    ),
    (
        dict(path=Path("/srv/work/test manual 01.pdf")),
        dict(name="test manual 01_20230108_154025.pdf"),
    ),
]

# endregion: PyTest parametrized variables


class TestIOOps:
    @pytest.mark.parametrize("payload", create_directories_happy)
    def test_happy_create_directories(self, payload):
        create_directories(**payload)

        [directory.mkdir.assert_called() for directory in payload["paths"]]

    @pytest.mark.parametrize("payload", delete_directory_happy)
    def test_happy_delete_directory(self, payload):
        with patch("pathlib.Path.iterdir", return_value=mock_files(3)) as mock:
            delete_directory(**payload)

            if payload.get("recursive") == True:
                payload["path"].iterdir.assert_called_once()
            else:
                payload["path"].rmdir.assert_called()

    # @pytest.mark.parametrize("payload, expect", delete_directory_sad)
    # def test_sad_delete_directory(self, payload, expect):
    #     with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
    #         delete_directory(**payload)

    @pytest.mark.parametrize("payload", list_directory_happy)
    def test_happy_list_directory(self, payload):
        results = list_directory(**payload)

        assert isinstance(results, Iterator)

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

    # @pytest.mark.parametrize("payload, expect", list_directory_sad)
    # def test_sad_list_directory(self, payload, expect):
    #     with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
    #         results = list_directory(**payload)

    #         results = list(results)

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

        with patch("builtins.open", mock_open(read_data=text)) as mocked_file:
            result = generate_file_hash(**payload)

            assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", generate_file_hash_sad)
    def test_sad_generate_file_hash(self, payload, expect):
        text = payload.pop("text").encode("utf-8")

        if text:
            with patch("builtins.open", mock_open(read_data=text)) as mocked_file:
                with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
                    result = generate_file_hash(**payload)
        else:
            with patch("builtins.open", new_callable=mock_open) as mocked_file:
                mf = mocked_file.return_value
                mf.read.side_effect = IsADirectoryError

                with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
                    result = generate_file_hash(**payload)

    @pytest.mark.parametrize("payload, expect", validate_file_hash_happy)
    def test_happy_validate_file_hash(self, payload, expect):
        text = payload.pop("text").encode("utf-8")

        with patch("builtins.open", mock_open(read_data=text)) as mocked_file:
            result = validate_file_hash(**payload)

            assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", suffix_datetime_happy)
    def test_happy_suffix_datetime_happy(self, payload, expect):
        with patch(f"{jt_snippets.io_ops.__name__}.datetime", wraps=datetime) as mock:
            mock.now.return_value = datetime(2023, 1, 8, 15, 40, 25, 100000)

            result = suffix_datetime(**payload)

            assert result == expect["name"]
