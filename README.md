# Resume Parser [WIP]
Extract information from resumes. Currently only tested on PDF format.
## Installation
Install [Apache Tika](https://tika.apache.org/download.html) before proceeding.

Then run
```
git clone --recurse-submodules git@github.com:abhaikollara/resume-parser.git
cd resume-parser
pip install -r requirements.txt`
```

Obtain the trained model from [here](http://bit.ly/2TSxl4Y)
Extract the contents and place the `saved_model` folder inside the `model` directory

## Usage
```
python run.py myResume.pdf
```

## TODO:
 - ~Write a custom model for named entity recognition, currently using spacy.~
