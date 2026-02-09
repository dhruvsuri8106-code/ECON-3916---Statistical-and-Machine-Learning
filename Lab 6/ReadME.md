Here’s a clean, professional **README.md** entry you can drop straight into a project repo or portfolio. It’s written to signal *technical rigor + conceptual depth* (very ML-econ-meets-engineering, in a good way).

---

# Lab 5: The Architecture of Bias

## Overview

This lab investigates how bias can be *engineered into results* through the **Data Generating Process (DGP)** and **sampling design**, even before any model is trained. Using controlled simulations and statistical diagnostics, the project demonstrates how flawed sampling and data collection mechanisms produce misleading inferences in machine learning and experimentation systems.

The lab bridges **statistical theory**, **machine learning practice**, and **experimental forensics**, with a particular focus on bias that arises *upstream* of model estimation.

---

## Objectives

* Analyze how sampling methods alter empirical distributions and downstream model behavior
* Demonstrate variance inflation and covariate shift caused by naïve sampling
* Detect hidden engineering failures in A/B tests using statistical hypothesis testing
* Connect applied diagnostics to economic concepts such as **survivorship bias** and **selection bias**

---

## Tech Stack

* **Python**
* **pandas**, **numpy**
* **scipy** (Chi-Square goodness-of-fit tests)
* **scikit-learn** (Stratified Sampling, preprocessing)

---

## Methodology

### 1. Simple Random Sampling (SRS) — Variance Amplification

* Manually implemented Simple Random Sampling on the **Titanic dataset**
* Demonstrated how small or unbalanced samples produce:

  * High variance in feature distributions
  * Instability in class proportions
* Showed that “random” does not imply “representative,” especially under finite samples

**Key takeaway:** Random sampling alone does not protect against distributional distortion.

---

### 2. Stratified Sampling — Eliminating Covariate Shift

* Applied **stratified sampling** using `sklearn` to preserve class distributions
* Ensured consistent representation across key covariates (e.g., survival outcome)
* Reduced sampling error and stabilized downstream model inputs

**Key takeaway:** Stratification explicitly controls the DGP instead of hoping randomness behaves.

---

### 3. Sample Ratio Mismatch (SRM) Forensic Audit

* Simulated an A/B test with a planned 50/50 split
* Detected imbalance using **Chi-Square goodness-of-fit tests**
* Diagnosed SRM as evidence of **systemic failure**, not random noise

**Use case:**

* Load balancer bugs
* Eligibility filtering errors
* Logging or instrumentation loss

**Key takeaway:** Statistical tests can be used as *forensic tools* to audit experimental infrastructure.

---

## Theoretical Extension: Survivorship Bias & Ghost Data

### Question

**Why does analyzing only successful Unicorn startups (e.g., TechCrunch coverage) lead to Survivorship Bias, and what Ghost Data is required to correct it using a Heckman Correction?**

### Answer

Analyzing only successful Unicorn startups introduces **Survivorship Bias** because the dataset is *conditioned on success*. The observed firms are not a random sample of all startups—they are the subset that survived long enough to grow, raise capital, and attract media coverage.

This creates a **selection problem**:

* Failure is not random
* The probability of being observed depends on latent variables such as:

  * Founder background
  * Access to capital
  * Network effects
  * Timing and macro conditions

As a result, naïve regression estimates (e.g., “what predicts Unicorn status?”) are **biased and inconsistent**.

---

### Ghost Data Required for a Heckman Correction

To fix this, you need **Ghost Data** from the *selection equation*—data that explains *why some startups are observed and others are not*, even if their outcomes are missing.

Specifically, you need data on **non-surviving startups**, including:

* Startups that failed, shut down, or never raised follow-on funding
* Firms that existed but were never covered by TechCrunch
* Variables that affect *selection* but not *outcomes* directly (exclusion restrictions), such as:

  * Local investor density
  * Accelerator access
  * Industry funding cycles
  * Founder geography

This Ghost Data allows you to:

1. Model the **probability of being observed** (selection equation)
2. Estimate the **Inverse Mills Ratio**
3. Correct outcome regressions for non-random sample selection

---

### Core Insight

> Bias is rarely a modeling problem.
> It is almost always a **data visibility problem**.

If you don’t model *why data appears*, you will systematically misinterpret *what the data means*.

---

## Key Takeaways

* Sampling is part of the model
* Randomness does not imply fairness or representativeness
* Statistical tests can audit systems, not just data
* Missing data is often *structural*, not accidental

---

If you want, I can:

* Tighten this for a **resume / portfolio blurb**
* Rewrite it in a **research-paper tone**
* Add **figures, equations, or pseudo-code** for the Heckman framework
