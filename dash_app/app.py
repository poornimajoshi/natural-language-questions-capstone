import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv("/Users/poornimajoshi/Desktop/capstone_dash_app/answers_from_model.csv")


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'cdqa-app'
app.layout = html.Div([
    html.Div(html.H1('Question Answering visualization')),
    html.Div(html.H6('Choose an example from the below list')),
    dcc.Dropdown(
        id='query-dropdown',
        options=[{"label": i, "value": i} for i in df['query']],
        value=df['query'][0]
    ),
    html.Div(html.H6('Answer')),
    html.Div(id='output-container-answer'),
    html.Div(html.H6('Passage Context')),
    html.Div(id='output-container-context'),
    html.Div(html.H6('Original Document')),
    html.Div(id='output-container-document')
    
], style={'padding': '40px 40px 40px 40px'})
#'background-image': 'url(https://hougumlaw.com/wp-content/uploads/2016/05/light-website-backgrounds-light-color-background-images-light-color-background-images-for-website-1024x640-300x188.jpg)'})


@app.callback(
    [dash.dependencies.Output('output-container-answer', 'children'),
    dash.dependencies.Output('output-container-context', 'children'),
    dash.dependencies.Output('output-container-document', 'children')],
    [dash.dependencies.Input('query-dropdown', 'value')])
def update_output(value):
    return (df[df['query']==value]['answer']),(df[df['query']==value]['paragraph']),(df[df['query']==value]['title'])


if __name__ == '__main__':
    app.run_server(debug=True)