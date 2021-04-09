Hallo und willkommen zum Methoden-Workshop _„How to build an artificial Coder? Einführung in die automatisierte Inhaltsanalyse mit Machine Learning“_ des Nachwuchsnetzwerks politische Kommunikation [NapoKo](http://napoko.de/workshop-artificial-coder/)! Schön, dass ihr dabei gewesen seid! 

Auf dieser Seite findet ihr das Workshop-Material sowie weiterführnde Tutorials und Literatur zum Thema Machine Learning und Automatisierte Inhaltsanalyse. Ihr könnt das Workshop-Material gerne unter der [CC-Licence](https://github.com/ankekat1000/Workshop-ML-Automatisierte-Inhaltsanalyse/blob/main/LICENSE) weiterverwenden! Der Workshop ist auf **4h (+ 1h extra Übungseinheit)** ausgelegt und für **Kommunikationswissenschaftler:innen ohne Vorkenntnisse** auf dem Gebiet der Informatik oder des Maschinellen Lernens konzipiert worden.

Bei Fragen zum Inhalt schreibt einfach eine Mail an die Dozentin [Anke Stoll](mailto:anke.stoll@hhu.de). Weitere Workshop-Angebote zu aktuellen Methoden für die (politische) Kommunikationsiwssenschaft findet ihr auf der [NapoKo-Webiste](http://napoko.de/).

Viel Spaß :two_hearts:

### Hier kannst du das Material herunterladen 

Klicke [hier](https://github.com/ankekat1000/Workshop-ML-Automatisierte-Inhaltsanalyse/archive/main.zip), um den Workshop-Ordner als **.zip-Datei** herunterzuladen oder guck dir das Material direkt auf [GitHub](https://github.com/ankekat1000/Workshop-ML-Automatisierte-Inhaltsanalyse) an. Im Workshop-Ordner findest du alle **Skripte, Folien und Datensätze**, die wir im Workshop benutzt haben. Im `README` des Workshop-Ordners findest du noch eine detaillierte Beschreibung zu den einzelnen Inhalten und Dateien.

### Workshop-Agenda

Der Workshop ist auf ca. 2x 2h (+ 1h optionale Übungssession) angelegt. Präsentation und praktische Umsetzung ergänzen sich und wechseln sich ab.

Block 1 (2h mit Pausen)

- #KI, #MachineLearning, #DeepLearning - Buzzwords klären!
- ML für die automatisierte Inhaltsanalyse
- Software Set-up und Data Prep für ML mit Textdokumenten

Block 2 (2h mit Pausen)
 
- Einen Hate-Speech-Classifier bauen - Step by Step
- ML-Modelle evaluieren und bewerten

Übungssession (1 h)

- An einem anderen Datensatz gemeinsam einen Classifier programmieren und evaluieren


## Vorraussetzungen

Für den Workshop sind keine Programmiervorkenntnisse nötig. Fürs Programmieren sollten aber Python sowie die nötigen Packages fürs Machine Learning vorab installiert werden. Hier findest du eine Anleitung zu den einzelnen Schritten:

- **Python mit Anaconda installieren**: Gehe auf die [Homepage von Anaconda](https://www.anaconda.com/products/individual) und und lade dir unter _Individual Edition_ die Software (Your data science toolkit -> Download) für dein Betriebssystem. Anaconda benutzen wir, damit wir unter Windows- und Mac einfacher programmieren können. Mit Anaconda erhälts du Python, viele vorinstallierte Python-Packages und Programmiersoftware, wie z.B. Jupyter Notebook. In diesem [Tutorial](https://www.youtube.com/watch?v=5mDYijMfSzs "Watch this first tutorial") kannst du dir ansehen, wie du Anaconda unter Windows 10 installierst (bis min 05:07).

[![IMAGE ALT TEXT](http://img.youtube.com/vi/5mDYijMfSzs/0.jpg)](http://www.youtube.com/watch?v=5mDYijMfSzs "Watch this first tutorial")

- **Python-Packages installieren**: Folge dem Tutorial weiter (min 05:08 - 06:41) um zu lernen, wie man Python-Packages installiert. (Dies ist nur eine von mehreren Möglichkeiten.) Versuche die folgenden Packages zu installieren, die wir für die Automatisierte Inhaltsanaylse mit Machine Learning benötigen:

```
conda install pandas
conda install scikit-learn
```

Für das `Extra_Notebook_Advanced.ipynb` braucht ihr diese Packages. Dieses Notebook geht jedoch über die Workshop-Agenda hinaus und ist optional.

```
conda install matplotlib
conda install seaborn
```

- **Lerne die Programmierumgebung kennen**: Die Software [**Jupyter Notebook**](https://jupyter.org/) macht mit ihrem intuitiven Design Nicht-Programmierer:innen den Einstieg leicht! Jupyter Notebook ist mit Anaconda bereits auf deinem Computer gelandet. Lerne mit Hilfe dieses kurzen [Tutorials](https://www.youtube.com/watch?v=NIGcXjhXNug "Watch this cute tutorial") die Jupyter-Notebook-Programmierumgebung kennen.

[![IMAGE ALT TEXT](http://img.youtube.com/vi/NIGcXjhXNug/0.jpg)](https://www.youtube.com/watch?v=NIGcXjhXNug "Watch this cute tutorial")

- **Packages importieren**: Navigiere dich nun im Menü von Jupyter Notebook in den Workshop-Ordner und versuche das Notebook `requirements.ipynb` auszuführen. Wenn sich alle Packages ohne Fehlermeldung importieren lassen, bist du gewappnet für den Workshop!


- **Optional: Can't wait!** Wenn du schon mal anfangen möchtest, dich mit **Python** zu beschäftigen, empfehlen wir dir diese [Video-Series](https://www.youtube.com/watch?v=5_QXMwezPJE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=2 "Watch some videos of one of my favorite ML YouTubers"). Es handelt sich um eine Einführung in die wunderbare Python-Bibliothek `Pandas`, mit der Daten in Python eingelesen und bearbeiten werden können und die aus der Welt des ML und der Data Sciences nicht mehr wegzudenken ist! (Du kannst mit dem 2. Video beginnen). Im Workshop-Ordner `Data Sets` findest du zwei .csv-Dateien mit Tweets, die du als Übung einlesen und untersuchen kannst.

[![IMAGE ALT TEXT](http://img.youtube.com/vi/5_QXMwezPJE/0.jpg)](https://www.youtube.com/watch?v=5_QXMwezPJE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=2 "Watch some videos of one of my favorite ML YouTuber")


## Weiterführendes Material

#### Daten bearbeiten, manipulieren, analysieren und visualisieren mit Pandas

[Video-Series: Data with Pandas for Beginners](https://www.youtube.com/watch?v=5_QXMwezPJE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=2 "Watch some videos of one of my favorite ML YouTubers")

[Kurzer und leicht verständlicher Blog Post](https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673)

[Etwas ausführlicherer und leicht verständlicher Blog Post](https://towardsdatascience.com/a-complete-pandas-guide-2dc53c77a002)

#### Machine Learning und Document Classification allg.

[Video-Series: ML mit scikit-learn for Beginners](https://www.youtube.com/playlist?list=PL5-da3qGB5ICeMbQuqbbCOQWcS6OYBr5A)

Video: Spam Detection mit scikit-learn [Part 1](https://www.youtube.com/watch?v=RZYjsw6P4nI&t=23s) und [Part 2](https://www.youtube.com/watch?v=bPYJi1E9xeM&t=354s)

[Sehr langes Video: ML mit scikit-learn am Bsp. User Reviews](https://www.youtube.com/watch?v=M9Itm95JzL0)

[Tipp: ML noch mal als Kurs im Schnelldurchlauf](https://www.youtube.com/watch?v=vTaxdJ6VYWE) 


#### Deep Learning

Basic Einführung in DL mit der Bibliothek Keras [Part 1](https://www.youtube.com/watch?v=hBPT6_JoUvU) und [Part 2](https://www.youtube.com/watch?v=eMtbdZC6p80)


**Lehrbücher**

Géron, A. (2019). *Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow: Concepts, tools, and techniques to build intelligent systems.* O'Reilly Media.
(Kapitel 1, S. 23-32 & Kapitel 4)

Müller, A. C., & Guido, S. (2016). *Introduction to machine learning with Python: a guide for data scientists.* O'Reilly Media, Inc.. 
(Kapitel 2, 5 & 7)


Raschka, S., & Mirjalili, V. (2017). *Python machine learning.* Packt Publishing Ltd.
(Kapitel 3, 4, 6 & 8)


Viel Spaß!
