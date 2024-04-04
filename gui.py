
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import keyboard
import re
from algorytm import algorytm2,transform_object
import json


class GraphEditor:
    """
    A class representing a graph editor.

    Attributes:
        vertices (list): A list of vertices in the graph.
        edges (list): A list of edges in the graph.
        path (list): A list representing the path in the graph.
        root (tkinter.Tk): The root window of the graph editor.
        canvas (tkinter.Canvas): The canvas widget for drawing the graph.

    Methods:
        __init__(): Initializes the GraphEditor class.
        add_vertex(event): Adds a vertex to the graph.
        remove_vertex(event): Removes a vertex from the graph.
        drag_vertex(event): Drags a vertex in the graph.
        draw_graph(): Draws the graph on the canvas.
        distance(x1, y1, x2, y2): Calculates the distance between two points.
        clear_canvas(event): Clears the canvas.
        save_vertices(event): Saves the vertices to a file.
        load_vertices(event): Loads the vertices from a file.
        check_vertices(event): Checks the validity of the vertices in the graph.
    """

    def __init__(self):
        """
        Initializes the GraphEditor class.

        Creates the root window and canvas widget for drawing the graph.
        Binds various events to the canvas and root window.
        """
        self.vertices = []
        self.edges = []
        self.path = []

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Set canvas to fill the window
        self.canvas.bind("<Button-1>", self.add_vertex)
        self.canvas.bind("<Button-3>", self.remove_vertex)
        self.canvas.bind("<B1-Motion>", self.drag_vertex)  # Added binding for dragging vertex
        self.root.bind("<F5>", self.check_vertices)  # Added binding for F5
        self.root.bind("<Control-n>", self.clear_canvas)  # Added binding for Ctrl+N
        self.root.bind("<Control-s>", self.save_vertices)  # Added binding for Ctrl+S
        self.root.bind("<Control-o>", self.load_vertices)  # Added binding for Ctrl+O
        
        self.root.mainloop()

    # Rest of the code...
class GraphEditor:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.path = []

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Set canvas to fill the window
        self.canvas.bind("<Button-1>", self.add_vertex)
        self.canvas.bind("<Button-3>", self.remove_vertex)
        self.canvas.bind("<B1-Motion>", self.drag_vertex)  # Added binding for dragging vertex
        self.root.bind("<F5>", self.check_vertices)  # Added binding for F5
        self.root.bind("<Control-n>", self.clear_canvas)  # Added binding for Ctrl+N
        self.root.bind("<Control-s>", self.save_vertices)  # Added binding for Ctrl+S
        self.root.bind("<Control-o>", self.load_vertices)  # Added binding for Ctrl+O
        
        self.root.mainloop()
    
    def add_vertex(self, event):
        if keyboard.is_pressed('ctrl'):
            return
        x, y = event.x, event.y
        d = True
        for vertex in self.vertices:
            if self.distance(x, y, vertex["x"], vertex["y"]) <= 20: 
                neighbors = tk.simpledialog.askstring("Edytuj listę sąsiedztwa", "Edytuj listę sąsiedztwa wierzchołka (oddzielone przecinkami):", initialvalue=",".join([f"{key}:{value}" for key, value in vertex["neighbors"].items()]))
                if neighbors is not None and neighbors.replace(" ","") != "":
                    neighbors=neighbors.replace(" ","").upper().replace(';',',').replace(',,',',').replace('::',':')
                    vertex["neighbors"] = {}
                    for neighbor in neighbors.split(","):
                        if ":" in neighbor:
                            name, weight = neighbor.split(":")
                        elif len(neighbor) > 0:
                            name, weight = neighbor, 0
                        vertex["neighbors"][name] = float(weight)
                    self.path = []
                    self.draw_graph()
                d = False
                break
        if d:
            name = tk.simpledialog.askstring("Podaj nazwę wierzchołka", "Podaj nazwę wierzchołka:", parent=self.root)
            if name:
                neighbors = tk.simpledialog.askstring("Podaj listę sąsiedztwa wierzchołka", "Podaj listę sąsiedztwa wierzchołka (oddzielone przecinkami):", parent=self.root)
                if neighbors is not None:
                    neighbors=neighbors.replace(" ","").upper().replace(';',',').replace(',,',',').replace('::',':')
                    neighbors = neighbors.split(",")
                    vertex = {
                        "name": name,
                        "x": x,
                        "y": y,
                        "neighbors": {}
                    }
                    for neighbor in neighbors:
                        if ":" in neighbor:
                            name, weight = neighbor.split(":")
                            vertex["neighbors"][name] = float(weight)
                        elif len(neighbor) > 0:
                            vertex["neighbors"][neighbor] = 0
                    self.vertices.append(vertex)
                    self.path = []
                    self.draw_graph()
    
    def remove_vertex(self, event):
        if keyboard.is_pressed('ctrl'):
            return
        x, y = event.x, event.y
        
        for vertex in self.vertices:
            if self.distance(x, y, vertex["x"], vertex["y"]) <= 20:
                confirm = messagebox.askquestion("Potwierdzenie", "Czy na pewno chcesz usunąć wierzchołek {}?".format(vertex["name"]), parent=self.root)
                if confirm == "yes":
                    self.vertices.remove(vertex)
                    self.path = []
                    self.draw_graph()
                break
    
    def drag_vertex(self, event):
        x, y = event.x, event.y
        
        for vertex in self.vertices:
            if self.distance(x, y, vertex["x"], vertex["y"]) <= 20:
                vertex["x"] = x
                vertex["y"] = y
                self.draw_graph()
                break
    
    def draw_graph(self):
        self.canvas.delete("all")
        
        for vertex in self.vertices:
            x, y = vertex["x"], vertex["y"]
            name = vertex["name"]
            
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="white")
            self.canvas.create_text(x, y, text=name)
            
            for neighbor, weight in vertex["neighbors"].items():
                for v in self.vertices:
                    if v["name"] == neighbor:
                        radius = 20
                        dx = v["x"] - x
                        dy = v["y"] - y
                        length = (dx ** 2 + dy ** 2) ** 0.5
                        if length > radius:
                            dx = dx * radius / length
                            dy = dy * radius / length
                        self.canvas.create_line(x+dx, y+dy, v["x"]-dx, v["y"]-dy, arrow=tk.LAST,width=3)
                        self.canvas.create_text((x+dx+v["x"]-dx)/2, (y+dy+v["y"]-dy)/2+10, text=str(weight))
            
            if vertex["name"] in vertex["neighbors"]:
                self.canvas.create_line(x-20, y, x+20, y, arrow=tk.LAST)
        if len(self.path) > 0:
            for i in range(len(self.path)-1):
                for vertex in self.vertices:
                    if vertex["name"] == self.path[i]:
                        x1, y1 = vertex["x"], vertex["y"]
                    if vertex["name"] == self.path[i+1]:
                        x2, y2 = vertex["x"], vertex["y"]
                dx=x2-x1
                dy=y2-y1
                radius=20
                length = (dx ** 2 + dy ** 2) ** 0.5
                if length > radius:
                    dx = dx * radius / length
                    dy = dy * radius / length
                self.canvas.create_line(x1+dx, y1+dy, x2-dx, y2-dy, fill="red", width=2,arrow=tk.LAST)
        
    def distance(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def clear_canvas(self, event):
        confirm = messagebox.askquestion("Potwierdzenie", "Czy na pewno chcesz wyczyścić płutno?", parent=self.root)
        if confirm == "yes":
            self.vertices = []
            self.draw_graph()
            self.path = []
    
    def save_vertices(self, event):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                json.dump(self.vertices, file)
    
    def load_vertices(self, event):
        filename = tk.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "r") as file:
                self.vertices = json.load(file)
            self.draw_graph()
    
    def check_vertices(self, event):
        wierzcholki=[]
        laczenia=[]
        for vertex in self.vertices:
            wierzcholki.append(vertex["name"])
            for neighbor, _ in vertex["neighbors"].items():
                laczenia.append(neighbor)
        
        existing_vertices = wierzcholki
        
        
        missing_vertices = [vertex for vertex in laczenia if vertex not in existing_vertices]
        
        if missing_vertices:
            messagebox.showinfo("Brakujące wierzchołki", f"Następujące wierzchołki nie istnieją na planszy: {', '.join(missing_vertices)}", parent=self.root)
        else:
            start_vertex = simpledialog.askstring("Podaj wierzchołek początkowy", "Podaj nazwę wierzchołka początkowego:", parent=self.root)
            end_vertex = simpledialog.askstring("Podaj wierzchołek końcowy", "Podaj nazwę wierzchołka końcowego:", parent=self.root)
            start_vertex = start_vertex.upper().replace(" ","")
            end_vertex = end_vertex.upper().replace(" ","")
            if start_vertex not in existing_vertices:
                messagebox.showinfo("Błąd", f"Wierzchołek początkowy '{start_vertex}' nie istnieje na planszy.", parent=self.root)
            elif end_vertex not in existing_vertices:
                messagebox.showinfo("Błąd", f"Wierzchołek końcowy '{end_vertex}' nie istnieje na planszy.", parent=self.root)
            else:
                msg,self.path=algorytm2(transform_object(self.vertices), start_vertex, end_vertex)
                messagebox.showinfo("Wynik", msg, parent=self.root)
                self.draw_graph()



if __name__ == "__main__":
    editor = GraphEditor()
