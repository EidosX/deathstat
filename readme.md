# Death Stat

This repo tries to visualise mortality in France over the years.  
All source data is official (INSEE).  
Links, guides to download the files manually (not necessary) and notes
are put in yaml files inside the `assets` folder, each corresponding to
a source data file.

## Dependencies

- pyyaml (download_assets.py only)
- requests (download_assets.py only)
- Jupiter notebook
- pandas
- xlrd
- openpyxl
- matplotlib

## Usage

Make sure all the dependencies are installed (you can use pip install)

Run `python3 download_assets.py` to download all the data files directly from the INSEE.  
Then, run `jupyter notebook main.ipynb` to see the results.

## Methodology

- We only cover metropolitan France to get the widest time range
  (France and overseas data typically start from 1991)
- We use the generational age
  e.g in 2020, age 0 means "born in 2019" (no-one reached age 0 on the 1st of January).
