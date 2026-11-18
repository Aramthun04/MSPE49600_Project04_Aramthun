# Project 4: Airfoil Analysis

**Author:** Andrew Ramthun
**Course:** MSPE 49600 
**Date:** Nov. 17th 2026

## Project Overview

The purpose of this project was to get students real world experince incorperating Ansys with VS Code for analyze aerodynamic elements and platforms. 

## Project Contents

- `MSPE49600_Project04_Aramthun.wbpj` — Ansys analysis project
- `run_airfoil_project.py` — Runs an individual airfoil case and appends its force results to a CSV file.
- `run_airfoil_sweep.py` — Generates and runs a ten-angle Latin hypercube sweep from 0 to 20 degrees.
- `airfoil_results.csv` — Results from 'run_airfoil_sweep.py' 

## Requirements

- Ansys Workbench with the project opened.
- Python and the project virtual environment in `.venv`.
- SciPy installed in that environment for the sweep script.

## How to Run

1. Open the Workbench project.
2. In Workbench, run `StartServer()` and note the port it reports.
3. Check `PORT`, `SECURITY`, and the parameter IDs in `run_airfoil_project.py` and update them if needed for your setup.
4. Open a PowerShell terminal in this project folder.
5. To run one case, execute:

   ```powershell
   .\.venv\Scripts\python.exe .\run_airfoil_project.py
   ```

6. To run the ten-angle sweep, execute:

   ```powershell
   .\.venv\Scripts\python.exe .\run_airfoil_sweep.py
   ```

If SciPy is not installed in the project environment, install it with:

```powershell
.\.venv\Scripts\python.exe -m pip install scipy
```

