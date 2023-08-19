k2dg
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/fjclark/k2dg/workflows/CI/badge.svg)](https://github.com/fjclark/k2dg/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/fjclark/k2dg/branch/main/graph/badge.svg?token=UMH0OUSUJY)](https://codecov.io/gh/fjclark/k2dg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A command line tool to convert between dissociation constants and free energies.

## Installation

```bash
pip install k2dg
```

## Usage

To see the available options, run:

```bash
k2dg --help
```

For example, to convert a dissociation constant of 0.3 uM to a free energy in kcal/mol at 298.15 K:

```bash
k2dg 2dg 0.3 uM
```

Or, to convert a free energy of -9.4 kcal/mol to a dissociation constant at 310 K:

```bash
k2dg 2kd -9.4 kcal/mol -t 310
```
