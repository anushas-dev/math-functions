import numpy as np
import matplotlib.pyplot as plot

_graph = input("Enter math function to plot graph for: ")
if _graph == 'sine': 
    x = np.arange(0, 20, 0.1);
    amplitude   = np.sin(x)
    plot.plot(x, amplitude)
    plot.title('Sine wave')
    plot.xlabel('x ->')
    plot.ylabel('sin(time)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()

if _graph == 'cosine': 
    x = np.arange(0, 20, 0.1);
    amplitude   = np.cos(x)
    plot.plot(x, amplitude)
    plot.title('Cosine wave')
    plot.xlabel('x ->')
    plot.ylabel('Cosine(x)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()

if _graph == 'square': 
    x = np.arange(0, 20, 0.1);
    amplitude   = np.square(x)
    plot.plot(x, amplitude)
    plot.title('Square wave')
    plot.xlabel('x ->')
    plot.ylabel('square(x)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()

if _graph == 'log': 
    x = np.arange(0, 20, 0.1);
    amplitude   = np.log(x)
    plot.plot(x, amplitude)
    plot.title('Log wave')
    plot.xlabel('x ->')
    plot.ylabel('log(x)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()

if _graph == 'mod': 
    x = np.arange(0, 20, 0.1);
    amplitude   = np.mod(x,2)
    plot.plot(x, amplitude)
    plot.title('Mod wave')
    plot.xlabel('x ->')
    plot.ylabel('mod(x)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()

if _graph == 'sqrt': 
    x = np.arange(0, 20, 0.1);
    amplitude   = np.sqrt(x)
    plot.plot(x, amplitude)
    plot.title('Sqrt wave')
    plot.xlabel('x ->')
    plot.ylabel('sqrt(x)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()