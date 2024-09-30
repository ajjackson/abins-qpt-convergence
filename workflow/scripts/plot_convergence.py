import matplotlib.pyplot as plt
import matplotlib.style
import numpy as np
from snakemake.script import snakemake

cutoffs = snakemake.params["cutoffs"]
config = snakemake.params["config"]
energy_unit = snakemake.params["energy_unit"]


def read_csv(filename: str) -> np.ndarray:
    """Read csv file from Abins / SaveAscii"""
    return np.loadtxt(filename, delimiter=",", unpack=True, usecols=[0, 1], skiprows=2)


matplotlib.style.use(config["style"])
fig, ax = plt.subplots(figsize=config["figsize"])

for cutoff, filename in zip(cutoffs, snakemake.input):
    ax.plot(*read_csv(filename), label=f"{cutoff} $\\AA$")

ax.set_xlim(config["x_min"], config["x_max"])
ax.set_xlabel(f"Energy transfer / {energy_unit}")

ax.set_yticklabels([""])
ax.set_ylabel("Intensity")

ax.legend()

fig.tight_layout()
for output in snakemake.output:
    fig.savefig(output)
