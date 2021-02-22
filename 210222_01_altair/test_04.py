import altair as alt
from vega_datasets import data

source = data.ohlc()

open_close_color = alt.condition("datum.open <= datum.close",
                                 alt.value("#06982d"),
                                 alt.value("#ae1325"))

base = alt.Chart(source).encode(
    alt.X('date:T',
          axis=alt.Axis(
              format='%m/%d',
              labelAngle=-45,
              title='2009年'
          )
    ),
    color=open_close_color
)

rule = base.mark_rule().encode(
    alt.Y(
        'low:Q',
        title='Price',
        scale=alt.Scale(zero=False),
    ),
    alt.Y2('high:Q')
).properties(
    width=800,
    height=400
)

bar = base.mark_bar().encode(
    alt.Y('open:Q'),
    alt.Y2('close:Q')
).properties(
    width=800,
    height=400
)

chart = rule + bar

chart.save('test_04.html')

# HTMLの"Click to view actions"アイコンを削除する方法
alt.renderers.enable('kaggle')
alt.renderers.set_embed_options(actions=False)

with open('test_04.code', mode='w') as f:
    f.write(chart._repr_mimebundle_(None, None)['text/html'])