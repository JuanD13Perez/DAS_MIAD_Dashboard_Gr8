from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from src.const import get_constants

from src.dash1 import generate_visualizations as generate_visualizations1
from src.dash2 import generate_visualizations as generate_visualizations2
from src.dash3 import generate_visualizations as generate_visualizations3
# from src.dash4 import generate_visualizations as generate_visualizations4

HA = pd.read_csv('data/HeartAttack.csv')
HA['Creatina']=pd.to_numeric(HA['Creatina en suero'].str.replace(",", "."))
num_pacientes,edad_promedio,tiempo_seguimiento,factores_de_riesgo = get_constants(HA)

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='Factores de Riesgo asociados a E.C')
server = app.server


def generate_stats_card(title, value, image_path):
    return html.Div(
        dbc.Card([
            dbc.CardImg(src=image_path, top=True, style={'width': '55px','alignSelf': 'center'}),
            dbc.CardBody([
                html.P(value, className="card-value", style={'margin': '0px','fontSize': '22px','fontWeight': 'bold'}),
                html.H4(title, className="card-title", style={'margin': '0px','fontSize': '12px','fontWeight': 'bold'})
            ], style={'textAlign': 'center'}),
        ], style={'paddingBlock':'10px',"backgroundColor":'#8889a9','border':'none','borderRadius':'10px','color':'white'})
    )



tab_style = {
    'idle':{
        'borderRadius': '10px',
        'padding': '0px',
        'marginInline': '5px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'bold',
        'backgroundColor': '#8889a9',
        'border':'none',
        'color':'white'
    },
    'active':{
        'borderRadius': '10px',
        'padding': '0px',
        'marginInline': '5px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'bold',
        'border':'none',
        'backgroundColor': '#dcdcdc',
        'color':'white'
    }
}

MAX_OPTIONS_DISPLAY = 3300
fig1, fig2, fig3 = generate_visualizations1(HA)

# Define the layout of the app
app.layout = html.Div([
    dcc.Textarea(
    id='textarea-title',
    value='Factores de Riesgo asociados a Enfermedades Cardíacas',
    style={'height':'45px','textAlign': 'center','width': '100%',"backgroundColor":'#2e304b','border':'none','color':'white','fontWeight': 'bold','fontSize': '32px'},
    ),
    dbc.Container([
        dbc.Row([
            dbc.Col(html.Img(src="./assets/HA_banner.png",width=150), width=2),
            dbc.Col(
                dcc.Tabs(id='graph-tabs', value='Demográfica', children=[
                    dcc.Tab(label='Demográfica', value='Demográfica',style=tab_style['idle'],selected_style=tab_style['active']),
                    dcc.Tab(label='Antecedentes', value='Antecedentes',style=tab_style['idle'],selected_style=tab_style['active']),
                    dcc.Tab(label='Factores', value='Factores',style=tab_style['idle'],selected_style=tab_style['active'])
                ], style={'marginTop': '15px', 'width':'800px','height':'50px'})
            ,width=6)
        ]),
        dbc.Row([
            dbc.Col(generate_stats_card("Pacientes",num_pacientes,"./assets/paciente_icon.png"), width=3),
            dbc.Col(generate_stats_card("Edad Promedio", edad_promedio,"./assets/edad_icon.png"), width=3),
            dbc.Col(generate_stats_card("Tiempo Seguimiento (días)",tiempo_seguimiento,"./assets/tiempo_seguimiento_icon.png"), width=3),
            dbc.Col(generate_stats_card("Factores de Riesgo analizados",factores_de_riesgo,"./assets/factores_de_riesgo_icon.png"), width=3),
        ],style={'marginBlock': '10px'}),
        dbc.Row([
            dcc.Loading([
                html.Div(id='tabs-content')
            ],type='default',color='#2e304b')
        ])
    ], style={'padding': '0px'})
],style={'backgroundColor': '#2e304b', 'minHeight': '100vh'})

@app.callback(
    Output('tabs-content', 'children'),
    [Input('graph-tabs', 'value')]
)
def update_tab(tab):
    if tab == 'Demográfica':
        fig1, fig2, fig3 = generate_visualizations1(HA)
        return html.Div([
        html.Div([
            dcc.Graph(id='graph1', figure=fig1),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph2', figure=fig2),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph3', figure=fig3),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([dcc.Textarea(
        id='textarea-demografica',
        value='''
        
        

        
        La edad promedio de los pacientes que se les realizan seguimiento es de 61 años, el rango de edad esta entre los 45 a los 95 años. El 64.9% son hombres, y el 35.1% restantes son mujeres. De los 299 pacientes a lo que se le realizo el seguimiento, 203 han sobrevivido a una insuficiencia cardiaca, y desafortunadamente 96 pacientes fallecieron por esta causa.''',
        style={'height':'450px','textAlign': 'center','width': '100%',"backgroundColor":'#8889a9','border':'none','color':'white','fontSize':'14px', 'display':'flex'},
        )], style={'width': '50%', 'display': 'inline-block', 'justifyContent':'center'})
    ])
    elif tab == 'Antecedentes':
        fig1, fig2, fig3, fig4, fig5 = generate_visualizations2(HA)
        return html.Div([
        html.Div([
            dcc.Graph(id='graph1', figure=fig1),
        ], style={'width': '25%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph2', figure=fig2),
        ], style={'width': '25%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph3', figure=fig3),
        ], style={'width': '25%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph4', figure=fig4),
        ], style={'width': '25%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph5', figure=fig5),
        ], style={'width': '100%', 'display': 'inline-block'})
    ])
    elif tab == 'Factores':
        fig1, fig2, fig3 = generate_visualizations3(HA)
        return html.Div([
        html.Div([
            dcc.Graph(id='graph1', figure=fig1),
        ], style={'width': '100%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph2', figure=fig2),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph3', figure=fig3),
        ], style={'width': '50%', 'display': 'inline-block'})
        ])


if __name__ == '__main__':
    app.run_server(debug=False)

