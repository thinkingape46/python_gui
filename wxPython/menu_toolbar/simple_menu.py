import wx

class simpleMenu(wx.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        # Create menu bar
        menu_bar = wx.MenuBar()

        # Add menu item "file_menu"
        file_menu = wx.Menu()
        # Append "file_menu" to "menu_bar"
        menu_bar.Append(file_menu, '&File')

        # Creat file item and append to file_menu in one step
        file_item = file_menu.Append(wx.ID_EXIT, "Quit", "Quit Application")

        #  we call the SetMenuBar() method. This method belongs to the wx.Frame widget. It sets up the menubar.
        self.SetMenuBar(menu_bar)

        # We bind the wx.EVT_MENU of the menu item to the custom OnQuit() method. This method will close the application.
        # Binding wx.EVT_MENU to file_item i.e. quit
        self.Bind(wx.EVT_MENU, self.onQuit, file_item)

        # Center the window on the screen.
        self.Center()

    def onQuit(self, e):
        self.e = e
        self.Close()

def main():

    app = wx.App()
    frame = simpleMenu(parent = None, title = "Simple Menu")
    frame.Show()
    app.MainLoop()

main()