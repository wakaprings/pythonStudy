
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Markdown('''
# 見出し１
## 見出し２

- 箇条書き
- 箇条書き
- 箇条書き
    ''')

])

if __name__ == '__main__':
    app.run_server(host='192.168.100.142', port='8050', debug=True)
