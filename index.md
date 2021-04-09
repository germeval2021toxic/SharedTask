# Welcome!
# To the Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments

If you have any questions, please do not hesitate to [contact us](mailto:germeval2021toxic@gmail.com)!

:warning: ***Disclaimer**: Please note that we display examples of toxic user comments on this website for better understanding and transparency.*

## Task Overview

With this year´s shared task, we want participants to go beyond the identification of offensive comments.
To this end, we extend the focus to two other classes of comments that are highly **relevant** to **moderators** and **community managers** on online discussion platforms: **engaging** comments and **fact-claiming** comments, meaning comments that should be considered as a **priority for fact-checking**.


### :imp: Subtask 1: Toxic Comment Classification (Binary Classification Task)


Still, the detection of **toxic content** in online discussions **remains challenging** and new approaches are constantly being demanded and developed. With this subtask we aim to **continue** the series of previous **GermEval Shared Tasks** on Offensive Language Identification.

| message      | Sub1_Toxic |
| ----------- | ----------- |
| *"Na,  welchem tech riesen hat er seine Eier verkauft..?"*      | 1       |
| *"Ich macht mich wütend, dass niemand den Schülerinnen Gehör schenkt"*   | 0        |


### Subtask 2: Engaging Comment Classification (Binary Classification Task)

In addition to the detection of toxic language, community managers and moderators increasingly express interest in **identifying particularly valuable** user content, for example, to highlight them and to give them more visibility. That includes rational, respectful, and reciprocal comments that can **encourage** readers to join the discussion, **increase positive perceptions** of discussion providers, and can enhance more **fruitful** and less violent exchange.

| message      | Sub2_Engaging |
| ----------- | ----------- |
| *"Wie wär’s mit einer Kostenteilung. Schließlich haben beide Parteien (Verkäufer und Käufer) etwas von der Tätigkeit des Maklers. Gilt gleichermassen für Vermietungen. Die  Kosten werden so oder soweit verrechnet, eine Kostenreduktion ist somit nicht zu erwarten."*      | 1       |
| *"neutral comment....................."*   | 0        |


### Subtask 3: Fact-Claiming Comment Classification (Binary Classification Task)

Beyond the challenge to ensure non-hostile debates, platforms and moderators are under pressure to act due to the rapid spread of **misinformation** and fake news. 
Platforms need to review and verify posted information to meet their **responsibility** as information providers and distributors. 
As a result, there is an increasing demand for systems that automatically identify comments that should befact-checked manually.
Note that this subtask is not about the fact-checking itself or the identification of fake news.
However, the identification of fact-claiming comments is a **pre-processing step for manual fact-checking**.

| message      | Sub3_FactClaiming |
| ----------- | ----------- |
| *"Die aktuelle Situation zeigt vor allem eines: viele Kinder mussten erkennen, dass ihre Mutter bestenfalls das Niveau Grundschule, Klasse 3 haben."*      | 1       |
| *"neutral comment....................."*   | 0        |


## How to Participate

Teams can participate either in all three subtasks or just one ore two of the following subtasks. Please register via google forms with your name and your institution or company. After your registration, you will recieve the password to the training data set via mail.

## Data Set and Resources

We provide an annotated dataset of Facebook usercomments that have been labeled by four trainedannotators. The dataset is drawn from the Facebook page of a German news broadcast, including user discussions from February till July 2019. The dataset will be shared with registered participants and will be made accessible for academic research purposes  after  the  shared  task has ended. The  dataset is provided in anonymized form. User information and comment ID’s will not be shared.
For allcomments, we provide information on the shared context by adding the teaser text of the Facebook article posting. If a comment is a reply comment(sublevel-comment), the initial comment’s text is also provided (toplevel-comment).

## Evaluation


## Recent Germeval Tasks

## Please Cite


Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
