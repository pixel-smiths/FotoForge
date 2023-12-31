import tkinter as tk
import Tool



class Toolbar:
    def __init__(self, master, canvas, layers):
        self.tools = []
        self.master = master
        self.canvas = canvas
        self.line_color = "black"
        self.line_width = 2
        # create a frame for toolbar
        self.current_tool = None
        self.frame = tk.Frame(master, height=80, bg="#282828")
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.pen_tool = Tool.PenTool(canvas,self,layers)
        self.pen_button = tk.Button(self.frame, text="Pen", command=self.select_pen)
        self.pen_button.pack(side=tk.LEFT)

        self.textbox_tool = Tool.TextBoxTool(self.canvas,self,layers)
        self.textbox_button = tk.Button(self.frame, text="Text", command=self.select_textbox)
        self.textbox_button.pack(side=tk.RIGHT)

        self.Earaser_tool = Tool.EraserTool(self.canvas,self,layers)
        self.Earaser_button = tk.Button(self.frame, text="Eraser", command=self.Select_EraserTool)
        self.Earaser_button.pack(side=tk.RIGHT)


        self.margin = 8
        self.button_width = 64

    def set_line_color(self, color):
        self.line_color = color

    def set_line_width(self, width):
        self.line_width = width

    def add_tool(self, tool):
        # add tool to toolbar
        self.tools.append(tool)
        # set tool's index
        tool.index = len(self.tools) - 1

        # create a button for the tool
        tool.button = tk.Button(self.frame, text=tool.name, command=lambda: self.select_tool(tool))
        tool.button.pack(side=tk.LEFT, padx=self.margin, pady=self.margin)

    def select_pen(self):
        if self.current_tool == self.pen_tool:
            # If the pen tool is currently selected, deselect it
            print("Pen deselected")
            self.current_tool = None
            self.pen_tool.canvas.unbind("<ButtonPress-1>")
            self.pen_tool.canvas.unbind("<B1-Motion>")
            self.pen_tool.canvas.unbind("<ButtonRelease-1>")
        else:
            # If the pen tool is not currently selected, select it
            print("Pen selected")
            self.current_tool = self.pen_tool
            self.pen_tool.canvas.bind("<ButtonPress-1>", self.pen_tool.on_button_press)
            self.pen_tool.canvas.bind("<B1-Motion>", self.pen_tool.on_motion)
            self.pen_tool.canvas.bind("<ButtonRelease-1>", self.pen_tool.on_button_release)

    def select_textbox(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonPress-1>", self.textbox_tool.on_click)

    def Select_EraserTool(self):
        if self.current_tool == self.Earaser_tool:
            # If the pen tool is currently selected, deselect it
            print("Eraser deselected")
            self.current_tool = None
            self.Earaser_tool.canvas.unbind("<ButtonPress-1>")
            self.Earaser_tool.canvas.unbind("<B1-Motion>")
            self.Earaser_tool.canvas.unbind("<ButtonRelease-1>")
        else:
            # If the pen tool is not currently selected, select it
            print("Eraser selected")
            self.current_tool = self.Earaser_tool
            self.canvas.bind("<ButtonPress-1>", self.Earaser_tool.on_button_press)
            self.canvas.bind("<B1-Motion>", self.Earaser_tool.on_motion)
            self.canvas.bind("<ButtonRelease-1>", self.Earaser_tool.on_button_release)

    def select_tool(self, tool):
        # handle tool selection
        print(f"Tool selected: {tool.name}")
        # Add your tool selection logic here

    def get_tool(self, name):
        # get tool by name

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

