# BioBERT
This repository provides code to fine-tune models for Named Entity Recognition (NER) on bio-medical datasets.

## Pre-requisites
Clone repository and install requirements.

`git clone https://github.mskcc.org/knowledgesystems/BioBERT.git`

`cd BioBERT; pip install -r requirements.txt`

## Dataset 
Within the folder /datasets, BC5CDR-IOB dataset was used for demo and consists of entities tagged to obtain disease and chemical (including drugs) names.

Other NER datasets are available [here](https://github.com/cambridgeltl/MTL-Bioinformatics-2016).

## BioBERT pretrained models 
All the pre-trained model checkpoints are found [here](https://github.com/naver/biobert-pretrained/releases).

Recommeded by authors to use **Pre-trained weight of BioBERT v1.1 (+PubMed 1M)**

`cd /pretrained_weights` and `wget https://github.com/naver/biobert-pretrained/releases/download/v1.1-pubmed/biobert_v1.1_pubmed.tar.gz` to download model folder. 

## Fine-tune the pre-trained model for Named Entity Recognition (NER)

### Run fine-tuning script (can change hyper-parameters in this script)
`bash ner_finetune.sh`

### Run inference on an example
`ner_infer.sh` has paths to BERT's vocab.txt and config file.

Modify example string of less than 512 tokens to extract disease and chemical entities 

`python ner_example.py`

Output predictions are availabe in $Results_dir within the file **NER_result_preds.tsv**

