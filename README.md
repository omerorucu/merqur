<div align="center">

<img src="icon/MerQur_icon_256.png" alt="MerQur" width="160" />

# MerQur

### *Data · Analysis · Model · Meaning*

**ANALYZE · MODEL · INTERPRET · REPORT**

*İNCELE · MODELLE · YORUMLA · RAPORLA*

*ANALIZA · MODELA · INTERPRETA · REPORTA*

**End-to-End Academic Data Analysis & Reporting Platform**
*by Ömer K. Örücü*

---

![Version](https://img.shields.io/badge/version-1.0.24-7C3AED?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=flat-square)
![Languages](https://img.shields.io/badge/i18n-TR%20%7C%20EN%20%7C%20ES-success?style=flat-square)
![Analyses](https://img.shields.io/badge/analyses-124-7C3AED?style=flat-square)
![APA 7](https://img.shields.io/badge/reports-APA%207-27AE60?style=flat-square)



</div>

---

## 🔍 What is MerQur?

**MerQur** is an **integrated, end-to-end statistics platform** designed for academic
data analysis. From data ingestion to APA-7 publication-ready reports —
everything in a single tool.

<div align="center">

| **124** | **17** | **6** | **APA 7** |
|:---:|:---:|:---:|:---:|
| Statistical<br>Analyses | Analysis<br>Categories | Map-tab<br>Methods | Report<br>Generator |

</div>

In a single tool: **data import** · **descriptive statistics** · **parametric & non-parametric tests** · **regression** (LASSO, Robust, Quantile, GAM) · **survival analysis** (Cox, KM, Time-Dependent Cox) · **mixed models** (LMM, GLMM, GEE) · **multivariate** (PCA, EFA, CFA, LDA, CCA) · **complex survey design** · **spatial analysis** (KDE, Hexbin, DBSCAN, Hotspot, Moran's I, kriging) · **meta-analysis** · **SEM & IRT** · **econometrics** (panel, IV, propensity score, DiD) · **time series** (ARIMA, VAR, cointegration, GARCH) · **APA 7 reports** in DOCX/PDF/HTML/Excel.

---

## 👥 Who is it for?

| | | |
|---|---|---|
| 🎓 **Graduate students** writing theses | 🔬 **Researchers** at universities & institutes | 🩺 **Health sciences** (clinical, epidemiology, biostatistics) |
| 📊 **Social scientists** (psychology, sociology, education) | 💼 **Data analysts** moving from SAS / SPSS / R | 📈 **Econometricians** in economics, finance, public policy |

---

## ⚖️ Why MerQur?

MerQur is built around five principles for academic data analysis:

### 🎯 Comprehensive in One Tool
- **124 statistical analyses** across 17 categories — from descriptive statistics
  to Bayesian hierarchical models, spatial regression, and structural equation modeling
- **22 advanced methods**: VARCOMP, Crossed/Nested LMM, Time-Dependent Cox, Tobit/Probit,
  Quantile Regression, LASSO/Ridge/ElasticNet, GAM, Robust Regression, PLS, Multiple Imputation
- **6 spatial methods** (KDE, Hexbin, DBSCAN, Moran's I, Getis-Ord Gi*, variogram + kriging) on the Map tab
  with interactive Folium output

### 🌍 Native Multilingual Interface
- **Turkish · English · Spanish** — ~1,300 translated UI strings
- Hot-swap language without restart
- All reports (DOCX/PDF/HTML) generated in the active language

### 📄 Publication-Ready Reports
- **APA 7 compliant** report generator — tables, figures, footnotes
- Export formats: **DOCX · PDF · HTML · Excel**
- Multi-analysis chained reports (one document with all t-tests, ANOVAs, regressions, plots)

### 🗺 Spatial Analysis Built In
- Lat/lon auto-detection from imported data
- **Vector layer overlay** (SHP / KML / KMZ / GPKG / GeoJSON)
- **Geotagged photo import** (EXIF + GPS → DataFrame → Map) for fieldwork
- **Spatial regression** (SAR, Spatial Error, GWR) for ecology, epidemiology, urban studies

### 🤖 AI Interpreter · optional, off by default
- A language model can write the academic commentary (Findings / Interpretation /
  Limitations) in your reports — **Claude, NVIDIA NIM or DeepSeek**, with your own API key
- **Your raw data never leaves the machine.** Only the already-computed statistical
  summary is sent; rows, cell values, file paths and figures are not
- **Every number is verified** against the analysis output. A value that is not in the
  source causes the whole commentary to be rejected in favour of the rule-based text
- Explicit consent dialog on first use; the key is kept in the OS credential vault
- ⚠ The AI commentary is offered **only to suggest ideas**. It is not a substitute for
  scientific assessment or peer review and **must not be accepted without checking**

### 📊 Modern Statistical Methods
- **Bayesian**: BEST t-test, Bayes Factor correlation, Bayesian ANOVA, Hierarchical Bayesian
- **Mixed Models**: LMM, GLMM, Nested LMM, Crossed LMM, VARCOMP (variance components / heritability)
- **Survival**: Kaplan-Meier, Cox PH, Parametric AFT, Competing Risks, Frailty Cox, Time-Dependent Cox
- **Multivariate**: PCA, EFA, CFA→SEM, MANOVA, LDA, CCA, Correspondence Analysis

> **Free for academic use** — T.C. Kültür ve Turizm Bakanlığı 2026/18517 sayılı eser tescili ile
> koruma altında. DOI baseline: `10.53463/merqur.2026001`.

---

## 📥 Download

> Pre-built binaries — no Python installation required.

**Latest release: v1.0.24** — see the
[release notes](https://github.com/omerorucu/merqur/releases/tag/v1.0.24) and the
full changelog in [English](CHANGELOG.en.md) or [Turkish](CHANGELOG.md).

| Platform | Installer | Notes |
|---|---|---|
| 🪟 **Windows 10/11** | [`MerQur-1.0.24-windows-x64-Setup.exe`](https://github.com/omerorucu/merqur/releases/download/v1.0.24/MerQur-1.0.24-windows-x64-Setup.exe) · 349 MB | Code-signed · run the installer |
| 🪟 **Windows portable** | [`MerQur-1.0.24-windows-x64-portable.zip`](https://github.com/omerorucu/merqur/releases/download/v1.0.24/MerQur-1.0.24-windows-x64-portable.zip) · 524 MB | Extract & run `MerQur.exe` |
| 🍎 **macOS** | [`MerQur-1.0.24-macos.dmg`](https://github.com/omerorucu/merqur/releases/download/v1.0.24/MerQur-1.0.24-macos.dmg) · 554 MB | Notarized by Apple · open the DMG and drag MerQur to Applications |
| 🐧 **Linux** | [`MerQur-1.0.24-linux-x86_64.AppImage`](https://github.com/omerorucu/merqur/releases/download/v1.0.24/MerQur-1.0.24-linux-x86_64.AppImage) · 923 MB | `chmod +x` & run |

The newest release is always at [releases/latest](https://github.com/omerorucu/merqur/releases/latest).

**Sample data packs** — 15 discipline packs, each with 130+ ready-to-use datasets matching the MerQur analyses
(Medicine, Anaesthesiology, Dentistry, Infectious Diseases, Education, Psychology & Sociology, Social Sciences,
Economics & Business, Engineering, Natural Sciences & Mathematics, Landscape Architecture, Limnology,
Forest Genetics, Agriculture/Forestry/Aquatic, Sport Sciences). Download them from the
[MerQur download page](https://merqur.sdu.edu.tr/en/download/).

> 💡 Auto-update built in — Help → Check for Updates pulls only changed files.

---

## 🚀 Quick Start

1. **Open data** (Ctrl+O) — Excel / CSV / SPSS `.sav` / Stata `.dta` / SAS `.sas7bdat` / R `.rds` / JSON / Parquet
2. **Data tab** — columns are auto-classified:
   - 🔵 Numeric · 🟠 Categorical · 🟢 Geo (lat/lon) · 🟣 Date · 🔴 Binary · ⚪ Text
   - Multi-choice columns (comma/semicolon-separated) auto-highlighted in purple
3. **Statistics tab** — pick analysis from the sidebar (124 options across 17 categories)
4. **Run** ▶ — results appear as a **card** with Results / Chart / Table / Frequency tabs
5. **Report tab** — select cards → export to **DOCX / PDF / HTML / Excel** with cover page

Every analysis ships with three auto-generated paragraphs in your locale:
**Purpose** · **Assumptions** · **Interpretation**, plus an **APA 7 summary** line:

```
── APA 7 SUMMARY ──
t(118) = 2.45, p = .016, d = 0.45 (small)
```

(Symbols `t · p · d · F · r · M · SD · η² · χ² · …` are auto-italicised in DOCX exports.)

---

## 🧮 Analysis Catalogue

<details>
<summary><b>📊 Descriptive Statistics</b> — 5 analyses</summary>

- Descriptive statistics (M, SD, IQR, skewness, kurtosis)
- Normality tests (Shapiro-Wilk, Kolmogorov-Smirnov, Anderson-Darling)
- Frequency analysis
- Outlier detection (IQR, Z-score, modified Z-score)
- Bland-Altman agreement analysis

</details>

<details>
<summary><b>📈 Parametric Tests</b> — 11 analyses</summary>

- One-sample / Independent / Paired t-tests
- One-way / Two-way / Repeated-measures ANOVA
- ANCOVA · MANOVA
- Bootstrap CI · Permutation Test
- Multiple Comparison Correction

</details>

<details>
<summary><b>📉 Non-Parametric Tests</b> — 7 analyses</summary>

- Mann-Whitney U
- Wilcoxon Signed-Rank
- Kruskal-Wallis · Friedman
- Binomial · Sign · Runs Test

</details>

<details>
<summary><b>📋 Categorical Data</b> — 7 analyses</summary>

- Chi-square independence & goodness-of-fit
- Crosstab
- Multi-Response (MR Frequency, MR×Categorical, MR×MR)
- Cochran's Q
- Conditional Logit (choice model)

</details>

<details>
<summary><b>🔗 Association & Regression</b> — 17 analyses</summary>

- Pearson · Spearman · Kendall correlations
- Bland-Altman · Effect Size · Canonical Correlation (CCA)
- Multiple linear regression with interactions & polynomials
- Logistic regression
- Ridge · LASSO · ElasticNet (regularised)
- Robust regression (Huber, Tukey biweight)
- Quantile regression
- Mediation · Path analysis
- LMM · GLMM · GEE (mixed models)
- Multiple imputation

</details>

<details>
<summary><b>⏱ Survival Analysis</b> — 5 analyses</summary>

- Kaplan-Meier survival curves
- Cox regression (proportional hazards)
- Parametric survival (AFT — Weibull, Log-Normal, Log-Logistic)
- Competing Risks (Cause-specific Cox + CIF)
- Time-dependent Cox

</details>

<details>
<summary><b>🎯 Classification</b> — 3 analyses</summary>

- ROC curve (with optimal threshold via Youden's J)
- TSS (True Skill Statistic)
- Confusion matrix metrics (10 metrics including MCC, Cohen's κ)

</details>

<details>
<summary><b>🧬 Clustering & Dimensionality</b> — 5 analyses</summary>

- K-Means · Hierarchical · DBSCAN
- PCA · t-SNE

</details>

<details>
<summary><b>📝 Survey & Reliability</b> — 8 analyses</summary>

- Cronbach's α (with item-deletion analysis)
- Likert scale analysis (5/7-point auto-detect)
- Exploratory Factor Analysis (EFA — KMO, Bartlett, Varimax)
- Confirmatory Factor Analysis (CFA — CFI, TLI, RMSEA)
- ICC (6 variants)
- Survey Means / Freq / Total (Taylor linearisation)

</details>

<details>
<summary><b>🧪 Modern Statistics</b> — 4 analyses</summary>

- GAM (Generalized Additive Models with splines)
- Discriminant Analysis (LDA / QDA)
- SEM (Structural Equation Modelling)

</details>

<details>
<summary><b>🗺 Spatial Analysis</b> — 5 analyses</summary>

- **KDE** density map (heatmap)
- **Hexbin** density (scalable to 50K+ points)
- **DBSCAN-Spatial** clustering
- **Getis-Ord G\*** hotspot analysis
- **Moran's I** spatial autocorrelation (global + local)

</details>

<details>
<summary><b>📅 Time Series</b> — 2 analyses</summary>

- Stationarity tests (ADF, KPSS)
- Trend & seasonal decomposition

</details>

<details>
<summary><b>🆕 Added in v1.0.20 - v1.0.24</b> — 15 analyses + kriging</summary>

- Mixed-design (split-plot) ANOVA · Meta-analysis (fixed/random effects, meta-regression, publication bias)
- Full SEM (measurement invariance, FIML) · Item Response Theory (Rasch, 2PL/3PL, GRM, PCM)
- Latent Class Analysis (LCA) · Latent Profile Analysis (LPA)
- Econometrics: panel data regression · instrumental variables (2SLS) · propensity score analysis · difference-in-differences
- Time series: VAR · cointegration (Johansen / Engle-Granger) · GARCH
- Machine learning: decision tree (CART) · neural network (MLP)
- Map tab: empirical variogram, model fitting and kriging
- Results validated against R; SPSS and SAS comparisons for the classic analyses

</details>

---

## 🌍 Multilingual

| Locale | Code | Coverage |
|---|---|---|
| 🇹🇷 Türkçe | `tr` | 100% |
| 🇬🇧 English | `en` | 100% (baseline) |
| 🇪🇸 Español | `es` | 100% |

**Add your own language** — drop a ZIP language pack via *Settings → Install Pack*.
Contact the author for the translator guide.

---

## 📖 Documentation

- 📘 **In-app User Guide** — press **F1** inside MerQur for the full feature
  reference (available in TR / EN / ES)
- 📄 **Promotional Presentation** — 57-page deck with worked examples for every
  analysis (uploaded as a Release asset)

Developer and translator documentation lives with the source code;
contact the author for access.

---

## 🏗 MerQur Stands on Giants

> *Built upon a vast open-source ecosystem.*

### Python Ecosystem · Foundations of scientific computing
**NumPy** · **Pandas** · **SciPy** · **Statsmodels** · **Scikit-learn**
**Lifelines** · **pygam** · **svy** · **semopy**
**PyQt6** · **Matplotlib** · **Folium** · **Plotly**
**pyreadstat** · **openpyxl** · **python-docx** · **reportlab** · **Babel**

### Artificial Intelligence · Architectural and coding partner
**Anthropic Claude** — served as a continuous development partner throughout
MerQur's architecture, code authoring, and testing. Collaborated on the design
and implementation of 70+ analyses.

> ***«If I have seen further, it is by standing on the shoulders of giants.»***
> — *Isaac Newton*

---

## 📜 License

MerQur is **free for academic and personal use**. Source code is held privately
by the author. Binaries are distributed through GitHub Releases.

For **commercial licensing**, source access, or institutional deployment,
please contact the author directly.

---

## 💌 Dedication

<div align="center">

*Dedicated to*

### Nevin & Tuncer Örücü

✦

*The two principal components I have lost.*
*The model is meaningless without them.*

— Ömer K. Örücü

</div>

---

## 👤 Author & Contact

**Ömer K. Örücü**
📧 merqur@sdu.edu.tr
🏛️ Süleyman Demirel University

For bug reports, feature requests, or translation contributions:
[open an issue](https://github.com/omerorucu/merqur/issues) or email the author.

---

<div align="center">

**MerQur v1.0.24** · 124 Analyses · 17 Categories · Spatial Modeling · APA 7 Reports

*With MerQur, your academic research stays one step ahead.*

© 2026 Ömer K. Örücü

</div>
