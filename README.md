BioBERT

Pre-requisites

Run requirements script to download tensorflow

Download dataset from https://github.com/cambridgeltl/MTL-Bioinformatics-2016/tree/master/data/BC5CDR-IOB

Download BioBERT pretrained models from https://github.com/naver/biobert-pretrained/releases

Fine-tune the pre-trained model for Named Entity Recognition (NER)

bash ner_finetune.sh

Inference example

python ner_example.py
