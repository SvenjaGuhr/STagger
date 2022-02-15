# STagger
**Simple Sentiment Analysis Tool for French**  
Der Sentimenttagger STagger für Französisch parst kurze Textsegmente zeilenweise und extrahiert aus ihnen die verwendeten Adjektive, zählt sie, annotiert sie bezüglich ihrer Gefühlspolarität (pos, neg, neutral) und summiert anschließend die Anzahl der Sentiment-getaggten Adjektive auf. 


## Installation
Installieren Sie die Pakete pandas, nltk und collections mit pip install.

## Aufbereitung eigener Texte 
Um den STagger auf eigene Texte anwenden zu können, müssen die Texte folgendermaßen aufbereitet sein:

Username (oder anderer Text, der nicht geparst werden soll)  
Nach einem Zeilenumbruch folgt in den nächsten Zeilen der Fließtext, dessen Adjektive mit Sentimenttags annotiert werden sollen...  
[2 Leerzeilen als Trennelement zum nächsten Textsegment]  

Als Beispieltexte können die anonymisierten Leserkommentare aus dem zip-folder verwendet werden.

## Publikationen und mehr mit Bezug zum STagger
Guhr, Svenja. (2019). Computergestützte Analyse von französischen Onlinemedien zur Präsidentschaftswahl 2017. Masterarbeit im Master Romanistik. Georg-August-Universität Göttingen [unpublished].  

Brokering, Annalena, & Guhr, Svenja. (2020). Interdisziplinäres Streitgespräch – Nutzerkommentaranalysen aus ethisch-rechtlicher Perspektive, **Abstract**. Book of Abstracts, DHd 2020 Spielräume: Digital Humanities zwischen Modellierung und Interpretation. 7. Tagung des Verbands "Digital Humanities im deutschsprachigen Raum" (DHd 2020), Paderborn. Zenodo. https://doi.org/10.5281/zenodo.4621919. 

Brokering, Annalena, & Guhr, Svenja. (2020). Interdisziplinäres Streitgespräch – Nutzerkommentaranalysen aus ethisch-rechtlicher Perspektive, **Poster**. DHd 2020 Spielräume: Digital Humanities zwischen Modellierung und Interpretation. 7. Tagung des Verbands "Digital Humanities im deutschsprachigen Raum" (DHd 2020), Paderborn. Zenodo. https://doi.org/10.5281/zenodo.6091650.

