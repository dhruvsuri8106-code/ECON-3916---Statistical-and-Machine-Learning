# Clustering World Economies with K-Means & PCA

## Objective
This project applies unsupervised machine learning to group countries with similar macro-development profiles, using K-Means clustering and PCA to identify cross-country patterns in economic structure and assess how closely data-driven clusters align with World Bank income classifications.

## Methodology
- Retrieved 10 World Bank development indicators for approximately 160 countries using the `wbgapi` package.
- Built a country-level feature matrix capturing multiple dimensions of economic and development performance.
- Standardized all features with `StandardScaler` to ensure that each variable contributed equally to the K-Means distance calculations.
- Fit K-Means clustering models to the standardized country data, with an initial benchmark specification of **K = 4**.
- Applied PCA to reduce the feature space to two principal components and visualize cluster structure in a 2D scatter plot.
- Evaluated cluster solutions from **K = 2 through K = 10** using both the elbow method and silhouette analysis.
- Cross-tabulated model-generated clusters against official World Bank income classifications to assess external interpretability.
- Replicated the same clustering pipeline on the California Housing census tract dataset to test the generalizability of the workflow across datasets.

## Key Findings
- The clustering analysis identified meaningful structure in the cross-country development data, showing that countries can be grouped according to broader macroeconomic similarity rather than income level alone.
- PCA visualization indicated that the main variation in the dataset could be represented effectively in two dimensions while still preserving visible cluster separation.
- Based on the combined evidence from the elbow method and silhouette analysis, **K = 3** emerged as the optimal cluster solution.
- The resulting clusters showed **moderate alignment** with World Bank income classifications, suggesting that income groupings capture part of the underlying structure in the data but do not fully explain broader development similarities.
- Differences between algorithmic clusters and income classifications pointed to meaningful heterogeneity within traditional income categories.
- Applying the same workflow to the California Housing dataset demonstrated that the clustering framework is transferable and useful for identifying latent structure in other socioeconomic datasets.

## Interpretation
From a data science and economic analysis perspective, this project demonstrates that K-Means can serve as a valuable exploratory tool for segmenting economies in a more multidimensional way than standard income classifications allow. The results suggest that while income level remains informative, a broader indicator-based approach can reveal more nuanced patterns of economic similarity across countries.
