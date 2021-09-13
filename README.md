<img src="Images/UMBC_Graduate_School.jpg" width="150">

# Analyzing How Research on Telepsychology has Changed as a Result of the Coronavirus Pandemic 
### An Application of Natural Language Processing

Jessica C. Conroy, Daniel B. Babcock, Adam M. Goldstein, Yunpeng Li, Jinqing Liang, and Jorge Neyra
UMBC Master's in Data Science Data690

# Project Abstract

The Coronavirus pandemic has had a tremendous effect on all areas of life, perhaps the most salient being the rapid transition to remote life. This paper aims to understand how that shift has impacted academic work produced in the field of telepsychology. We used a variety of Natural Language Processing (NLP) techniques to explore keywords, named entities, topics, and more across articles published between 2016 and 2021. Furthermore, we compared the results for those articles published before 2020 and the outbreak of the COVID-19 Pandemic with those published during the pandemic in order to find the changes that have occurred as a result. We identified three major groups in the literature: 1. Implementation, barriers, and evidence-based treatment; 2. Training and ethics; and 3. Covid-19 and Stress related disorders. We also identified major shifts during the pandemic towards discussing stress and stress-related disorders and away from discussing depression and self-help technologies. This paper summarizes some of the existing research on telemental health and provides a model for systematically applying NLP to identify trends in literature.

In order to obtain an unbiased understanding of the existing literature on telemental health and telepsychology,
as well as how COVID-19 has affected that literature, we used text summarization techniques including keyword extraction,
topic modelling, text similarity analysis and more to perform a review of the literature.

Keywords: Telepsychology, telemental health, NLP, NER, Topic Modeling, Text Mining, Covid-19, NMF 

# Project Framework

<p align="center">
    <img src="https://user-images.githubusercontent.com/63023492/133001304-88a725c9-51c7-474a-b668-5358f8dede4b.png">
</p>

# Key Findings Findings:

### Keyword Extraction
Frequency Counts of Unigrams, Bigrams, and Trigrams Before the COVID-19 Pandemic: (2017-2019):
![Frequency Counts Before the COVID-19 Pandemic: (2017-2019)](./Images/pre_covid_freq_count.png)

Frequency Counts of Unigrams, Bigrams, and Trigrams During the COVID-19 Pandemic: (2020-2021):
![Frequency Counts During COVID-19 Pandemic: (2020-2021)](./Images/covid_freq_count.png)

### Topic Modeling

Table 1. First 10 topics identified in the entire corpus using NMF.

<table>
  <tr>
    <th>Topic Number</th>
    <th>Key Themes within Topics</th>
    <th>Generated Topic Words</th>
  </tr>
  <tr>
    <td>Topic 1:</td>
    <td>Topic 2:</td>
    <td>Topic 3:</td>
    <td>Topic 4:</td>
    <td>Topic 5:</td>
    <td>Topic 6:</td>
    <td>Topic 7:</td>
    <td>Topic 8:</td>
    <td>Topic 9:</td>
    <td>Topic 10:</td>
  </tr>
  <tr>
    <td>Pandemic and Stress</td>
    <td>American Psychological Association and telepsychology</td>
    <td>Veteran affairs and veteran care</td>
    <td>Online technologies</td>
    <td>Research</td>
    <td>Supervision and Training</td>
    <td>Caregiver and skill-based treatment</td>
    <td>Methods of self help</td>
    <td>Rural Care and Latinx Communities</td>
    <td>Remote testing/assessment</td>
  </tr>
  <tr>
    <td>trauma, 2020, pandemic, disorder, disease, 2019, stress, posttraumatic, coronavirus, telepsychotherapy</td>
    <td>psychology, concern, american, psychological, association, client, state, practice, psychologist, telepsychology</td>
    <td>service, healthcare, care, york, harbor, affairs, telemental, hub, veteran, veterans</td>
    <td>bit, service, providers, online, couple, technologies, module, client, intervention, telemental</td>
    <td>randomized, meta, clinician, veteran, deliver, studies, face, intervention, analysis, telepsychology</td>
    <td>Director, transition, supervision, student, telepsychology, supervisor, telesupervision, training, clinic, trainee</td>
    <td>score, caregiver, posttreatment, tutorial, behavior, skill, therapy, interaction, child, parent</td>
    <td>television, book, user, guide, internet, patient, borgueta, self, help, guided</td>
    <td>family, model, integrate, primary, community, disparity, brazil, rural, care, latinx</td>
    <td>kbit, taker, index, examinee, proctor, subtest, remote, wisc, test, administration</td>
  </tr>
</table>

## Implementation Instructions
For the Implementation of the code we recommend to have the following libraries:

  - pandas
  - matplotlib
  - string
  - spacy
  - sciSpacy
  - genism
  - rake-nltk
  - sklearn
  - pattern
  - nltk
  - string
  - textwrap
  - json
  - rouge
