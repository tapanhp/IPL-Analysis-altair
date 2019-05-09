import altair as alt
from . import data_reader as dr


def win_loss():
    team_win_bar = alt.Chart(dr.win_loss).mark_bar(color='steelblue', opacity=0.8).encode(
        x='sum(wins):Q',
        y='team:N',
        tooltip=['team', 'total', 'wins']
    )
    team_loss_bar = alt.Chart(dr.win_loss).mark_bar(color='red', opacity=0.5).encode(
        x='sum(loss):Q',
        y='team:N',
        tooltip=['team', 'total', 'loss']
    )
    return (team_win_bar + team_loss_bar).configure_axis(
        grid=False
    ).configure_view(
        strokeOpacity=0
    ).configure_axisBottom(
        labelAngle=-45
    ).resolve_scale(x='shared', y='shared').properties(height=300, width=900)
