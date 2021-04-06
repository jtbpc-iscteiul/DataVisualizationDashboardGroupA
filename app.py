import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output
import plotly.express as px
#import itertools
#import collections
#import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('result.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#CSS
tabs_styles = {'height': '60px'}
tab_style = {'fontSize': '15px'}
tab_selected_style = {
    'backgroundColor': '#b3b3b3',
    'color': 'white',
    'fontWeight': 'bold'
}

#DROPDOWNS
country_options_athletes = [
    dict(label=country, value=country) for country in df['region'].unique()
]

dropdown_country_athletes = dcc.Dropdown(id='country_drop_athletes',
                                         options=country_options_athletes,
                                         value=['Portugal'],
                                         multi=True)

sport_options_athletes = [
    dict(label=sport, value=sport) for sport in df['Sport'].unique()
]

dropdown_sport_athletes = dcc.Dropdown(id='sport_drop_athletes',
                                       options=sport_options_athletes,
                                       value=['Portugal'],
                                       multi=True)

year_slider_world = dcc.Slider(
    id='year_slider_world',
    min=df['Year'].min(),
    max=df['Year'].max(),
    marks={str(i): '{}'.format(str(i))
           for i in (1896, 2017)},
    value=1964,
    step=1,
)

medal_options_world = [
    {
        'label': 'Total Medals',
        "value": 'Total_Medal'
    },
    {
        'label': 'Gold Medals',
        'value': 'Gold'
    },
    {
        'label': 'Silver Medals',
        'value': 'Silver'
    },
    {
        'label': 'Bronze Medals',
        'value': 'Bronze'
    },
    {
        'label': 'No Medals',
        'value': 'Sem_Medalha'
    },
]

#ATHLETES
country_options_athletes = [
    dict(label=str(country), value=str(country))
    for country in df['region'].unique()
]
country_options_athletes = sorted(country_options_athletes,
                                  key=lambda x: x["label"])

sport_options_athletes = [
    dict(label=str(sport), value=str(sport)) for sport in df['Sport'].unique()
]
sport_options_athletes = sorted(sport_options_athletes,
                                key=lambda x: x["label"])

dropdown_country_athletes = dcc.Dropdown(id='country_drop_athletes',
                                         options=country_options_athletes,
                                         value='Portugal')

dropdown_sport_athletes = dcc.Dropdown(id='sport_drop_athletes',
                                       options=sport_options_athletes,
                                       value='Swimming')

year_slider_athletes = dcc.RangeSlider(
    id='year_slider_athletes',
    min=df['Year'].min(),
    max=df['Year'].max(),
    marks={str(year): str(year)
           for year in range(1896, 2017, 4)},
    step=4,
    value=[1896, 2016])

#TEAMS
country_options_teams = [
    dict(label=str(country), value=str(country))
    for country in df['region'].unique()
]
sorted_country_options_teams = sorted(country_options_teams,
                                      key=lambda x: x["label"])

sport_options_teams = [
    dict(label=str(sport), value=str(sport)) for sport in df['Sport'].unique()
]
sorted_sport_options_teams = sorted(sport_options_teams,
                                    key=lambda x: x["label"])

medal_options_teams = [
    {
        'label': 'Total Medals',
        'value': 'Total_Medal'
    },
    {
        'label': 'Gold Medal',
        'value': 'Gold'
    },
    {
        'label': 'Silver Medal',
        'value': 'Silver'
    },
    {
        'label': 'Bronze Medal',
        'value': 'Bronze'
    },
    {
        'label': 'Without medal',
        'value': 'Sem_Medalha'
    },
]

dropdown_country_teams = dcc.Dropdown(id='country_drop_teams',
                                      options=sorted_country_options_teams,
                                      value=['USA'],
                                      multi=True)

dropdown_sport_teams = dcc.Dropdown(id='sport_drop_teams',
                                    options=sorted_sport_options_teams,
                                    value=['Athletics'],
                                    multi=True)

slider_year_teams = dcc.Slider(
    id='year_slider_teams',
    min=df['Year'].min(),
    max=df['Year'].max(),
    marks={str(i): '{}'.format(str(i))
           for i in (1896, 2017)},
    value=1964,
    step=1,
)

checklist_medals_teams = dcc.RadioItems(
    id='radioitems_teams',
    options=medal_options_teams,
    value='Gold',
    labelStyle={
        'display': 'inline-block',
        'margin-left': '30px'
    },
)

#test_png = 'OGimage.png'
#test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

app.layout = html.Div([
    html.Br(),
    html.Div([
        html.Div([
          #  html.Img(src='data:image/png;base64,{}'.format(test_base64),
          #           style={
           #              'width': '185px',
            #             'height': '80px',
             #            'margin-top': '5px'
              #       }),
            html.H1('Olympic Games',
                    style={
                        'color': 'black',
                        'fontSize': 44,
                        'margin-top': '20px',
                        'margin-left': '5px',
                        'textAlign': 'center',
                        'height': '70px',
                    })
        ],
                 style={
                     'textAlign': 'center',
                     'justify-content': 'center'
                 },
                 className='row'),
    ]),

    #WORLD
    dcc.Tabs(
        [
            dcc.Tab(
                label='WORLD',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Br(),
                    html.Div([
                    html.H2(
                        "Olympic Medals per Country",
                        style={
                            'fontSize': 25,
                        }),
                     ],
                             style={
                                 'margin-left': '30px'
                             }),
                    html.Div([
                        dcc.Dropdown(
                            id='medal_drop_world',
                            options=medal_options_world,
                            value="Sem_Medalha",
                            multi=False,
                        ),
                        dcc.Graph(id='world graph', style={'width': '95%'}),
                    ],
                             style={
                                 'width': '95%',
                                 'textAlign': 'center'
                             },
                             className='box'),
                    html.Div([
                        html.
                        H3("The modern Olympic Games or Olympics was first held in Athens, Greece in 1896 and are leading international sporting events featuring summer and winter sports competitions in which thousands of athletes from around the world participate in a variety of competitions. The Olympic Games are considered the world's foremost sports competition with more than 200 nations participating. The Olympic Games are normally held every four years, alternating between the Summer and Winter Olympics every two years in the four-year period. There are still some countries that do not have medals or have very few medals. More medals are owned by countries that have high economic power such as USA, Germany, UK.",
                           style={
                               'color': 'black',
                               'fontSize': 18,
                               'width': '95%',
                               'textAlign': 'justify',
                           })
                    ],
                             style={
                                 'width': '95%',
                                 'textAlign': 'center'
                             },
                             className='box'),
                    html.Br(),
                    html.Br(),
                    html.H1('WORLD DATA'),
                       html.Br(),
                    html.Div([
                                year_slider_world,
                            ]),
                               html.Br(),
                    html.Div(
                        [
                            html.Div([
                                dcc.Graph(id='graph3_teams'),
                            ],
                                     className='box',
                                     style={
                                         'width': '50%',
                                         'textAlign': 'center'
                                     }),
                            html.Div([dcc.Graph(id='graph4_teams')],
                                     className='box',
                                     style={'width': '50%'}),
                        ],
                        style={'justify-content': 'center'},
                        className='row',
                    ),
                    html.Br(),
                    html.Div(
                        [
                            html.Div([
                                dcc.Graph(id='graph5_teams'),
                            ],
                                     className='box'),
                        ],
                        style={'justify-content': 'center'},
                        className='row',
                    ),
                ]),

            #TEAMS
            dcc.Tab(
                label='TEAMS',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.Div([
                            html.Br(),
                            html.Label('COUNTRY'),
                            dropdown_country_teams,
                            html.Br(),
                            html.Label('SPORT'),
                            dropdown_sport_teams,
                            html.Br(),
                            html.Br(),
                            html.H3('PLEASE SELECT ONE OR MORE COUNTRIES AND SPORT TYPES TO GET STATISTICS ABOUT.', style={'fontSize':15, 'textAlign':'center'}),
                        ],
                                 style={'width': '30%'},
                                 className='box'),
                        html.Br(),
                        html.Div([
                            html.Div([
                                html.H2('Number of Athletes', style={'width':'10%', 'textAlign':'center', 'margin-left':'2%'}), 
                                html.H2('Total Medals', style={'margin-left':'6%'}),
                                html.H2('Gold Medals', style={'margin-left':'6%'}),
                                html.H2('Silver Medal', style={'margin-left':'7%'}),
                                html.H2('Bronze Medal', style={'margin-left':'7%'}),
                                html.H2('No Medals', style={'margin-left':'6%'}),
                            ],style={'width':'100%'}, className='row'),
                            html.Br(),
                            html.Div([
                                html.Label(
                                    id='n_athlets_teams',
                                    className='box3',
                                    style={'left': '1%'},
                                ),
                                html.Label(id='n_total_medal_teams',
                                           className='box3',
                                           style={'margin-left': '6%'}),
                                html.Label(id='n_gold_medal_teams',
                                           className='box3',
                                           style={'margin-left': '6%'}),
                                html.Label(id='n_silver_medal_teams',
                                           className='box3',
                                           style={'margin-left': '6%'}),
                                html.Label(id='n_bronze_medal_teams',
                                           className='box3',
                                           style={'margin-left': '6%'}),
                                html.Label(id='n_without_medal_teams',
                                           className='box3',
                                           style={'margin-left': '6%'}),
                            ],
                                     style={
                                         'width':'100%'
                                     }, className="row"),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Div([
                                slider_year_teams,
                                html.Div(id='slider-output-container')
                            ]),
                        ],
                                 style={
                                     'width': '70%',
                                     'justify-content': 'center'
                                 },
                                 className='box'),
                    ],
                             style={'margin-top': '15px'},
                             className='row'),
                    html.Div([
                        html.Div([
                            html.H2('Olympic City: '),
                            html.Label(id='games_city_teams', className='box'),
                        ],
                                 style={'justify-content': 'center'},
                                 className='row'),
                    ],
                             className='box'),
                    html.Div(
                        [
                            html.Div([
                                html.H4('Medals'),
                                html.Br(),
                                checklist_medals_teams,
                                dcc.Graph(id='bar_graph_teams'),
                            ],
                                     className='box',
                                     style={
                                         'width': '50%',
                                         'textAlign': 'center'
                                     }),
                            html.Div([dcc.Graph(id='bar_graph1_teams')],
                                     className='box',
                                     style={'width': '50%'}),
                        ],
                        style={'justify-content': 'center'},
                        className='row',
                    ),
                    
                ]),

            #ATHLETES
            dcc.Tab(label='ATHLETES',
                    style=tab_style,
                    selected_style=tab_selected_style,
                    children=[
                        html.Br(),
                         html.Div([
                        html.Label('Country Choice'),
                        dropdown_country_athletes,
                        html.Br(),
                        html.Label('Sport Choice'), dropdown_sport_athletes,
                        html.Br(),
                        html.Label('Year Choice'), year_slider_athletes,
                         ], style={'width':'97%', 'margin-left':'1%'}),
                        html.Br(),
                          html.Br(),
                        html.Div([
                        html.Div([
                            html.Div([dcc.Graph(id='graph_scatter_athletes')],
                                     className="nine columns", style={'height':'100%'}),
                            html.Div([dcc.Graph(id='graph_ratio_athletes')],
                                     className="eight columns", style={'height':'100%'}),
                      ], className="row", style={'height':'500px'})
                        ], className="box"),
                        html.Div([
                            html.Div([
                        dcc.Graph(id='graph_table_athletes')
                          ], style={'width':'90%', 'margin-left':'5%'}),
                          ], style={'width':'100%'}, className="box"),
                    ]),
        ],
        style=tabs_styles)
])

@app.callback(Output(component_id='world graph', component_property='figure'),
              Input(component_id='medal_drop_world',
                    component_property='value'))
def update_graph(medal):
    df1 = df.groupby(['region', 'NOC'])[medal].sum()
    df1 = df1.reset_index()
    a = df1[medal].values.tolist()
    print(df1.NOC)
    b = df1.NOC.values.tolist()

    data_choropleth = dict(
        type='choropleth',
        locations=df1.NOC,
        locationmode='ISO-3',
        z=a,
        text=df1['region'],
        colorscale='blues',
        zmin=0,
        zmax=500,
    )

    layout_choropleth = dict(
        geo=dict(
            scope='world',  # default
            projection=dict(type='equirectangular'),
            showland=True,  # default = True
            landcolor='white',
            lakecolor='white',
            showocean=True,  # default = False
            oceancolor='azure'),
        title=dict(
            x=.5  # Title relative position according to the xaxis, range (0,1)
        ))
    fig_choropleth = go.Figure(data=data_choropleth, layout=layout_choropleth)

    return fig_choropleth


@app.callback([
    Output("bar_graph_teams", "figure"),
    Output("bar_graph1_teams", "figure")
], [
    Input('country_drop_teams', 'value'),
    Input('sport_drop_teams', 'value'),
    Input('year_slider_teams', 'value'),
    Input('radioitems_teams', 'value')
])
#===================================================================================================================
def plots(countries, sport, year, medal):

    #=================================================First Bar Plot=====================================================
    df_loc = df.loc[(df['region'].isin(countries)) & (df['Sport'].isin(sport))
                    & (df['Year'] == year)]
    df_loc1 = df_loc.groupby(
        by=['Interval_Age', 'Sex'])[medal].sum().reset_index()

    trace1 = go.Bar(x=list(df_loc1[df_loc1.Sex == 'F']['Interval_Age']),
                    y=list(df_loc1[df_loc1.Sex == 'F'][medal]),
                    name='Female',
                    marker_color='#a60085')

    trace2 = go.Bar(x=list(df_loc1[df_loc1.Sex == 'M']['Interval_Age']),
                    y=list(df_loc1[df_loc1.Sex == 'M'][medal]),
                    name='Male',
                    marker_color='#00298a')

    data = [trace1, trace2]

    layout_bar = dict(
        title=dict(text='Number of Medals per Age and Sex'),
        yaxis=dict(title='Number of Medals'),
        xaxis=dict(title='Age'),
        paper_bgcolor='#f9f9f9',
        barmode='group',
    )

    #=================================================Second Bar Plot=====================================================
    df_loc = df.loc[(df['Year'] == year)]

    list_country = []

    list1 = []
    list2 = []
    list3 = []

    for country in countries:
        df_bar = df_loc.loc[(df_loc['region'] == country)
                            & (df['Sport'].isin(sport))]

        list_country.append(country)

        list1.append(df_bar['Gold'].sum())
        list2.append(df_bar['Silver'].sum())
        list3.append(df_bar['Bronze'].sum())

        trace1 = go.Bar(x=list1,
                        y=list_country,
                        name='Gold Medal',
                        orientation='h',
                        marker_color='#ffd700')

        trace2 = go.Bar(x=list2,
                        y=list_country,
                        name='Silver Medal',
                        orientation='h',
                        marker_color='#c0c0c0')

        trace3 = go.Bar(x=list3,
                        y=list_country,
                        name='Bronze Medal',
                        orientation='h',
                        marker_color='#cd7f32')

        data1 = [trace1, trace2, trace3]

        layout_bar1 = dict(title=dict(text='Medals per Country'),
                           yaxis=dict(title='Countries'),
                           xaxis=dict(title='Number of Medals'),
                           paper_bgcolor='#f9f9f9',
                           barmode='stack')

    if len(data1) == 0:
        data1 = []

    return go.Figure(data=data, layout=layout_bar),\
           go.Figure(data=data1, layout=layout_bar1),


#===================================================================================================================
@app.callback([
    Output('n_athlets_teams', 'children'),
    Output('n_total_medal_teams', 'children'),
    Output('n_gold_medal_teams', 'children'),
    Output('n_silver_medal_teams', 'children'),
    Output('n_bronze_medal_teams', 'children'),
    Output('n_without_medal_teams', 'children'),
    Output('games_city_teams', 'children')
], [
    Input("country_drop_teams", "value"),
    Input("year_slider_teams", "value"),
    Input("sport_drop_teams", "value"),
])
def indicator(countries, year, sport):
    df_loc = df.loc[(df['region'].isin(countries))
                    & (df['Sport'].isin(sport))].groupby(
                        ['Year']).sum().reset_index()

    if (len(df_loc.loc[df_loc['Year'] == year]['Number_Person'].values) == 0):
        value_1 = 0
    else:
        value_1 = df_loc.loc[df_loc['Year'] == year]['Number_Person'].values[0]

    if (len(df_loc.loc[df_loc['Year'] == year]['Total_Medal'].values) == 0):
        value_2 = 0
    else:
        value_2 = df_loc.loc[df_loc['Year'] == year]['Total_Medal'].values[0]

    if (len(df_loc.loc[df_loc['Year'] == year]['Gold'].values) == 0):
        value_3 = 0
    else:
        value_3 = df_loc.loc[df_loc['Year'] == year]['Gold'].values[0]

    if (len(df_loc.loc[df_loc['Year'] == year]['Gold'].values) == 0):
        value_4 = 0
    else:
        value_4 = df_loc.loc[df_loc['Year'] == year]['Silver'].values[0]

    if (len(df_loc.loc[df_loc['Year'] == year]['Bronze'].values) == 0):
        value_5 = 0
    else:
        value_5 = df_loc.loc[df_loc['Year'] == year]['Bronze'].values[0]

    if (len(df_loc.loc[df_loc['Year'] == year]['Sem_Medalha'].values) == 0):
        value_6 = 0
    else:
        value_6 = df_loc.loc[df_loc['Year'] == year]['Sem_Medalha'].values[0]

    if (len(df[(df['Year'] == year)]['City'].unique()) == 0):
        value_7 = 'Year without Olympic Games'
    else:
        value_7 = df[(df['Year'] == year)]['City'].unique()[0]


    return str('') + str(value_1), \
           str('') + str(value_2), \
           str('') + str(value_3), \
           str('') + str(value_4), \
           str('') + str(value_5), \
           str('') + str(value_6), \
           str('') + str(value_7)


#===================================================================================================================


@app.callback(
    [Output("graph3_teams", "figure"),
     Output("graph4_teams", "figure")], [
         Input('year_slider_world', 'value'),
     ])
#===================================================================================================================
def plots1(year):
    #=================================================First Scatter Plot=====================================================
    df_loc = df.loc[df['Year'] == year]

    dic = {}
    sorted_dict = {}

    if df_loc.empty:
        data = {
            'ID': [0],
            'Name': ['0'],
            'Sex': ['0'],
            'Age': [0],
            'Team': ['0'],
            'NOC': ['0'],
            'Games': ['0'],
            'Year': [0],
            'Season': ['0'],
            'City': ['0'],
            'Sport': ['0'],
            'Event': ['0'],
            'Medal': [0],
            'Height': [0],
            'Weight': [0],
            'region': ['0'],
            'Number_Person': [0],
            'Sem_Medalha': [0],
            'Gold': [0],
            'Silver': [0],
            'Bronze': [0],
            'Total_Medal': [0],
            'Interval_Age': ['0']
        }
        df_loc = pd.DataFrame.from_dict(data)

    for country in df_loc.region.unique():
        df1 = df_loc.loc[df_loc.region == country]['Total_Medal'].sum()

        dic[country] = df1

    sorted_keys = sorted(dic, key=dic.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = dic[w]

 #   sorted_dict = dict(itertools.islice(sorted_dict.items(), 10))

    trace_1 = go.Scatter(x=list(sorted_dict.values()),
                         y=list(sorted_dict.keys()),
                         mode='markers',
                         marker=dict(color='black', symbol='star', size=16))

    layout_scatter = dict(
        title=dict(text='Countries with more Medals'),
        yaxis=dict(title='Countries', autorange="reversed"),
        paper_bgcolor='#f9f9f9',
        xaxis=dict(
            title='Total of Medals',
            showgrid=False,
            showline=True,
            linecolor='rgb(102, 102, 102)',
            tickfont_color='rgb(102, 102, 102)',
            showticklabels=True,
            dtick=10,
            ticks='outside',
            tickcolor='rgb(102, 102, 102)',
        ),
    )

    data_scatter = [trace_1]

    #=================================================Second Scatter Plot=====================================================
    df_loc = df.loc[df['Year'] == year]

    dic = {}
    sorted_dict = {}

    if df_loc.empty:
        data = {
            'ID': [0],
            'Name': ['0'],
            'Sex': ['0'],
            'Age': [0],
            'Team': ['0'],
            'NOC': ['0'],
            'Games': ['0'],
            'Year': [0],
            'Season': ['0'],
            'City': ['0'],
            'Sport': ['0'],
            'Event': ['0'],
            'Medal': [0],
            'Height': [0],
            'Weight': [0],
            'region': ['0'],
            'Number_Person': [0],
            'Sem_Medalha': [0],
            'Gold': [0],
            'Silver': [0],
            'Bronze': [0],
            'Total_Medal': [0],
            'Interval_Age': ['0']
        }
        df_loc = pd.DataFrame.from_dict(data)

    for sport in df_loc.Sport.unique():
        df1 = df_loc.loc[df_loc.Sport == sport]['Number_Person'].sum()

        dic[sport] = df1

    sorted_keys = sorted(dic, key=dic.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = dic[w]

    sorted_dict = dict(itertools.islice(sorted_dict.items(), 10))

    trace_2 = go.Scatter(x=list(sorted_dict.values()),
                         y=list(sorted_dict.keys()),
                         mode='markers',
                         marker=dict(color='black', symbol='star', size=16))

    layout_scatter_1 = dict(
        title=dict(text='Sports with more People'),
        yaxis=dict(title='Sports', autorange="reversed"),
        paper_bgcolor='#f9f9f9',
        xaxis=dict(
            title='Total of People',
            showgrid=False,
            showline=True,
            linecolor='rgb(102, 102, 102)',
            tickfont_color='rgb(102, 102, 102)',
            showticklabels=True,
            dtick=100,
            ticks='outside',
            tickcolor='rgb(102, 102, 102)',
        ),
    )

    data_scatter_1 = [trace_2]

    return go.Figure(data=data_scatter, layout = layout_scatter), \
           go.Figure(data=data_scatter_1, layout = layout_scatter_1)


#===================================================================================================================


@app.callback([Output("graph5_teams", "figure")], [
    Input('year_slider_world', 'value'),
])
def plots1(year):
    #=================================================First Bar Plot=====================================================
    df_loc = df.loc[(df.Year == year)]
    df_loc = df_loc.groupby(['Sport',
                             'Season'])['Number_Person'].sum().reset_index()

    if df_loc.empty:
        data = {'Sport': ['0'], 'Season': ['0'], 'Number_Person': ['0']}
        df_loc = pd.DataFrame.from_dict(data)

    df_loc_winter_sport = df_loc[df_loc.Season == 'Winter']['Sport']
    df_loc_summer_sport = df_loc[df_loc.Season == 'Summer']['Sport']

    df_loc_number_person = df_loc['Number_Person'].to_list()

    trace1 = go.Scatter(x=df_loc_summer_sport,
                        y=df_loc_number_person,
                        name='Summer',
                        mode='markers',
                        marker_color='#ffd700')

    trace2 = go.Scatter(x=df_loc_winter_sport,
                        y=df_loc_number_person,
                        name='Winter',
                        mode='markers',
                        marker_color='#808080')

    layout_scatter = dict(
        title=dict(text='Number of People per Sport'),
        yaxis=dict(
            title='Number of People',
            dtick=200,
        ),
        xaxis=dict(
            title='Sports',
            showgrid=False,
            linecolor='rgb(102, 102, 102)',
            tickfont_color='rgb(102, 102, 102)',
            showticklabels=True,
            ticks='outside',
            tickcolor='rgb(102, 102, 102)',
        ),
    )

    data = [trace1, trace2]

    return go.Figure(data=data, layout=layout_scatter),


#=====================================================================================================================
@app.callback(dash.dependencies.Output('slider-output-container', 'children'),
              [dash.dependencies.Input('year_slider_teams', 'value')])
def update_output(value):
    return 'Year Selected: {}'.format(value)


#=====================================================================================================================

#=====================================================================================================================


@app.callback(
    Output(component_id="graph_scatter_athletes", component_property="figure"),
    Output(component_id="graph_ratio_athletes", component_property="figure"),
    Output(component_id="graph_table_athletes", component_property="figure"),
    Input(component_id='country_drop_athletes', component_property='value'),
    Input(component_id='sport_drop_athletes', component_property='value'),
    Input(component_id='year_slider_athletes', component_property='value'))
def plots(country, sport, year):

    list1 = []
    list1.append(country)

    list2 = []
    list2.append(sport)

    dff = df.loc[df['region'].isin(list1) & df['Sport'].isin(list2) &
                 (df['Year'] >= year[0]) & (df['Year'] <= year[1])]

    if dff.empty:
        data = []
        layout = dict()
        return go.Figure(data=data, layout=layout), go.Figure(
            data=data, layout=layout), go.Figure(data=data, layout=layout)

    events_df = dff.groupby([
        'Event'
    ])['ID'].count().reset_index(name='Records').sort_values(by='Records',
                                                             ascending=False)

    fig1 = px.bar(events_df,
                  y='Records',
                  x='Event',
                  text='Records',
                  labels={
                      "Records": "Participations Nr.",
                      "Event": "Events"
                  },
                  title="Number of Participations for each Event")

    fig1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig1.update_traces(marker_color='#00b153')

    fig1.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    ###############################Second Table###############
    dff['Medal'] = dff['Medal'].replace(
        ['Gold', 'Bronze', 'Silver', 'Sem Medalha'], [1, 1, 1, 0])

    groupby_df = dff.groupby(['Name'])['Medal'].sum().reset_index(
        name='Medals').sort_values(by='Medals', ascending=False).head(10)

    fig2 = go.Figure(data=[
        go.Table(header=dict(values=list(groupby_df.columns),
                             fill_color='#f01c00',
                             align='left'),
                 cells=dict(values=[groupby_df.Name, groupby_df.Medals],
                            fill_color='lavender',
                            align='left'))
    ])
    fig2.update_layout(title="Top 10 Athletes with the most Medals won")

    ###############################Third Gender Ratio######################
    #number_df = dff.groupby(['Sex','Year'])['ID'].count().reset_index(name='Records')

    df_area = pd.crosstab(dff['Year'], dff['Sex']).reset_index()

    if 'F' not in df_area:
        df_area['F'] = 0

    fig3 = go.Figure()
    fig3.add_trace(
        go.Scatter(x=df_area['Year'],
                   y=df_area['M'],
                   name='Male',
                   mode='lines',
                   line=dict(width=0.5, color='#0004ff'),
                   stackgroup='one',
                   groupnorm='percent'))
    fig3.add_trace(
        go.Scatter(x=df_area['Year'],
                   y=df_area['F'],
                   name='Female',
                   mode='lines',
                   line=dict(width=0.8, color='#a80087'),
                   stackgroup='one'))

    fig3.update_layout(title="Gender Ratio per Year",
                       yaxis=dict(type='linear', ticksuffix='%'))
    fig3.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig3.update_xaxes(title_text='Year')
    fig3.update_yaxes(title_text="Participation per Gender (%)",
                      range=(0, 100))

    fig1.update_layout(transition_duration=500)
    fig2.update_layout(transition_duration=500)
    fig3.update_layout(transition_duration=500)

    return fig1, fig2, fig3


if __name__ == '__main__':
    app.run_server(debug=True)
