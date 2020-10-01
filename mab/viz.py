import plotly.graph_objects as go
import numpy as np


def plot(
    mc,
    metric="accuracy",
    title="",
    horizon=None,
    add_diagonal=False,
    is_marketing_name=False,
    is_percents=False,
):
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
        title=title,
        autosize=True,
    )
    if is_percents:
        fig.update_layout(yaxis=dict(tickformat="0.0%"))

    return fig