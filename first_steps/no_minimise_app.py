import wx

app = wx.App()


# Here style for minimising window is removed i.e. , style= wx.MINIMIZE_BOX
# Notes from zetcode.com
# Our intention was to display a window without a minimise box. So we did not specify this flag in the style parameter.

frame = wx.Frame(None, title="No Minimise Window", style= wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

frame.Show()

app.MainLoop()