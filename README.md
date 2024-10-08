[![DOI](https://zenodo.org/badge/865356741.svg)](https://doi.org/10.5281/zenodo.13902655)

# Abins q-point convergence

A workflow to examine q-point convergence of simulated INS spectra using AbINS

## Introduction
This workflow calls the [Abins algorithm](https://docs.mantidproject.org/nightly/algorithms/Abins-v1.html) in [Mantid](https://www.mantidproject.org/) to compute a simulated inelastic neutron scattering (INS) spectrum.
A real-space "cutoff" parameter is adjusted to examine convergence over a series of q-point meshes which form balanced Monkorst-Pack grids. The implementation is essentially the same as [kgrid](https://github.com/wmd-group/kgrid)

## Limitations
- This method only applies when force-constant data is available (i.e. using the FORCECONSTANTS mode of Abins). If only the q-points and frequencies are available, we don't have a convenient tool to interpolate them.
- Mantid 6.10 is not built for ARM-based Mac; it should be possible to do something clever with a Rosetta/x86 conda environment, but this is not tested

## Installation
To use this workflow, you need access to Conda (or Mamba) and Snakemake. For example, [IDAaaS](https://isis.analysis.stfc.ac.uk/) users should be able to create a suitable environment from a terminal with

```
mamba create -n snakemake -c bioconda -c conda-forge snakemake python=3.12
```

and activate it with

```
mamba activate snakemake
```


## Running the workflow

Input files are configured in *config/config.yaml*. This workflow includes sample data for Si computed with CASTEP;
to use your own data and modify other workflow parameters, either edit the *config.yaml* and run

```
snakemake -c 1 --sdm conda
```

or create a modified copy of *config.yaml* and point to it with

```
snakemake -c 1 --sdm conda --config /path/to/my/config.yaml
```
