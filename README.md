# Interactive visualizations for Ultrafast Optics 
This repo contains my exploration of different frameworks for interactive physics visualizations. 


## Thoughts on methods attempted so far:

### Bokeh app
Running the app requires a server. Each update of the plot requires a callback to the server. This means that the server can get overloaded with multiple users interacting with a simulation. Front loading a lot of the data into the client side might be able to lower the load on the server during callbacks, but it will likely make the loading time too long. 
In terms of integration in a jupyter notebook: the server can serve and Jupyter notebooks might be able to process embedding of the client. 
Open source. 

### Bokeh static
Running this doesn't require a server. Interactions with the figure trigger javascript functions. The calculation of new data and the update of the plot all happen in the browser on the client side. No callbacks to a server needed. This means that the user experience will solely depend on the browser ability of the user and won't be affected when multiple users interact with the visualization. The static HTML which is outputed from running the code can be intergrated in a Jupyter notebook. The main headache is coding up the javascript functions for the plot updates. I don't actually know Javascript. It's too different from C/C++ for me to be able to just intuitively be able to code in it. 
Open source.

### Bokeh in notebook 
I don't know much about the server requirement for this option. The nice thing is that no integration is needed. The output renders directly in notebook, which I assume will be propegated forward when the notebook is knit into a webpage. The syntax is similar to the Bokeh app and is fully Python. 
Open source.
**For some reason it only works on port 8888. Check if deployment port matches**

### Dash app (from plotly)
The dash app requires a server. The open source version can be easily run locally on the localhost. However, deployment to a server might require enterprise access or building our own server. Dash functions and libraries are well documented and the callback is easy and intuitive. The default look of the visualizations seems very "large dataset" oriented, which looks weird for physics visualizations. However, changing the CSS and HTML is easy enough. One advantage over the Bokeh app is the ability to explicitly layout the page with HTML tags. User experience and loading is smooth on the localhost app, but unclear how it will scale with deployment. 

### Dash in notebook
The new version of Dash runs in a Jupyter notebook without need to change anything or use special Jupyter rendering. Ease of coding and maintaining is identicle to the Dash app. The layout is nice, but the HTML tags look awkward in the Jupyter layout cell. Unclear how this option interacts with the deployment, but if I had to guess, the knitting of Jupyter book will bypass the need for a server. 