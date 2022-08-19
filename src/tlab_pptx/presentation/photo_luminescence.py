import datetime

import plotly.graph_objects as go

from tlab_pptx import core, figure


def build(
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
) -> core.Presentation:
    """
    Build a Presentation object for a photo luminescence experiment.

    Parameters
    ----------
    title_text : str
        The title text of a slide.
    excitation_wavelength : int
        The excitation wavelength of the experiment.
    excitation_power : int
        The excitation power of the experiment.
    time_range : int
        The time range of the experiment.
    center_wavelength : int
        The center wavelength of the PL intensity.
    FWHM : float
        The full width at half maximum of the PL intensity.
    frame : int
        The frame count of the streak scope used in the experiment.
    date : datetime.date
        The date of the experiement.
    v_fig : plotly.graph_objects.Figure
        A figure of PL intensity vs. wavelength.
    h_fig : plotly.graph_objects.Figure
        A figure of PL intensity vs. time.
    a : float
        The weight of the fast decay.
    b : float
        The weight of the slow decay.
    tau1 : float
        The decay time of the fast decay.
    tau2 : float
        The decay time of the slow decay.

    Returns
    -------
    tlab_pptx.core.Presentation
        A built presentation.

    Exapmles
    --------
    >>> prs = build(
    ...     title_text="Title",
    ...     excitation_wavelength=400,
    ...     excitation_power=1,
    ...     time_range=10,
    ...     center_wavelength=480,
    ...     FWHM=50,
    ...     frame=10000,
    ...     date=datetime.date.today(),
    ...     h_fig=go.Figure(),
    ...     v_fig=go.Figure(),
    ...     a=63,
    ...     b=37,
    ...     tau1=1.2,
    ...     tau2=3.6
    ... )
    """
    prs = core.new_presentation()
    slide = prs.slides[0]
    _a = int(100 * a / (a + b))
    slide.update_title(text=title_text).add_figure(
        _get_formatted_figure(h_fig, date), left=0.33, top=5.0
    ).add_figure(_get_formatted_figure(v_fig, date), left=12.33, top=5.0).add_text(
        f"Excitation wavelength : {int(excitation_wavelength):d} nm\n"
        f"Excitation power : {int(excitation_power):d} mW\n"
        f"Time range : {int(time_range):d} ns\n",
        left=2.33,
        top=2.5,
    ).add_text(
        f"Center wavelength : {int(center_wavelength):d} nm\n"
        f"FWHM : {FWHM:.2g} nm\n"
        f"Frame : {int(frame):d}\n",
        left=14.33,
        top=2.5,
    ).add_text(
        f"a : b = {_a:d} : {100 - _a:d}",
        left=14.33,
        top=17.0,
        font_name="Cambria Math",
    ).add_text(
        f"τ₁ = {tau1:.2g} ns\n" f"τ₂ = {tau2:.2g} ns\n",
        left=19.33,
        top=17.0,
        font_name="Cambria Math",
    )
    return prs


def _get_formatted_figure(fig: go.Figure, date: datetime.date) -> go.Figure:
    return (
        go.Figure(fig)
        .add_annotation(figure.get_date_annotation(date))
        .update_layout(figure.get_default_layout(), showlegend=False)
        .update_xaxes(figure.get_default_axis())
        .update_yaxes(figure.get_default_axis())
        .update_traces(line=dict(width=1))
    )
