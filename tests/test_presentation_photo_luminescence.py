import datetime

import plotly.graph_objects as go
import pytest

from tlab_pptx import core
from tlab_pptx.presentation import photo_luminescence


@pytest.mark.parametrize("title_text", ["title", "title2"])
@pytest.mark.parametrize("excitation_wavelength", [400])
@pytest.mark.parametrize("excitation_power", [1])
@pytest.mark.parametrize("time_range", [5])
@pytest.mark.parametrize("center_wavelength", [450])
@pytest.mark.parametrize("FWHM", [30])
@pytest.mark.parametrize("frame", [1000])
@pytest.mark.parametrize("date", [datetime.date(2022, 1, 1)])
@pytest.mark.parametrize("h_fig", [go.Figure()])
@pytest.mark.parametrize("v_fig", [go.Figure()])
@pytest.mark.parametrize(["a", "b"], [(40, 60), (0.4, 0.6)])
@pytest.mark.parametrize(["tau1", "tau2"], [(0.5, 1.5)])
def test_build(
    title_text: str,
    excitation_wavelength: int,
    excitation_power: int,
    time_range: int,
    center_wavelength: int,
    FWHM: float,
    frame: int,
    date: datetime.date,
    h_fig: go.Figure,
    v_fig: go.Figure,
    a: float,
    b: float,
    tau1: float,
    tau2: float,
) -> None:
    prs = photo_luminescence.build(
        title_text,
        excitation_wavelength,
        excitation_power,
        time_range,
        center_wavelength,
        FWHM,
        frame,
        date,
        h_fig,
        v_fig,
        a,
        b,
        tau1,
        tau2,
    )
    assert isinstance(prs, core.Presentation)
    assert prs.slides[0]._slide.shapes.title.text == title_text
