import altair as alt
from vega_datasets import data

source = data.seattle_weather()
brush = alt.selection(type='interval', encodings=['x'])

bars = alt.Chart().mark_bar().encode(
    x='month(date):O',
    y='mean(precipitation):Q',
    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7)),
).add_selection(
    brush
).properties(
    width=800,
    height=600
)

line = alt.Chart().mark_rule(color='firebrick').encode(
    y='mean(precipitation):Q',
    size=alt.SizeValue(3)
).transform_filter(
    brush
).properties(
    width=800,
    height=600
)

chart = alt.layer(bars, line, data=source)

# chart.save('test_03.json')
# chart.save('test_03.html')

# HTMLの"Click to view actions"アイコンを削除する方法
alt.renderers.enable('kaggle')
alt.renderers.set_embed_options(actions=False)

with open('test_03.code', mode='w') as f:
    f.write(chart._repr_mimebundle_(None, None)['text/html'])