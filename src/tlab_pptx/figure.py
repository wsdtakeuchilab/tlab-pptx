import datetime
import typing as t


def get_default_layout() -> dict[str, t.Any]:
    """
    Gets the default layout of a plotly.graph_objects.Figure object for PowerPoint.

    Returns
    -------
    dict[str, Any]
        The default layout.

    See also
    --------
    https://plotly.com/python/reference/layout/

    Examples
    --------
    >>> import plotly.graph_objects as go
    >>> fig = go.Figure()
    >>> fig.update_layout(get_default_layout())
    Figure({
        'data': [],
        'layout': {'font': {'family': 'Arial', 'size': 18},
                   'height': 450,
                   'legend': {'title': {}, 'x': 1, 'xanchor': 'right'},
                   'margin': {'b': 10, 'l': 10, 'r': 10, 't': 20},
                   'template': '...',
                   'width': 450,
                   'xaxis': {'mirror': True, 'showline': True, 'ticks': 'inside'},
                   'yaxis': {'mirror': True, 'showline': True, 'ticks': 'inside'}}
    })
    """
    return dict(
        height=450,
        width=450,
        margin=dict(l=10, r=10, t=20, b=10),
        font=dict(size=18, family="Arial"),
        legend=dict(title=None, x=1, xanchor="right"),
        template="simple_white",
        xaxis=get_default_axis(),
        yaxis=get_default_axis(),
    )


def get_default_axis() -> dict[str, t.Any]:
    """
    Gets the default axis of a plotly.graph_objects.Figure object for PowerPoint.

    Returns
    -------
    dict[str, Any]
        The default axis.

    See also
    --------
    https://plotly.com/python/reference/layout/xaxis/
    https://plotly.com/python/reference/layout/yaxis/

    Examples
    --------
    >>> import plotly.graph_objects as go
    >>> fig = go.Figure()
    >>> fig.update_xaxes(get_default_axis())
    Figure({
        'data': [], 'layout': {'template': '...', 'xaxis': {'mirror': True, 'showline': True, 'ticks': 'inside'}}
    })
    """
    return dict(ticks="inside", mirror=True, showline=True)


def get_date_annotation(date: datetime.date | tuple[int, int, int]) -> dict[str, t.Any]:
    """
    Gets a date annotation of a plotly.graph_objects.Figure object for PowerPoint.

    Parameters
    ----------
    date : datetime.date | tuple[int, int, int]
        A date object or compiatible tuple.

    Returns
    -------
    dict[str, Any]
        An annotation of date.

    Raises
    ------
    ValueError
        If date is not compiatible with `datetime.date`.

    See also
    --------
    https://plotly.com/python/reference/layout/annotations/#layout-annotations

    Examples
    --------
    >>> import plotly.graph_objects as go
    >>> fig = go.Figure()
    >>> date = datetime.date(2022, 1, 1)
    >>> fig.add_annotation(get_date_annotation(date))
    Figure({
        'data': [],
        'layout': {'annotations': [{'font': {'size': 14},
                                    'showarrow': False,
                                    'text': '2022.01.01',
                                    'x': 1.0,
                                    'xref': 'paper',
                                    'y': -0.125,
                                    'yref': 'paper'}],
                   'template': '...'}
    })
    """
    if isinstance(date, tuple):
        try:
            date = datetime.date(*date[:3])
        except (ValueError, TypeError) as err:
            raise ValueError(f"{date} is not compiatible with `datetime.date`") from err
    return dict(
        text=date.strftime("%Y.%m.%d"),
        x=1.0,
        y=-0.125,
        xref="paper",
        yref="paper",
        showarrow=False,
        font=dict(size=14),
    )
