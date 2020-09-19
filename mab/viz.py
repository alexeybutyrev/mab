import plotly.graph_objects as go
import numpy as np


def plot(results, metric="accuracy", title="", horizon=None, add_diagonal=False):
    """
        Help function to make plotly charts of the metric results
            results - dictionaries with results of experiments

    Args:
        results (dict): dictionary with simulaions for different algorythms
        metric (str): Metric to plot. Defaults to "accuracy".
        title (str): Title of the plot. Defaults to "".
        horizon (int): Time horizon. Nuber of times arm was selected

    Returns:
        [plotly.fig]: returns figure with data
    """
    if horizon is None:
        horizon = len(results[0][metric])

    fig = go.Figure()
    for res in results:
        fig.add_trace(
            go.Scatter(
                x=np.array(range(horizon)),
                y=np.array(res[metric]),
                mode="lines",
                name=res["algorythm"],
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

    return fig