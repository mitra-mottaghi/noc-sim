import matplotlib.pyplot as plt

from src.faults import random_link_faults
from src.simulator import simulate

ks = range(0, 9)
seeds = range(10)

plt.figure(figsize=(6, 4))
for routing in ["xy", "adaptive"]:
    ratios = []
    for k in ks:
        vals = []
        for s in seeds:
            faults = random_link_faults(4, 4, k, s)
            res = simulate(4, 4, 0.1, 2000, routing, "uniform", s, faults)
            vals.append(res["delivery_ratio"])
        ratios.append(sum(vals) / len(vals))
    print(routing, [round(r, 3) for r in ratios])
    plt.plot(list(ks), ratios, "o-", label=routing)

plt.xlabel("Number of failed links (of 24)")
plt.ylabel("Delivery ratio")
plt.title("Fault tolerance, uniform traffic, 4x4 mesh")
plt.legend()
plt.tight_layout()
plt.savefig("docs/fault_tolerance.png", dpi=200)
print("Saved docs/fault_tolerance.png")