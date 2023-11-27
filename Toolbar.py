import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

class Toolbar:
    def __init__(self, master):
        self.tools = []
        self.master = master

        # create a frame for toolbar
        self.frame = tk.Frame(master, height=80, bg="#282828")
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.margin = 8
        self.button_width = 64

    def add_tool(self, tool):
        # add tool to toolbar
        self.tools.append(tool)
        # set tool's index
        tool.index = len(self.tools) - 1

        # create a button for the tool
        tool.button = tk.Button(self.frame, text=tool.name, command=lambda: self.select_tool(tool))
        tool.button.pack(side=tk.LEFT, padx=self.margin, pady=self.margin)

    def select_tool(self, tool):
        # handle tool selection
        print(f"Tool selected: {tool.name}")
        # Add your tool selection logic here

    def get_tool(self, name):
        # get tool by name
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None

