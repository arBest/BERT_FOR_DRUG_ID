# BioBERT
This repository provides code to fine-tune models for Named Entity Recognition (NER) on bio-medical datasets.

## Pre-requisites
Clone repository end install requirements.

`git clone https://github.mskcc.org/knowledgesystems/BioBERT.git`

`cd BioBERT; pip install -r requirements.txt`

## Download dataset 
`git clone https://github.com/cambridgeltl/MTL-Bioinformatics-2016.git`

Use any NER dataset, for demo MTL-Bioinformatics-2016/BC5CDR-IOB dataset was used that consists of entities tagged to obtain disease and chemical (including drugs) names.

## Download BioBERT pretrained models 
All the pre-trained model checkpoints are found [here](https://github.com/naver/biobert-pretrained/releases).

Recommeded by authors to use **Pre-trained weight of BioBERT v1.1 (+PubMed 1M)**

`wget https://github.com/naver/biobert-pretrained/releases/download/v1.1-pubmed/biobert_v1.1_pubmed.tar.gz`

## Fine-tune the pre-trained model for Named Entity Recognition (NER)
Within the script, **modify paths** to provide downloaded pre-trained model and dataset dir.

### Run fine-tuning script (can change hyper-parameters in this script)
`bash ner_finetune.sh`

### Run inference on an example
**Modify paths** in `ner_infer.sh` to give paths to vocab.txt and config file of the BERT model.

Modify example string of less than 512 tokens to extract disease and chemical entities 

`python ner_example.py`

Output predictions are availabe in $Results_dir within the file **NER_result_preds.tsv**

