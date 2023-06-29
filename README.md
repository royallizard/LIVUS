# MA
## Installation
### Requirements:
* [python3](https://www.python.org/downloads/)
* [jupyter-lab](https://jupyter.org/install)
* if required, all related imports of LIVUS and the parse_NVD
### Recommended: 
* [Installation of jupyter-lab through Conda environment](https://jupyterlab.readthedocs.io/en/latest/getting_started/installation.html) such as [miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Usage:
* LIVUS is used by running it in the Jupyter-Lab environment.
* To use the NVD parser on LIVUS' predictions, run the related function in the Notebook, otherwise run it from the CLI with -n [keyword] or --name [keyword] to parse the NVD database with the given keyword
* Be aware that too many requests to the NVD API will lead to being blocked.

  
### Folder structure
* util
  * preprocess.py: The script I used to turn all binaries into text files containing their respective strings output.
  * parse_NVD.py: The script to parse the NVD
* src
  * LIVUS.ipynb: The Jupyter Notebook containing all of LIVUS source code
* out 
  * SO: Contains all outputs related to the SO function highest_predictions
  * exec: Contains all outputs related to threshold_predictions such as the results of the NVD Parser for each library
* data
  * training: The folder containing the training data LIVUS should use
  * testing: The folder containing the testing data LIVUS should use
  * SO
    * datasets_tests: A folder containing the curated dataset for each test of the Evaluation
    * dataset_so: All SO files used in the Evaluation
  * exec
    * programs_txt: Contains the output of strings for Gimp, VLC, OpenTTD and Wireshark
    * libraries: A small dataset of libraries related to the OSLDetector Evaluation
    * fedora_txt: A big dataset of text files containing the output of strings after having been applied to the libraries that I was able to extract from LibDB (29 of 100 archives)
  
## SO Sources
libpulse
* https://archive.archlinux.org/packages/l/lib32-libpulse/
* https://packages.debian.org/de/sid/amd64/libpulse0/download
* https://packages.debian.org/de/bullseye/libpulse0
* preinstalled version from Debian 15.99

samba
* https://archive.archlinux.org/packages/s/samba/
* https://packages.debian.org/sid/samba

nautilus
* https://archive.archlinux.org/packages/n/nautilus/
* https://packages.debian.org/bookworm/nautilus

gedit
* https://packages.debian.org/bullseye/gedit
* https://archive.archlinux.org/packages/g/gedit/

## OSLDetector library sources in addition to [LibDB's Fedora dataset](https://figshare.com/s/4a007e78f29243531b8c)
* https://packages.debian.org/unstable/liblzo2-dev
* https://packages.debian.org/unstable/libavutil57
* https://packages.debian.org/sid/amd64/libavcodec-dev/download
* https://packages.debian.org/source/stable/golang-github-remyoudompheng-go-liblzma
* https://packages.debian.org/sid/amd64/liblzma-dev/download
* https://archive.archlinux.org/packages/g/gnutls/
* https://archive.archlinux.org/packages/o/openssl/
