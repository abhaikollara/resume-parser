# Resume Parser [WIP]
Extract information from resumes. Currently only tested on PDF format.

## Requirement
Install [Apache Tika](https://tika.apache.org/download.html) before proceeding.

## Installation script
Run
```
curl "https://gist.githubusercontent.com/abhaikollara/fbab77616077ab9f94cce6e9158e7f1b/raw/6cbb0bd050a16c3c8b9075f8ee4f75cdd7e1ce5e/install.sh" | bash
```

## Manual Installation
Then run
```
git clone --recurse-submodules git@github.com:abhaikollara/resume-parser.git
cd resume-parser
pip install -r requirements.txt`
```

- Obtain the trained model from [here](http://bit.ly/2TSxl4Y)
- Extract the contents and place the `saved_model` folder inside the `model` directory

## Usage
```
python run.py myResume.pdf
```
## Acknowledgement
[BERT-NER implementation](https://github.com/kamalkraj/BERT-NER) by Kamalraj

## TODO:
 - ~Write a custom model for named entity recognition, currently using spacy.~
