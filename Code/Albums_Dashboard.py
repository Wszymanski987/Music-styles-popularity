import pandas as pd
import statsmodels.api as sm
import plotly.express as px
from dash import Dash, html, dash_table, Input, Output, dcc

df_combined = pd.read_csv('/path/Albums_full.csv', sep=';', dtype=str)
df1 = pd.read_csv('/path/polaczony.csv', delimiter=',', dtype=str)

df_all_styles = df_combined.copy(deep=True)

df_combined = pd.get_dummies(df_combined, columns=['Style'], drop_first=True)

df_combined['Year'] = pd.to_numeric(df_combined['Year'], errors='coerce')
df_combined['Ratings'] = pd.to_numeric(df_combined['Ratings'], errors='coerce')
df1['Fans'] = pd.to_numeric(df1['Fans'], errors='coerce')
df_combined = df_combined[df_combined['Year'] >= 1660]


app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Music Style'),
    html.Hr(),
    dash_table.DataTable(data=df_combined.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='graph'),
    dcc.Dropdown(
        id='chart-value',
        options=['music_style_popularity', 'top_albums', 'top_bands', 'music_styles'
                 ],
        value='music_style_popularity'),
    dcc.Dropdown(
        id='music-style',
        options=[{'label': col, 'value': col}
                 for col in df_combined.columns if col.startswith('Style_')],
        value='Style_melodic black'),
    html.Div(id='regression-results')
])

x = df_combined['Year']
y = df_combined['Ratings']
x = sm.add_constant(x)


@app.callback(
    Output('graph', 'figure'),
    [Input('chart-value', 'value'),
     Input('music-style', 'value')]
)
def update_chart(model, dependent_value):
    if model == 'music_style_popularity':
        fig = px.scatter(df_combined, x='Year', y='Ratings', facet_col=dependent_value,
                         trendline='ols', trendline_scope='overall', trendline_color_override='black ')
        fig.update_layout(xaxis_title='Year', yaxis_title='Ratings')
        return fig
    elif model == 'top_albums':
        df_filtered = df_combined.nlargest(20, 'Ratings')
        fig = px.bar(df_filtered, x='Album', y='Ratings')
        return fig
    elif model == 'top_bands':
        df_filtered = df1.nlargest(20, 'Fans')
        fig = px.bar(df_filtered, x='Band', y='Fans')
        return fig
    elif model == 'music_styles':
        fig = px.scatter(df_all_styles, x='Year', y='Ratings', color='Style')
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
