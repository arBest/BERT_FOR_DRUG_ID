import nltk
import csv
import subprocess
import regex as re

text = "11/28/16 concurrent chemo with weekly carbo/taxol and RT, completed 5 cycles of weekly chemotherapy    seen in triage for left neck mass, found to have DVT in the left internal jugular vein and cervical lymphadenopathy."

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
	print(items, len(items))
	if len(items) != 1:
		final_preds_writer.writerow((items[0], items[2].strip()))
final_preds_file.close()

