#!/bin/sh

# modify
results_dir=ner_outputs_BC5CDR-chem-IOB
pretrained_model=biobert_v1.1_pubmed
finetuned_model=model.ckpt-1425

: '
mkdir -p ./$results_dir/tf
mkdir -p ./$results_dir/pytorchh
mkdir -p ./$results_dir/spacy
mkdir -p ./$results_dir/spacy-package

# copy finetuned or model of choice and its metadata to the results dir

cp ./$results_dir/$finetuned_model.data-00000-of-00001 ./$results_dir/tf/model.ckpt
cp ./$results_dir/$finetuned_model.index ./$results_dir/tf/model.ckpt.index
cp ./pretrained_weights/$pretrained_model/bert_config.json ./$results_dir/tf/config.json

# convert tf to pytorch
python3 -m pytorch_transformers.convert_tf_checkpoint_to_pytorch --tf_checkpoint_path ./$results_dir/tf/model.ckpt.index --bert_config_file ./$results_dir/tf/config.json --pytorch_dump_path ./$results_dir/pytorch-biobert/pytorch_model.bin

'

# model in spacy

cp ./pretrained_weights/$pretrained_model/bert_config.json ./$results_dir/pytorch-biobert/config.json
cp ./pretrained_weights/$pretrained_model/vocab.txt ./$results_dir/pytorch-biobert/vocab.txt
