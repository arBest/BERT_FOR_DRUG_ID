#BioBERT
This repository provides code to fine-tune models for Named Entity Recognition (NER) on bio-medical datasets.

##Pre-requisites

Run requirements script to download tensorflow

##Download dataset 
git clone https://github.com/cambridgeltl/MTL-Bioinformatics-2016/tree/master/data/BC5CDR-IOB

##Download BioBERT pretrained models 
All the pre-trained model checkpoints are found here https://github.com/naver/biobert-pretrained/releases

Recommeded by authors to use Pre-trained weight of BioBERT v1.1 (+PubMed 1M)
wget https://github.com/naver/biobert-pretrained/releases/download/v1.1-pubmed/biobert_v1.1_pubmed.tar.gz

##Fine-tune the pre-trained model for Named Entity Recognition (NER)
Within the script modify paths to provide downloaded pre-trained model dir and dataset dir.

Run bash ner_finetune.sh

Inference example
Modify the paths in ner_infer.sh to give paths to vocab.txt and config file of the BERT model.

Run python ner_example.py
