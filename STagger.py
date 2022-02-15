#durch das Importieren werden die folgenden Softwarepakete aktiviert und zum Gebrauch bereitgestellt
import pandas, nltk, collections 

#Sentimentlexikon einlesen
#mithilfe des Softwarepakets pandas ist es möglich, Daten, die als Excel-Datei vorliegen, einzulesen.
#für das Einlesen wird sofort das Französische als verwendete Sprache definiert
sentiments = pandas.read_excel('Sentimentlexikon_French.xlsx', index_col='French')

#mit der folgenden Zeile wird der Tokenizer von der NLTK-Plattform abgerufen
nltk.tokenize.word_tokenize("Je suis malheureuse à cause de son absence.", language='french')

#Inputdaten
#im Folgenden wird eine Textdatei eingelesen
text = open('VoteBlancouAbstentionComments.txt').read().strip()

#Definition für die Summenausgabe
#die nächst Zeile definiert die Aufsummierung der Summe an Sentimentangaben am Ende der Datei
allSentiments = collections.Counter(pos=0,neut=0,neg=0)

#Aufteilung der Inputdaten in verschiedene Abschnitte, Satz- und Absatzerkennung
#in der folgenden for-Schleife werden die Kommentartexte aufbereitet, indem sie in Abschnitte bei Zeilenumbruch aufgeteilt werden;
#Da jeder Kommentar  durch einen doppelten Zeilenumbruch ('\n\n') voneinander getrennt steht,
#kann diese Abschnittseigenschaft zur separaten Betrachtung der einzelnen Kommentare verwendet werden.s
#die erste Zeile ist der Username (immer Zeile [0] eines Abschnitts), danach folgt der Usertext bis zum Ende des Kommentars,
#das wieder durch eine Leerzeile ('\n') gekennzeichnet erkannt wird
for comment in text.split('\n\n'):
    lines = comment.split('\n')
    user = lines[0]
    ctext = '\n'.join(lines[1:])

#Tokenisierung der Inputdaten   
#der Inputtext wird durch den NLTK-Tokenizer tokenisiert
    tokens = nltk.tokenize.word_tokenize(ctext, language='french')

#Im Folgenden wird ein Dictionary erstellt, das später mit den erkannten Sentiments gefüllt wird:
    sentiment = {}
    #mit den folgenden zwei Printausgaben können die strukturierten Kommentare als Zwischenergebnisse angezeigt werden
    #print('User: {}\n'.format(user, ctext))
    #print('Tokens: [{}]\nText: {}\n'.format(', '.join(tokens)))
    
#hierbei wird auf die Tokenisierung zurückgegriffen, wobei alle Tokens gezählt werden,
#wenn sie einen Eintrag im Sentimentslexikon (sentiments.index) haben
#steht das Wort im Sentimentlexikon, wird es dem Dictionary
    for i, token in enumerate(map(str.lower, tokens)):
        if token in sentiments.index:
            #print(sentiments.loc[token].sentiment)
            #sentiment.update([sentiments.loc[token].sentiment])
#bei Übereinstimmung mit einem Lexikoneintrag wird das erkannte Token dem oben definierten Sentimentdictionary hinzugefügt.
            sentiment[token] = sentiments.loc[token].sentiment
#durch die folgendene Zeile wird ein Token vor und ein Token nach dem erkannten Sentiment
#sowie das Sentiment selbst zwischen den beiden Tokens ausgegeben
            print("Window:", tokens[max(i-2, 0):i+2])

            
#in der nächsten Zeile wird mit dem Paket collections ein Counter erstellt,
#der die erkannten Sentimentwörter zählt und als Ausgabe das im Lexikoneintrag angegebene Sentiment ausgibt
    sentimentCounter = collections.Counter(sentiment.values())
    
    print('User: {}\nText: {}\nSentiments: {}\nCounter: {}\n'.format(user, ctext, sentiment, sentimentCounter))
    allSentiments = allSentiments+sentimentCounter
print('All Sentiments: {}\n'.format(allSentiments))

#die drei hier drüber stehenden Zeilen definieren das Output, das wie folgt angezeigt wird:
#Window: ['t-1', 't', 't+1']
#User: Peter 01/01/2017 - 12h00
#Text: Salut, tout le monde!
#Sentiment: Counter({'pos': n, 'neutral': n, 'neg': n})
