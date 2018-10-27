# anatomy-selector

This is a simple program written in Python to display the gross anatomy of the chest as a checklist. Selecting an anatomical region will select its parent regions. Deselecting a region will deselect all of its sub regions. 


Prerequisites:
- Python version of at least 3.0 
- Tkinter for Python; this should be included with more recent versions of Python
- anytree 2.4.3; install on the command line with 'pip install anytree'

To run:
- Run 'python AnatomySelector.py' from the root project directory

Test cases: 
- Select all 
- Deselect all
- Select a checkbox with ancestors
- Select a checkbox with no ancestors
- Deselect a checkbox with descendants
- Deselect a checkbox with no descendants
- Select a checkbox with the same text as another checkbox
- Deselect a checkbox with the same text as another checkbox
- Select/deselect checkboxes that are in different unrelated nodes of the tree
