import wx

app = wx.App()


# Here style for minimising window is removed i.e. , style= wx.MINIMIZE_BOX
frame = wx.Frame(None, title="No Minimise", style= wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

frame.Show()

app.MainLoop()