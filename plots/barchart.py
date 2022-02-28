import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# 'DRT links', 'CST links', 'DRT rechts', 'CST rechts'
oben = [6.22, 20.81, 2.64, 20.94]
unten = [6, 25.85, 5.53, 10.05]


width =0.3
plt.bar(np.arange(len(oben)), oben, width=width, label="oben")
plt.bar(np.arange(len(unten))+ width, unten, width=width, label="unten")

for i, (o, u) in enumerate(zip(oben, unten)):
    plt.text(i - (width / 2), o + 1, o)
    plt.text(i + (width / 2), u + 1, u)


labels = ['DRT links', 'CST links', 'DRT rechts', 'CST rechts']


plt.xticks(range(len(oben)), labels)
ax = plt.gca()
ax.set_ylim([0, 100])
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f %%'))
plt.legend()
plt.show()