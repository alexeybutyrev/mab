""" Vizalization Tools """
import plotly.graph_objects as go
import numpy as np

# pylint: disable=too-many-arguments
def plot(
    mc_sim,
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
        mc_sim (MonteCarloSimulation): mc_sim simulaions for different algorythms
        metric (str): Metric to plot. Defaults to "accuracy".
        title (str): Title of the plot. Defaults to "".
        horizon (int): Time horizon. Nuber of times arm was selected

    Returns:
        [plotly.fig]: returns figure with data
    """
    if horizon is None:
        horizon = mc_sim.horizon

    fig = go.Figure()
    for simulation in mc_sim:
        algorythm_name = (
            simulation.marketing_name if is_marketing_name else simulation.name
        )

        fig.add_trace(
            go.Scatter(
                x=np.array(range(horizon)),
                y=np.array(simulation.metrics[metric]),
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
        fig.update_layout(yaxis={"tickformat": "0.0%"})

    return fig
