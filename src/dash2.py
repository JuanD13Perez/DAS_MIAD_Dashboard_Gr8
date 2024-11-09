import plotly.express as px
def generate_visualizations(HA):
    #1
    anemia = HA['Anemia'].value_counts().reset_index(name='count')
    fig_donut_anemia = px.pie(anemia, 
                             names='Anemia',  
                             values='count', 
                             color = 'Anemia',
                             color_discrete_map={
                                    "Si": "#2e304b",
                                    "No": "#86164a"},
                             title='<b>Anemia</b>',
                             hole=0.5)
    fig_donut_anemia.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    #2
    Diabetes = HA['Diabetes'].value_counts().reset_index(name='count')
    fig_donut_diabetes = px.pie(Diabetes, 
                             names='Diabetes',  
                             values='count', 
                             color = 'Diabetes',
                             color_discrete_map={
                                    "Si": "#2e304b",
                                    "No": "#86164a"},
                             title='<b>Diabetes</b>',
                             hole=0.5)
    fig_donut_diabetes.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    #3
    HA['Hipertension'] = HA['Presión en la sangre - Hipertensión']
    Hipertension = HA['Hipertension'].value_counts().reset_index(name='count')
    fig_donut_hipertension = px.pie(Hipertension, 
                             names='Hipertension',  
                             values='count', 
                             color = 'Hipertension',
                             color_discrete_map={
                                    "Si": "#2e304b",
                                    "No": "#86164a"},
                             title='<b>Hipertension</b>',
                             hole=0.5)
    fig_donut_hipertension.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    #4
    Fumador = HA['Fumador'].value_counts().reset_index(name='count')
    fig_donut_fumador = px.pie(Fumador, 
                             names='Fumador',  
                             values='count', 
                             color = 'Fumador',
                             color_discrete_map={
                                    "Si": "#2e304b",
                                    "No": "#86164a"},
                             title='<b>Fumador</b>',
                             hole=0.5)
    fig_donut_fumador.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    #5
    tiempo = HA.groupby('Tiempo').size().reset_index(name='count').sort_values(by ='Tiempo')

    fig_line_count = px.line(tiempo, x='Tiempo', y='count', title='<b>¿Cuanto tiempo de seguimiento tuvieron los pacientes?</b>')
    fig_line_count.update_traces(line=dict(color='#86164a'))
    fig_line_count.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    return fig_donut_anemia, fig_donut_diabetes, fig_donut_fumador, fig_donut_hipertension, fig_line_count