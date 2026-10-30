# MerQur — Release Notes

**MerQur — Integrated Academic Data Analysis & Reporting Platform**

> Turkish original: [CHANGELOG.md](CHANGELOG.md)

---

## [2.3.1] — 30 October 2026 · **Maintenance Release**

- Custom contrasts (L matrix): contrast expressions accept parentheses, division, multiplication by numbers, unary minus and nested parentheses; for example `(A + B)/2 - C` now gives the same row as `0.5*A + 0.5*B - C`. Results of contrasts written in the earlier form are unchanged. Unbalanced parentheses, a product of two coefficients and division by zero or by a coefficient are reported with a translated error message.
- Closing the program: the occasional Windows error dialog (access violation) when closing after a long session, especially after using the Map tab, has been fixed. The main window is now closed in an orderly way before the exit clean-up. Analysis results and saved files were not affected.
- Likert analysis: with automatic scale range, a very large outlier now gives a clear error message instead of making the program hang.
- MGWR: the covariate-specific bandwidth search uses the global method of GWR (coarse full grid + refinement around the best points) instead of a golden-section search, both for the initial bandwidth and at every backfitting step. The golden-section search could miss small-scale bandwidths and stop at a local solution; MGWR bandwidths, AICc and all dependent MGWR results may change (the new solution has a lower AICc). For n > 2000 observations the previous method is used for speed and a note says so.
- GWR local R²: the default definition (map, distribution) is unchanged and is now stated in a result note. The local results table has a second definition, the column "Local R² (local fit)" (fit of the weighted local regression at each point).
- GWR local condition number (CN): now computed for models with a single explanatory variable (it was silently empty); the definition is the same as with several explanatory variables and is stated in a note in the result text. With a single explanatory variable the local VIF is undefined.
- GWR Monte Carlo test of local coefficient variability: the p value is now (b + 1)/(N + 1) (Phipson & Smyth 2010; b: number of permutations exceeding the observed standard deviation, N: number of permutations). The previous b/N definition gave p = 0 when no permutation exceeded; the smallest p is now 1/(N + 1). All Monte Carlo p values change slightly; the definition is stated in a result note.
- GWR local results table: a second local condition number column, "Local CN (W½X)", the condition number of W^½X with columns scaled to unit length. The default CN (W·X definition) and all other results are unchanged; both definitions are stated in result notes. MGWR has no such column.
- Hierarchical Bayesian regression: if the selected group variable or nested subgroup forms more levels than half the number of observations (fewer than two observations per level on average) or contains non-integer numeric values, a translated warning is shown before the computation with "Run anyway" and "Cancel" options; the same warning is written to the result notes. Previously such a choice (e.g. age as a subgroup) could run for minutes without any warning. Numerical results are unchanged.
- Running scripts from the command line (`--run`) or starting the program without a console: the program could close without a message on some Qt notices; fixed.
- macOS: the macOS packages of 2.3.0 (Intel and Apple Silicon) closed immediately after start on macOS 12–13; the numerical libraries are now packaged in a form compatible with older macOS versions, and a minimum-version check has been added to the build.

- Mixed models (LMM, GLMM, GEE, nested and crossed LMM): two new options for estimated marginal means. A "Level order" field (e.g. `time: Week1, Month1, Month3`) sets the order of levels in EMM tables, simple-effect comparisons, pairwise lists and the EMM line plot (levels were previously sorted alphabetically, e.g. Month1, Month3, Week1); estimates and reference levels are unchanged. In LMM, GLMM and GEE an "Adjustment scope" option corrects the simple comparisons either within each level of the second EMM factor (default, previous behaviour) or across all comparisons as one family (e.g. with 2 groups × 3 times, Bonferroni p = min(1, 3·p)); Tukey is not defined for one family, so Šidák is applied and noted. Holm (step-down Bonferroni) was added to the p-value adjustment list of EMM pairwise comparisons. Raw p values, differences and confidence intervals are unchanged; the default remains Bonferroni.
- Language: on first start the program opens in the language of the operating system (Turkish → Turkish, Spanish → Spanish, all other languages → English); previously it always opened in English. A language chosen in Settings is kept. The Windows setup wizard no longer asks for a language and follows the same rule; the licence agreement page is shown in the wizard's language (English text for Spanish).
---

## [2.3.0] — 29 October 2026 · **Moderation and Mediation**

> "Societies that wish to live in comfort without working, without tiring and without producing are doomed to lose first their dignity, then their freedom, and then their independence and their future."
> — Mustafa Kemal Atatürk

> "Las sociedades que quieren vivir cómodamente sin trabajar, sin cansarse y sin producir están condenadas a perder primero su dignidad, luego su libertad y después su independencia y su futuro."
> — Mustafa Kemal Atatürk

> Published under the same DOI registration as v1.0.0 (2026/18517).

MerQur 2.3.0 gathers moderation and mediation analyses in a new "Moderation & Mediation" category and adds five new analyses. Mediation and Path Analysis were moved to this category. Numerical results of earlier analyses on valid data are unchanged; the places where output changes are listed separately below.

Conditional Process Engine: the moderation and mediation analyses run on a common engine that estimates templates 1–92 of Hayes's conditional process models. It provides conditional direct and indirect effects, simple slopes, Johnson-Neyman regions, the index of moderated mediation and contrasts of indirect effects; percentile and BCa bootstrap and Monte Carlo confidence intervals; covariates, multicategorical X and W, a logistic model for a binary outcome and correction for measurement error.

New analyses:
- Moderation Analysis (Models 1–3): simple-slope tables, the Johnson-Neyman region and interaction plots.
- Multilevel Mediation: 1-1-1, 2-1-1 and 2-2-1 designs; random slopes, within-cluster/cluster-mean centering, Kenward-Roger and Satterthwaite degrees of freedom, Monte Carlo confidence intervals.
- Causal Mediation Analysis: average causal mediation effect (ACME) and direct effect (ADE), the VanderWeele decomposition, X × M interaction and sensitivity analysis.
- Multilevel SEM Mediation (MSEM): random-intercept model with latent cluster means and maximum likelihood; 1-1-1, 2-1-1 and 2-2-1 designs; within- and between-level indirect effects.
- Bayesian Mediation Analysis: Models 4, 6, 7 and 14; continuous and binary outcome; equal-tailed and highest-density (HDI) credible intervals from the posterior, and the index of moderated mediation.

Mediation and Path Analysis: the Mediation and Conditional Process Analysis panel now runs on the Conditional Process Engine. Path Analysis gains specific indirect, total indirect and total effects (delta-method and bootstrap confidence intervals); direct, indirect and total effects are now reported in a single section using the selected estimation method.

Validation: the new analyses were validated against R, SAS and SPSS and against published data downloaded from the internet (including the data of Hayes's 2022 book). The technical note and the validation data package are among the files of this release.

Interface: long-running analyses (resampling, machine learning, time series, SEM) run with a progress window and can be stopped with Cancel. The "NEW" badges were removed from the menu. In the Turkish interface, analysis names, result-table headings and messages were translated and terminology was unified; program and package names were removed from interface texts. The About window shows an APA 7 citation (the version number is taken from the running version).

Changes in results:
- Mediation: the "full / partial mediation" classification was removed. The decision line now reads "indirect effect significant / not significant" and is accompanied by an explanatory note.
- In mediation and conditional process models, the logistic model for a binary outcome is estimated with R's convergence criterion (successive deviance change, 1e-8); the iteration limit is effective and a note is given if the model does not converge.
- Path Analysis: with MLM estimation, exogenous variables are treated as fixed (fixed.x); standard errors of path coefficients, the scaled χ² and standard errors of indirect effects match R lavaan MLM and may differ slightly from the previous version. Bootstrap confidence limits use percentile interpolation.
- Survey frequencies: the "Wald (symmetric)" proportion confidence interval is also applied at the 95% level (previously the logit interval remained at this level).
- VAR: the APA summary states whether residual autocorrelation is present according to the portmanteau test (previously it always stated "no autocorrelation"); the portmanteau test is skipped when the diagnostic lag reaches the number of observations.

---

## [2.2.0] — 26 October 2026 · **Multi-Location RCBD and Robustness Round**

> Published under the same DOI registration as v1.0.0 (2026/18517).

MerQur 2.2.0 adds one new analysis and the fixes from a robustness round in which every analysis was systematically tested with broken, missing and extreme data. Numerical results on valid data are unchanged; the places where output changes are listed separately below.

New analysis: Multi-Location Randomized Complete Block Design (Combined Analysis of Variance). It produces the standard table used in variety and value-for-cultivation trials (F, CV, LSD and letter groups per location; combined means) and the combined analysis of variance (location fixed or random). It includes all options found in SAS and R: ten mean-separation methods, Dunnett, candidate-versus-standard and free contrasts, slice analysis, effect sizes, rank-based tests, homogeneity-of-variance and normality diagnostics, Type I-IV sums of squares, LS-means, mixed models (REML, ML, TYPE3, MIVQUE0; Kenward-Roger and Satterthwaite), location-specific error variances, transformations, missing plot (Yates), covariates, and genotype-by-environment and stability analyses (AMMI, GGE biplot, Eberhart-Russell, Finlay-Wilkinson and eleven parametric and rank-based statistics), with twenty-two chart types. Results were validated against SAS 9.4 and R; the technical note and the SAS comparison are included among the files of this release.

Data sheet: the program opens with an empty data-entry sheet (columns var1, var2…, rows 1, 2, 3…); data can be typed or pasted from Excel and similar programs. The sheet grows automatically near its edges and when pasted data do not fit; if the first pasted row is text, using it as column names is offered. Decimal commas (3,5) are converted to numbers; columns containing only numbers become numeric, others categorical, and the type can be changed from the column header menu. Empty columns and trailing empty rows are not included in analyses or saved files. Pasting beyond the table edge is no longer rejected for loaded files either.

Report: the text of each card's Results tab is added to Word, PDF, HTML, LaTeX and Excel reports (on by default).

Robustness round: each of the 132 analyses was run with every option on data variants containing small samples, missing values, empty cells, constant columns, single-level factors, unbalanced designs, outliers and duplicated rows (about 9,000 runs), and checks confirmed that p values lie in [0, 1], confidence limits are ordered, information criteria are not below −2LL, and the Turkish and English interfaces give identical numbers. Crashes and untranslated library messages found were turned into translated, explanatory warnings or errors; undefined values are shown as "—" with a footnote instead of "nan" or "inf"; remaining English labels in the Turkish interface were translated. This round will be repeated before every release.

Changes in results:
- Meaningless results are no longer printed for degenerate data. With a constant dependent variable, t-tests, ANOVA, ANCOVA, mixed models, MANOVA, the permutation test, ICC, quantile regression, Tobit and the multi-location RCBD give an explanatory error or "—", as R and SAS do (earlier versions could, in some cases, print meaningless F or t values arising from floating-point noise). In crosstabs with a single-level row or column variable no chi-square statistic is computed (as in SAS PROC FREQ); the frequency table is shown. Variance components give an explanatory error for an unidentifiable component.
- Survey analyses behave like the R `survey` package: finite population correction (FPC) values below 1 are interpreted as sampling fractions; with negative weights, means, totals and frequencies are computed while regression models stop, as in R; a constant predictor in survey regression is dropped and shown as "not estimable".
- In mixed models a constant numeric covariate is dropped with a warning, as in lme4; in MANOVA a constant dependent variable is dropped, as in SAS.
- In the multi-location RCBD with the mixed model and random variety, BIC is corrected (same as SAS) and no pairwise difference table is given (a random factor has no LS-means).
- In the two-group permutation test and the classical t line, the difference is taken from the first group in the data to the second, as since 2.1.2; one-sided p values follow this direction.
- In survey Cox regression (Survey-PHREG), when the design degrees of freedom are zero or negative (no more PSUs than strata), coefficient p values and confidence limits and the global Wald test are shown as "—" with an explanatory note, as in R (previously one degree of freedom was used); a crash with a single-PSU cluster was fixed. In geographically weighted regression an infinite local condition number is shown as "—" with a note.
- In normality and descriptive statistics the standard error of skewness is shown for n = 3 (same as SPSS).

Updater: when merqur.sdu.edu.tr cannot be reached, the in-app updater reads version information from the GitHub release page. In versions before 2.2.0, while the site is unreachable, the new version can be downloaded manually from the GitHub release page.

---

## [2.1.2] — 23 October 2026 · **3D Charts and Chart Fixes**

> Published under the same DOI registration as v1.0.0 (2026/18517).

MerQur 2.1.2 adds no new analyses; it extends the chart layer and fixes the problems found by reviewing every chart one by one. Computational methods are unchanged; the places where output changes are listed separately below.

3D charts: Chart Studio gains 3D scatter (with floor projection), 3D surface (triangulated, grid interpolation and quadratic fit), contour, bivariate density surface and 3D histogram; 3D charts can be exported as a rotation animation (GIF; MP4 when ffmpeg is installed) and as interactive HTML. Analysis panels gain 3D options: a response surface in RSM; 3D scores, loadings and biplots in PCA, factor analysis, MDS and correspondence analysis; a two-predictor 3D surface in linear, logistic, GAM, LOESS, count, quantile, robust, ridge/lasso/regularized, nonlinear, probit, tobit, ordinal and multinomial logistic regression; the S(t|x) surface in Cox and parametric survival; 3D partial dependence and decision surfaces in machine learning; joint posterior surfaces in Bayesian models; 3D views in clustering, discriminant analysis, t-SNE, UMAP, CCA and PLS; kriging/IDW and kernel density surfaces in the Map tab; and a power surface in power analysis.

The Chart Studio catalogue is complete: horizontal bar, lollipop, strip, hexbin, parallel coordinates, correlation matrix, step, stacked area, treemap, sunburst, icicle, circle packing, dendrogram, network, radar, polar, Gantt, waterfall, streamgraph, Sankey and alluvial, ridge, pair and error-bar charts and the calendar heatmap were added or wired to the menu; charts can be saved as PNG, SVG or PDF.

Survey: saved JSON files now reload with question type, options and skip logic intact (loading failed in the previous version); "Open JSON" and "Add from JSON" were added to the toolbar; the Scale Library imports ready-made scale forms (TR/EN) into a survey; the PDF and DOCX participant form prints only the instructions, with citation and licence details kept in a separate "researcher notes" field; questions can be reordered by drag and drop. Data: importing from Excel now offers sheet, header row and column selection (the dialog opens automatically for multi-sheet files).

Changes in results: very small p values are written as "p < 0.0001" everywhere; in Mann-Whitney U the first group is now determined by category order (otherwise by order of appearance in the data), so when the first group in the data is not first in that order the sign of U, r, the Hodges-Lehmann estimate and its confidence interval and the direction of the one-sided p change, while the two-sided p is the same; the sign of the difference in the permutation test follows the same language-independent rule; in random forest, gradient boosting, SVM and MLP classifiers the train/test split and cross-validation folds no longer depend on the language of the class labels (previously the same data could give different accuracy in the Turkish and English interface, so accuracy values on the sample data may change); a folded/two-sided option was added for the Getis-Ord Gi* permutation p (default is the previous behaviour); in multinomial logistic and log-linear analyses the default reference level is no longer the alphabetically first level but follows the categorical order, the natural numeric/interval order or the order of first appearance in the data, so Turkish and English copies of a dataset take the same reference; only the coefficient rows (which level is compared against) change, while log-likelihood, AIC/BIC, deviance, G²/χ², likelihood-ratio tests and predicted probabilities are unchanged; the log-linear panel gains an optional "Reference levels" field and the output states the reference used and how it was chosen.

Chart fixes: the Chart Studio dark theme leaked into the rest of the application, so later analysis charts and PDF/DOCX report figures came out on a dark background, and charts lost their font family after a report export; both are fixed. All Studio and analysis charts were scanned for WCAG contrast, overflow and overlap; titles, axis and legend texts left in English in the Turkish interface (and in Turkish in the English one) are now translated; untitled charts received titles and unnamed axes received names; group order and colours are identical in both languages (ANOVA, Kaplan-Meier, the chi-square family, multiple response); forest plots use plain log-axis ticks, centre the rows when there are few coefficients and add a value column; Bayesian charts use posterior language instead of frequentist terms and the BF axis extends for large values; the two-way ANOVA residual plot came out empty and is fixed; the "Observed" line in ARIMA/ETS is the raw series; mediation diagrams no longer truncate variable names; in SAR/SEM the intercept is reported as a note so it no longer distorts the scale; multi-class targets get one-vs-rest ROC curves; the gradient boosting learning curve is drawn without early stopping too; 3D loading/biplot labels no longer overlap; in the Studio, pie/donut/bar percentages and tick values follow the locale, months are readable on time axes, forest and funnel plots use the inverse-variance weighted pooled estimate, and the calendar heatmap layout and the lollipop, radar, stage funnel, waffle, contour, icicle and circle-packing labels were corrected; in power analysis the HR/OR effect grid covers both sides of 1 (protective effects) and legends were completed; point pattern envelopes stay within 0-1 and the KDE unit is the same on the map and in 3D; the result card title under-counted the independent variables by one, now fixed.

Platform: the Linux AppImage is built on Ubuntu 22.04 and opens on distributions with glibc 2.35 or later (installation and troubleshooting notes are in the README); for macOS, Apple Silicon and Intel DMGs are provided separately.

---

## [2.1.1] — 19 October 2026 · **Maintenance Release**

> Published under the same DOI registration as v1.0.0 (2026/18517).

MerQur 2.1.1 is a maintenance release; no new analyses were added. The computational methods are unchanged; the places where output changes are listed below.

Two changes in results: the Kolmogorov-Smirnov line in the assumption section of the t-tests now uses the Lilliefors correction (the same test as the Normality analysis; because the mean and standard deviation are estimated from the sample, the uncorrected p value accepted normality too easily); in Moran's I, Getis-Ord Gi* and point pattern analysis a fixed seed (12345) is used when the seed is set to "Auto", so permutation p values are identical on every run.

Fixes: very small p values are written as "<0.0001" instead of "0.0000" in the MANOVA Bonferroni line, multiple comparison corrections, multiple imputation, Cox and parametric survival models, and SAR and spatial error models; the description of the Normality analysis now states how tests are chosen by sample size and that normality is examined separately in each group in grouped analyses; in hierarchical clustering and k-means the chart is now updated when only the chart option is changed; in exponential smoothing with automatic selection the header shows the selected model and seasonal type; in variance components, choosing a column that differs on every row as a fixed effect gives an explanatory warning instead of an error; event labels in competing risks follow the interface language; in the Survey tab an edited question now appears in the list, and the "Other" option and rating limits are kept when editing; the "Missing value" choice in Data > Encoding (fill with mode, mark as unknown, drop row) is now applied; the titles of violin, ridge and Q-Q plots and the percentage format in the sample size calculator follow the interface language; the Windows installer now upgrades a previous version without waiting for confirmation in silent mode, and an all-users installation defaults to Program Files; a department name was corrected in an English sample dataset.

---

## [2.1.0] — 17 October 2026 · **Eight New Analyses and SPSS/SAS-Level Options**

> Published under the same DOI registration as v1.0.0 (2026/18517).

MerQur 2.1 adds the analyses and options that a systematic comparison found in SPSS, SAS and R but missing in MerQur. Every new method was validated against R on independent datasets downloaded from the internet, and against the published examples of SAS and Stata where these exist.

Eight new analyses: PLS-SEM (partial least squares path modeling, with reliability, validity, HTMT and bootstrapped indirect effects), LOESS local regression, response surface regression (canonical and ridge analysis), k-nearest neighbors (KNN), age standardization and SMR, the unobserved components model (structural time series), Heckman sample selection and truncated regression, and point pattern analysis in the Map tab (Ripley's K/L, G/F/J, Clark-Evans and CSR envelopes).

Added to existing analyses: reference level selection, interaction terms in GLMM and GEE, group x time estimated marginal means with group comparisons at each time and a plot in mixed models; custom contrasts (L matrix) in LMM, GLMM, GEE, ANOVA, ANCOVA, logistic, count, IV and survey regression; jackknife, BRR, Fay and bootstrap replicate variance and supplied replicate weights in weighted survey analyses; panel unit root tests, SUR and 3SLS; Van der Waerden, Savage and scale tests; REGWQ, lack-of-fit, Breusch-Pagan/White and Chow tests; spectral windows, cross-spectrum, CLS/ULS estimation in ARIMA and VARX; survival (log-rank) power; monotone imputation and MNAR sensitivity analysis; kNN and kernel discriminant analysis; the parallel reliability model; WLS weight estimation and an overdispersion scale; axis, colour and zoom controls on charts; wide-to-long data reshaping and LaTeX table export.

Important: in weighted survey regression and survey logistic regression, Wald F tests, coefficient t tests and confidence intervals now use the same degrees of freedom as the R survey package (design df + 1 - number of coefficients); p values and confidence intervals in these analyses may differ slightly from the previous version. Elsewhere, the defaults of the new options leave earlier results unchanged.

Fixes: fully empty rows inside the data are now kept as observations when a file is loaded (only trailing empty rows are dropped, as in R) - n may change in multiple-response analyses; in survey bootstrap variance a diverging replicate is excluded and a warning is written; fixed an error in count regression when the offset column is also a predictor, an error when switching templates in path analysis, the "factor=level" syntax for numerically coded levels in custom contrasts, and the one-sided quadrat count test in point pattern analysis; robust regression now shows coefficient confidence intervals; undefined values are shown as "—" instead of "nan", and very small p values as "p < .001" instead of "p = 0.0000"; double rounding in Likert item statistics was removed; the GAM analysis is now named "Generalized Additive Model" (it was easily confused with Non-Linear Regression); points on map cluster maps are outlined and drawn on a light basemap for better visibility; dialog buttons and remaining labels follow the interface language.

The validation data for the new analyses have been added to the data package attached to this release.

---

## [2.0.0] — 12 October 2026 · **Validated Against R, SPSS and SAS**

> Published under the same DOI registration as v1.0.0 (2026/18517).

MerQur 2.0 is the validation release: all 133 analyses were recomputed with independent datasets downloaded from the internet and compared, option by option, with R, SPSS and SAS. The errors found were fixed, options that had no effect on the result now work, and the small differences that remain between programs are documented as differences in method definitions.

Important: some analyses may give results that differ from v1.0.26. The main ones are varimax/promax rotation in factor analysis (SPSS/SAS definition), the seasonal period of sub-hourly time series (e.g. 48 for 30-minute data), robust standard errors in GARCH models, the log-likelihood of the frailty model and the concordance index of Cox models, weighted survey analyses, REML estimation in mixed models, and STL decomposition. Ridge and Lasso now build the penalty grid from the data and warn when the selected value lies on the edge of the grid. We recommend re-running analyses made with the previous version before reporting them.

The datasets used in the validation are attached to this release, organised by analysis name, with the source URL and SHA-256 of every file: [MerQur-2.1.0-validation-datasets.zip](https://github.com/omerorucu/merqur/releases/download/v2.1.0/MerQur-2.1.0-validation-datasets.zip)

---

## [1.0.26] — 10 October 2026 · **New Accuracy and Display Fixes**

> Published under the same DOI registration as v1.0.0 (2026/18517).

The analyses in the Psychology-Sociology, Landscape Architecture and Forest Genetics sample packs were compared with R, SPSS and SAS, and the differences found were fixed. Log-linear analysis gains a frequency (count) column option. Fixes cover the ICC interval in the Bayesian hierarchical model, confidence intervals of variance components at the boundary, AIC in spatial models, the Kaplan-Meier median, and the parametric survival model with zero-length durations. Multinomial logistic regression now warns about complete separation. Quantile regression shows the intercept, and Moran's I reports the expected value, variance and z. Small coefficients and confidence intervals are printed with more digits. The event column in some sample datasets was corrected.

---

## [1.0.25] — 10 October 2026 · **Accuracy Fixes**

> Published under the same DOI registration as v1.0.0 (2026/18517).

All 130 analyses in the Medicine sample data pack were checked one by one against R, SPSS and SAS, and the differences found were fixed. Corrections cover the direction of Tukey pairwise comparisons, confidence-interval headings in ANOVA and regression tables, the exact Mann-Whitney p-value with tied data, canonical correlation tests, the Benzécri correction in multiple correspondence analysis, anti-image correlations, Tobit censoring, time ordering in repeated-measures models, the GEE AR(1) correlation, the log-logistic survival model, complex-survey outputs, Holt-Winters forecasts, trend analysis with a year column, propensity-score subclassification and GARCH estimation. Quantile regression now uses the quantiles you enter. The Cox regression sample dataset was replaced with more realistic survival data.

---

## [1.0.24] — 6 October 2026 · **macOS Startup Fix and New Sample Datasets**

> Published under the same DOI registration as v1.0.0 (2026/18517).

Fixed MerQur not opening on macOS after the licence agreement was accepted: settings are now
stored in the user data folder, which also stops settings from being reset after updates on
Windows. The sample data packs gain 15 field-specific datasets for the newer analyses. Some
confidence-interval labels in Turkish reports were corrected.

---

## [1.0.23] — 5 October 2026 · **Compact Interface and Accuracy Fixes**

> Published under the same DOI registration as v1.0.0 (2026/18517).

The interface is more compact: checkboxes, drop-down lists and text are smaller and
unnecessary scroll bars are gone. Overlapping parameters on the Map tab were fixed.
ANCOVA now uses Type III sums of squares by default, matching SPSS/SAS. Accuracy fixes
were made to mixed models, multiple imputation, Mann-Kendall and spatial neighbourhood
calculations; the chosen significance level is now honoured by more analyses.

---

## [1.0.22] — 5 October 2026 · **IRT, Latent Class, Econometrics and Analysis Scripts**

> Published under the same DOI registration as v1.0.0 (2026/18517).

New analyses: item response theory and Rasch, latent class and latent profile analysis,
panel data, instrumental variables, propensity scores and difference-in-differences,
VAR, cointegration and GARCH, decision trees and neural networks. Analyses can be saved
as scripts and re-run. The help document was updated in three languages. The new outputs
were validated against R.

---

## [1.0.21] — 5 October 2026 · **Meta-Analysis, Full SEM and Kriging**

> Published under the same DOI registration as v1.0.0 (2026/18517).

New analyses: meta-analysis, full structural equation modeling (with measurement
invariance and FIML) and variogram + kriging. Power analysis was extended to G*Power
level; error covariance structures were added to mixed models and multi-factor designs
to repeated-measures ANOVA. The new outputs were validated against R. The default method
of several analyses now matches SPSS, R and SAS; results of these analyses may differ
from the previous version, and the former methods remain available as options. The
upgrade installer was hardened.

---

## [1.0.20] — 5 October 2026 · **Professional Analysis Options Update**

> Published under the same DOI registration as v1.0.0 (2026/18517).

Many analysis options, assumption checks and outputs available in SPSS, R and SAS
were added; the new outputs were validated against R. Several calculation errors
were fixed, the regression crash in the English and Spanish interfaces was resolved,
and interface stability was improved.

---

## [1.0.19] — 4 October 2026 · **Statistical Accuracy Update**

> Published under the same copyright registration (2026/18517) as v1.0.0.

Analyses were cross-validated against IBM SPSS Statistics 27 and R 4.5, and the
calculation and reporting differences found were corrected. Maximum-likelihood
estimation (adaptive Gauss-Hermite) was added to generalized linear mixed models (GLMM).

---

## [1.0.18] — 28 September 2026 · **AI Interpreter + Multilingual Hardening**

> Published under the same copyright registration (2026/18517) as v1.0.0.

### ✨ New — AI Interpreter
You can now have a language model write the academic commentary in your report
output (Findings / Interpretation / Limitations). **It is OFF by default**; unless
you turn it on, MerQur runs entirely offline exactly as in previous versions.

- **Your raw data is never sent.** Only the already-computed statistical summary
  goes out (analysis name, n, variable names, values such as t/F/p/R²); the rows
  of your dataset, its cell values, file paths and figures are not sent.
- **Number verification.** Every number the model writes is checked automatically
  against the analysis output. If a value does not exist in the source, the whole
  commentary is rejected and MerQur's rule-based text is used instead. In other
  words the model performs no calculation; it only writes sentences around the
  numbers it is given.
- **Explicit consent.** On first use a dialog shows the complete content that
  would be sent; no request is made until you approve it.
- **Academic disclosure.** A sentence stating that the text was produced with
  language-model assistance is appended automatically to every AI-written
  commentary.
- **Providers:** Claude (Anthropic), NVIDIA NIM (free tier) and DeepSeek. You
  supply your own API key; it is kept in the operating system's credential vault,
  never in a plain-text file.
- Optional **variable-name masking** (V1, V2 …) for cases where the names
  themselves are sensitive.

- **Scope warning.** That the AI commentary is offered only to suggest ideas,
  that it does not replace scientific assessment or peer review, and that it must
  not be accepted as-is without checking, is stated explicitly in the consent
  dialog, at the end of the generated commentary, and in the help document.

### ✨ New — Preview Commentary
A button in the Report panel that shows the academic commentary for a single
selected card without generating the report. It reports which engine (AI /
rule-based) and which model wrote the text, and the text can be copied to the
clipboard.

### 🔧 Improved
- **Report progress indicator:** the bar was enlarged and a counter and status
  line added ("Writing AI commentary — 3 / 12 cards", then "Writing report file").
- **Model fallback chain:** if a model has been withdrawn or is saturated at the
  provider (404/410/503/timeout), the next model is tried automatically. Key and
  quota errors break the chain.
- **Refresh models** button: downloads the provider's current model list.
- Provider error messages were made intelligible; for example, when the Claude API
  balance is insufficient, instead of a raw error code you now see a notice
  explaining that a Claude.ai/Max subscription does not cover API usage.
- Settings keys with no counterpart in the settings panel are now preserved when
  settings are saved.

### 🌍 Multilingual — comprehensive hardening
Turkish text had been reported as appearing here and there in the English and
Spanish interfaces. In this version the **entire** application was scanned and
every user-visible Turkish remnant was removed.

- **Analysis help texts:** the ⓘ description (purpose / assumptions /
  interpretation) of 39 analyses came out in Turkish in the English and Spanish
  interfaces — 117 paragraphs translated.
- **Analysis output:** table headers, provenance lines, report body and figure
  labels.
- **Error and warning messages:** 227 message patterns carried into all three
  languages.
- **Interface:** the whole of the Data, Analyze, Map, Report and Tools tabs; the
  data-preparation dialogs (Missing Values, Transform, Add Column, Find/Replace,
  Column Summary, Composite Score, Import Photos).
- **Report output:** Excel sheet names, PDF/DOCX/HTML headings and — most
  importantly — **the entire academic commentary** (Findings / Interpretation /
  Limitations). Previously an English report could contain a fully Turkish
  academic paragraph.
- **Map:** hotspot and LISA legends, spatial-analysis warnings.

> The Turkish interface is unchanged. Turkish values in **your own data** (column
> names, category labels) are never translated — ordinal-variable detection and
> identifier-column heuristics rely on those values, so they were deliberately
> left alone.

### 🐞 Fixed
- The ⓘ help text of **CFA / SEM** did not appear in any language.
- The **Canonical Correlation (CCA)** frequency table did not merge correctly in
  the English and Spanish interfaces.
- Changing the interface language **after** running an analysis caused Anomaly
  Detection, Crossed Random Mixed Model and Variable Clustering to fail; the
  Ridge/Lasso coefficient plot was affected for the same reason.
- In the **GAM**, **Discriminant** and **Robust Regression** panels a choice made
  in a drop-down was not recognised in the English/Spanish interface and silently
  fell back to the default.
- Two crashes were fixed: one in report export and one in the Add Column dialog.

### 📄 Documentation
- An **AI Interpreter Guide** was added to the Help menu (TR/EN/ES): where to
  obtain an API key, approximate cost, step-by-step setup, troubleshooting.

---

## [1.0.17] — 22 August 2026 · **Critical Startup Crash Fix**

> Published under the same copyright registration (2026/18517) as v1.0.0.

### 🐞 Fixed — the application could crash on startup
During the multilingual interface work in v1.0.16, some translation calls in the
main window had been bound to the wrong name; as a result the application failed
to start with `name '_t' is not defined`, notably when the **recent-projects list
was empty** (first launch on a clean install). Every affected point was fixed;
startup and menu construction are sound again.

## [1.0.16] — 21 August 2026 · **English Edition Improvements**

> Published under the same copyright registration (2026/18517) as v1.0.0.

The English edition was reviewed end to end for international users.

### ✨ Improved — English is now the default language
- **The application now always starts in English**, including the licence
  agreement (EULA) acceptance screen; users can switch to Turkish or Spanish from
  Settings whenever they wish. (The default was moved to English at three separate
  layers: the application setting, the i18n start-up language, and the EULA
  dialog.)

### 🐞 Fixed — Turkish text remaining in the interface
- The **search box** in the Data panel appeared in Turkish in English mode; fixed.
- About 90 hard-coded Turkish strings in dialogs and panels were made multilingual
  (TR/EN/ES): the agreement window, the update dialog, the column/transform/
  missing-value tools, the advisor panel, the multiple-choice panel and the
  general buttons (Close / Clear / Add / Delete / Apply / Copy / Undo …).
- Hidden leaks caused by Turkish words without special characters were scanned;
  no untranslated text remains in the interface (the three language catalogues
  match exactly).

## [1.0.15] — 2 August 2026 · **Multilingual Interface Fixes + LMM Stability**

> Published under the same copyright registration (2026/18517) as v1.0.0.

### 🐞 Fixed — analyses broken in the English/Spanish interface
The "no selection" placeholder in drop-down lists is translated
(`(yok)` → `(none)` → `(ninguno)`), but the code compared against the fixed
Turkish string; the placeholder was taken for a real column name and the analysis
failed:

- **LMM** → `Random slope '(none - intercept only)' not in data`
- **Weighted Mean / Frequency / Total / Regression / Logistic** →
  `Cluster/PSU column not found: '(none)'`
- Also **VARCOMP** nested factor, **Competing Risks** group,
  **Poisson/NegBin** offset, **Survey-PHREG** weight/cluster/stratum,
  **Conditional Logit** alternative column, **Path Analysis** template selection.

A single language-independent check was added; the Turkish interface was not
affected and its behaviour is unchanged.

### 🐞 Fixed — LMM "Singular matrix" error
The mixed-model optimizer was pinned to `lbfgs`; when the random-effects
covariance approached singularity the analysis would not run at all. Now
`lbfgs → bfgs → powell` are tried in turn; the same model converges without
trouble under the other optimizers.

### 🔀 Changed — where Discriminant Analysis lives
Although LDA/QDA is a classification method, it sat under **Advanced** in the
sidebar. It was moved to the **Classification** category, after Gradient Boosting.
The total number of analyses is unchanged (110).

---

## [1.0.14] — 28 June 2026 · **Professional Parameter Panel + Advanced Output + i18n Cleanup**

> Published under the same copyright registration (2026/18517) as v1.0.0. Existing
> users are directed to the new installer via **Help → Check for Updates**.

### ✨ New — every analysis parameter is now under user control
SPSS/JASP style, through a common "Advanced Parameters" framework:
- **t-tests (one-sample/independent/paired):** hypothesis direction, Welch/Student,
  Hedges g / Glass Δ / CLES / d_av, confidence interval for the effect size,
  Shapiro/K-S/Levene/Bartlett, descriptives, bootstrap CI.
- **ANOVA family:** one-way (Welch, ω²/ε²), two-way (SS I/II/III, post-hoc,
  η²ₚ/η²/ω², cell/marginal means), **ANCOVA** (SS type, homogeneity of slopes,
  EMM post-hoc), **MANOVA** (reference test, Box's M, univariate follow-up),
  **repeated measures** (Greenhouse-Geisser, Mauchly, generalised η², post-hoc).
- **Non-parametric:** Mann-Whitney (direction/continuity/method/CLES), Wilcoxon
  (zero_method), Kruskal (ε² + Dunn post-hoc), Friedman (pairwise Wilcoxon
  post-hoc).
- **Correlation:** p-value, direction and p-adjustment (Bonferroni/Holm/FDR) for
  all three methods, plus CI for r.
- **Categorical:** chi-square (Yates, G-test, φ/C, expected values, standardised
  residuals).
- **Regression:** linear (robust SE HC0-3, standardised β), logistic
  (Cox-Snell/Nagelkerke, classification/AUC, Hosmer-Lemeshow, VIF), Ridge/Lasso
  (automatic α by cross-validation).
- **Advanced output:** Cox proportional-hazards (Schoenfeld) test, LMM Nakagawa
  marginal/conditional R², Probit classification metrics.

### 🔧 Fixes
- All remaining hard-coded Turkish labels in the English/Spanish interface were
  removed: provenance lines ("Group"/"Target"/"Tested μ"), confidence-interval
  labels ("%95 GA" → "95% CI"), form labels (37) and drop-down items
  ("Automatic"/"None" etc.). The three languages are in sync (~4,408 keys).
- An "Advanced Parameters" description was added to the dataset packs for every
  analysis.

### 🔄 Update
This installer removes the previous version automatically and installs v1.0.14
into the same directory; your settings, projects and data are preserved.

---

## [1.0.13] — 25 June 2026 · **Two New Analyses: Descriptives by Group + Mixed-Design ANOVA**

> Published under the same copyright registration (2026/18517) as v1.0.0. Existing
> users are directed to the new installer via **Help → Check for Updates**.

### ✨ New
- **Descriptive statistics by group (SPSS "Split File" logic).** An optional
  **"By group (Split-File)"** selector was added to the Descriptive Statistics
  analysis: when a categorical variable is chosen, all descriptives of the numeric
  variable (mean, SD, median, quartiles, skewness/kurtosis, confidence interval)
  are computed separately for each group in a single table, and a comparative box
  plot across groups is produced. The confidence level (90%/95%/99%) is adjustable.
- **Mixed-Design ANOVA (Split-Plot).** A new analysis for mixed designs with one
  between-subjects factor (e.g. experiment/control) and one within-subjects factor
  (e.g. pre-test/post-test/follow-up). It reports three effects: the
  between-groups main effect, the within-subjects main effect and the
  **group × time interaction**. The sphericity (Mauchly) test runs automatically;
  on violation, Greenhouse-Geisser corrected p and partial eta-squared (ηp²)
  effect sizes are given. This is the standard analysis for pre-test/post-test
  experiment-control designs in education and psychology.

### 🔧 Fixes
- Turkish phrases remaining in the English/Spanish interface for the two new
  analyses were removed; result text, provenance, table headers, the ⓘ
  description and figure titles are synchronised across the three languages.

### 🔄 Update
This installer removes the previous version automatically and installs v1.0.13
into the same directory; your settings, projects and data are preserved.

---

## [1.0.12] — 24 June 2026 · **Confidence Level Rolled Out + Stability**

> Published under the same copyright registration (2026/18517) as v1.0.0. Existing
> users are directed to the new installer via **Help → Check for Updates**.

### ✨ New
- **Adjustable Confidence Level (90% / 95% / 99% / Custom) rolled out to ~67
  analyses.** The selector, previously present in 10 parametric tests, is now
  available in most analyses that produce a confidence or credible interval:
  - **Regression:** Logistic (odds-ratio CI), Probit, Tobit, Log-Linear,
    Poisson/Negative Binomial, Multinomial, Ordinal, Conditional Logit, Quantile,
    Robust, Non-linear, Bayesian Linear.
  - **Mixed/Survey:** LMM, GEE, GLMM, Weighted (Survey) Regression/Logistic.
  - **Survival:** Cox, Kaplan-Meier, Parametric (AFT), Competing Risks,
    Frailty-Cox, Survey-PHREG, Interval-Censored, Time-Dependent Cox.
  - **Categorical:** CMH, Fisher (OR), Cohen's Kappa, Chi-Square Independence
    (2×2 OR), McNemar.
  - **Time series:** ARIMA, Mann-Kendall/Sen, Exponential Smoothing (forecast band).
  - **Other:** Bland-Altman, Bootstrap CI, Effect Size, Binomial, CFA/Path
    Analysis, Canonical Correlation, Nested/Crossed LMM, Cronbach's α, confusion
    matrix metrics, Sign/Permutation tests, Mann-Whitney/Wilcoxon
    (Hodges-Lehmann), Cross Tabulation, Descriptive Statistics, Multiple
    Imputation, Likert, Bayesian Correlation.

### 🐛 Fixes
- **Silent crash fixed** — running an analysis and then importing new data
  (particularly while on the Statistics tab) could close the application without
  an error. Rebuilding the analysis-output history was made safe; data reload and
  tab-switch stability were improved as well.

### 🔄 Update
This installer removes the previous version of MerQur automatically and installs
v1.0.12 into the same directory. Your settings, projects and data are preserved.

---

## [1.0.11] — 23 June 2026 · **Confidence Level and Multiple-Response Improvements**

> Published under the same copyright registration (2026/18517) as v1.0.0. Existing
> users are directed to the new installer via **Help → Check for Updates**.

### ✨ New
- **Confidence Level (adjustable confidence interval)** — selectable in 10
  hypothesis/regression panels; the confidence interval (90%/95%/99%) in result
  tables and figures is computed and labelled accordingly.
- **Manual Multiple-Response (MR) set definition** — columns already split in
  Excel (e.g. `Q10_1 … Q10_5`) can be declared directly to MerQur as a
  multiple-response set (raw counts or 0/1 binary form).

### 🐛 Fixes
- **Multiple-choice parsing** — separator selection was made deterministic (a
  wrong separator is now prevented), automatic question-number detection was
  improved, orphan helper columns are now cleaned up, and the low-frequency option
  threshold was made sensible.
- **Multiple-Response frequency chart** — switched to a single-colour palette (the
  two-colour leader highlight was removed).
- **Language-pack loading** — an old local language pack left behind by the
  updater could display new interface/result strings as raw keys; the bundled pack
  now fills in missing keys in all cases (layer merging).
- **Dark-theme readability** — the highlight colours in the multiple-choice column
  lists (manual/automatic/applied) now use light tones that remain readable on a
  dark background.
- **Interface** — several layout warnings and a stuck window reference were fixed.

### 🔄 Update
This installer removes the previous version of MerQur automatically and installs
v1.0.11 into the same directory. Your settings, projects and data are preserved.

---

## [1.0.9] — 12 June 2026 · **Improvements and Simplification**

> Published under the same copyright registration (2026/18517) as v1.0.0. Existing
> users are directed to the new installer via **Help → Check for Updates**.

### 🐛 Fixes
- **Bayesian Non-linear Regression** — numerical stability (overflow in
  logistic/exponential models eliminated, robust convergence from data-derived
  starting values).
- **Conditional Logit (Choice Model)** — coefficients collapsing to zero, and the
  accompanying warning, with large-scale predictors (price/income/distance) were
  fixed (feature scaling).
- **Conditional Logistic Regression** — the convergence warning was suppressed and
  the estimates are stable.

### ✨ Improvements
- **Plainer analysis descriptions** — the description texts were simplified.
- **Data loading** — the column-suggestion window shown on load was removed; the
  same detection is already available in the right-click menu.
- **Info icon (ⓘ)** — moved to the left of the analysis name, so the title row no
  longer requires scrolling.
- **Project file extension** — now `.mqr` (existing `.merqur` files still open).
- **Multilingual interface** — result texts, tables, tooltips and figures are in
  full sync across TR/EN/ES.

---

## [1.0.8] — 8 June 2026 · **Stability and Improvements**

> Published under the same copyright registration (2026/18517) as v1.0.0. Existing
> users are directed to the new installer via **Help → Check for Updates**.

### 🐛 Fixes
- **Startup stability** — the splash screen freezing at "Ready." without the
  interface appearing was fixed (window presentation moved into the event loop,
  plus a watchdog).
- **Canonical Correlation (CCA)** — Y variables are now added by selection just
  like X; the analysis works properly (previously it did not run because Y could
  not be read).
- **Mixed Models (LMM/GLMM/GEE/Bayesian Hierarchical)** — categorical variables
  can now be chosen in the fixed-effects list as well.
- **Gradient Boosting** — falls back to scikit-learn automatically when XGBoost is
  absent (the "Cannot find XGBoost Library" error is gone).
- **Nested LMM** — variance-table labels follow the selected variable names
  (instead of the former fixed Replication/Population/Family).
- **Data table** — columns whose values are all integers are displayed without
  decimals (397.00 → 397).
- **GLM table** — the empty "equation" column in Poisson/ordinal regression is
  hidden.

### 📦 New Sample Packs
- **Infectious Diseases** — an infection-themed dataset for every analysis (TR/EN).
- **Landscape — Cochran's Q** — a new sample dataset in multiple-choice format.

---

## [1.0.6] — 2 June 2026 · **Fully Multilingual Interface + Checkbox Variable Selection**

> Multilingual-interface completion update. Published under the same copyright
> registration (2026/18517) as v1.0.0. Existing users are directed to the new
> installer via **Help → Check for Updates**.

### 🌍 Fully Multilingual Interface (TR / EN / ES)

- Hard-coded Turkish labels in **89 analysis panels** were moved into the i18n key
  system. Users working in EN/ES now see form labels, drop-down options, result
  text headings and test names in the language they have selected.
- **~256 new keys × 3 languages = ~768 translation entries** were added:
  - **Form labels** (`form_*`): 135+ keys
  - **Result formatter** (`stats_*`): TEST / Statistic / p-value / df /
    Effect size / 95% CI / GROUP STATS / ANOVA TABLE / POST-HOC / DECISION / H₀
  - **Test names** (`test_*`): 17 names (Independent t-Test, Chi-Square Test of
    Independence, MANOVA Wilks' Lambda, etc.)
  - **Effect size** (`es_*`): Small / Medium / Large / Weak / Strong
  - **Cohen's Kappa** (`kappa_*`): agreement quality (poor → excellent) plus
    weighting type (none / linear / quadratic)
  - **Drop-down options**: Listwise/Pairwise, Type I/III SS, Random/Fixed,
    Ward/Complete/Average/Single, k-means++, Varimax, Bayesian modes,
    Pearson/Spearman/Kendall, etc.
  - **VariableSelector widget**: All/Clear/Profile + count + dialog
  - **Sidebar**: the analysis names of 8 Advanced categories (VARCOMP, Bayesian
    t/Correlation/ANOVA/Hierarchical, SAR/Error/GWR)
  - **Help → Licence Agreement** menu item

### ✅ Checkbox-Based Variable Selection

Multiple variables are now selected by **clicking checkboxes** instead of typing a
comma-separated list:

- **MANOVA** — dependent variables are now a checkbox list
- **Spatial Error Model (SAR Error)** — independent variables
- **Spatial Lag Model (SAR Lag)** — independent variables
- **GWR (Geographically Weighted Regression)** — independent variables
- **Hierarchical Bayesian Regression** — independent variables

With **Select All / Clear / Save Profile** buttons for fast work.

### 🐛 Fixes

- **Leftovers from a previous analysis are cleared when a new file is opened:**
  maps, figures and result texts produced from the previous file are deleted as
  soon as a new file is opened; worker threads are stopped; the method drop-down
  and the parameter form are reset.
- **Hierarchical Bayesian Regression — TypeError:** duplicate column names crashed
  the analysis (`arg must be a list, tuple, 1-d array, or Series`); column
  selection now filters duplicate names.

---

## [1.0.5] — 28 May 2026 · **Graphical Output Expansion + Multilingual Figures**

> Visualisation-focused update. Published under the same copyright registration
> (2026/18517) as v1.0.0. Existing users are directed to the new installer via
> **Help → Check for Updates**.

### 🆕 Analyses That Gained Figures (Chart tab)

- **Hierarchical Clustering** now draws a **dendrogram** (leaf labels = cultivar/ID
  names, Ward-coloured clusters).
- **Figures were added to 27 analyses** that previously had none:
  - **Group comparison (boxplot/interaction/profile)**: Independent/Paired/
    One-sample t-test, One-/Two-Way ANOVA, Repeated Measures ANOVA, Mann-Whitney,
    Kruskal-Wallis, Wilcoxon, Friedman, MANOVA.
  - **Categorical (bar)**: Chi-Square Independence, Chi-Square Goodness of Fit,
    Cross Tabulation.
  - **Ordination (2D scatter/biplot)**: MDS, UMAP, Correspondence, Discriminant.
  - **Regression**: Multiple Linear (residual plot), Logistic (probability
    distribution).
  - **Machine Learning**: Random Forest & Gradient Boosting (variable importance).
  - **Time series**: Time Series & STL (decomposition), ARIMA & Holt-Winters
    (forecast + 95% CI), Mann-Kendall (Sen's slope).

### 🌍 Multilingual Figures (TR / EN / ES)

- **All figure labels** (title, axes, legend, annotation) are now translated
  according to the selected interface language — both the newly added figures and
  all existing ones (PCA, Kaplan-Meier, ROC, Correlation, etc.). About 175 new keys
  were added to the language packs.

### 🐛 Fixes

- **Map (Map tab):** KDE/Hotspot maps now fill the screen; the legend and scale bar
  are visible on first run without scrolling (folium full-page render + full-height
  CSS).
- **Figure layout:** the "Tight layout not applied" warning on colorbar/multi-panel
  figures was eliminated (switched to constrained_layout).
- **Descriptive Statistics:** "Run" now shows the selected variable (it previously
  always reverted to the first variable).

---

## [1.0.4] — 21 May 2026 · **Import from Geotagged Photos**

> Feature update. Published under the same copyright registration (2026/18517) as
> v1.0.0. Existing users are directed to the new installer via **Help → Check for
> Updates**.

### 🆕 Import from Geotagged Photos (New Feature)

- **File → 📷 Import from Geotagged Photos…** (Ctrl+Shift+I).
- Pick a folder (subfolder scanning optional) — MerQur reads the EXIF + GPS
  metadata of every supported image file (JPG/JPEG/TIF/TIFF/HEIC/HEIF/PNG/WEBP)
  and turns it into a single table.
- The 22 columns produced: `foto_adi` (photo name), `dosya_yolu` (file path),
  `dosya_boyutu_kb` (size), `genislik_px`, `yukseklik_px` (width/height),
  `cekim_zamani` (DateTimeOriginal), `lat`, `lon`, `yukseklik_m` (altitude),
  `yon_derece` (GPSImgDirection), `hiz_kmh` (speed), `kamera_uretici`,
  `kamera_model`, `lens_model`, `focal_length_mm`, `apertur_f`, `pozlama_sn`
  (exposure), `iso`, `flash`, `beyaz_dengesi` (white balance), `geotag_var`
  (binary).
- DMS → decimal-degree GPS conversion; S/W reference → negative value.
- Capture time as an ISO 8601 datetime; speed converted to KPH automatically.
- A progress bar (16 px, petrol green) with the file name during the scan.
- Summary box: counts with/without GPS, camera-model distribution, date range,
  folder path.
- After import the DataFrame flows automatically into the Data/Analyze/Map panels;
  **lat/lon are detected automatically**, and KDE / Hotspot / Moran's I / vector
  layer analyses can be run directly on the Map tab.
- Full i18n (TR/EN/ES) — 5 new keys per language.

### 🐛 Fixes

- The urllib3/chardet version-mismatch warning from the `requests` library
  (RequestsDependencyWarning) is suppressed in main.py — no more harmless warning
  message at startup.

### 📥 Downloads

| File | Size |
|---|---|
| `MerQur-1.0.4-windows-x64-Setup.exe` | ~315 MB |
| `MerQur-1.0.4-windows-x64.zip` | ~467 MB |

---

## [1.0.3] — 19 May 2026 · **Vector Layers + UX & Bug Hotfix Update**

> Maintenance + feature update. Published under the same copyright registration
> (2026/18517) as v1.0.0. Existing users are directed to the new installer via
> **Help → Check for Updates**.

### 🆕 Vector Layers (New Feature)

- **SHP / KML / KMZ / GPKG / GeoJSON** overlay support on the Map tab. The
  researcher can drape a study-area boundary, points of interest or stream lines
  over analyses such as KDE / Hotspot / DBSCAN / Moran's I.
- A compact card per layer: ☑ show · name (inline edit) · 🎨 colour swatch ·
  🗑 delete · ◐ Filled (polygon; the boundary line is always visible) · ☑ Legend.
- Automatic **CRS transformation** (EPSG:4326 / WGS84) — KMZ is unzipped
  automatically.
- JS injection supporting both folium's **standalone HTML** and **iframe srcdoc**
  output (folium's quirky dual format).
- Legend stack: vector (top right) + analysis (below the vector) in a vertical
  stack.

### 🔧 UI / UX Fixes

- **Map tab toolbar**: the Run, Save Map and PNG buttons were moved from the left
  panel to the map's top toolbar (right-aligned, consistent with the other
  analysis tabs). More room in the left panel.
- **Left panel splitter**: min 280, max 560, default 340 px — the user can widen it
  with the splitter handle.
- **Analysis Assistant** = `data_welcome_dialog` (the card-based BRIEFING dialog
  added in v1.0.2). The old AdvisorPanel's sequential auto-runner behaviour was
  removed; it now only **suggests** and explains what each analysis is for, with no
  automatic execution. Both the automatic route (on data load) and the manual one
  (Tools → Calculators → 🎯 Analysis Assistant) open the same dialog.
- **ID column filter**: columns such as `ogrenci_id` are NOT suggested as analysis
  variables; auto-excluded columns are shown in an info banner.
- **Badge "Information"** (previously "BRIEFING").
- **"Don't show again"** wording clarified: "Do not open automatically when data is
  loaded (you can still open it from Tools → Analysis Assistant)".
- **🔍 Find/Replace** (Data tab toolbar): 3 modes (Contains/Whole cell/Regex),
  case-sensitivity option, all/selected column scope, with undo support.

### 🐛 Critical Bug Fixes

- **Map pan-cursor wheel-zoom regression**: after a mouse-wheel zoom the pan/grab
  cursor stayed stuck across all tabs. **`_override_poll_timer`** (200 ms) polls
  QGuiApplication.mouseButtons() — on NoButton, pan-type shapes are popped from the
  overrideCursor stack while Wait/Busy (the analysis hourglass) is preserved.
  `_cursor_enforce_timer.stop` was REMOVED — the timer runs continuously.
- **Data welcome dialog `t` shadow bug**: the loop variable in
  `for t in column_types.values()` shadowed the i18n `t()` function → TypeError
  silently caught → the dialog never opened. The loop variable was renamed to `ty`.
- **Settings migration**: a `_v103b_migrated_welcome` flag flips existing users'
  `show_data_welcome=False` to True once.

### 🌓 Dark Mode + Q1 Figure Hygiene

- **Hard-coded white backgrounds** (log panel, info popover, analysis card) became
  theme-aware via `palette(base)` + `palette(text)`.
- **Matplotlib figures always use the academic theme** (even when the GUI is dark).
  Because figures are embedded in reports and publications, they follow the Q1
  standard (white background, academic colour palette, thin grey grid).
  `apply_dark_theme()` is no longer called for matplotlib.

### 📥 Downloads

| File | Size |
|---|---|
| `MerQur-1.0.3-windows-x64-Setup.exe` | ~342 MB |
| `MerQur-1.0.3-windows-x64.zip` | ~515 MB |

---

## [1.0.2] — 18 May 2026 · **Bayesian + Spatial Regression + SEM Update**

> Feature update. Published under the same copyright registration (2026/18517) as
> v1.0.0. Existing users are directed to the new installer via **Help → Check for
> Updates**.

### 🆕 8 New Advanced Analyses

**The Bayesian quartet** (NO PyMC dependency — pingouin + Empirical Bayes):

- **Bayesian t-Test (BEST)** — the Bayesian counterpart of the one-sample/
  independent/paired t-test. JZS Cauchy prior, **BF₁₀** plus an 8-band Jeffreys
  interpretation-scale figure. Mode-aware form (Group / 2nd measurement / μ₀ fields
  enable/disable automatically).
- **Bayesian Correlation** — reports Pearson/Spearman/Kendall correlation with
  BF₁₀; direct evidence for "relationship present / absent".
- **Bayesian ANOVA** — pingouin `bayesfactor_anova` + BIC fallback for one-way and
  two-way (including interaction) ANOVA; a horizontal BF bar chart per effect.
- **Hierarchical Bayesian Regression** — statsmodels `MixedLM` + Empirical Bayes
  BLUP posteriors + BIC-based Bayes Factor (LMM vs OLS). A **caterpillar plot** of
  the group random intercepts with ±95% credible intervals.

**The spatial regression trio** (libpysal + spreg + mgwr):

- **SAR (Spatial Autoregressive Lag)** — `Y = ρWY + Xβ + ε`. KNN / DistanceBand
  neighbourhood matrices; spreg `ML_Lag`. Coefficient forest plot plus a ρ report.
- **Spatial Error Model** — `Y = Xβ + u, u = λWu + ε`. spreg `ML_Error`, with the
  λ spatial-error parameter.
- **GWR (Geographically Weighted Regression)** — mgwr `Sel_BW` AICc-optimal
  bandwidth plus local coefficient estimation. A spatial scatter map of local R²,
  and a min/Q25/median/Q75/max table with the percentage significant for each
  coefficient.

**CFA → SEM extension**:

- The CFA panel now accepts an optional **structural path** field
  (`"F2 ~ F1; F3 ~ F1 + F2"`). Left empty it is the classical measurement model
  (CFA); filled in it becomes a **full SEM** (measurement + structural). The semopy
  output parses latent~latent rows as structural paths.

### 🎨 Data Welcome Dialog (New)

- A modal welcome with a **"BRIEFING"** badge when the user loads a dataset. Based
  on column types (numeric / binary / categorical / datetime / geo), suitable
  analysis suggestions are laid out as cards: **icon · title · reason · example
  column roles (Group/Value/Target/Lat-Lon/…) · "Analyze → …" path**.
- Covers 13 analysis types: Descriptives, Normality, Correlation, Bayesian
  Correlation, t-Test, Bayesian t-Test, ANOVA, Chi-Square, Regression, Time Series,
  Spatial, Spatial Regression, Hierarchical Bayesian / LMM.
- The "Don't show again" preference is written to `settings.json`.
- Full **i18n**: TR/EN/ES (`welcome_*` keys, via t()).

### 🏷 Tab Renaming

- **"İstatistik" → "Analiz"** (TR), **"Statistics" → "Analyze"** (EN),
  **"Estadística" → "Analizar"** (ES). Consistent with the *Analyze* menu of
  SPSS/JASP/jamovi; a shorter name that also covers modern model classes such as
  Bayesian / SEM / Spatial Regression.

### 🐛 Bug Fixes (leaks from v1.0.1)

- Empty chart tab: 7 new ASCII_TYPEs in the `TAB_AVAILABILITY` filter; Turkish→ASCII
  mappings added to `_ANALYSIS_TYPE_MAP`; a delayed
  `QTimer.singleShot(50, canvas.draw)` redraw after Qt tab switching;
  `ax.set_facecolor("white")` to fix dark-mode contrast.
- BF₁₀ format overflow: a **scientific notation** threshold for `>1e6` or `<1e-6`;
  the old raw `200+ digit` astronomical float output was removed.
- VARCOMP nested model spec: thanks to the outer-as-dummy + nested ID chaining
  approach all factors sit under `vc_formula`, improving identifiability.

### 📦 Dependencies

- **Added**: `spreg` 1.9.0 (~5 MB), `mgwr` 2.2.1 (~10 MB).
- **Already in use**: `pingouin` (Bayesian BF), `semopy` (SEM), `libpysal` (spatial
  weights), `statsmodels.MixedLM` (Hierarchical Bayes).
- **NO PyMC** — an Empirical Bayes / BIC approach is used for Hierarchical
  Bayesian; ~500 MB saved in the bundle.

### 📥 Downloads

| File | Size |
|---|---|
| `MerQur-1.0.2-windows-x64-Setup.exe` | 342 MB |
| `MerQur-1.0.2-windows-x64.zip` | 515 MB |

---

## [1.0.1] — 15 May 2026 · **VARCOMP + Dark Theme Update**

> Maintenance and feature update. Published under the same copyright registration
> (2026/18517) as v1.0.0. Existing users are directed to the new installer via
> **Help → Check for Updates**.

### 🆕 New Analysis

- **VARCOMP (Variance Components Analysis)** — the Python equivalent of SAS
  *PROC VARCOMP*. A dynamic N-factor form (unlimited factors via the **"+ Add
  Factor"** button), a **nested / crossed** choice per factor, cumulative nested ID
  chaining, **a separate ICC for each component** plus heritability (h²)
  interpretation, and automatic diagnostic notes (singular fit, insufficient
  levels, confounding warning).

### 🐛 Critical VARCOMP / Mixed Model Fixes

- Fixed the problem where the `statsmodels` `lbfgs` optimizer returned `llf=inf` at
  the boundary and drove the result to zero (cascade: `bfgs` → `cg`).
- Fixed outer-factor variance **sticking at the 0 boundary** in multi-factor models
  (*dummy-outer strategy*) — all factors are now under vcomp, improving
  identifiability.

### 🌓 Dark Theme

- A full palette-based **dark theme** — switched on from Settings and hot-reloaded
  the moment it is enabled (no restart needed).
- The Survey Designer, the Statistics category sidebar, the Licence Agreement
  dialog and the Data tab toolbar are all theme-aware (they switch between
  light/dark automatically via `palette()`).
- Splash freeze fix: when the theme was changed and saved, the application used to
  hang at **"preparing…"** — resolved by extracting the `core/theme.py` module from
  `main.py`.

### 📋 Licence Agreement (EULA)

- A **modal EULA dialog** on first launch — the application will not open until it
  is accepted. Acceptance is written to `settings.json`; it is requested again on a
  version bump. Read-only viewing via the **Help menu**.

### ⏳ Modal Progress for Long Analyses

- **`gui/analysis_runner.py`** — a QThread-based worker plus a modal progress
  window for long analyses such as VARCOMP/LMM/GLMM. The UI no longer blocks, and
  a **cancel** button is supported. The Windows "MerQur is not responding" warning
  is gone.

### 📊 Data Tab Improvements

- A quick-action toolbar with 10 buttons: 🔍 Search, 📊 Column Summary, 🏷 Encode,
  🔗 Merge, ❌ Manage Missing, 🔄 Transform, 📤 Export, ➕ Add Column,
  🗑 Delete Column, ↶ Undo, ↷ Redo.
- **20-step undo / redo** (Ctrl+Z / Ctrl+Y) — `core/undo_redo.py`.
- A **continuous / discrete** numeric sub-type distinction plus per-column
  adjustable decimal precision.
- Discrete numeric columns (coded group IDs such as `okul_no = 1,2,3 …`) can now be
  chosen as random factors for **VARCOMP / LMM / Crossed LMM / Nested LMM**.

### 🗃 New Sample Data

- **`varcomp_orman_genetik_5faktor.xlsx`** — a 5-factor forest-breeding
  provenance/family trial: 6 sites × 5 populations × 30 families × 3 blocks ×
  3 individuals = 1,620 observations. The true variance components can be estimated
  correctly with VARCOMP (verified as test data).

### 🌐 Website

- The home-page badge was updated to **Version 1.0.1** (the DOI attribution keeps
  Version 1.0.0 as the baseline — the registered version).
- The `/indir/` (download) page is current with the v1.0.1 Setup.exe + ZIP links.
- A comprehensive analysis page was added for VARCOMP:
  `/bilim-dallari/ziraat-orman-su-urunleri/100-varcomp-varyans-bilesenleri/`.
- Acknowledgements were added to the home-page thanks band for the **SDÜ Rectorate**
  and the **Department of Information Technology**, together with the development
  tools **Python ecosystem + Visual Studio Code + Anthropic Claude Code**.

---

## [1.0.0] — 11 May 2026 · **Official SDÜ Launch Release**

> **MerQur** was officially published for the first time, hosted by **Süleyman
> Demirel University**. It is protected by **copyright registration no. 2026/18517**
> of the Republic of Türkiye Ministry of Culture and Tourism.
> Official address: **https://merqur.sdu.edu.tr**

---

### 🎯 101 Statistical Analyses

A complete set covering the basic and advanced statistical needs of academic
research:

- **Descriptive + Parametric** (13) — Descriptives, Normality, One-sample/
  Independent/Paired t-test, One-/Two-Way ANOVA, Repeated Measures ANOVA, MANOVA,
  ANCOVA, Bootstrap CI, Permutation, Multiple Comparison
- **Non-parametric** (7) — Mann-Whitney U, Wilcoxon, Kruskal-Wallis, Friedman,
  Binomial, Sign, Runs
- **Categorical** (12) — Chi-Square independence/goodness of fit, Fisher Exact,
  McNemar, Cohen's Kappa, CMH, Log-Linear, Cross Tabulation, MR Frequency,
  MR×Categorical, MR×MR, Cochran's Q
- **Correlation + Multivariate** (6) — Pearson/Spearman/Kendall, Bland-Altman,
  Effect Size, Canonical Correlation (CCA), Correspondence Analysis, VARCLUS
- **Regression** (12) — Multiple Linear, Logistic, Poisson, Multinomial, Ordinal,
  PLS, Probit, Tobit, Bayesian Linear, Non-linear, Ridge, LASSO
- **Mediation + Mixed Models** (9) — Mediation, Path Analysis, LMM, **Nested LMM**,
  **Crossed LMM**, Multiple Imputation, GEE, GLMM, Elastic Net, Robust, Quantile
- **Classification + Clustering** (13) — ROC, TSS, Confusion Matrix, Random Forest,
  SVM, Gradient Boosting, K-Means, Hierarchical, DBSCAN, PCA, t-SNE, MDS, UMAP
- **Reliability + Scale** (5) — Cronbach's α, Likert, EFA, ICC, CFA
- **Survey (Complex Sampling)** (5) — Means, Frequency, Total, Regression, Logistic
- **Modern + Survival** (11) — GAM, Discriminant, Conditional Logit, Kaplan-Meier,
  Cox, Parametric AFT, Competing Risks, Time-Dependent Cox, Survey-PHREG,
  Interval-Censored, Frailty Cox
- **Time Series + Anomaly** (6) — Descriptives, STL, ARIMA, ETS, Mann-Kendall + Sen,
  Anomaly Detection

### 🗺 5 Spatial Analyses (Map tab)

- **KDE Density Map** — automatic gradient legend, hotspot display
- **Hexbin Density** — hexagonal-grid density map
- **DBSCAN Spatial Clustering** — geographic density clusters with noise separation
- **Hotspot (Getis-Ord G\*)** — statistical hot/cold spot detection
- **Moran's I** — spatial autocorrelation + LISA local clusters

**Data Exploration mode:** before a spatial analysis, display the points on a map
**coloured automatically** by a categorical column (e.g. gender, age_group).
Automatic legend, LayerControl, scale bar, PNG export.

### 📄 One-Click APA 7 Report

Analysis output is interpreted automatically and turned into a Word report to the
American Psychological Association 7th-edition standard. The symbols *t*, *p*, *d*,
*F*, *r*, *M*, *SD* are italicised automatically. Tables and figures feed the report
on their own.

### 🎨 Chart Studio

30+ chart types: boxplot, violin plot, heatmap, sankey, stacked bar, ridge plot,
scatter matrix, dendrogram, parallel coordinates, and more. Titles and axis labels
are fully editable. PNG and interactive Plotly HTML output.

### 📋 Survey + Scale

A structured survey builder, branching logic, multiple-response questions, a
**sample-size calculator** (compact 2-column layout), Likert scale analysis
(Cronbach's α, EFA, CFA, ICC).

### 🌍 Trilingual Interface

**Turkish**, **English**, **Spanish** — not just the menus; analysis output, report
sentences, table headers and error messages are fully translated. Switch language
with one click.

### 📂 Multi-Format Support

Excel (.xlsx), CSV, SPSS (.sav), Stata (.dta), R (.rdata), Parquet. Built-in data
encoding, missing-value handling, transformation and merging.

### 🔄 In-App Update System

Download and install the latest version with one click via *Check for Updates* in
the Help menu. The manifest server runs on **merqur.sdu.edu.tr** — an SDÜ
institutional service.

### 🗺 11 Academic Sample Packs

Discipline-based ready-made datasets (each with 99 analyses + 5 spatial × .xlsx +
GUIDE.docx):

1. **Medicine / Health Sciences**
2. **Educational Sciences / Sociology**
3. **Sport Sciences**
4. **Agriculture / Forest Engineering**
5. **Landscape Architecture**
6. **Architecture · Urban & Regional Planning · Interior Architecture · Industrial
   Product Design**
7. **Visual Perception · Visual Quality · Sensory Landscape**
8. **Natural Sciences / Mathematics**
9. **Tourism**
10. **Social, Humanities / Administrative Sciences**
11. **Mixed (multidisciplinary)**

Plus a **shared Repeated Measures ANOVA reference dataset** (50 participants ×
4 time points, in both wide and long format).

### 📚 Documentation

- **User Guide** (in the Help menu, including a glossary of the 101 analyses)
- **MerQur SAS · SPSS Equivalence Table** (Word, 12 tables, SAS PROC + SPSS command
  equivalents for 104 analyses)
- **Statistics for Children Presentation** (PowerPoint, 50 slides, statistical
  concepts in a child's language)
- **EULA TR + EN** (Markdown + Word) — academic use open, commercial use by written
  permission, APA 7 citation required

### 🏛️ Registration and Institutional Identity

- **Republic of Türkiye Ministry of Culture and Tourism, Work Registry No:
  2026/18517**
- **Süleyman Demirel University** institutional subdomain: **merqur.sdu.edu.tr**
- Developer: **Ömer K. Örücü** (SDÜ Department of Landscape Architecture)
- Official contact: **merqur@sdu.edu.tr**

### 🔧 Technical Foundation

- A **Python 3.11 / PyQt6** desktop application
- Standalone Windows / macOS / Linux distribution via **PyInstaller --onedir**
- **Bundled multiprocessing fix** — `freeze_support()` + spawn start method for
  packages such as libpysal/esda
- **esda analytic mode** — no crand worker spawning for Hotspot/Moran, no BLAS
  int64 trouble
- **Map cursor v6** — a multi-layered Chromium WebEngine cursor-leak fix (CSS
  injection + Qt setCursor + CursorChange event filter)
- **QProgressDialog** — a modal waiting dialog for long analyses (Nested LMM,
  Crossed LMM)

---

*With this release MerQur officially entered publication as the first comprehensive
data analysis platform of Turkish origin offered free of charge to the academic
statistics community.*
