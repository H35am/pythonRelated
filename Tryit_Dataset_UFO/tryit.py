import matplotlib.pyplot as plt
import pandas as pd

csv_complete =
'complete.csv'
csv_scrubbed =
 'scrubbed.csv'

data = pd.read_csv(csv_scrubbed)

print (data.index)
