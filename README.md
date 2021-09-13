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
    <td>Pandemic and Stress</td>
    <td>trauma, 2020, pandemic, disorder, disease, 2019, stress, posttraumatic, coronavirus, telepsychotherapy</td>
  <tr>
    <th>Topic 2:</th>
    <th>American Psychological Association and telepsychology</th>
    <th>psychology, concern, american, psychological, association, client, state, practice, psychologist, telepsychologys</th>
  </tr>
  <tr>
    <th>Topic 3:</th>
    <th>Veteran affairs and veteran care</th>
    <th>service, healthcare, care, york, harbor, affairs, telemental, hub, veteran, veterans</th>
  <tr>
    <th>Topic 4:</th>
    <th>Online technologies</th>
    <th>bit, service, providers, online, couple, technologies, module, client, intervention, telemental</th>
  </tr>
  <tr>
    <th>Topic 5:</th>
    <th>Research</th>
    <th>randomized, meta, clinician, veteran, deliver, studies, face, intervention, analysis, telepsychology</th>
  </tr>
  <tr>
    <th>Topic 6:</th>
    <th>Supervision and Training</th>
    <th>Director, transition, supervision, student, telepsychology, supervisor, telesupervision, training, clinic, trainee</th>
  </tr>
  <tr>
    <th>Topic 7:</th>
    <th>Caregiver and skill-based treatment</th>
    <th>score, caregiver, posttreatment, tutorial, behavior, skill, therapy, interaction, child, parent</th>
  </tr>
  <tr>
    <th>Topic 8:</th>
    <th>Methods of self help</th>
    <th>television, book, user, guide, internet, patient, borgueta, self, help, guided</th>
  </tr>
  <tr>
    <th>Topic 9:</th>
    <th>Rural Care and Latinx Communities</th>
    <th>family, model, integrate, primary, community, disparity, brazil, rural, care, latinx</th>
  </tr>
  <tr>
    <th>Topic 10:</th>
    <th>Remote testing/assessment</th>
    <th>kbit, taker, index, examinee, proctor, subtest, remote, wisc, test, administration</th>
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
