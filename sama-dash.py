import json
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_table

# Load the data
with open('all_years_data_orcamento_receitas.json', 'r') as f:
    data = json.load(f)

# Combine data from all years into a single DataFrame
combined_df = pd.DataFrame()
for year, records in data.items():
    year_df = pd.json_normalize(records)
    year_df['year'] = year
    combined_df = pd.concat([combined_df, year_df], ignore_index=True)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    # Line chart for showing revenue over all years
    dcc.Graph(id='all-years-line-chart'),

    # Bar chart for comparing revenues among different management units across all years
    dcc.Graph(id='all-years-bar-chart'),

    # Pie chart for showing revenue distribution by category across all years
    dcc.Graph(id='all-years-pie-chart'),

    # Dropdown for selecting year
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in combined_df['year'].unique()],
        value=combined_df['year'].min(),
        multi=False
    ),

    # Line chart for showing revenue over selected year
    dcc.Graph(id='line-chart'),

    # Bar chart for comparing revenues among different management units for selected year
    dcc.Graph(id='bar-chart'),

    # Pie chart for showing revenue distribution by category for selected year
    dcc.Graph(id='pie-chart')
])


# Define callback for updating graphs
@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('year-dropdown', 'value')]
)
def update_graphs(selected_year):
    filtered_df = combined_df[combined_df['year'] == selected_year]

    # Line chart
    line_fig = px.line(filtered_df, x='year', y='valor', title=f'Evolução das Receitas em {selected_year}')

    # Bar chart
    bar_fig = px.bar(filtered_df, x='unidade_gestora', y='valor',
                     title=f'Receitas por Unidade Gestora em {selected_year}')

    # Pie chart
    pie_fig = px.pie(filtered_df, names='categoria', values='valor',
                     title=f'Distribuição de Receitas por Categoria em {selected_year}')

    return line_fig, bar_fig, pie_fig


# Create figures for all years data
all_years_line_fig = px.line(combined_df, x='year', y='valor', title='Evolução das Receitas ao Longo de Todos os Anos')
all_years_bar_fig = px.bar(combined_df, x='unidade_gestora', y='valor',
                           title='Receitas por Unidade Gestora ao Longo de Todos os Anos')
all_years_pie_fig = px.pie(combined_df, names='categoria', values='valor',
                           title='Distribuição de Receitas por Categoria ao Longo de Todos os Anos')

# Update figures for all years in layout
app.layout['all-years-line-chart'].figure = all_years_line_fig
app.layout['all-years-bar-chart'].figure = all_years_bar_fig
app.layout['all-years-pie-chart'].figure = all_years_pie_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

# Convert the pivot table to a DataFrame suitable for display in Dash DataTable
pivot_table_df = dash_table.reset_index()

# Add DataTable to the layout
app.layout.children.append(html.Hr())  # Horizontal line
app.layout.children.append(html.H3('Pivot Table: Amount of Each Type of Revenue per Managing Unit'))
app.layout.children.append(dash_table.DataTable(
    id='pivot-table',
    columns=[{'name': col, 'id': col} for col in pivot_table_df.columns],
    data=pivot_table_df.to_dict('records'),
    style_cell={'textAlign': 'left'},
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }
))
