import pickle
file_pkl='Documents\GitHub\Python_Tasks/file.pkl'
with open(file_pkl,'rb') as f:
    t1=pickle.load(f)
    t2=pickle.load(f)
print(t1)
print(t2)