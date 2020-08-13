import spacy

nlp = spacy.load('en_biobert_v11')

text = "Smoker with stage IV EGFR mutant lung adenocarcinoma with metastases to lungs, LN, mediastinum and liver, initially responded to afatinib with recent progression of disease status post craniotomy and brain RT at Mt Sinai Medical Center in 12/2016. He presents to clinic seeking a transfer of care."

doc = nlp(text)

print(doc.ents)

for ent in doc.ents:
	print(ent.text, ent.start_char, ent.end_char, ent.label_)

