import altair as alt
from . import data_reader as dr


def win_loss():
    team_win_bar = alt.Chart(dr.win_loss).mark_bar(color='steelblue', opacity=0.8).encode(
        x=alt.X('sum(wins):Q', axis=alt.Axis(title='wins and loses')),
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


def win_by_runs(team):
    win_by_runs_data = dr.win_by_runs[dr.win_by_runs['winner'] == team]
    bar = alt.Chart(win_by_runs_data).mark_bar().encode(
        x=alt.X('match:N', axis=alt.Axis(labelOpacity=0)),
        y='won by runs:Q',
        color='won by runs:Q',
        tooltip=['team 1', 'team 2', 'winner', 'won by runs']
    ).properties(
        height=300,
        width=900,
    ).configure_axis(
        grid=False
    ).configure_view(
        strokeOpacity=0
    )
    return bar


def win_by_wickets(team):
    win_by_wickets_data = dr.win_by_wickets[dr.win_by_wickets['winner'] == team]
    bar = alt.Chart(win_by_wickets_data).mark_bar().encode(
        x=alt.X('match:N', axis=alt.Axis(labelOpacity=0)),
        y='won by wickets:Q',
        color='won by wickets:Q',
        tooltip=['team 1', 'team 2', 'winner', 'won by wickets']
    ).properties(
        height=300,
        width=700,
    ).configure_axis(
        grid=False
    ).configure_view(
        strokeOpacity=0
    )
    return bar
