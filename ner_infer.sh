#!/bin/bash

# Inference using fine-tuned model for NER

# modify - dir to pretrained model
export BIOBERT_DIR=./pretrained_weights/biobert_v1.1_pubmed
echo $BIOBERT_DIR
# modify - dataset
export NER_DIR=./datasets/BC5CDR-IOB
# modify - output
export OUTPUT_DIR=./ner_outputs_BC5CDR-IOB

python run_ner.py --do_train=false --do_eval=false --do_predict=true --vocab_file=$BIOBERT_DIR/vocab.txt --bert_config_file=$BIOBERT_DIR/bert_config.json --init_checkpoint=/home/rajannaa/biobert/ner_outputs_BC5CDR-chem-IOB/model.ckpt-1425 --data_dir=$NER_DIR --output_dir=$OUTPUT_DIR

python biocodes/ner_detokenize.py --token_test_path=$OUTPUT_DIR/token_test.txt --label_test_path=$OUTPUT_DIR/label_test.txt --answer_path=$NER_DIR/test.tsv --output_dir=$OUTPUT_DIR

perl biocodes/conlleval.pl < $OUTPUT_DIR/NER_result_conll.txt
