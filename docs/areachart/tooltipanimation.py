
import dash_mantine_components as dmc
from .data import data

component = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    type="stacked",
    tooltipAnimationDuration=200,
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"}
    ]
)

