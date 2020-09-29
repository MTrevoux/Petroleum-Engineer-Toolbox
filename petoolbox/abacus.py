def abacus(func, parameter_range,x_plot_range, y_plot_range, \
           color_map = ['red','green','blue','orange'], parameter2_range = None, resolution = 1, \
           title = "", parameter_name = "", parameter2_name = "", unit = "", unit2="", xlabel = "", ylabel = "", \
           rotation = 90, transparancy_min = 0.35, xy_step = (10,10) , \
           figsize = (10,10), loc = 'best'):
    
    import matplotlib.pyplot as plt
    from matplotlib.colors import to_rgb
    from numpy import arange
    from numpy import mod
    
    '''
    func: function is under the form f(x,p,p2) /
    p: first parameter of the function
    p2: second parameter and is optional
    variables_range: list of list: [p_variables]
    '''
    plt.figure(figsize=figsize)
    
    RGB = to_rgb(color_map[0])
    COLOR_STEP = (1 - transparancy_min) / ( len(parameter_range) - 1 )
    COLOR_MAP = [transparancy_min + i*COLOR_STEP for i in range(0,len(parameter_range))]
    STEP = 0
    
    x = arange(x_plot_range[0], x_plot_range[1],resolution)
    
    if parameter2_range == None:
        for p in parameter_range:
            RGBA = list(RGB) + [COLOR_MAP[STEP]]
            f = [func(i,p) for i in x]
            plt.plot(x, f, color = RGBA, label = f'{parameter_name} {p} {unit}' )
            STEP = STEP +1
    else:
        STEP2 = 0
        for p2 in parameter2_range:
            STEP = 0
            RGB = to_rgb( color_map[ mod(STEP2, len(color)) ] )
            for p in parameter_range:
                RGBA = list(RGB) + [COLOR_MAP[STEP]]
                f = [func(i,p,p2) for i in x]
                plt.plot(x, f, color = RGBA, label = f'{parameter2_name} {p2} {unit2} / {parameter_name} {p} {unit}' )
                STEP = STEP +1
            STEP2 = STEP2 +1
    
    XSTEP = int((x_plot_range[1] - x_plot_range[0]) / xy_step[0]) + 1
    YSTEP = int((y_plot_range[1] - y_plot_range[0]) / xy_step[1]) + 1
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f'{parameter_name} paramater in range {parameter_range} {unit}')
    plt.xticks(rotation=rotation)
    
    plt.ylim(bottom = y_plot_range[0], top = y_plot_range[1])
    plt.xticks(arange(x_plot_range[0], XSTEP * xy_step[0] , step=xy_step[0]))
    plt.yticks(arange(y_plot_range[0], YSTEP * xy_step[1] , step=xy_step[1]))
    
    plt.legend(loc = loc)
    plt.grid()
    plt.show()
