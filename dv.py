#import plotly.express as px

#df=px.data.iris()
#print(df)
#fig=px.scatter(df,x='sepal_width',y='sepal_length',color='species',size='petal_length',hover_data=['petal_width'])
#fig.show()
#--------------------------------


#import plotly.graph_objects as go
#import numpy as np

#x=np.linspace(-5,5,100)
#y=np.linspace(-5,5,100)
#x,y=np.meshgrid(x,y)
#z=np.sin(np.sqrt(x**2 + y**2))

#create 3d surface plot 
#fig=go.Figure(data=[go.Surface(z=z,x=x,y=x)])
#fig.update_layout(title='3D Surface Plot',autosize=False,width=600,height=500,margin=dict(l=65,r=50,b=65,t=90))
#fig.show()
#-----------------------------


import plotly.express as px 
df=px.data.gapminder().query("year == 2007")
print(df)
fig= px.choropleth(df,locations="iso_alpha",color='lifeExp',hover_name='country',projection='natural earth')
fig.show()