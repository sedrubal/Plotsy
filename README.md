Plotsy
======

Lightweight ASCII plotting module for python

Documentation (I am new to writing docs, please help make the docs better):

    object.config((x, y)[, str])
        Define info about the graph. There are two parameters, one of which is optional.
        The first parameter is the height and width of the graph. This is written as a
        list or tuple, like [x, y]. The second, optional, parameter is the background.
        The background is an ASCII character, like "@" or " ". The default is " ".
        
    object.plot((x, y)[, str])
        Plot a point on the graph. There are two parameters, one of which is optional.
        The first parameter is the x and y or the point, written as a list or tuple,
        like [x, y]. The second, optional, parameter is the icon that is plotted. This
        is an ASCII character, like "@" or "#". The default is "#".
        
    object.draw()
        Print out the graph. Takes no parameters.

If you find a bug or can make a small change to make the module better, please fork this repo and commit your idea!
