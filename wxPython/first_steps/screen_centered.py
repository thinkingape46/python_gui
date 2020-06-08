import wx

screen_center_app = wx.App()

class screenCenter(wx.Frame):

    def __init__(self, parent, title):
        self.parent = parent
        self.title = title

        super().__init__(parent = parent, title = title)
        self.Center()

def main():

    x = screenCenter(parent=None, title="Window Centered")
    x.Show()
    screen_center_app.MainLoop()

main()