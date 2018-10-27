#!/usr/bin/python3

from anytree import Node, RenderTree

# Create tree structure for data	
def createBodyStructure():
	chest = Node("Chest", id=0)
	lungs = Node("Lungs", id=1, parent=chest)
	rLung = Node("Right Lung", id=2, parent=lungs)
	lLung = Node("Left Lung", id=3, parent=lungs)
	rSupLobe = Node("Superior Lobe", id=4, parent=rLung)
	midLobe = Node("Middle Lobe", id=5, parent=rLung)
	rInfLobe = Node("Inferior Lobe", id=6, parent=rLung)
	lSupLobe = Node("Superior Lobe", id=7, parent=lLung)
	rInfLobe = Node("Inferior Lobe", id=8, parent=lLung)
	heart = Node("Heart", id=9, parent=chest)
	lventricle = Node("Left Ventricle", id=10, parent=heart)
	rventricle = Node("Right Ventricle", id=11, parent=heart)
	latrium = Node("Left Atrium", id=12, parent=heart)
	ratrium = Node("Right Atrium", id=13, parent=heart)
	septum = Node("Septum", id=14, parent = heart)
	return chest; 