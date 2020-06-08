import wx


class sizing(wx.Frame):

    def __init__(self, parent, title):
        self.parent = parent
        self.title = title

        #  super() is useful for accessing inherited methods that have been overridden in a class.
        # The search order is same as that used by getattr() except that the type itself is skipped.
        # The current sizing class has inherited "wx.Frame", so when we use the keyword "super" we are calling the wx.Frame class.
        # And the giving the parameters "title" and "size"
        # I removed the parameter title, it still works.
        super(sizing, self).__init__(parent, title = title, size = (640, 360))

def main():

    app = wx.App()
    frame = sizing(None, title="Custom Window Size")
    frame.Show()

    app.MainLoop()

main()


