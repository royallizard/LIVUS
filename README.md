# LIVUS
## Installation
### Requirements:
- python3
- jupyter-lab

### Recommended: 
- installation of jupyter-lab through Conda environment

### Folder structure
#### LIVUS
The Notebook to identify libraries in binaries.
- data: input files used by LIVUS
- src: main
- util: scripts, that are used for LIVUS as well as additional useful ones 
- out: all output files such as the results for the testing dataset, the single file and the results from NVD

#### LIVUSplus
The Notebook to identify libraries in programs.
- data: input files used by LIVUS
- src: main
- util: scripts, that are used for LIVUS as well as additional useful ones 
- out: all output files such as the results for the testing dataset, the single file and the results from NVD

## Additional notes
Be aware that too many requests to the NVD API will lead to being blocked.

The Fedora_txt folder in LIVUSplus contains the 29 retrievable archives from LibDB after their strings have been extracted.

LIVUS/data/datasets_tests contain all datasets in the combination they were used for the specific test

## Library Sources
libpulse
- https://archive.archlinux.org/packages/l/lib32-libpulse/
- https://packages.debian.org/de/sid/amd64/libpulse0/download
- https://packages.debian.org/de/bullseye/libpulse0
- preinstalled version from Debian 15.99

samba
- https://archive.archlinux.org/packages/s/samba/
- https://packages.debian.org/sid/samba

nautilus
- https://archive.archlinux.org/packages/n/nautilus/
- https://packages.debian.org/bookworm/nautilus

gedit
- https://packages.debian.org/bullseye/gedit
- https://archive.archlinux.org/packages/g/gedit/

## LIVUSplus libraries (additionally to the LibDB dataset)
- https://packages.debian.org/unstable/liblzo2-dev
- https://packages.debian.org/unstable/libavutil57
- https://packages.debian.org/sid/amd64/libavcodec-dev/download
- https://packages.debian.org/source/stable/golang-github-remyoudompheng-go-liblzma
- https://packages.debian.org/sid/amd64/liblzma-dev/download
- https://archive.archlinux.org/packages/g/gnutls/
- https://archive.archlinux.org/packages/o/openssl/
