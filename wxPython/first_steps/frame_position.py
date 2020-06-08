import wx

app = wx.App()

class moveFrame(wx.Frame):

    def __init__(self, parent, change_title):
        self.parent = parent
        self.change_title = change_title

        super().__init__(parent, title = change_title, size = (500, 500))

        self.Move(0, 0)

def main():

    x = moveFrame(None, "Custom Frame Position")
    x.Show()
    app.MainLoop()

main()