import wx
from textwrap import wrap

class PyColorGUI(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="PyColor")
        self.SetSize(280, 130)
        self.mainPanel = wx.Panel(self)

        self.staticRGB = wx.StaticText(self.mainPanel, label="RGB : ")
        self.textRGB = wx.TextCtrl(self.mainPanel, value="255, 255, 255")
        self.staticHEX = wx.StaticText(self.mainPanel, label="HEX : ")
        self.textHEX = wx.TextCtrl(self.mainPanel, value="#ffffff")

        self.gridSizer = wx.GridSizer(rows=2, cols=2, hgap=5, vgap=5)
        self.gridSizer.Add(self.staticRGB)
        self.gridSizer.Add(self.textRGB, 0, wx.EXPAND)
        self.gridSizer.Add(self.staticHEX)
        self.gridSizer.Add(self.textHEX, 0, wx.EXPAND)

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.gridSizer, 1, wx.EXPAND|wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_TEXT, self.OnTextChangeRGB, self.textRGB)
        self.Bind(wx.EVT_TEXT, self.OnTextChangeHEX, self.textHEX)
        self.ChangeColorRGB()

    def rgbToHex(self, int1, int2, int3):
        a = str(hex(int1)).replace("0x", "")
        b = str(hex(int2)).replace("0x", "")
        c = str(hex(int3)).replace("0x", "")

        if len(a) == 1:
            a = "0" + a
        if len(b) == 1:
            b = "0" + b
        if len(c) == 1:
            c = "0" + c

        hexInString = "#" + a + b + c
        return hexInString

    def hexToRGB(self, hex):
        int1 = None
        int2 = None
        int3 = None
        hexInList = wrap(hex.replace("#", ""), 2)
        rgbFrame = "{0}, {1}, {2}"

        for string in hexInList:
            if not int1:
                int1 = str(int(string, 16))
            elif not int2:
                int2 = str(int(string, 16))
            elif not int3:
                int3 = str(int(string, 16))

        return rgbFrame.format(int1, int2, int3)

    def OnTextChangeRGB(self, e):
        self.ChangeColorRGB();

    def OnTextChangeHEX(self, e):
        self.ChangeColorHEX();

    def ChangeColorRGB(self):
        rgbValue = self.textRGB.GetValue()
        if rgbValue.count(", ") == 2:
            r = None
            g = None
            b = None
            splitedRGB = str(rgbValue).split(", ")
            for num in splitedRGB:
                if not r:
                    r = str(num)
                elif not g:
                    g = str(num)
                elif not b:
                    b = str(num)
            self.textHEX.SetValue(self.rgbToHex(int(r), int(g), int(b)))
            self.mainPanel.SetBackgroundColour(wx.Colour(int(r), int(g), int(b)))
            self.mainPanel.Refresh()

    def ChangeColorHEX(self):
        hexValue = self.textHEX.GetValue()

        if not hexValue.startswith("#"):
            hexValue = "#"+hexValue

        if len(hexValue) == 7:
            responseRGB = self.hexToRGB(hexValue)
            r = None
            g = None
            b = None
            splitedRGB = str(responseRGB).split(", ")
            for num in splitedRGB:
                if not r:
                    r = str(num)
                elif not g:
                    g = str(num)
                elif not b:
                    b = str(num)

            rgbFrame = "{0}, {1}, {2}"
            self.textRGB.SetValue(rgbFrame.format(r, g, b))
            self.mainPanel.SetBackgroundColour(wx.Colour(int(r), int(g), int(b)))
            self.mainPanel.Refresh()


if __name__ == "__main__":
    app = wx.App()
    frame = PyColorGUI()
    frame.Show()

    app.MainLoop()