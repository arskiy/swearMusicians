import matplotlib.pyplot as plt

def makegraph(data, artists, fieldname, destination = "f"):
    """
    Inputs: 
    data object (dict), 
    artists (list of artist names as strings), 
    fieldname (which field of data object you wish graph to be plotted against.)
    destination (string) one of: 's': to output graph to screen or 'f': output graph to png file. (default : file)
    
    Output: 
    Horizontal Bargraph of artists vs fieldname given.
    
    Example Input:
    data ={'Number of Words': [254388, 31023, 6981], 'Number of slangs': [7922, 1466, 154], 'Average of words until a slang': [32, 21, 45]}
    artists = ['50_cent', '21_savage', 'B-Real']
    makegraph(data, artists, 'Number of Words', 's')
    
    This will plot a graph of rappers vs Number of words on the screen.
    """    
    # The parameter to plot on the x-axis.
    x_parameter = data[fieldname]

    # Setting the theme to use for the plot.
    plt.style.use('seaborn')
    # Variables to refer to the figure and the axes for separate customization (fontsize etc)
    fig, ax = plt.subplots()
    ax.barh(artists, x_parameter)
    labels = [ax.get_xticklabels(),ax.get_yticklabels()]
    plt.setp(labels,fontsize=12)
    plt.xlabel(fieldname ,fontsize =18)
    plt.title("Comparison of rappers " + fieldname, fontsize = 20)
    
    if destination == "s":
        # plt.show() draws the graph to screen.
        plt.show()
    elif destination == "f":
        # Saves the figure to file, the dpi is quality, the bbox tight makes the figure not get cropped out.
        fig.savefig("fig.png", dpi=180, bbox_inches="tight")




