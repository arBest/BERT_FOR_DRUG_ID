import nltk
import csv
import subprocess
import regex as re

text = "63 year-old man, never smoker with stage IV EGFR mutant lung adenocarcinoma with metastases to lungs, LN, mediastinum and liver, and has been on afatinib since 08/2015 with response."


# tokenize
tokens = nltk.word_tokenize(text)

print(tokens, len(tokens))

file_path = open('./datasets/BC5CDR-IOB/test.tsv', 'w')
writer = csv.writer(file_path, delimiter='\t')

for item in tokens:
	writer.writerow((item, 'O'))
file_path.close()

# call inference on tokens
cmd = subprocess.run(['bash', './ner_infer.sh'])

# word predictions
results_pred_file = './ner_outputs_test/NER_result_conll.txt'

pred_file = open(results_pred_file, 'r')

final_preds_file = open('./ner_outputs_test/NER_result_preds.tsv', 'w')
final_preds_writer = csv.writer(final_preds_file, delimiter='\t')
for line in pred_file.readlines():
	items = line.split(' ')
	if len(items) != 1:
		final_preds_writer.writerow((items[0], items[1].strip()))
final_preds_file.close()
