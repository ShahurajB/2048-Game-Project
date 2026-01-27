import numpy as np 


arr = np.zeros((4,4), dtype=int) ## Default numpy returns as float hence mentioning type
score = 0

undo_score = 0
redo_score = 0
undo_arr = np.zeros((4,4), dtype=int)
redo_arr = np.zeros((4,4), dtype=int)