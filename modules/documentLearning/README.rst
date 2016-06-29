.. image:: http://userpages.uni-koblenz.de/~mschanz/ass03.jpg
   :align: center
   :target: https://github.com/fuuman/101worker/tree/master/modules/documentLearning
   :alt: documentLearning Logo

Usage
-----
Die Jsondateien müssen in den Projektordner eingefügt werden sowie die wiki-content.json
Der z Wert innerhalb der Datein jsonExtractor.py muss angepasst werden, sodass er auch wirklich nur json Dateien innerhalb des Ordners einliest.
Der eigentlich Aufruf befindet sich in NatLan.py ganz unten.

External Code
-------------
We took the Naive Bayes algorithm from the NLTK.
For more information, visit http://www.nltk.org/ , or more specifically http://www.nltk.org/api/nltk.classify.html?highlight=naive%20bayes#module-nltk.classify.naivebayes

Our module
----------
Document learning: The different namespaces on the wiki come with different expected sections. For instance, each page in the namespace
"Contribution" is supposed to contain a section "Characteristics".
The complete set of possible (actual) section names can be found by extracting all section names from the dump wiki-content.json.
Apply machine learning to provide a prediction model with the namespace as the input data and section names as labels. Use some pages as a training set.
By applying the prediction model to further pages, try to identify pages with missing or unexpected sections.
A missing section means that prediction suggests that a section should be there for the page's namespace at hand; likewise for an unexpected section.

Interpretation of the result 
----------------------------
Wir haben aus den Json-Dateien die Namespaces und ihre jeweiligen Sections extrahiert. Danach haben wir anhand der Daten ein Prediction Model mit machine learning erstellt.
Uns fehlt dabei jedoch der Übergang, zu testen und damit missing und unexspected in jeweilige json Dateien einzutragen.
Wir wollten mit dem Prediction Model die jeweiligen sections der namespaces vergleichen und wenn ein neues erkannt wird, ist es unexpected und wenn eines fehlt, dann ist es missing.
Bei den ausgegebenen Dictionaries wurde jeder Section eines Namespaces eine bestimmte approximierte Wahrscheinlichkeit über den Bayes Algorithmus zugewiesen.
In 'List for comparison for tests' stehen alle Sections dieses Namespaces drin, die nicht über unser Prediction Model aussortiert wurden, wenn also die Wahr-
scheinlichkeit der Section über 10% lag.

Problems
--------
Probleme traten jedoch dabei auf, die Prediction Models jeweiligen Namespaces zuzuweisen, sodass wir nicht mehr fortfahren konnten mit unserer Arbeit.
Diese Probleme traten vor allem auf, durch mangelnde Python-Kenntnisse und der gleichzeitig zu erlernenden NLTK Library. Mit mehr Zeit wäre uns wahrscheinlich ein abschließendes Ergebnis gelungen.
Wir wissen, dass dies unglaubwürdig klingt, jedoch haben wir zeitgemäß vor zwei Wochen mit der Implementation begonnen.

Developers
----------
- Marco Schanz
- Diana Richter
- Marius Beckmann
- Frank Schaust
- André-Gilbert Thomas
- Isabelle Kuhlmann
