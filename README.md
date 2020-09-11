# BioBERT
This repository provides code using Tensorflow v1 to pre-train Language Models (LMs) and fine-tune models for Named Entity Recognition (NER) on bio-medical datasets to extract disease names and drug names.

## Pre-requisites

Access to GPU (>=12GB), CUDA (v10.1) / CUDNN (v7.6) libraries and enough CPU (>=12GB) RAM.

### Clone repository and install requirements

```
git clone https://github.mskcc.org/knowledgesystems/BioBERT.git
cd BioBERT
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cd pretrained_weights
wget https://github.com/naver/biobert-pretrained/releases/download/v1.1-pubmed/biobert_v1.1_pubmed.tar.gz 
tar -xzvf biobert_v1.1_pubmed.tar.gz
cd ..
cp pretrained_weights/biobert_v1.1_pubmed/model.ckpt-1000000.data-00000-of-00001 pretrained_weights/biobert_v1.1_pubmed/model.ckpt-1000000
```

## Datasets 
Within the folder /datasets, BC5CDR-IOB dataset was used for demo. It consists of entities for disease and drug names.

Other NER datasets are available [here](https://github.com/cambridgeltl/MTL-Bioinformatics-2016).

### How to add custom annotated data for NER?
Please look at /datasets/BC5CDR-IOB/train.tsv to check example formatting of tagged tokens that applies for validation and test datasets.

Example (from `train.tsv`):

```
Selegiline      B-Chemical
-       O
induced O
postural        B-Disease
hypotension     I-Disease
in      O
Parkinson       B-Disease
.
.
.
```

## BioBERT pre-trained models 
All the pre-trained model checkpoints are found [here](https://github.com/naver/biobert-pretrained/releases).

Recommeded by authors to use **Pre-trained weight of BioBERT v1.1 (+PubMed 1M)** which is what will be used for fine-tuning.

## 1. BERT for Named Entity Recognition (NER)

### Fine-tune (can change hyper-parameters in this script)
`bash ner_finetune.sh`

Creates and writes results into **ner_outputs_test** directory.

Evaluation results on dev dataset:

After training for 10 epochs
```
eval_f = 0.9089838, eval_precision = 0.89400303, eval_recall = 0.9247942, global_step = 1425, loss = 25.761856
```

After training for 20 epochs
```
eval_f = 0.91215086, eval_precision = 0.89916015, eval_recall = 0.9257976, global_step = 2850, loss = 38.24469
```

### Run inference using fine-tuned model on example string to extract named entites
Example input string is provided to BERT to extract disease and chemical entities. 

`python ner_example.py`

 Note: Please pass 1 sentence at a time & length of input len(sub-tokens) < model's input limit (128 sub-tokens) to avoid trimming of text. Check run_ner.py for setting the max (from 128 to 384 sub-tokens).

Input string (as provided in **ner_example.py**) is initially tokenized using NLTK tokenizer to get **tokens** and are further tokenized into the below **sub-tokens**:

Tokens:
```
['His', 'afatinib', 'has', 'been', 'poorly', 'tolerated', 'despite', 'dose', 'reduction', ',', 'therefore', 'I', 'concur', 'with', 'Dr.', 'Z', "'s", 'recommendation', 'to', 'switch', 'to', 'either', 'gefitinib', 'or', 'low', 'dose', 'erlotinib', '.']
```

Sub-tokens (fed into BERT):
```
['His', 'a', '##fa', '##tin', '##ib', 'has', 'been', 'poorly', 'tolerate', '##d', 'despite', 'dose', 'reduction', ',', 'therefore', 'I', 'con', '##cu', '##r', 'with', 'Dr', '.', 'Z', "'", 's', 'recommendation', 'to', 'switch', 'to', 'either', 'g', '##ef', '##iti', '##ni', '##b', 'or', 'low', 'dose', 'er', '##lot', '##ini', '##b', '.']
```

Output entity predictions for tokens (and not sub-tokens) are availabe in results dir within the file **NER_result_preds.tsv**

Token entities can be either: 

`B-Disease - Beginning Disease, I-Disease - Intermediate Disease, B-Chemical - Beginning Chemical, I-Chemical - Intermediate Chemical, Others`

## 2. BERT for embeddings extraction

### Word embeddings
Based on Sub-token words (obtain by WordPiece vocabulary) have embeddings (aka word embeddings) of size (28996, 768)

### Sentence embeddings
`python get_embedding.py` extracts pre-trained contextual features(like ELMo) from hidden layer(s) (can be specified).

(1) A input txt file to be provided to this script where there is a sentence per line.

(2) Output returns a json file per line.

TODO - Use task specific fine-tuned model to extract features instead of pre-trained model.

## NER model usable in spaCy
The fine-tuned BERT model is available in spacy.

Please follow the command line instructions below to get a spacy model which converts tf to pytorch model and package it with spacy. 

```
bash convert_tf_pytorch_spacy.sh
python serialize_save_spacy.py
python -m spacy package $PWD/ner_outputs_test/spacy $PWD/ner_outputs_test/spacy-package
```

From `$PWD/ner_outputs_test/spacy-package` folder, go into model en_biobert_v11-0.0.0 folder to modify meta.json

```
cd en_biobert_v11-0.0.0/
python setup.py sdist
```

Model succesfully created:
`$PWD/ner_outputs_test/spacy-package/en_biobert_v11-0.0.0/en_biobert_v11`

Install it with:
`pip3 install en_biobert_v11-0.0.0/dist/en_biobert_v11-0.0.0.tar.gz`

## Credits
We like to credit the authors of [BERT](https://arxiv.org/pdf/1810.04805.pdf) and [BioBERT](https://arxiv.org/pdf/1901.08746.pdf) for the pre-trained models and starter code for pre-training and fine-tuning.

