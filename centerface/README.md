# Data Compliance: Face Anonymization with CenterFace

[TOC]

## Setup

### Source Code

[CenterFace](https://github.com/Star-Clouds/CenterFace)

### Prerequisites

- Python 3.6+
- Numpy
- OpenCV 4.1.0+

### Install from Gitlab

1. Clone DTN Main Repo

```
git clone git@gitlab.informatik.fb2.hs-intern.de:kweronek/dtn.git
```

2. Change directory to `centerface` folder and set up virtual environment

```
cd .\centerface\
py -m venv .venv
```

3. Activate virtual environment

```
.\.venv\Scripts\activate # For Windows
```

4. Install requirements

```
pip install -r requirements.txt
```

## Execution

- For execution, run (one at a time) the three test methods listed in `prj-python\demo.py`.
- For detailed information, please look at the code documentation.

## Output

- Output is written to `output` folder (See `output_path` in the main method of `prj-python\demo.py`).
- For input image and video, the format of the output is the same as the input. 
- For streaming input, the format of the output is, by default, MP4.

## Known Bugs

- Thus far, no bug has been reported.
- If you encounter `AttributeError: 'NoneType' object has no attribute 'shape'`, make sure your current directory is the `centerface` folder and activate the virtual environment once before running `prj-python\demo.py`.




