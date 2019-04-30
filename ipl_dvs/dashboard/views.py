from django.shortcuts import render
import pandas as pd
import altair as alt
import json


# Create your views here.
def index(request):
    alt.renderers.enable('json')
    alt.data_transformers.enable('default', max_rows=None)
    match_count = pd.read_csv('data_files/citywise_match_count.csv', delimiter=',')
    player_count = pd.read_csv('data_files/countrywise_player_count.csv', delimiter=',')
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

    context = {
        'match_city_data': json.dumps(match_bars.to_dict()),
        'player_country_data': json.dumps(player_bars.to_dict())
    }
    return render(request, 'batsman/index.html', context)
