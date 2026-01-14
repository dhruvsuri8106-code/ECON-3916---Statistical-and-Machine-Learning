# The Illusion of Growth & The Composition Effect

## Objective
Built a Python pipeline to ingest live economic data from the Federal Reserve API (FRED) to analyze wage stagnation in the U.S. and identify statistical biases that distort our understanding of real economic growth.

## Tech Stack
- **Python**: Data processing and analysis
- **fredapi**: Federal Reserve Economic Data API integration
- **pandas**: Time-series data manipulation
- **matplotlib**: Economic data visualization

## Methodology

### 1. Data Acquisition via FRED API
Fetched two critical datasets directly from the Federal Reserve:
- **AHETPI**: Average Hourly Earnings of Production and Nonsupervisory Employees (nominal wages)
- **CPI**: Consumer Price Index for All Urban Consumers (inflation measure)

### 2. Real Wage Calculation
Converted nominal wages to real purchasing power by adjusting for inflation, revealing the true trajectory of worker compensation over 50+ years.

### 3. Anomaly Detection: The 2020 Spike
Identified a sharp, unexpected increase in real wages during the COVID-19 pandemic—a statistical anomaly that contradicted economic conditions.

### 4. Composition Effect Correction
To validate the anomaly, I integrated the **Employment Cost Index (ECI)**, which controls for changes in workforce composition. This proved the 2020 spike was artificial: low-wage workers exiting the labor force inflated the average, not genuine wage growth.

## Key Findings

### The Money Illusion
Visualized over five decades of wage data, demonstrating that while nominal paychecks have grown substantially, real purchasing power has remained essentially flat—workers today can buy roughly the same amount as workers in the 1970s.

### The Pandemic Paradox
The 2020 wage "boom" was a statistical mirage. When restaurants, retail, and service industries shed millions of low-wage jobs, the remaining workforce skewed higher-income, artificially inflating average wages. The ECI data confirmed no true increase in labor demand or compensation occurred—only a compositional shift in who remained employed.

**Implication**: This analysis highlights the critical importance of understanding statistical bias in economic data. Raw averages can deceive policymakers and the public, masking the real economic struggles of American workers.
