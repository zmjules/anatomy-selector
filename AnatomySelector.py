#!/usr/bin/python3

from tkinter import *
import BodyStructure
from anytree import Node, RenderTree, PreOrderIter

class MyGUI:
    
    def __init__(self, master):
        self.master = master
        
        # Create tree with data nodes
        self.bStructure = BodyStructure.createBodyStructure()

        # Create dictionary to associate a node ID with the state of its corresponding checkbox
        self.checkboxes = {}
    
        # Set window options
        master.title("Anatomy Selector")
        master.geometry("700x400")

         # Draw static buttons
        self.label = Label(master, text="Select a Region:").grid(row=2, sticky=W)

        self.selectAllBtn = Button(root, text='Select All', command=self.selectAll).grid(row=40, sticky = W)

        self.deselectAllBtn = Button(root, text='Reset', command=self.deselectAll).grid(row=42, sticky = W)

        # Draw tree, define checkbox state variable, and define function for when a button is clicked
        i = 1
        for node in PreOrderIter(self.bStructure):
            var = IntVar()
            tmpCheckBtn = Checkbutton(master, text=node.name, variable=var, command=lambda name = node.id: self.onclick(name)).grid(row=i+2, column= node.depth+1, sticky=W)
            i += 1
            self.checkboxes[node.id] = var
    
    # Check the state of a checkbox associated with a node ID        
    def buttonState(self,id):
            s = 0
            for key, value in self.checkboxes.items():
                    if key == id:
                       btn = self.checkboxes[key]
                       s = btn.get() 
            return s

    # Select a checkbox and all of its ancestor checkboxes
    def select(self,id):
        # find node in tree, then get its ancestors
        ancestors = ()
        for node in PreOrderIter(self.bStructure):
            if node.id==id:
                ancestors = node.ancestors

        # check off the boxes for all of the ancestors
        for ancestor in ancestors:
            for key, value in self.checkboxes.items():
                if ancestor.id == key:
                    tmpBtn = self.checkboxes[key]
                    tmpBtn.set(1)

    # Deselect a checkbox and all of its descendant checkboxes
    def deselect(self,id):
        # find node in tree, then get its descendants
        descendants = ()
        for node in PreOrderIter(self.bStructure):
            if node.id==id:
                descendants = node.descendants

        # uncheck the boxes for all of the descendants
        for descendant in descendants:
            for key, value in self.checkboxes.items():
                if descendant.id == key:
                    tmpBtn = self.checkboxes[key]
                    tmpBtn.set(0)

    # Callback function when an individual checkbox is clicked               
    def onclick(self,id):
        if self.buttonState(id) == 1:
            self.select(id)
        else:
            self.deselect(id)
        
    # Checks off all boxes when Select All is clicked 
    def selectAll(self): 
        for key, value in self.checkboxes.items():
            tmpBtn = self.checkboxes[key]
            tmpBtn.set(1)

    # Checks off all boxes when Reset is clicked
    def deselectAll(self):
        for key, value in self.checkboxes.items():
            tmpBtn = self.checkboxes[key]
            tmpBtn.set(0)


root = Tk()
my_gui = MyGUI(root)
root.mainloop()