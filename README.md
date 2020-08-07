# BioBERT
This repository provides code using Tensorflow framework to fine-tune models for Named Entity Recognition (NER) on bio-medical datasets.

## Pre-requisites

Access to GPU/TPUs, CUDA/CUDNN libraries and enough CPU RAM.

### Clone repository and install requirements

```
git clone https://github.mskcc.org/knowledgesystems/BioBERT.git
cd BioBERT
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Datasets 
Within the folder /datasets, BC5CDR-IOB dataset was used for demo and consists of entities tagged to obtain disease and chemical (including drugs) names.

Other NER datasets are available [here](https://github.com/cambridgeltl/MTL-Bioinformatics-2016).

## BioBERT pre-trained models 
All the pre-trained model checkpoints are found [here](https://github.com/naver/biobert-pretrained/releases).

Recommeded by authors to use **Pre-trained weight of BioBERT v1.1 (+PubMed 1M)**

`cd /pretrained_weights` and `wget https://github.com/naver/biobert-pretrained/releases/download/v1.1-pubmed/biobert_v1.1_pubmed.tar.gz` to download model folder. 

## Fine-tune the pre-trained model for Named Entity Recognition (NER)

### Run fine-tuning script (can change hyper-parameters in this script) for an NLP task on a task-specific dataset
`bash ner_finetune.sh`

### Run inference on an example
`ner_infer.sh` has paths to BERT's vocab.txt and config file.

Modify example string (less than 512 tokens) to extract disease and chemical entities. 

`python ner_example.py`

Output predictions are availabe in $Results_dir within the file **NER_result_preds.tsv**

## Spacy package
The fine-tuned BERT model is available in spacy.

Please follow the command line instructions below to get a spacy model which converts tf to pytorch model and package it with spacy. 

```
bash convert_tf_pytorch_spacy.sh
python serialize_save_spacy.py
python -m spacy package $PWD/ner_outputs_BC5CDR-chem-IOB/spacy $PWD/ner_outputs_BC5CDR-chem-IOB/spacy-package
```

From spacy-package folder, go into model (en_biobert_v11-0.0.0) folder to modify meta.json


```
cd en_biobert_v11-0.0.0/
python setup.py sdist
```

Model succesfully created:
`./biobert/ner_outputs_BC5CDR-chem-IOB/spacy-package/en_biobert_v11-0.0.0/en_biobert_v11`

Install it with:
`pip3 install en_biobert_v11-0.0.0/dist/en_biobert_v11-0.0.0.tar.gz`

## Credits
We like to credit the authors of [BERT](https://arxiv.org/pdf/1810.04805.pdf) and [BioBERT](https://arxiv.org/pdf/1901.08746.pdf) for the pre-trained models and starter code for pre-training and fine-tuning.

