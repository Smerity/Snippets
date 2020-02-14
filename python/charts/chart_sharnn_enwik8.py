import matplotlib.pyplot as plt
import numpy as np


#plt.style.use('fivethirtyeight')
plt.style.use('seaborn-whitegrid')

# grep "valid bpc" runs.enwik8.with.ln.on.q.and.dropout.on.v.and.separate.ln.for.ff.input.with.git.1ad4e15a15995 | rev | cut -d ' ' -f 1 | rev
y = '''1.315
1.241
1.201
1.178
1.165
1.151
1.145
1.137
1.132
1.128
1.124
1.122
1.117
1.116
1.112
1.112
1.112'''
# grep "valid bpc" runs.enwik8.with.ln.on.q.and.dropout.on.v.and.separate.ln.for.ff.input.with.git.1ad4e15a15995.resume.lr.1e3 | rev | cut -d ' ' -f 1 | rev
y += '''
1.096
1.095
1.096'''
y = [float(v) for v in y.split()]

x = [i for i, _ in enumerate(y)]

plt.rcParams.update({'font.size': 16})

fig, ax = plt.subplots()
#plt.tight_layout()

ax.plot(x, y)
#ax.set_title("'fivethirtyeight' style sheet")
ax.margins(x=0)
ax.set_xlabel('Epochs')
ax.set_ylabel('Bits per character (bpc) on validation')

from matplotlib.ticker import MaxNLocator
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.axhline(y=1.2, linewidth=1, color='r')

plt.savefig('sharnn_enwik8.pdf')
plt.show()
