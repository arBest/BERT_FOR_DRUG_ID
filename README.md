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

## Credits
We like to credit the authors of [BERT](https://arxiv.org/pdf/1810.04805.pdf) and [BioBERT](https://arxiv.org/pdf/1901.08746.pdf) for the pre-trained models and starter code for pre-training and fine-tuning.
