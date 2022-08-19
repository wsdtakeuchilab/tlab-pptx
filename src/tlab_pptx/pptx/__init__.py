import pathlib

_PPTX_DIR = pathlib.Path(__file__).parent
_DEFAULT_PPTX = _PPTX_DIR / "universal.pptx"

PPTX_DIR = str(_PPTX_DIR)
"""The pptx directory in this package."""
DEFAULT_PPTX = str(_DEFAULT_PPTX)
"""The filepath of the default pptx file."""


def get_pptx_filenames() -> list[str]:
    """
    Return a list of filenames of built-in `.pptx` files.

    Returns
    -------
    list[str]
        A list of filenames of built-in `.pptx` files.
    """
    return [path.name for path in _PPTX_DIR.glob("**/*.pptx")]


def get_pptx_filepaths() -> list[str]:
    """
    Return a list of filepaths of built-in `.pptx` files.

    Returns
    -------
    list[str]
        A list of filepaths of built-in `.pptx` files.
    """
    return [str(path) for path in _PPTX_DIR.glob("**/*.pptx")]
