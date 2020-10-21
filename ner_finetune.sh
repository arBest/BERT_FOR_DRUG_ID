#!/bin/bash

# Fine-tune for NER

# modify - path to pretrained BioBERT model
export BIOBERT_DIR=./pretrained_weights/biobert_v1.1_pubmed

# modify - path to dataset
export NER_DIR=./datasets/BC5CDR-IOB

# modify - create and output results to a output dir
export OUTPUT_DIR=./ner_outputs_test
mkdir -p $OUTPUT_DIR

python run_ner.py --do_train=true --do_eval=true --vocab_file=$BIOBERT_DIR/vocab.txt --bert_config_file=$BIOBERT_DIR/bert_config.json --init_checkpoint=$BIOBERT_DIR/model.ckpt-1000000 --num_train_epochs=20.0 --data_dir=$NER_DIR --output_dir=$OUTPUT_DIR
