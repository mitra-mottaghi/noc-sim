import matplotlib.pyplot as plt

from src.simulator import simulate

rates = [0.02, 0.05, 0.1, 0.15, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3]
results = [simulate(4, 4, r, 5000) for r in rates]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(rates, [r["avg_latency"] for r in results], "o-")
ax1.set_xlabel("Injection rate (packets/node/cycle)")
ax1.set_ylabel("Average latency (cycles)")
ax1.set_title("Latency vs load")

ax2.plot(rates, [r["throughput"] for r in results], "o-")
ax2.set_xlabel("Injection rate (packets/node/cycle)")
ax2.set_ylabel("Throughput (packets/node/cycle)")
ax2.set_title("Throughput vs load")

plt.tight_layout()
plt.savefig("docs/xy_4x4_results.png", dpi=200)
print("Saved docs/xy_4x4_results.png")
