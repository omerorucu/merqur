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

![Version](https://img.shields.io/badge/version-2.2.0-7C3AED?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=flat-square)
![Languages](https://img.shields.io/badge/i18n-TR%20%7C%20EN%20%7C%20ES-success?style=flat-square)
![Analyses](https://img.shields.io/badge/analyses-132%20%2B%207%20map-7C3AED?style=flat-square)
![APA 7](https://img.shields.io/badge/reports-APA%207-27AE60?style=flat-square)
![Validated](https://img.shields.io/badge/validated-R%20%7C%20SPSS%20%7C%20SAS-0F766E?style=flat-square)



</div>

---

## 🔍 What is MerQur?

**MerQur** is an **integrated, end-to-end statistics platform** designed for academic
data analysis. From data ingestion to APA-7 publication-ready reports —
everything in a single tool.

Every analysis has been **validated option by option against R, SPSS and SAS** on independent,
publicly available datasets: **140 analysis forms, 686 datasets and 7,180 cases**, with every number in
the output compared (2.36 million statistics) and **no MerQur error remaining in the comparisons** (see [Validation](#-validated-against-r-spss-and-sas)).

<div align="center">

| **131** | **17** | **7** | **APA 7** |
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

## ✔ Validated Against R, SPSS and SAS

MerQur 2.2.0 is a **validated release**. Every analysis was recomputed on **independent, publicly
available datasets** downloaded from the internet, and its output was compared **option by option**
with **R 4.5.3**, **IBM SPSS Statistics 27** and **SAS 9.4 (SAS/STAT 15.4, SAS/ETS 15.4)**, and with
published values from textbooks, software documentation and NIST reference datasets where they exist.

<div align="center">

| **140** | **686** | **7,180** | **7,340** |
|:---:|:---:|:---:|:---:|
| Analysis forms<br>(incl. Map tab and tools) | Independent datasets<br>(1,894 data files) | Validation cases<br>(analysis × dataset × options) | Parameter options<br>tested |

</div>

Within these cases, **every number in the output** was checked, not only the headline result: each
coefficient, standard error, test statistic, p value, interval limit, fit index, pairwise comparison,
cluster label and forecast, against each reference that provides it. This gives **2,359,810 individual
statistic comparisons**. They measure the *breadth* of the check; they are not 2.36 million independent
tests (numbers from the same model depend on each other, e.g. a correct standard error largely implies a
correct confidence interval). Every comparison was classified:

| Class | Comparisons | Share* | Meaning |
|---|--:|--:|---|
| **Agree** | 2,072,921 | 94.2% | Same value within the numerical tolerance of the statistic |
| **Definitional difference** | 68,901 | 3.1% | The programs use a different, documented definition (e.g. SPSS vs. R default for a df, a quantile type, a variance divisor); MerQur offers the alternative as an option where it is in use |
| **Random variation** | 37,892 | 1.7% | Bootstrap, permutation, cross-validation or MCMC results that differ only by Monte Carlo error |
| **Reference limitation** | 16,641 | 0.8% | The reference program rounds, truncates or cannot compute the value |
| **Unexplained** | 4,817 | 0.2% | A small residual difference whose cause could not be pinned down; documented per analysis |
| **Published-value discrepancy** | 339 | 0.02% | The published reference value itself differs from all programs |
| **MerQur error** | **0** | **0%** | All errors found during validation were fixed before release |

\* Share of the 2,201,511 comparisons that have a counterpart in the reference (158,299 statistics
have no equivalent in that program and are not counted).

| Reference | Comparisons | Agree* |
|---|--:|--:|
| R 4.5.3 | 1,134,135 | 93.9% |
| SPSS 27 | 569,712 | 94.3% |
| SAS 9.4 | 584,804 | 94.3% |
| Published values | 71,159 | 96.7% |

**What you can check yourself.** The validation datasets are attached to every release
([`MerQur-2.2.0-validation-datasets.zip`](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-validation-datasets.zip)):
one folder per analysis, the data files used, and an index (`DIZIN.csv`) with the **source URL and
SHA-256** of every file, so each comparison can be reproduced from the original source.

---

## 🧭 MerQur in Detail

### 1 · Data in, ready to analyse
- **Open almost anything**: Excel (`.xlsx/.xls`), CSV/TSV, SPSS `.sav`, Stata `.dta`, SAS `.sas7bdat`,
  R `.rds`, JSON and Parquet (Ctrl+O).
- **Automatic column typing** with colour codes: 🔵 numeric · 🟠 categorical · 🟢 geographic (lat/lon) ·
  🟣 date · 🔴 binary · ⚪ text. You can override any type.
- **Multiple-response columns** (comma or semicolon separated answers) are detected and highlighted;
  binary indicator sets can be grouped into multiple-response sets.
- **Data tab**: an editable table with undo/redo and column add/delete, **wide-to-long reshaping** for
  repeated measures, **Encoding** (dummy and ordinal coding with value mapping), **Merge** (key-based
  joins with key validation) and a **data profile** that suggests suitable analyses.
- **Missing data**: multiple imputation (chained equations, monotone imputation) with MNAR
  sensitivity analysis.
- Fully empty rows inside a file are kept as observations (as R does); only trailing empty rows are dropped.

### 2 · 132 analyses with professional options
- **17 categories** in the Statistics tab: descriptive statistics, normality, parametric and
  non-parametric tests, categorical data, multiple response, association and multivariate, meta-analysis,
  regression, econometrics and causal inference, classification, clustering and dimension reduction,
  scales and surveys, complex samples, advanced models, survival and time series.
- **SPSS/SAS-level options**: post-hoc families (Tukey, REGWQ, Games-Howell, Dunnett, Scheffé …),
  planned and custom contrasts (L matrix), Type I/II/III sums of squares, estimated marginal means,
  robust and cluster-robust standard errors, exact and Monte Carlo p values, effect sizes with
  confidence intervals, assumption tests, and alternative definitions where programs differ.
- **Mixed and multilevel models**: LMM, GLMM, GEE, nested and crossed designs, variance components,
  reference-level choice, interactions and group × time marginal means.
- **Survival**: Kaplan-Meier, Cox (incl. time-dependent and frailty/cluster-robust), parametric AFT,
  competing risks, interval censoring, survey-weighted Cox.
- **Complex samples**: strata, clusters, weights and finite-population corrections with Taylor
  linearisation or replicate weights (jackknife, BRR, Fay, bootstrap).
- **Modern methods**: Bayesian t test, correlation, ANOVA and hierarchical models; SEM, CFA, PLS-SEM,
  IRT, LCA/LPA; GAM, LOESS, response surface regression; regularised regression; CART, random forest,
  gradient boosting, SVM, KNN, MLP; VAR, cointegration, GARCH, ARIMA, ETS, unobserved components.

### 3 · Map tab: spatial analysis built in
- Latitude/longitude columns are detected automatically and drawn on an interactive map.
- **7 spatial methods**: KDE density, hexbin, spatial DBSCAN, Moran's I (global and LISA),
  Getis-Ord Gi\* hot spots, empirical variogram with kriging, and point pattern analysis
  (Ripley's K/L, G/F/J, Clark-Evans, CSR envelopes).
- **Vector layers** (SHP, KML, KMZ, GPKG, GeoJSON) as overlays, and **geotagged photos** (EXIF + GPS)
  imported straight into a data table for fieldwork.
- Spatial regression (SAR, spatial error, GWR) in the Statistics tab.

### 4 · Results you can read
- Every run produces a **result card** with *Results · Chart · Table · Frequency* tabs; cards stay in
  the session history and can be sent to the report.
- Each analysis writes three plain-language paragraphs in the interface language — **Purpose**,
  **Assumptions**, **Interpretation** — and an **APA 7 summary line**.
- Undefined values are shown as "—" and very small p values as "p < .001".
- Charts can be adjusted (axis limits, colours, zoom) and refined further in the **Chart Studio**.
- **Tools tab**: Chart Studio, **power analysis** and **sample size** calculators.

### 5 · Publication-ready reports
- **APA 7 report generator**: select cards and export one document with a cover page, numbered tables
  and figures, and italicised statistical symbols.
- Formats: **DOCX · PDF · HTML · Excel**, and **LaTeX** tables.
- Reports are written in the active language (Turkish, English or Spanish).

### 6 · Reproducible analysis scripts
- Every analysis you run is recorded with its full form settings. Save the session as an analysis
  script (`.mqs`) and **replay it later on the same or updated data**, including from the command line,
  to regenerate all results, tables and charts.

### 7 · Optional AI interpreter (off by default)
- A language model (Claude, NVIDIA NIM or DeepSeek, with your own API key) can draft the academic
  commentary in reports. **Raw data never leaves your computer**: only the computed statistical summary
  is sent. **Every number is checked** against the analysis output; if a value is not in the source, the
  commentary is rejected and the rule-based text is used. The AI text is a suggestion and must be checked.

### 8 · Multilingual, signed and self-updating
- **Turkish · English · Spanish** interface, switchable without restarting; language packs can be added.
- Code-signed Windows installer, Apple-notarized macOS build, Linux AppImage.
- **Help → Check for Updates** downloads only the files that changed.

### 9 · Learn with real examples
- **15 discipline sample packs** with field-specific datasets for every analysis, each with a scenario,
  variable selection, MerQur output and interpretation (Turkish and English).
- Press **F1** for the full in-app user guide (Turkish, English, Spanish).

> **Free for academic use** — registered work, T.C. Kültür ve Turizm Bakanlığı no. 2026/18517.
> DOI: `10.53463/merqur.2026001`.

---

## 📥 Download

> Pre-built binaries — no Python installation required.

**Latest release: v2.2.0** — see the
[release notes](https://github.com/omerorucu/merqur/releases/tag/v2.2.0) and the
full changelog in [English](CHANGELOG.en.md) or [Turkish](CHANGELOG.md).

| Platform | Installer | Notes |
|---|---|---|
| 🪟 **Windows 10/11** | [`MerQur-2.2.0-windows-x64-Setup.exe`](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-windows-x64-Setup.exe) · 352 MB | Code-signed · run the installer |
| 🪟 **Windows portable** | [`MerQur-2.2.0-windows-x64-portable.zip`](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-windows-x64-portable.zip) · 526 MB | Extract & run `MerQur.exe` |
| 🍎 **macOS (Apple Silicon)** | [`MerQur-2.2.0-macos.dmg`](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-macos.dmg) · 569 MB | Notarized by Apple · open the DMG and drag MerQur to Applications |
| 🍎 **macOS (Intel)** | [`MerQur-2.2.0-macos-intel.dmg`](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-macos-intel.dmg) · 614 MB | Notarized by Apple · for Intel Macs; the row above is for Apple Silicon |
| 🐧 **Linux** | [`MerQur-2.2.0-linux-x86_64.AppImage`](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-linux-x86_64.AppImage) · 933 MB | `chmod +x` & run |

**Linux notes** — the AppImage is built on Ubuntu 22.04 and runs on 64-bit distributions with glibc 2.35
or later (Ubuntu 22.04+, Debian 12+, Linux Mint 21+, Fedora 36+). If it does not start:
`AppImages require FUSE to run` → `sudo apt install libfuse2` (Ubuntu 24.04+: `libfuse2t64`; Fedora:
`sudo dnf install fuse-libs`), or run with `--appimage-extract-and-run`;
`could not load the Qt platform plugin xcb` → `sudo apt install libxcb-cursor0 libxkbcommon-x11-0 libegl1 libgl1`.


**Validation datasets** — [`MerQur-2.2.0-validation-datasets.zip`](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-validation-datasets.zip) · 40 MB:
the independent datasets used to validate every analysis against R, SPSS and SAS, organised by
analysis name, with the source URL and SHA-256 of every file.

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
3. **Statistics tab** — pick analysis from the sidebar (132 options across 17 categories)
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
<summary><b>🆕 Added in v2.2</b> — 1 new analysis + empty data sheet</summary>

- **Multi-location RCBD (combined analysis of variance)** for variety and value-for-cultivation trials:
  per-location tables (F, CV, LSD, letter groups) and combined ANOVA with location fixed or random,
  ten mean-separation methods, Dunnett and free contrasts, Type I-IV sums of squares, LS-means,
  mixed models (REML, ML, TYPE3, MIVQUE0; Kenward-Roger, Satterthwaite), location-specific error
  variances, missing plot (Yates), covariates, and G × E / stability analyses (AMMI, GGE biplot,
  Eberhart-Russell, Finlay-Wilkinson and eleven stability statistics) with 22 chart types —
  validated against SAS 9.4 and R
- **Empty data sheet on start-up** (var1, var2, …) that grows as you type or paste from Excel;
  decimal commas are converted, column types are inferred and can be changed from the header menu
- Results tab text added to Word, PDF, HTML, LaTeX and Excel reports
- **Robustness round**: all 132 analyses run with every option on broken, missing and extreme data
  (~9,000 runs); degenerate data now give an explanatory error or "—", as in R and SAS
- The in-app updater falls back to GitHub when merqur.sdu.edu.tr is unreachable

</details>

<details>
<summary><b>🆕 Added in v2.1</b> — 8 new analyses</summary>

- **PLS-SEM** (partial least squares path modeling: reliability, validity, HTMT, bootstrapped indirect effects)
- **LOESS** local regression · **response surface regression** (canonical and ridge analysis)
- **k-nearest neighbours (KNN)** · **age standardisation and SMR**
- **Unobserved components model** (structural time series)
- **Heckman sample selection** and truncated regression
- Map tab: **point pattern analysis** (Ripley's K/L, G/F/J, Clark-Evans, CSR envelopes)
- New options in existing analyses: custom contrasts (L matrix), GLMM/GEE interactions and group × time
  EMMs, replicate-weight survey variance (jackknife, BRR, Fay, bootstrap), panel unit-root tests, SUR/3SLS,
  REGWQ, lack-of-fit, Breusch-Pagan/White and Chow tests, spectral windows, CLS/ULS ARIMA and VARX,
  wide-to-long reshaping and LaTeX table export

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
- 📑 **Technical Note: Analyses** — every analysis with its options, worked
  examples and interpretation: [Turkish](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-Teknik-Not-TR.pdf) ·
  [English](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-Technical-Note-EN.pdf) (Release assets)
- 📊 **Technical Note: Charts** — all 353 charts of the Chart Studio, analysis
  panels, 3D options, Map and power analysis with data, settings and reading tips:
  [Turkish](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-Grafik-Teknik-Notu-TR.pdf) ·
  [English](https://github.com/omerorucu/merqur/releases/download/v2.2.0/MerQur-2.2.0-Chart-Technical-Note-EN.pdf) (Release assets)

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
and implementation of 130+ analyses.

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

**MerQur v2.2.0** · 132 Analyses · 7 Map Methods · 17 Categories · Spatial Modeling · APA 7 Reports

*With MerQur, your academic research stays one step ahead.*

© 2026 Ömer K. Örücü

</div>
