from tlab_pptx import pptx


def test_get_pptx_filenames() -> None:
    filenames = pptx.get_pptx_filenames()
    assert filenames == [path.name for path in pptx._PPTX_DIR.glob("**/*.pptx")]


def test_get_pptx_filepaths() -> None:
    filepaths = pptx.get_pptx_filepaths()
    assert filepaths == [str(path) for path in pptx._PPTX_DIR.glob("**/*.pptx")]
