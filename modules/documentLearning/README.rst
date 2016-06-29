.. image:: http://userpages.uni-koblenz.de/~mschanz/documentLearning.jpg
   :align: center
   :target: https://github.com/fuuman/101worker/tree/master/modules/lookupMaven
   :alt: lookupMaven Logo


zu Usage:
Die Jsondateien müssen in den Projektordner eingefügt werden.
Der z Wert innerhalb der Datein jsonExtractor.py muss angepasst werden.
Der eigentlich Aufruf befindet sich in NatLan.py ganz unten.

zu Readme:

Unsere Aufgabe:
Document learning: The different namespaces on the wiki come with different expected sections. For instance, each page in the namespace
"Contribution" is supposed to contain a section "Characteristics".
The complete set of possible (actual) section names can be found by extracting all section names from the dump wiki-content.json.
Apply machine learning to provide a prediction model with the namespace as the input data and section names as labels. Use some pages as a training set.
By applying the prediction model to further pages, try to identify pages with missing or unexpected sections.
A missing section means that prediction suggests that a section should be there for the page's namespace at hand; likewise for an unexpected section.

Was wir geschafft haben:
Wir haben aus den Json-Dateien die Namespaces und ihre jeweiligen Sections extrahiert. Danach haben wir anhand der Daten ein Prediction Model mit machine learning erstellt.
Uns fehlt dabei jedoch der Übergang, zu testen und damit missing und unexspected in beliebige json Dateien einzutragen.
Wir wollten mit dem Prediction Model die jeweiligen sections der namespaces vergleichen und wenn ein neues erkannt wird, ist es unexspected und wenn eines fehlt, dann ist es missing.
Probleme traten jedoch dabei auf, die Prediction Models jeweligen Namespaces zu zuweisen, sodass wir nicht mehr fortfahren konnten mit unserer Arbeit.
Diese Probleme traten vor allem auf, durch mangelnde Python-Kenntnisse und der gleichzeitig zu erlernenden NLTK Libary. Mit mehr Zeit wäre uns wahrscheinlich ein abschließendes Ergebnis gelungen.
Wir wissen, dass dies unglaubwürdig klingt, jedoch haben wir zeitgemäß vor zwei Wochen mit der Implementation begonnen.
