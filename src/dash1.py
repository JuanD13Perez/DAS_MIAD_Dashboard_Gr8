import plotly.express as px

def generate_visualizations(HA):
    #1
    edades_top = HA['Edad'].value_counts().head(10).reset_index(name='count')
    edades_top['Edad']=edades_top['Edad'].astype('str')
    fig_bar_edad = px.bar(edades_top, 
                          x='Edad',
                          y="count", 
                          orientation='v',
                          text='count',
                          title='<b>Distribución Edad</b>',
                          labels={'count': 'Count', 'index': 'Edad'},
                          color_discrete_sequence=['#86164a']
                          )
    fig_bar_edad.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    fig_bar_edad.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    #2
    evento_muerte = HA['Evento de muerte'].value_counts().reset_index(name='count')
    fig_bar_muerte = px.bar(evento_muerte, 
                          x='count',
                          y="Evento de muerte", 
                          orientation='h',
                          text='count',
                          title='<b>Pacientes que fallecieron</b>',
                          labels={'count': 'Count', 'index': 'Fallecieron'},
                          color='Evento de muerte',
                          color_discrete_map={
                                    "No": "#2e304b",
                                    "Si": "#86164a"}
                          )
    fig_bar_muerte.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    fig_bar_muerte.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    #3
    generos = HA['Sexo'].value_counts().reset_index(name='count')
    fig_donut_sexo = px.pie(generos, 
                             names='Sexo',  
                             values='count', 
                             color = 'Sexo',
                             color_discrete_map={
                                    "Hombre": "#2e304b",
                                    "Mujer": "#86164a"},
                             title='<b>Genero</b>',
                             hole=0.5)
    fig_donut_sexo.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))


    return fig_bar_edad,fig_bar_muerte,fig_donut_sexo