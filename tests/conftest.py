import os
import pathlib
import typing as t

import pytest

from tests import FixtureRequest
from tlab_pptx import typing


@pytest.fixture(params=["str", "Path"])
def filepath(request: FixtureRequest[str], filename: str) -> typing.FilePath:
    match request.param:
        case "str":
            return str(filename)
        case "Path":
            return pathlib.Path(filename)
        case _:
            raise NotImplementedError


@pytest.fixture(params=["buffer", "filepath"])
def filepath_or_buffer(
    request: FixtureRequest[str],
    filepath: typing.FilePath,
    tmpdir: str,
    open_mode: t.Literal["rb", "wb"],
) -> t.Generator[typing.FilePathOrBuffer, None, None]:
    match request.param:
        case "buffer":
            if "r" in open_mode:
                with open(pathlib.Path(tmpdir) / filepath, "rb") as f:
                    yield f
            elif "w" in open_mode:
                with open(pathlib.Path(tmpdir) / filepath, "wb") as f:
                    yield f
            else:
                raise ValueError(f"Invalid open_mode {open_mode}.")
        case "filepath":
            if isinstance(filepath, str):
                yield os.path.join(tmpdir, filepath)
            else:
                yield pathlib.Path(tmpdir) / filepath
