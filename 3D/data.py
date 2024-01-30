import cooler
import numpy as np

file = 'GSM1551550_HIC001.mcool'
c = cooler.Cooler(file + '::/resolutions/1000000')


mat = c.matrix(balance=False)[:]

mat_del = np.delete(mat, -1, axis=0)
mat_del = np.delete(mat_del, -1, axis=1)

mat_float = mat_del.astype(np.float64)
print(mat_float)
np.save("Mat_noMT_1M.npy", mat_float)


