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
