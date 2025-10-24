# Statistical analysis for MR 

MR analysis requires that genetic variants be associated with the exposure but not with potential confounders.

[IEU OpenGWAS project](https://gwas.mrcieu.ac.uk/)

Use the [TwoSampleMR](https://mrcieu.github.io/TwoSampleMR/) R package to apply the data to Mendelian randomization, and the [gwasglue](https://mrcieu.github.io/gwasglue/) for fine mapping, colocalisation, etc.

- **P-value Threshold**: Effective for controlling false positives. p < 5×10−6
- **R² Threshold**: Ensures independence of SNPs, but a stringent threshold (r² < 0.01) may need to be evaluated for appropriateness based on genetic architecture and LD patterns.
- **Clumping Distance**: A stringent clumping distance (e.g., 500 kb or 1,000 kb) ensures more independent SNPs and reduces linkage disequilibrium impact.
- **F Statistic**: An F statistic greater than 10 indicates a strong instrument. To minimize bias from weak instruments, an F statistic threshold of >20 is preferred.

### Weak Instrument Bias
Weak instrument bias occurs when genetic variants (SNPs) used as instruments have a weak association with the exposure. This can lead to biased estimates in Mendelian Randomization (MR). 

- **Weak Instrument Variables (IVs)**: Instruments are weak if the association with the exposure is low. An F statistic <10 indicates weak instruments, which can result in imprecise and biased estimates.
- **Minimizing Weak Instrument Bias**: Strong instruments (F statistic >10 or ideally >20) provide robust estimates and minimize weak instrument bias.

### Two-Sample Mendelian Randomization (MR)
Two-sample MR uses genetic data from two different samples: one for exposure and another for outcome. This method leverages large-scale GWAS summary statistics and follows these steps:

1. **Select Instrumental Variables (IVs)**: Identify genetic variants associated with the exposure.
2. **Estimate Causal Effect**: Use these IVs to estimate the association with the outcome.

### Other MR Approaches
1. **One-Sample MR**: Uses individual-level data for both exposure and outcome.
2. **Multivariable MR**: Examines multiple exposures simultaneously to account for confounding.
3. **Reverse MR**: Tests whether the outcome causes the exposure.
4. **Panel MR**: Assesses dynamic causal relationships over time using panel data.
5. **Generalized MR**: Extends MR for various data types, such as ordinal or continuous exposures.

### Estimation of the Causal Relationship Between IBU (a drug) and OA (a disease)
Here are key statistical methods used in MR to estimate causal relationships:

1. **Inverse-Variance Weighted (IVW)**:
   - Combines estimates from multiple SNPs.
   - Assumes all genetic variants are valid instruments.
2. **MR-Egger Regression**:
   - Adjusts for pleiotropy, includes intercept to account for bias.
3. **Weighted Median Estimator**:
   - Robust even if up to 50% of the SNPs are invalid instruments.
4. **Simple Mode**:
   - A non-parametric approach that identifies the most frequent causal estimate.
5. **Weighted Mode**:
   - Assigns more weight to SNPs with lower variance to improve robustness.

These methods use summary statistics to estimate causal relationships, each addressing different aspects of instrument validity and pleiotropy.

### Heterogeneity and Sensitivity Tests in MR
Heterogeneity and sensitivity tests assess the robustness of causal estimates.

#### Heterogeneity Tests
1. **Cochran's Q-Statistics**:
   - Measures variation in effect estimates across SNPs. Significant Q indicates heterogeneity.
2. **I² Statistic**:
   - Quantifies the proportion of variation due to heterogeneity, with values close to 0% indicating low heterogeneity.

#### Sensitivity Test
1. **Leave-One-Out Analysis**:
   - Assesses how the removal of each SNP affects the overall causal estimate.
   - A substantial change suggests that a single SNP may disproportionately influence the results.
