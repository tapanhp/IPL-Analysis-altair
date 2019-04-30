from django.shortcuts import render
import pandas as pd
import altair as alt
import json


# Create your views here.
def index(request):
    alt.renderers.enable('json')
    alt.data_transformers.enable('default', max_rows=None)
    match_count = pd.read_csv('data_files/citywise_match_count.csv', delimiter=',')
    bars = alt.Chart(match_count).mark_bar().encode(
        x='city_name:N',
        y='matches:Q',
    ).properties(
        height=300,
        width=900,
    )

    # bars = base.mark_bar()

    context = {
        'match_city_data': json.dumps(bars.to_dict())
    }
    print(context['match_city_data'])
    return render(request, 'batsman/index.html', context)
