# Global Purchasing Power Parity Analysis

## Objective
Empirically tested the Law of One Price using "Burgernomics"—a novel application of purchasing power parity theory through standardized Big Mac prices across international markets.

## Tech Stack
- **Python**: Data analysis and statistical computation
- **pandas**: Currency valuation calculations and comparative analysis

## Methodology

### 1. Data Construction
Manually structured a comprehensive cross-country dataset using The Economist's 2015 Big Mac Index, capturing local currency prices and official exchange rates for identical goods across 50+ global markets spanning six continents.

### 2. Implied PPP Calculation
Computed theoretical exchange rates based on Big Mac price equivalence, establishing what currency values *should* be if purchasing power parity held perfectly in frictionless markets.

### 3. Currency Misalignment Analysis
Quantified the percentage deviation between market exchange rates and implied PPP rates to identify systemic overvaluation and undervaluation patterns relative to the US Dollar baseline.

### 4. Regional Pattern Recognition
Segmented findings by economic development level and geographic region to identify structural trends in currency misalignment across developed, emerging, and frontier markets.

## Key Findings

### Systematic Currency Deviations
The analysis revealed substantial and persistent deviations from the Law of One Price across global markets, with currency misalignments ranging from -50% to +40% relative to PPP-implied values.

### Developed Market Patterns
Scandinavian and Western European currencies demonstrated consistent overvaluation, reflecting higher labor costs, stronger purchasing power, and premium pricing in service-intensive economies. These findings align with the Balassa-Samuelson effect—wealthier nations sustain higher price levels due to productivity differentials in tradable versus non-tradable sectors.

### Emerging Market Dynamics
Emerging and developing economy currencies exhibited significant undervaluation, suggesting either competitive exchange rate positioning or structural inefficiencies in local markets. This pattern presents potential arbitrage opportunities but also reflects real economic factors including lower wage levels and reduced non-tradable service costs.

### Economic Interpretation
The persistent violations of the Law of One Price underscore real-world market frictions: trade barriers, transportation costs, labor market heterogeneity, tax structures, and the substantial non-tradable service component embedded in Big Mac production. Currency overvaluation correlates with reduced export competitiveness, while undervaluation may indicate either deliberate monetary policy or fundamental economic constraints. This analysis demonstrates that PPP serves as a long-run equilibrium concept rather than a short-term arbitrage mechanism, with deviations providing insights into relative living costs and competitive positioning across global markets.
