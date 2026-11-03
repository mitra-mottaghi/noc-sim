import matplotlib.pyplot as plt

from src.simulator import simulate

rates = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

for routing in ["xy", "adaptive"]:
    res = [simulate(4, 4, r, 5000, routing, "transpose") for r in rates]
    ax1.plot(rates, [x["avg_latency"] for x in res], "o-", label=routing)
    ax2.plot(rates, [x["throughput"] for x in res], "o-", label=routing)

ax1.set_ylim(0, 60)
ax1.set_xlabel("Injection rate (packets/node/cycle)")
ax1.set_ylabel("Average latency (cycles)")
ax1.set_title("Latency, transpose traffic, 4x4 mesh")
ax2.set_xlabel("Injection rate (packets/node/cycle)")
ax2.set_ylabel("Throughput (packets/node/cycle)")
ax2.set_title("Throughput, transpose traffic, 4x4 mesh")
ax1.legend()
ax2.legend()

plt.tight_layout()
plt.savefig("docs/compare_xy_adaptive.png", dpi=200)
print("Saved docs/compare_xy_adaptive.png")
