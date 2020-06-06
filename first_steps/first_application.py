# My first python gui file.
# Learning from http://zetcode.com/wxpython
# Inspections specific for this py file is at http://zetcode.com/wxpython/firststeps/

# import the wxPython modules, such as core, controls, gdi (graphics device interface), windows etc.
import wx

# Creation of an application object. i.e. app
# Each wxPython program must have one application object.
app = wx.App()

# Creating of wx.frame object. It is an important container widget.
# The wx.Frame widget is parent widget to all widgets, it has no parents.
# If "None" is specified for a parent widget, it means that it doesn't have a parent.
# Constructor for wx.Frame has 7 parameters.
# "wx.Frame(# wx.Window 
# parent, 
# int id=-1, 
# string title='', 
# wx.Point pos=wx.DefaultPosition, 
# wx.Size size=wx.DefaultSize, 
# style=wx.DEFAULT_FRAME_STYLE, 
# string name="frame")"
frame = wx.Frame(None, title = "My First wxPython Application")

button = wx.Button(frame, label="I am a Button", name="Name")

# After we create the frame widget, must call the Show() method to actually display it on the screen.
frame.Show(True)
button.Show(False)

# Then we add the MainLoop line, the main loop is an endless cycle, it catches and dispatches all events that exist during the life of our application.

app.MainLoop()

# This was a very simplistic example. Despite this simplicity we can do quite a lot with this window. 
# We can resize the window, maximise it, minimise it. This functionality requires a lot of coding.
# All this is hidden and provided by default by the wxPython toolkit. There is no reason for reinventing the wheel.