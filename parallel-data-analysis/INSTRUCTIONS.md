# DataAnalysisParallel-PyData
Complete code used during the Data Analysis in Parallel tutorial at PyData London 2019. It includes a notebook actually shown in the tutorial, a notebook for fitting the sentiment model, and input data


## Installation instructions:

1. Install Anaconda (if you don't have it already)
3. Open a terminal (Anaconda Prompt on Windows)
2. Unpack this repo and `cd` into it
3. Get all the packages with `conda env create -f tutorialenv.yaml`
5. Activate the environment with `source activate tutorial` or `conda activate tutorial`
5. Run the following: `python -m nltk.downloader wordnet`
6. Start Jupyter with `jupyter lab`
7. In the lab open the notebook AnalysisTasks.ipynb which is the main demo


CLUSTER CODE: ipcluster https://ipyparallel.readthedocs.io/en/latest/direct.html
