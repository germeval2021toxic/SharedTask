# Welcome!
# To the Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments

:warning: ***Disclaimer**: Please note that we display examples of toxic user comments on this website for better understanding and transparency.*

## Task Overview

With this year´s shared task, we want participants to go beyond the identification of offensive comments.
To this end, we extend the focus to two other classes of comments that are highly **relevant** to **moderators** and **community managers** on online discussion platforms: **engaging** comments and **fact-claiming** comments, meaning comments that should be considered as a **priority for fact-checking**.


### Subtask 1: :imp: Toxic Comment Classification (Binary Classification Task)


The detection of **toxic content** in online discussions **remains challenging** and new approaches are constantly being demanded and developed. With this subtask we aim to **continue** the series of previous **GermEval Shared Tasks** on Offensive Language Identification.

| message      | Sub1_Toxic |
| ----------- | ----------- |
| *"Na,  welchem tech riesen hat er seine Eier verkauft..?"*      | 1       |
| *"Ich macht mich wütend, dass niemand den Schülerinnen Gehör schenkt"*   | 0        |


### Subtask 2: :hugs: Engaging Comment Classification (Binary Classification Task)

In addition to the detection of toxic language, community managers and moderators increasingly express interest in **identifying particularly valuable** user content, for example, to highlight them and to give them more visibility. That includes rational, respectful, and reciprocal comments that can **encourage** readers to join the discussion, **increase positive perceptions** of discussion providers, and can enhance more **fruitful** and less violent exchange.

| message      | Sub2_Engaging |
| ----------- | ----------- |
| *"Wie wär’s mit einer Kostenteilung. Schließlich haben beide Parteien (Verkäufer und Käufer) etwas von der Tätigkeit des Maklers. Gilt gleichermassen für Vermietungen. Die  Kosten werden so oder soweit verrechnet, eine Kostenreduktion ist somit nicht zu erwarten."*      | 1       |
| *"Die aktuelle Situation zeigt vor allem eines: viele Kinder mussten erkennen, dass ihre Mutter bestenfalls das Niveau Grundschule, Klasse 3 haben."*   | 0        |


### Subtask 3: :point_up: Fact-Claiming Comment Classification (Binary Classification Task)

Beyond the challenge to ensure non-hostile debates, platforms and moderators are under pressure to act due to the rapid spread of **misinformation** and fake news. 
Platforms need to review and verify posted information to meet their **responsibility** as information providers and distributors. 
As a result, there is an increasing demand for systems that automatically identify comments that should be fact-checked manually.
Note that this subtask is not about the fact-checking itself or the identification of fake news.
However, the identification of fact-claiming comments is a **pre-processing step for manual fact-checking**.

| message      | Sub3_FactClaiming |
| ----------- | ----------- |
| *"Kinder werden nicht nur seltener krank, sie infizieren sich wohl auch seltener mit dem Coronavirus als ihre Eltern - das ist laut Ministerpräsident Winfried Kretschmann (Grüne) das Zwischenergebnis einer Untersuchung der Unikliniken Heidelberg, Freiburg und Tübingen."*      | 1       |
| *"hmm...das kann ich jetzt nich nachvollziehen..."*   | 0        |


## How to Participate

Teams can participate either in all three or just in one or two of the subtasks. Please register individually [via google forms](https://docs.google.com/forms/d/e/1FAIpQLSe7R-rfHNU-mXlP6w7sg6A3rogduuityeM_lhF8OiS8zJnixg/viewform) with your name and your institution or company. After your registration, you will receive the link and password to the training data sent via email. All teams that have submitted a system response will be invited to write a (short) paper about their approach by July 15, 2021 to be published in the GermEval2021 conference proceedings. (Overleaf and Word tamplates can be provided.) Have a look at [recent year's proceedings](https://germeval.github.io/) of the GermEval Shared Tasks on the Identification of Offensive Languagen for inspiration.


## Data Set and Resources

We provide an annotated dataset of over **3,000 Facebook user comments** that have been labeled by four trained annotators. The dataset is drawn from the Facebook page of a **political talk show of a German television broadcaster**, including user discussions from February till July **2019**. The dataset will be shared with **registered participants** and will be made accessible for academic research purposes  after  the  shared  task has ended. The  dataset is provided in **anonymized** form. User information and comment IDs will not be shared. Links to users are replaced by *@USER*. Links to the show are replaced by *@MEDIUM,* and links zu the moderator of the show are replacd by *@MODERATOR*. The data is provided in .csv-format and the following structure:

| comment_id | comment_text | Sub1_Toxic | Sub2_Engaging | Sub3_FactClaiming |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 1 | *"Kinder werden...."*      | 0 | 0 | 1 |
| 2 | *"Die aktuelle Situation zeigt vor allem..."* | 0 | 1 | 0 |
| ... | ... | ... | ... | ... | 

For trial data, a sample of user comments to two shows are provided. The user comments in the test data will be drawn from discussions on different shows than in the training data. This way, we can provide a realistic use case and further can control a possible bias causes by topics.

The annotation guidelines for the data set can be obtained upon request.


## Evaluation

To evaluate your approach, you will upload your predictions on the test data set that will be released shortly before the task will terminate. We will use the platform [codalab](https://codalab.org/) for evaluation.
For evaluation, the metrics precision, recall, and macro-average F1-score are used. 

## Time Line

- :heavy_check_mark: Registration is open: April 15, 2021
- :heavy_check_mark: Trial data release: April 15, 2021
- Train data release: April 30, 2021
- Test data release: June 23, 2021
- Submission deadline to codalab: June 30, 2021
- Results are announced: July 7, 2021
- Paper submission due: July 15, 2021
- Camera ready due: August 10, 2021
- KONVENS conference: September 6-10, 2021


## About GermEval

GermEval is a series of shared task evaluation campaigns that focus on Natural Language Processing for the German language. So far, there have been six iterations of GermEval, each with different types of tasks: [https://germeval.github.io/tasks/](https://germeval.github.io/tasks/) GermEval shared tasks have been run informally by self-organized groups of interested researchers. However, many of the shared tasks were endorsed by special interest groups within the [German Society for Computational Linguistics (GSCL)](https://gscl.org/en). The Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments is endorsed by the [IGGSA (Interest Group on German Sentiment Analysis)](https://sites.google.com/site/iggsahome/home).


## About KONVENS

The GermEval 2021 workshop is part of [KONVENS 2021](https://konvens2021.phil.hhu.de/). KONVENS (Konferenz zur Verarbeitung natürlicher Sprache/Conference on Natural Language Processing) is an annual conference series on computational linguistics that is organized under the auspices of the German Society for Computational Linguistics and Language Technology (GSCL), the Special Interest Group on Computational Linguistics of the German Linguistic Society (DGfS-CL) and the Austrian Society for Artificial Intelligence (ÖGAI).

## Organizers

- Julian Risch (Hasso Plattner Institute, University of Potsdam)
- Anke Stoll (Department of Social Sciences, Heinrich Heine University Düsseldorf)
- Lena Wilms (Department of Social Sciences, Heinrich Heine University Düsseldorf)
- Michael Wiegand (Digital Age Research Center, University of Klagenfurt)

If you have any questions, please do not hesitate to [contact us](mailto:germeval2021toxic@gmail.com)!
