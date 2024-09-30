from pathlib import Path

import mantid.simpleapi

import abins.parameters
from snakemake.script import snakemake

abins_kwargs = snakemake.params.abins_kwargs

abins_kwargs = abins_kwargs | dict(
    AbInitioProgram="FORCECONSTANTS",
    OutputWorkspace="spectrum",
    SumContributions=True,
    SaveAscii=False,
)

abins.parameters.sampling["force_constants"]["qpt_cutoff"] = float(
    snakemake.params.cutoff
)
mantid.simpleapi.Abins(**abins_kwargs)  # Run Abins, creating new workspace

mantid.simpleapi.SaveAscii(
    InputWorkspace="spectrum_total",
    Filename=str(Path(snakemake.output[0]).resolve()),
    AppendToFile=False,
    Separator="CSV",
)
