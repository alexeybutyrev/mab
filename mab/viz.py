import plotly.graph_objects as go
import numpy as np


def plot(
    mc,
    metric: str = "accuracy",
    title: str = "",
    horizon: int = None,
    add_diagonal: bool = False,
    is_marketing_name: bool = False,
    is_percents: bool = False,
) -> go.Figure:
    """
        Help function to make plotly charts of the monte carlo simulation

    Args:
        mc (MonteCarloSimulation): mc simulaions for different algorythms
        metric (str): Metric to plot. Defaults to "accuracy".
        title (str): Title of the plot. Defaults to "".
        horizon (int): Time horizon. Nuber of times arm was selected

    Returns:
        [plotly.fig]: returns figure with data
    """
    if horizon is None:
        horizon = mc.horizon

    fig = go.Figure()
    for m in mc:
        algorythm_name = m.marketing_name if is_marketing_name else m.name

        fig.add_trace(
            go.Scatter(
                x=np.array(range(horizon)),
                y=np.array(m.metrics[metric]),
                mode="lines",
                name=algorythm_name,
            )
        )

    if add_diagonal:
        fig.add_trace(
            go.Scatter(
                x=np.array(range(horizon)),
                y=np.array(range(horizon)),
                mode="lines",
                name="Best Possible",
            )
        )

    fig.update_layout(
        title=title, autosize=True,
    )
    if is_percents:
        fig.update_layout(yaxis=dict(tickformat="0.0%"))

    return fig


def plot(
    metrics,
    names,
    metric_name="accuracy",
    title=None,
    horizon=None,
    add_diagonal=False,
    is_marketing_name=False,
    is_percents=False,
):
    """
        Help function to make plotly charts of the monte carlo simulation

    Args:
        measurements (list): mc simulaions for different algorythms
        metric (str): Metric to plot. Defaults to "accuracy".
        title (str): Title of the plot. Defaults to "".
        horizon (int): Time horizon. Nuber of times arm was selected

    Returns:
        [plotly.fig]: returns figure with data
    """
    if horizon is None:
        horizon = len(metrics[0][metric_name])

    if title is None:
        title = metric_name.replace("_", " ").capitalize()

    fig = go.Figure()
    for i, m in enumerate(metrics):
        algorithm_name = names[i]

        fig.add_trace(
            go.Scatter(
                x=np.array(range(horizon)),
                y=np.array(m[metric_name]),
                mode="lines",
                name=algorithm_name,
            )
        )

    if add_diagonal:
        fig.add_trace(
            go.Scatter(
                x=np.array(range(horizon)),
                y=np.array(range(horizon)),
                mode="lines",
                name="Best Possible",
            )
        )

    fig.update_layout(
        title=title, autosize=True,
    )
    fig.update_yaxes(rangemode="tozero")
    if is_percents:
        fig.update_layout(yaxis=dict(tickformat="0.0%"))

    return fig
