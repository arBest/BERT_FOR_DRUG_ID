import os
import json
import numpy as np
import tensorflow as tf
import tokenization

def get_bert_input_tokens(in_text):
  print(in_text)
  tokenizer = tokenization.FullTokenizer(vocab_file='/home/rajannaa/biobert/pretrained_weights/biobert_v1.1_pubmed/vocab.txt', do_lower_case=False)
  tokens = tokenizer.tokenize(in_text)
  print(tokens, len(tokens))


def get_bio_bert_context_sent_embedding():
  # contextual embeddings (elmo like)
  os.system('python3 extract_features.py \
   --input_file=./input.txt \
   --vocab_file=/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/vocab.txt \
   --bert_config_file=/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/bert_config.json \
   --init_checkpoint=/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/model.ckpt \
   --layers=-1,-2,-3,-4 \
   --output_file=/home/rajannaa/biobert/output.jsonl')

  with open('output.jsonl') as f:
    d = json.load(f)

  sentence_vector = np.zeros(768).tolist()
  for i in range (1, len(d['features'])-1):
    print(type(d['features'][i]['layers'][0]), d['features'][i]['layers'][0]['index'], len(d['features'][i]['layers'][0]['values']))
    sentence_vector = sentence_vector + d['features'][i]['layers'][0]['values']

  '''  
  number_of_tokens = len(d['features']) - 2
  for elem in sentence_vector:
    elem = elem/number_of_tokens

  return sentence_vector
  '''
  return None

def get_bio_bert_actual_word_embedding():
  path = '/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/model.ckpt'

  '''
  tf.reset_default_graph()
  with tf.Session() as sess:
    saver = tf.compat.v1.train.import_meta_graph('/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/model.ckpt.meta')
    saver.restore(sess, "/home/rajannaa/biobert/pretrained_weights/biobert_v11_pubmed/model.ckpt")
    # sess.run(tf.get_variable('w'))
  '''

  imported = tf.compat.v1.saved_model.load(str(path))
  for i in imported.trainable_variables:
    print(i)
    if i.name == 'bert/word_embeddings/embeddings:0':
      embeddings = i


text = "His afatinib has been poorly tolerated despite dose reduction, therefore I concur with Dr. Z's recommendation to switch to either gefitinib or low dose erlotinib."
get_bert_input_tokens(text)

# sent_vect = get_bio_bert_context_sent_embedding()

# word_vect = get_bio_bert_actual_word_embedding()

