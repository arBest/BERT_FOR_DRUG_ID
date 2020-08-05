import nltk
import csv
import subprocess

text = "Smoker with stage IV EGFR mutant lung adenocarcinoma with metastases to lungs, LN, mediastinum and liver, initially responded to afatinib with recent progression of disease (T790M negative) status post craniotomy and brain RT at Mt Sinai Medical Center in 12/2016. He presents to clinic to start carboplatin pemetrexed bevacizumab."

# tokenize
tokens = nltk.word_tokenize(text)

print(tokens)

file_path = open('./datasets/BC5CDR-IOB/test.tsv', 'w')
writer = csv.writer(file_path, delimiter='\t')

for item in tokens:
	writer.writerow((item, 'O'))
file_path.close()

# call inference on tokens
cmd = subprocess.run(['bash', './ner_infer.sh'])

# word predictions
results_pred_file = './ner_outputs_BC5CDR-IOB/NER_result_conll.txt'
pred_file = open(results_pred_file, 'r')

final_preds_file = open('./ner_outputs_BC5CDR-IOB/NER_result_preds.tsv', 'w')
final_preds_writer = csv.writer(final_preds_file, delimiter='\t')
for line in pred_file.readlines():
	items = line.split(' ')
	final_preds_writer.writerow((items[0], items[2].strip()))
final_preds_file.close()

