import os
import json
import numpy as np

def get_bio_bert_embedding(sentence):
  # contextual word embeddings

  '''
  os.system('python3 extract_features.py \
   --input_file=./input.txt \
   --vocab_file=/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/vocab.txt \
   --bert_config_file=/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/bert_config.json \
   --init_checkpoint=/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/model.ckpt \
   --layers=-1 \
   --output_file=/home/rajannaa/biobert/output.jsonl')
  '''

  with open('output.jsonl') as f:
    d = json.load(f)
    
  sentence_vector = np.zeros(768).tolist()
  for i in range (1, len(d['features'])-1):
    sentence_vector = sentence_vector + d['features'][i]['layers'][0]['values']
  
  number_of_tokens = len(d['features']) - 2
  for elem in sentence_vector:
    elem = elem/number_of_tokens

  print(sentence_vector)
  return sentence_vector

sent_vect = get_bio_bert_embedding("The patient has lung adenocarcinoma.")

