import plotly.express as px
import pandas as pd

def generate_visualizations(HA):
    #1
    line2_combined = round(HA.groupby('Edad').agg({'Creatina':'mean', 'Fracción de Eyección':'mean'}),2).reset_index()
    
    fig_line_combined = px.line(line2_combined,
                                x='Edad',
                                y=['Creatina', 'Fracción de Eyección'],
                                title='<b>Creatina en suero y fracción de eyección promedio por edad</b>',
                                markers=True,
                               color_discrete_sequence=['#2e304b', '#86164a'])
    fig_line_combined.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    #2
    ss = HA.groupby('Sodio sérico').size().reset_index(name='count')

    fig_bar_ss = px.bar(ss, 
                          x='count',
                          y="Sodio sérico", 
                          orientation='h',
                          text='count',
                          title='<b>Niveles de sodio sérico</b>',
                          labels={'count': 'Count', 'index': 'Nro. Pacientes'},
                          color_discrete_sequence=['#86164a']
                       )
    fig_bar_ss.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    fig_bar_ss.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    #3
    plaquet = HA.groupby('Edad').agg({'Plaquetas':'mean'}).reset_index()

    fig_bar_plaquet = px.bar(plaquet, 
                          x='Edad',
                          y="Plaquetas", 
                          orientation='v',
                          text='Plaquetas',
                          title='<b>Número de plaquetas promedio por edad</b>',
                          labels={'Plaquetas': 'Plaquetas', 'index': 'Edad'},
                          color_discrete_sequence=['#2e304b']
                       )
    fig_bar_plaquet.update_layout(paper_bgcolor='#8889a9', plot_bgcolor='#8889a9', font=dict(color='#d9d9d9'))
    fig_bar_plaquet.update_traces(texttemplate='%{text:.0f}', textposition='outside')
        
    return fig_line_combined, fig_bar_ss, fig_bar_plaquet