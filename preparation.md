# Preparation

## Format

The tutorial consists of lecture segments, followed by hands-on
exercises.  We strongly encourage you to bring a laptop with all the
required packages installed in order to participate fully.

## Software required

- **Python**

  If you are new to Python, please install the
  [Anaconda distribution](https://www.anaconda.com/downloads) for
  **Python version 3** (available on OSX, Linux, and Windows).
  Everyone else, feel free to use your favorite distribution, but
  please ensure the requirements below are met:

  - `numpy` >= 1.12
  - `scipy` >= 1.0
  - `matplotlib` >= 2.1
  - `scikit-image` >= 0.15
  - `scikit-learn` >= 0.18
  - `itk` >= 4.1

  Please see "Test your setup" below.

- **ITK**

  ITK is an open-source toolkit for multidimensional image analysis.
  If you are using Anaconda, it is easy to install ITK using the
  [conda-forge](https://conda-forge.org/) repository, through the
  following command:

  `$ conda install -c conda-forge itk`

  You can also use the PyPI package:

  `$ pip3 install --upgrade itk`

- **Jupyter**

  The lecture material includes Jupyter notebooks.  Please follow the
  [Jupyter installation instructions](http://jupyter.readthedocs.io/en/latest/install.html),
  and ensure you have version 4 or later:

  ```bash
  $ jupyter --version
  4.1.0
  ```

## Download lecture material

1. [Install Git](https://git-scm.com/downloads)
2. Clone the repository at
   [https://github.com/stefanv/imagexd_scientific_python](https://github.com/stefanv/imagexd_scientific_python)

We may make editorial corrections to the material until the day before
the workshop, so please execute `git pull` to update.

## Test your setup

Please switch into the repository you downloaded in the previous step,
and run `python check_setup.py` to validate your installation.

On my computer, the previous command results in:

```
[✓] scikit-image  0.16.dev0
[✓] numpy         1.16.4
[✓] scipy         1.3.0
[✓] matplotlib    3.1.0
[✓] notebook      6.0.0
[✓] scikit-learn  0.21.2
```

Please note your version numbers may differ.

**If you do not have a working setup, please contact the instructors.**
