# FedSpeak Analysis — NLP on FOMC Minutes

## Objective
This project applies natural language processing and unsupervised learning to Federal Open Market Committee meeting minutes in order to quantify shifts in tone, uncertainty, and thematic structure across monetary policy regimes over time.

## Methodology
- Collected and organized FOMC meeting minutes spanning more than two decades.
- Preprocessed the text corpus through tokenization, lemmatization, and stop word removal to create a cleaner representation of policy language.
- Constructed a TF-IDF document-term matrix using both unigrams and bigrams to capture economically meaningful single terms and multi-word policy phrases.
- Computed dictionary-based sentiment measures using the Loughran-McDonald lexicon, including net sentiment and uncertainty scores for each document.
- Visualized the evolution of sentiment and uncertainty over time to identify changes in communication patterns across monetary policy periods.
- Reduced the dimensionality of the TF-IDF feature space with PCA and applied K-Means clustering to group FOMC minutes by linguistic similarity.
- Compared sentiment distributions between the pre-COVID and post-COVID periods to assess whether the tone of Fed communication shifted meaningfully after the pandemic shock.

## Key Findings
- The analysis revealed that FOMC communication can be separated into distinct linguistic groupings, indicating that the language of policy minutes changes systematically across different macroeconomic environments.
- K-Means clustering suggested the emergence of **[INSERT CLUSTER INTERPRETATION]**, such as clusters corresponding to more stable expansionary periods, crisis-era communication, or inflation-focused policy discussions.
- The sentiment analysis showed that net sentiment and uncertainty varied meaningfully over time, with major shifts coinciding with periods of economic stress and policy transition.
- Comparing the pre-COVID and post-COVID periods suggested that Fed communication became **[more cautious / more uncertain / less positive / more polarized]** after the pandemic, reflecting a policy environment shaped by elevated inflation, labor market volatility, and unusual macroeconomic uncertainty.
- Taken together, the results suggest that FOMC minutes contain measurable signals about evolving policy tone and economic conditions, and that NLP methods can recover those patterns in a systematic way.

## Interpretation
From a tech-economics perspective, this project demonstrates that central bank communication is not only qualitatively important but also quantitatively measurable. By combining TF-IDF text representation, dictionary-based sentiment scoring, and clustering techniques, the analysis provides a structured view of how Fed language evolves across time and policy regimes.
