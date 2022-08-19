import datetime

import plotly.graph_objects as go
import pytest

from tlab_pptx import figure


@pytest.mark.parametrize(
    "date",
    [datetime.date(2022, 1, 1), datetime.date(2023, 12, 31)],
)
def test_get_date_annotaion(date: datetime.date) -> None:
    annotation = figure.get_date_annotation(date)
    assert annotation["text"] == date.strftime("%Y.%m.%d")
    assert go.layout.Annotation(annotation)  # TODO: Expect assert not raises ValueError


def test_get_default_layout() -> None:
    layout = figure.get_default_layout()
    assert go.Layout(layout)  # TODO: Expect assert not raises ValueError


def test_get_default_axis() -> None:
    axis = figure.get_default_axis()
    assert go.layout.XAxis(axis)  # TODO: Expect assert not raises ValueError
    assert go.layout.YAxis(axis)  # TODO: Expect assert not raises ValueError
