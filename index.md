# Welcome!
# To the Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments

## GermEval Workshop @KONVENS 2021

The GermEval wrkshop will take place on **Monday, 06.09.2021** from 09:00 a.m. to 02:00 p.m. at [KONVENS](https://konvens2021.phil.hhu.de/). Please do not forget to [register for the conference](https://konvens2021.phil.hhu.de/registration/), if you want to attend the workshop.

| Time      | Program |
| ----------- | ----------- |
| 09:00      | Welcome and presentation of the Shared Task |
| 09:30   | One Minute Madness for all participants |
| 09:50   | <b>Session 1</b> (chair: Anke Stoll): <br /> *DFKI SLT at GermEval 2021: Multilingual Pre-training and Data Augmentation for the Classification of Toxicity in Social Media Comments* by R. Calizzano, M. Ostendorff, G. Rehm (25 min) <br /> <br /> *UPAppliedCL at GermEval 2021: Identifying Fact-Claiming and Engaging Facebook Comments Using Transformers* by R. Schäfer, M. Stede (25 min) |
| 10:40 | break |
| 11:00   | <b>Session 2</b> (chair: Michael Wiegand): <br /> *Data Science Kitchen at GermEval 2021: A Fine Selection of Hand-Picked Features, Delivered Fresh from the Oven*  by N. Hildebrandt, B. Boenninghoff, D. Orth, C. Schymura  (25 min) <br /> <br /> *DeTox at GermEval 2021: Toxic Comment Classification*  by M. Schütz, C. Demus, J. Pitz, N. Probol, M. Siegel, D. Labudde  (25 min) <br /> <br /> *AIT FHSTP at GermEval 2021: Automatic Fact Claiming Detection with Multilingual Transformer Models*  by J. Böck, D. Liakhovets, M. Schütz, A. Kirchknopf, D. Slijepčević, M. Zeppelzauer, A. Schindler  (25 min)|
| 12:15 | break |
| 12:35   | <b>Session 3</b> (chair: Lena Wilms): <br /> *FHAC at GermEval 2021: Identifying German toxic, engaging, and fact-claiming comments with ensemble learning*  by T. Bornheim, N. Grieger, S. Bialonski  (25 min) <br /> <br /> *WLV-RIT at GermEval 2021: Multitask Learning with Transformers to Detect Toxic, Engaging, and Fact-Claiming Comments*  by S. Morgan, T. Ranasinghe, M. Zampieri  (25 min) |
| 13:25 | Feedback & Further Information |
| 14:00 | End of the Event |

## GermEval 2021 Proceedings

The proceedings have been published by <a href="https://netlibrary.aau.at/">netlibrary</a>. You can find them <a href="https://netlibrary.aau.at/obvukloa/content/titleinfo/6435190">here</a>.<br />
If you want to browse the individual contributions, you may find <a href="https://netlibrary.aau.at/obvukloa/content/structure/6435190">this link</a> more helpful. <br /> 

URN: <a href="https://resolver.obvsg.at/urn:nbn:at:at-ubk:3-798">urn:nbn:at:at-ubk:3-798</a> <br />
DOI: <a href="https://dx.doi.org/10.48415/2021/fhw5-x128">10.48415/2021/fhw5-x128</a> <br /> 

## Task Overview

:warning: ***Disclaimer**: Please note that we display examples of toxic user comments on this website for better understanding and transparency.*

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


## Survey

We compiled a survey for this year's shared task in which we asked each participant to provide details on their submission. 
You can find the **responses to our survey** [here](https://github.com/germeval2021toxic/SharedTask/blob/main/GermEval2021_Survey.pdf).

## Data Set and Resources

We provide an annotated dataset of over **3,000 Facebook user comments** that have been labeled by four trained annotators. The dataset is drawn from the Facebook page of a **political talk show of a German television broadcaster**, including user discussions from February till July **2019**. The dataset will be shared with **registered participants** and will be made accessible for academic research purposes  after  the  shared  task has ended. The  dataset is provided in **anonymized** form. User information and comment IDs will not be shared. Links to users are replaced by *@USER*. Links to the show are replaced by *@MEDIUM,* and links zu the moderator of the show are replacd by *@MODERATOR*. The data is provided in .csv-format and the following structure:

| comment_id | comment_text | Sub1_Toxic | Sub2_Engaging | Sub3_FactClaiming |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 1 | *"Kinder werden...."*      | 0 | 0 | 1 |
| 2 | *"Die aktuelle Situation zeigt vor allem..."* | 0 | 1 | 0 |
| ... | ... | ... | ... | ... | 

For trial data, a sample of user comments to two shows are provided. The user comments in the test data will be drawn from discussions on different shows than in the training data. This way, we can provide a realistic use case and further can control a possible bias causes by topics. The annotation guidelines for the data set can be obtained upon request. 

To gain access to the data set of the GermEval2021 Shared Task, please register [via google forms](https://docs.google.com/forms/d/e/1FAIpQLSe7R-rfHNU-mXlP6w7sg6A3rogduuityeM_lhF8OiS8zJnixg/viewform) with your name and your institution or company. You will be asked to agree not to share the data with third parties or use them for commercial purposes. Afterwards, you will receive the link and password to the data set sent via email.


## Evaluation

To evaluate your approach, you will upload your predictions on the test data set that will be released shortly before the task will terminate. We will use the platform [codalab](https://codalab.org/) for evaluation.
For evaluation, the metrics precision, recall, and macro-average F1-score are used. 

## Time Line

- :heavy_check_mark: Registration is open: April 15, 2021
- :heavy_check_mark: Trial data release: April 15, 2021
- :heavy_check_mark: Training data release: April 30, 2021
- :heavy_check_mark: Test data release: June 23, 2021
- :heavy_check_mark: Submission deadline of system runs: June 30, 2021
- :heavy_check_mark: Paper submission due: July 15, 2021
- :heavy_check_mark: Camera ready version due: August 2, 2021
- GermEval Workshop: September 6,  2021
- [KONVENS conference](https://konvens2021.phil.hhu.de/): September 6-10, 2021


## About GermEval

GermEval is a series of shared task evaluation campaigns that focus on Natural Language Processing for the German language. So far, there have been six iterations of GermEval, each with different types of tasks: [https://germeval.github.io/tasks/](https://germeval.github.io/tasks/) GermEval shared tasks have been run informally by self-organized groups of interested researchers. However, many of the shared tasks were endorsed by special interest groups within the [German Society for Computational Linguistics (GSCL)](https://gscl.org/en). The Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments is endorsed by the [IGGSA (Interest Group on German Sentiment Analysis)](https://sites.google.com/site/iggsahome/home).


## About KONVENS

The GermEval 2021 workshop is part of [KONVENS 2021](https://konvens2021.phil.hhu.de/). KONVENS (Konferenz zur Verarbeitung natürlicher Sprache/Conference on Natural Language Processing) is an annual conference series on computational linguistics that is organized under the auspices of the German Society for Computational Linguistics and Language Technology (GSCL), the Special Interest Group on Computational Linguistics of the German Linguistic Society (DGfS-CL) and the Austrian Society for Artificial Intelligence (ÖGAI).

## Organizers

- [Julian Risch](https://julianrisch.de/) ([deepset](https://www.deepset.ai/))
- [Anke Stoll](https://www.phil-fak.uni-duesseldorf.de/kmw/juniorprofessur-fuer-politische-online-kommunikation/team/anke-stoll/) (Department of Social Sciences, Heinrich Heine University Düsseldorf)
- [Lena Wilms](https://www.sozwiss.hhu.de/institut/abteilungen/kommunikations-und-medienwissenschaft/juniorprofessur/lena-wilms) (Department of Social Sciences, Heinrich Heine University Düsseldorf)
- [Michael Wiegand](https://www.aau.at/team/wiegand-michael/) (Digital Age Research Center, University of Klagenfurt)

If you have any questions, please do not hesitate to [contact us](mailto:germeval2021toxic@gmail.com)!
