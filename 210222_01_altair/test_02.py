# https://altair-viz.github.io/gallery/index.html
# https://www.javaer101.com/ja/article/62938314.html

import altair as alt
import pandas as pd

source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

chart = alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)

# # HTMLの"Click to view actions"アイコンを削除する方法
# alt.renderers.enable('kaggle')
# alt.renderers.set_embed_options(actions=False)

# print(chart._repr_mimebundle_(None, None)['text/html'])

chart.save('test_02.json')
chart.save('test_02.html')
