import dash_mantine_components as dmc

data = ["Dash", "Mantine", "Bootstrap", "Core"]

component = dmc.Group(
    direction="column",
    children=[
        dmc.SegmentedControl(data=data, size=x) for x in ["xs", "sm", "md", "lg", "xl"]
    ],
)
