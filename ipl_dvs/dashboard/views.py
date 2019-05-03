from altair import datum
from django.shortcuts import render
import pandas as pd
import altair as alt
import json


# Create your views here.

def facet_wrap(subplts, plots_per_row):
    rows = [subplts[i * plots_per_row:i * plots_per_row + plots_per_row] for i in range(len(subplts) // plots_per_row)]
    rows = [alt.hconcat(*charts) for charts in rows]
    return alt.vconcat(*rows).configure_axis(grid=False).configure_view(strokeOpacity=0)


def index(request):
    alt.renderers.enable('json')
    alt.data_transformers.enable('default', max_rows=None)
    match_count = pd.read_csv('data_files/citywise_match_count.csv', delimiter=',')
    player_count = pd.read_csv('data_files/countrywise_player_count.csv', delimiter=',')
    wickets_by_bowling_style = pd.read_csv('data_files/wickets_by_bowling_style.csv', delimiter=',')
    match_bars = alt.Chart(match_count).mark_bar().encode(
        x='city:N',
        y='matches:Q',
    ).properties(
        height=300,
        width=900,
    ).configure_axis(
        labelFontSize=15,
        titleFontSize=17,
    ).configure_axisBottom(
        labelAngle=-45
    )
    player_bars = alt.Chart(player_count).mark_bar().encode(
        x='country:N',
        y='players:Q',
    ).properties(
        height=300,
        width=900,
    ).configure_axis(
        labelFontSize=15,
        titleFontSize=17,
    ).configure_axisBottom(
        labelAngle=-45
    )

    # wicket_bars = alt.Chart(wickets_by_bowling_style).mark_bar().encode(
    #     x='sum(wickets):Q',
    #     y='bowling_style:N',
    # )
    subplts = []

    for stadium in wickets_by_bowling_style['stadium'].unique():
        subplts.append(
            alt.Chart(wickets_by_bowling_style[wickets_by_bowling_style['stadium'] == stadium]).mark_bar().encode(
                x='wickets:Q',
                y='bowling_style:N',
                tooltip=['wickets', 'bowling_style']
            ).properties(
                height=300,
                width=350,
                title=stadium,

            ))

    compound_chart = facet_wrap(subplts, plots_per_row=2)
    context = {
        'match_city_data': json.dumps(match_bars.to_dict()),
        'player_country_data': json.dumps(player_bars.to_dict()),
        'wicket_bowling_style_data': compound_chart.to_json(),
        'app_name': 'dashboard'
    }
    return render(request, 'dashboard/index.html', context)
