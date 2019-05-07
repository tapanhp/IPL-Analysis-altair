from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
import altair as alt
from . import charts_generator

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def facet_wrap(subplts, plots_per_row):
    rows = [subplts[i * plots_per_row:i * plots_per_row + plots_per_row] for i in range(len(subplts) // plots_per_row)]
    rows = [alt.hconcat(*charts) for charts in rows]
    return alt.vconcat(*rows).configure_axis(grid=False).configure_view(strokeOpacity=0).configure_axisBottom(
        labelAngle=0
    )


def index(request):
    top_runs = pd.read_csv('data_files/Top_10_Runs_All_Seasons.csv', delimiter=',')
    top_runs.sort_values('Runs', ascending=False, inplace=True)
    top_runs_vs_team = pd.read_csv('data_files/top_10_batsman_against_teams.csv', delimiter=',')
    top_runs_vs_team.sort_values('runs', ascending=False, inplace=True)
    player_list = pd.read_csv('data_files/players.csv', delimiter=',')
    player_list.sort_values('Player_Name', inplace=True)
    team_list = pd.read_csv('data_files/teams.csv', delimiter=',')
    team_list.sort_values('Team_Name', inplace=True)
    batsman_vs_team = pd.read_csv('data_files/batsman_vs_team.csv', delimiter=',')
    batsman_vs_team = batsman_vs_team[batsman_vs_team['player'] == 'V Kohli'][
        batsman_vs_team['team'] == 'Chennai Super Kings']
    top_runs_bars = alt.Chart(top_runs.head(10)).mark_bar().encode(
        x=alt.X('Player:N', sort=alt.EncodingSortField(field='Runs:Q', order='ascending')),
        y='Runs:Q',
        tooltip=['Player', 'Runs', 'Season'],
        color='Season:N',
    ).properties(
        height=300,
        width=900,
    ).configure_axis(
        labelFontSize=15,
        titleFontSize=17,
    ).configure_axisBottom(
        labelAngle=-45
    )
    subplts = []
    for team in top_runs_vs_team['team'].unique():
        subplts.append(
            (alt.Chart(top_runs_vs_team[top_runs_vs_team['team'] == team]).mark_bar(opacity=0.5).encode(
                x=alt.X('player:N'),
                y=alt.Y('runs:Q', axis=alt.Axis(tickCount=20)),
                tooltip=['player', 'runs', 'average'],
            ) + alt.Chart(top_runs_vs_team[top_runs_vs_team['team'] == team]).mark_line(point=True).encode(
                x=alt.X('player:N'),
                y=alt.Y('average:Q', axis=alt.Axis(tickCount=20)),
                tooltip=['player', 'runs', 'average'],
            )).properties(
                height=300,
                width=700,
                title=team
            )
        )
    compound_chart = facet_wrap(subplts, plots_per_row=1)

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
    batsman_vs_team_chart = batsman_vs_team_points + batsman_vs_team_lines

    print(batsman_vs_team_chart.to_json())

    context = {
        'top_score_data': top_runs_bars.to_json(),
        'top_score_vs_team_data': compound_chart.configure_line(
            color='red'
        ).configure_point(
            color='green',
            filled=True,
            opacity=1
        ).to_json(),
        'batsman_vs_team_data': batsman_vs_team_chart.to_json(),
        'app_name': 'players',
        'player_list': player_list['Player_Name'].tolist(),
        'team_list': team_list['Team_Name'].tolist()
    }
    return render(request, 'players/index.html', context)


@csrf_exempt
def update_batsman_vs_team(request):
    player = request.POST['player']
    team = request.POST['team']
    batsman_vs_team_chart = charts_generator.batsman_vs_team(player, team)
    return JsonResponse(batsman_vs_team_chart.to_dict(), safe=False)
