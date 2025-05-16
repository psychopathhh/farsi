# This branch is experimental
This is an attempt to migrate this project over to newer versions of python.
Right now it doesn't work properly - new versions of libraries broke word and character bounding boxes detection somewhere deep in the code, more time is needed to figure this out

# Proper instruction for running the project
1. Virtual Environment setup (I use anaconda)
  - `python=3.10`
  - `pip install -r requirements.txt`
2. Setting up `data/` folder
  - copy everything from `data AM substitution/` into `data/`
  - if you experience any errors, change "End of line sequence" of files in `data/models/` to `LF` instead of `CRLF`
  - check `preprocessing.ipynb` to configure source files
3. Now you are ready to run `dataset_toolkit.ipynb`


# SynthText Armenian

This is modification of the [original repository](https://github.com/ankush-me/SynthText)
by HSE Applied Math first course students Dorozhkin Dmitry, Magomed Omarov and Abilov Damir, led by David Kagramanyan.

![Armenian Synthetic Scene-Text Samples](<sample images/samples1.png> "Synthetic Samples")

Changes:

- fixed a lot of syntax bugs
- added `merge.ipynb` that merges pics, depth and segmentation from 
[Pre-processed Background Images](https://academictorrents.com/details/2dba9518166cbd141534cbf381aa3e99a087e83c)
- added support of armenian fonts, added armenian text source
- reworked project structure to make it easier to understand
  - now everything that you need to run is inside Jupyter Notebooks
  - all python modules where moved to `SynthTextCore` local package 

Environment requirements can be found in `requirements.txt`, python==3.10
Use notebooks to run this project

For information about original repository consult [it's README](https://github.com/ankush-me/SynthText)
