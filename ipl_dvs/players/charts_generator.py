import pandas as pd
import altair as alt


def batsman_vs_team(player, team):
    batsman_vs_team = pd.read_csv('data_files/batsman_vs_team.csv', delimiter=',')
    batsman_vs_team = batsman_vs_team[batsman_vs_team['player'] == player][
        batsman_vs_team['team'] == team]
    highlight = alt.selection(type='multi', on='mouseover',
                              fields=['season'], nearest=True)

    batsman_vs_team_base = alt.Chart(batsman_vs_team).encode(
        x='match:O',
        y='runs:Q',
        tooltip=['player', 'runs', 'season'],
    )

    batsman_vs_team_points = batsman_vs_team_base.mark_circle().encode(
        opacity=alt.value(0),
    ).add_selection(
        highlight,
    ).properties(
        height=300,
        width=900
    )

    batsman_vs_team_lines = batsman_vs_team_base.mark_line(point=True).encode(
        opacity=alt.condition(~highlight, alt.value(1), alt.value(1)),
        size=alt.condition(~highlight, alt.value(5), alt.value(5))
    )
    return batsman_vs_team_points + batsman_vs_team_lines
