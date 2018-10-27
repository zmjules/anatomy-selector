#!/usr/bin/python3

from anytree import Node, RenderTree
	
def createBodyStructure():
	chest = Node("Chest", id=0, selected=False)
	lungs = Node("Lungs", id=1, parent=chest, selected=False)
	rLung = Node("Right Lung", id=2, parent=lungs, selected=False)
	lLung = Node("Left Lung", id=3, parent=lungs, selected=False)
	rSupLobe = Node("Superior Lobe", id=4, parent=rLung, selected=False)
	midLobe = Node("Middle Lobe", id=5, parent=rLung, selected=False)
	rInfLobe = Node("Inferior Lobe", id=6, parent=rLung, selected=False)
	lSupLobe = Node("Superior Lobe", id=7, parent=lLung, selected=False)
	rInfLobe = Node("Inferior Lobe", id=8, parent=lLung, selected=False)
	heart = Node("Heart", id=9, parent=chest, selected=False)
	lventricle = Node("Left Ventricle", id=10, parent=heart, selected=False)
	rventricle = Node("Right Ventricle", id=11, parent=heart, selected=False)
	latrium = Node("Left Atrium", id=12, parent=heart, selected=False)
	ratrium = Node("Right Atrium", id=13, parent=heart, selected=False)
	septum = Node("Septum", id=14, parent = heart, selected=False)
	#print(RenderTree(chest))
	return chest; 