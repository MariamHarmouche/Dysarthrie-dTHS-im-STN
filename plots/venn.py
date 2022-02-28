from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

# Das hier anpassen

nw = 18.8
drt = 5.87
cst = 19.7
nw_drt = 1.04
nw_cst = 1.89
nw_drt_cst = 0.2
bc = 2.89


# Ab hier nichts mehr ändern

nw_label = "Nebenwirkungsfeld"
drt_label = "DRT"
cst_label = "CST"

a = round(nw - nw_drt - nw_cst + nw_drt_cst, 2)
b = round(drt - nw_drt - bc, 2)
c = round(cst - nw_cst - bc, 2)
ab = round(nw_drt - nw_drt_cst, 2)
ac = round(nw_cst - nw_drt_cst, 2)
abc = round(nw_drt_cst, 2)
v = venn3(subsets = (a, b, ab, c, ac, bc, abc),
      set_labels = (f"{nw_label} ({nw})",
                    f"{drt_label} ({drt})",
                    f"{cst_label} ({cst})"), alpha = 0.5)
v.get_label_by_id("011").set_text("2.89")  # Nummer von BC ausblenden
# plt.legend(labels=["A", "B"], title="counts")

plt.show()

