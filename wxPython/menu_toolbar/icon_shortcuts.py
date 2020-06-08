import wx

APP_EXIT = 1

class simple_menu(wx.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        # Create menu bar
        menu_bar = wx.MenuBar()

        # Create file menu
        file_menu = wx.Menu()

        # Create a Menu Item
        # & specifies the acclerator key.
        # Ctrl+Q is short for quitting
        qmi = wx.MenuItem(file_menu, APP_EXIT, "&Quit\tCtrl+Q")
        # Apply the method "SetBitmap" to provide a icon.
        qmi.SetBitmap(wx.Bitmap("exit.png"))
        # qmi is now appended to file_menu
        file_menu.Append(qmi)

        # Bind the 
        self.Bind(wx.wxEVT_MENU, self.OnQuit, id = APP_EXIT)

        menu_bar.Append(file_menu, "&File")

        self.SetMenuBar(menu_bar)

    def OnQuit(self, e):
        self.Close()    

def main():

    app_a = wx.App()
    frame = simple_menu(None, title="Icons")
    frame.Show()
    app_a.MainLoop()

main()
