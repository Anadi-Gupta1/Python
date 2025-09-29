"""
SciPy Statistics - Complete Statistical Analysis and Probability Guide
===================================================================

Comprehensive guide to SciPy's statistical capabilities, covering probability 
distributions, hypothesis testing, statistical inference, descriptive statistics,
and advanced statistical modeling for data science and research applications.

Author: Python Learning Notes
Date: September 2025
Topic: Statistical Analysis, Probability Distributions, Hypothesis Testing
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, t, chi2, f, binom, poisson, expon
import pandas as pd
from typing import Dict, List, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# STATISTICAL FOUNDATIONS AND PROBABILITY DISTRIBUTIONS
# =============================================================================

def statistics_fundamentals():
    """
    Complete introduction to statistical concepts and SciPy stats module
    """
    print("📊 SCIPY STATISTICS FUNDAMENTALS")
    print("=" * 34)
    
    print("🎯 Statistical Analysis Overview:")
    print("   Statistics is the science of collecting, analyzing, interpreting,")
    print("   and presenting data to make informed decisions under uncertainty.")
    
    print(f"\n📚 Types of Statistical Analysis:")
    analysis_types = [
        ("Descriptive", "Summarize and describe data", "Mean, median, std, percentiles"),
        ("Inferential", "Make conclusions about populations", "Hypothesis testing, confidence intervals"),
        ("Predictive", "Forecast future observations", "Regression, time series analysis"),
        ("Exploratory", "Discover patterns and relationships", "Correlation, visualization"),
        ("Confirmatory", "Test specific hypotheses", "Designed experiments, A/B testing")
    ]
    
    print("   ┌──────────────┬─────────────────────────────────┬──────────────────────────────────┐")
    print("   │ Type         │ Purpose                         │ Methods                          │")
    print("   ├──────────────┼─────────────────────────────────┼──────────────────────────────────┤")
    
    for analysis_type, purpose, methods in analysis_types:
        print(f"   │ {analysis_type:<12} │ {purpose:<31} │ {methods:<32} │")
    
    print("   └──────────────┴─────────────────────────────────┴──────────────────────────────────┘")
    
    print(f"\n🔢 SciPy Stats Module Capabilities:")
    capabilities = [
        "Continuous & discrete probability distributions (100+)",
        "Statistical hypothesis tests (t-tests, ANOVA, chi-square, etc.)",
        "Descriptive statistics and summary measures",
        "Correlation and regression analysis",
        "Non-parametric statistical tests",
        "Distribution fitting and goodness-of-fit tests",
        "Random variable generation and sampling",
        "Statistical functions and special distributions"
    ]
    
    for i, capability in enumerate(capabilities, 1):
        print(f"   {i}. {capability}")
    
    # Demonstrate random number generation
    print(f"\n🎲 Random Number Generation Example:")
    
    np.random.seed(42)
    
    # Generate samples from different distributions
    normal_samples = stats.norm.rvs(loc=50, scale=10, size=1000)
    uniform_samples = stats.uniform.rvs(loc=0, scale=1, size=1000)
    exponential_samples = stats.expon.rvs(scale=2, size=1000)
    
    print(f"   Normal(50, 10²):     mean={np.mean(normal_samples):.2f}, std={np.std(normal_samples):.2f}")
    print(f"   Uniform(0, 1):       mean={np.mean(uniform_samples):.2f}, std={np.std(uniform_samples):.2f}")
    print(f"   Exponential(λ=0.5):  mean={np.mean(exponential_samples):.2f}, std={np.std(exponential_samples):.2f}")

def probability_distributions_comprehensive():
    """
    Comprehensive exploration of probability distributions in SciPy
    """
    print("\n📈 PROBABILITY DISTRIBUTIONS COMPREHENSIVE")
    print("=" * 43)
    
    print("🎯 Distribution Categories:")
    
    # Continuous distributions
    continuous_dists = [
        ("Normal", "norm", "Bell curve, Central Limit Theorem", "μ, σ²"),
        ("Student's t", "t", "Small sample inference", "df"),
        ("Chi-square", "chi2", "Goodness of fit, variance tests", "df"),
        ("F-distribution", "f", "ANOVA, variance ratio tests", "dfn, dfd"),
        ("Exponential", "expon", "Waiting times, reliability", "λ"),
        ("Uniform", "uniform", "Equal probability over interval", "a, b"),
        ("Beta", "beta", "Bounded continuous, proportions", "α, β"),
        ("Gamma", "gamma", "Waiting times, Poisson process", "α, β")
    ]
    
    print(f"\n   📊 Continuous Distributions:")
    print("   Distribution    │ SciPy Name │ Applications                    │ Parameters")
    print("   ────────────────┼────────────┼─────────────────────────────────┼───────────")
    
    for name, scipy_name, application, params in continuous_dists:
        print(f"   {name:<15} │ {scipy_name:<10} │ {application:<31} │ {params}")
    
    # Discrete distributions
    discrete_dists = [
        ("Binomial", "binom", "Success/failure trials", "n, p"),
        ("Poisson", "poisson", "Count data, rare events", "λ"),
        ("Negative Binomial", "nbinom", "Overdispersed count data", "n, p"),
        ("Hypergeometric", "hypergeom", "Sampling without replacement", "M, n, N"),
        ("Geometric", "geom", "First success waiting time", "p")
    ]
    
    print(f"\n   🎲 Discrete Distributions:")
    print("   Distribution       │ SciPy Name │ Applications              │ Parameters")
    print("   ───────────────────┼────────────┼───────────────────────────┼───────────")
    
    for name, scipy_name, application, params in discrete_dists:
        print(f"   {name:<18} │ {scipy_name:<10} │ {application:<25} │ {params}")
    
    # Detailed examples for key distributions
    print(f"\n📊 Distribution Properties and Examples:")
    
    # Normal Distribution
    print(f"\n   🔔 Normal Distribution N(μ=100, σ²=15²):")
    mu, sigma = 100, 15
    norm_dist = stats.norm(loc=mu, scale=sigma)
    
    # Key properties
    print(f"      Mean: {norm_dist.mean():.1f}")
    print(f"      Variance: {norm_dist.var():.1f}")
    print(f"      Standard deviation: {norm_dist.std():.1f}")
    print(f"      68% interval: [{norm_dist.ppf(0.16):.1f}, {norm_dist.ppf(0.84):.1f}]")
    print(f"      95% interval: [{norm_dist.ppf(0.025):.1f}, {norm_dist.ppf(0.975):.1f}]")
    print(f"      P(X < 115): {norm_dist.cdf(115):.4f}")
    print(f"      P(X > 85): {1 - norm_dist.cdf(85):.4f}")
    
    # Binomial Distribution  
    print(f"\n   🎯 Binomial Distribution B(n=20, p=0.3):")
    n, p = 20, 0.3
    binom_dist = stats.binom(n=n, p=p)
    
    print(f"      Mean: {binom_dist.mean():.1f}")
    print(f"      Variance: {binom_dist.var():.1f}")
    print(f"      P(X = 6): {binom_dist.pmf(6):.4f}")
    print(f"      P(X ≤ 5): {binom_dist.cdf(5):.4f}")
    print(f"      P(X ≥ 8): {1 - binom_dist.cdf(7):.4f}")
    print(f"      95% interval: [{binom_dist.ppf(0.025):.0f}, {binom_dist.ppf(0.975):.0f}]")
    
    # Poisson Distribution
    print(f"\n   ⚡ Poisson Distribution Poisson(λ=4.5):")
    lam = 4.5
    poisson_dist = stats.poisson(mu=lam)
    
    print(f"      Mean: {poisson_dist.mean():.1f}")
    print(f"      Variance: {poisson_dist.var():.1f}")
    print(f"      P(X = 4): {poisson_dist.pmf(4):.4f}")
    print(f"      P(X ≤ 3): {poisson_dist.cdf(3):.4f}")
    print(f"      P(X ≥ 7): {1 - poisson_dist.cdf(6):.4f}")
    
    return {
        'normal_dist': norm_dist,
        'binomial_dist': binom_dist, 
        'poisson_dist': poisson_dist
    }

def descriptive_statistics_comprehensive():
    """
    Complete guide to descriptive statistics and data summarization
    """
    print("\n📈 DESCRIPTIVE STATISTICS COMPREHENSIVE")
    print("=" * 37)
    
    # Generate sample datasets
    np.random.seed(42)
    
    # Dataset 1: Normal distribution
    data_normal = stats.norm.rvs(loc=75, scale=12, size=200)
    
    # Dataset 2: Skewed distribution
    data_skewed = stats.gamma.rvs(a=2, scale=10, size=200)
    
    # Dataset 3: Bimodal distribution
    data_bimodal = np.concatenate([
        stats.norm.rvs(loc=40, scale=5, size=100),
        stats.norm.rvs(loc=80, scale=5, size=100)
    ])
    
    datasets = [
        ("Normal", data_normal, "Symmetric, bell-shaped"),
        ("Skewed", data_skewed, "Right-skewed, positive tail"),
        ("Bimodal", data_bimodal, "Two peaks, mixed population")
    ]
    
    print("📊 Comprehensive Descriptive Statistics:")
    print("   Measure         │ Normal    │ Skewed    │ Bimodal   │ Interpretation")
    print("   ────────────────┼───────────┼───────────┼───────────┼───────────────")
    
    measures = []
    for name, data, description in datasets:
        # Central tendency
        mean_val = np.mean(data)
        median_val = np.median(data)
        
        # Spread/variability
        std_val = np.std(data, ddof=1)
        var_val = np.var(data, ddof=1)
        range_val = np.ptp(data)
        iqr_val = stats.iqr(data)
        
        # Shape
        skewness = stats.skew(data)
        kurtosis = stats.kurtosis(data)
        
        # Percentiles
        q25 = np.percentile(data, 25)
        q75 = np.percentile(data, 75)
        
        measures.append({
            'name': name,
            'mean': mean_val,
            'median': median_val,
            'std': std_val,
            'skewness': skewness,
            'kurtosis': kurtosis,
            'iqr': iqr_val,
            'range': range_val
        })
    
    # Display key measures
    stats_to_show = [
        ('Mean', 'mean', 'Central value for symmetric distributions'),
        ('Median', 'median', 'Central value, robust to outliers'),
        ('Std Dev', 'std', 'Typical deviation from mean'),
        ('Skewness', 'skewness', 'Asymmetry: >0 right-skewed, <0 left-skewed'),
        ('Kurtosis', 'kurtosis', 'Tail heaviness: >0 heavy tails, <0 light tails'),
        ('IQR', 'iqr', 'Middle 50% spread, robust measure'),
        ('Range', 'range', 'Total spread, affected by outliers')
    ]
    
    for stat_name, key, interpretation in stats_to_show:
        values = [f"{m[key]:.2f}" for m in measures]
        print(f"   {stat_name:<15} │ {values[0]:>9} │ {values[1]:>9} │ {values[2]:>9} │ {interpretation}")
    
    # Advanced descriptive statistics
    print(f"\n🔍 Advanced Descriptive Analysis:")
    
    for i, (name, data, description) in enumerate(datasets):
        print(f"\n   📊 {name} Dataset ({description}):")
        
        # Five-number summary
        min_val, q25, median, q75, max_val = np.percentile(data, [0, 25, 50, 75, 100])
        print(f"      Five-number summary: [{min_val:.1f}, {q25:.1f}, {median:.1f}, {q75:.1f}, {max_val:.1f}]")
        
        # Coefficient of variation
        cv = (measures[i]['std'] / measures[i]['mean']) * 100
        print(f"      Coefficient of variation: {cv:.1f}%")
        
        # Outlier detection using IQR method
        iqr = q75 - q25
        lower_fence = q25 - 1.5 * iqr
        upper_fence = q75 + 1.5 * iqr
        outliers = data[(data < lower_fence) | (data > upper_fence)]
        print(f"      Outliers (IQR method): {len(outliers)} ({len(outliers)/len(data)*100:.1f}%)")
        
        # Mode (for demonstration, find approximate mode)
        hist, bin_edges = np.histogram(data, bins=20)
        mode_bin = np.argmax(hist)
        mode_approx = (bin_edges[mode_bin] + bin_edges[mode_bin + 1]) / 2
        print(f"      Approximate mode: {mode_approx:.1f}")
        
        # Normality tests
        shapiro_stat, shapiro_p = stats.shapiro(data)
        jarque_bera_stat, jarque_bera_p = stats.jarque_bera(data)
        
        print(f"      Normality tests:")
        print(f"        Shapiro-Wilk: W = {shapiro_stat:.4f}, p = {shapiro_p:.4f}")
        print(f"        Jarque-Bera:  JB = {jarque_bera_stat:.4f}, p = {jarque_bera_p:.4f}")
        print(f"        Normal? {'Yes' if shapiro_p > 0.05 else 'No'} (α = 0.05)")
    
    return {
        'datasets': dict(zip([d[0] for d in datasets], [d[1] for d in datasets])),
        'measures': measures
    }

# =============================================================================
# HYPOTHESIS TESTING AND STATISTICAL INFERENCE
# =============================================================================

def hypothesis_testing_comprehensive():
    """
    Complete guide to hypothesis testing and statistical inference
    """
    print("\n🧪 HYPOTHESIS TESTING COMPREHENSIVE")
    print("=" * 35)
    
    print("📋 Hypothesis Testing Framework:")
    print("   1. State null (H₀) and alternative (H₁) hypotheses")
    print("   2. Choose significance level (α, typically 0.05)")
    print("   3. Select appropriate test statistic")
    print("   4. Calculate test statistic and p-value")
    print("   5. Make decision: Reject H₀ if p < α")
    print("   6. Interpret results in context")
    
    # Generate sample data for demonstrations
    np.random.seed(42)
    
    # Example 1: One-sample t-test
    print(f"\n🎯 Example 1: One-Sample t-Test")
    print("   Question: Is the mean IQ of a sample significantly different from 100?")
    print("   H₀: μ = 100 vs H₁: μ ≠ 100")
    
    # Sample data: IQ scores
    iq_scores = stats.norm.rvs(loc=105, scale=15, size=25)  # True mean = 105
    
    # Perform one-sample t-test
    t_stat, p_value = stats.ttest_1samp(iq_scores, 100)
    
    print(f"   Sample: n = {len(iq_scores)}, mean = {np.mean(iq_scores):.2f}, std = {np.std(iq_scores, ddof=1):.2f}")
    print(f"   Test statistic: t = {t_stat:.3f}")
    print(f"   Degrees of freedom: df = {len(iq_scores) - 1}")
    print(f"   p-value: {p_value:.6f}")
    print(f"   Decision (α = 0.05): {'Reject H₀' if p_value < 0.05 else 'Fail to reject H₀'}")
    print(f"   Conclusion: The sample mean {'is' if p_value < 0.05 else 'is not'} significantly different from 100")
    
    # Effect size (Cohen's d)
    cohens_d = (np.mean(iq_scores) - 100) / np.std(iq_scores, ddof=1)
    print(f"   Effect size (Cohen's d): {cohens_d:.3f} ({'Small' if abs(cohens_d) < 0.5 else 'Medium' if abs(cohens_d) < 0.8 else 'Large'})")
    
    # Example 2: Two-sample t-test
    print(f"\n👥 Example 2: Independent Two-Sample t-Test")
    print("   Question: Do two groups have significantly different means?")
    print("   H₀: μ₁ = μ₂ vs H₁: μ₁ ≠ μ₂")
    
    # Two groups: Control vs Treatment
    control_group = stats.norm.rvs(loc=72, scale=12, size=30)
    treatment_group = stats.norm.rvs(loc=78, scale=10, size=35)
    
    # Independent t-test (assuming unequal variances)
    t_stat_2samp, p_value_2samp = stats.ttest_ind(control_group, treatment_group, equal_var=False)
    
    # Welch's t-test degrees of freedom
    s1_sq = np.var(control_group, ddof=1)
    s2_sq = np.var(treatment_group, ddof=1)
    n1, n2 = len(control_group), len(treatment_group)
    
    welch_df = (s1_sq/n1 + s2_sq/n2)**2 / ((s1_sq/n1)**2/(n1-1) + (s2_sq/n2)**2/(n2-1))
    
    print(f"   Control group:   n₁ = {n1}, mean = {np.mean(control_group):.2f}, std = {np.std(control_group, ddof=1):.2f}")
    print(f"   Treatment group: n₂ = {n2}, mean = {np.mean(treatment_group):.2f}, std = {np.std(treatment_group, ddof=1):.2f}")
    print(f"   Test statistic: t = {t_stat_2samp:.3f}")
    print(f"   Degrees of freedom (Welch): df = {welch_df:.1f}")
    print(f"   p-value: {p_value_2samp:.6f}")
    print(f"   Decision (α = 0.05): {'Reject H₀' if p_value_2samp < 0.05 else 'Fail to reject H₀'}")
    
    # Effect size (Cohen's d for two groups)
    pooled_std = np.sqrt(((n1-1)*s1_sq + (n2-1)*s2_sq) / (n1+n2-2))
    cohens_d_2samp = (np.mean(treatment_group) - np.mean(control_group)) / pooled_std
    print(f"   Effect size (Cohen's d): {cohens_d_2samp:.3f}")
    
    # Example 3: Paired t-test
    print(f"\n🔄 Example 3: Paired t-Test")
    print("   Question: Is there a significant change before vs after treatment?")
    print("   H₀: μd = 0 vs H₁: μd ≠ 0 (where d = after - before)")
    
    # Paired data: Before and after treatment
    before_scores = stats.norm.rvs(loc=65, scale=8, size=20)
    after_scores = before_scores + stats.norm.rvs(loc=5, scale=3, size=20)  # True improvement ~5 points
    
    # Paired t-test
    t_stat_paired, p_value_paired = stats.ttest_rel(after_scores, before_scores)
    
    differences = after_scores - before_scores
    
    print(f"   Sample size: n = {len(before_scores)}")
    print(f"   Before: mean = {np.mean(before_scores):.2f}, std = {np.std(before_scores, ddof=1):.2f}")
    print(f"   After:  mean = {np.mean(after_scores):.2f}, std = {np.std(after_scores, ddof=1):.2f}")
    print(f"   Differences: mean = {np.mean(differences):.2f}, std = {np.std(differences, ddof=1):.2f}")
    print(f"   Test statistic: t = {t_stat_paired:.3f}")
    print(f"   Degrees of freedom: df = {len(differences) - 1}")
    print(f"   p-value: {p_value_paired:.6f}")
    print(f"   Decision (α = 0.05): {'Reject H₀' if p_value_paired < 0.05 else 'Fail to reject H₀'}")
    
    # Example 4: Chi-square goodness of fit
    print(f"\n🎲 Example 4: Chi-Square Goodness of Fit Test")
    print("   Question: Does a die follow a uniform distribution?")
    print("   H₀: Die is fair (equal probabilities) vs H₁: Die is not fair")
    
    # Observed frequencies for each face (1-6)
    observed = np.array([18, 22, 16, 25, 22, 17])  # Total: 120 rolls
    expected = np.array([20, 20, 20, 20, 20, 20])  # Expected for fair die
    
    chi2_stat, p_value_chi2 = stats.chisquare(observed, expected)
    
    print(f"   Observed frequencies: {observed}")
    print(f"   Expected frequencies: {expected}")
    print(f"   Test statistic: χ² = {chi2_stat:.3f}")
    print(f"   Degrees of freedom: df = {len(observed) - 1}")
    print(f"   p-value: {p_value_chi2:.6f}")
    print(f"   Decision (α = 0.05): {'Reject H₀' if p_value_chi2 < 0.05 else 'Fail to reject H₀'}")
    
    # Example 5: Mann-Whitney U Test (Non-parametric)
    print(f"\n📊 Example 5: Mann-Whitney U Test (Non-parametric)")
    print("   Question: Do two groups have different distributions?")
    print("   H₀: Distributions are identical vs H₁: One tends to be larger")
    
    # Two groups with different distributions (not necessarily normal)
    group_a = stats.gamma.rvs(a=2, scale=3, size=25)
    group_b = stats.gamma.rvs(a=3, scale=2.5, size=30)
    
    # Mann-Whitney U test
    u_stat, p_value_u = stats.mannwhitneyu(group_a, group_b, alternative='two-sided')
    
    print(f"   Group A: n = {len(group_a)}, median = {np.median(group_a):.2f}")
    print(f"   Group B: n = {len(group_b)}, median = {np.median(group_b):.2f}")
    print(f"   Test statistic: U = {u_stat:.0f}")
    print(f"   p-value: {p_value_u:.6f}")
    print(f"   Decision (α = 0.05): {'Reject H₀' if p_value_u < 0.05 else 'Fail to reject H₀'}")
    
    return {
        'one_sample_t': (t_stat, p_value),
        'two_sample_t': (t_stat_2samp, p_value_2samp),
        'paired_t': (t_stat_paired, p_value_paired),
        'chi_square': (chi2_stat, p_value_chi2),
        'mann_whitney': (u_stat, p_value_u)
    }

def advanced_statistical_tests():
    """
    Advanced statistical tests and procedures
    """
    print("\n🚀 ADVANCED STATISTICAL TESTS")
    print("=" * 31)
    
    # Generate sample data
    np.random.seed(42)
    
    # Example 1: Analysis of Variance (ANOVA)
    print("📊 Example 1: One-Way ANOVA")
    print("   Question: Do multiple groups have equal means?")
    print("   H₀: μ₁ = μ₂ = μ₃ = μ₄ vs H₁: At least one mean differs")
    
    # Four treatment groups
    group1 = stats.norm.rvs(loc=75, scale=10, size=25)
    group2 = stats.norm.rvs(loc=80, scale=12, size=22)
    group3 = stats.norm.rvs(loc=78, scale=8, size=28)
    group4 = stats.norm.rvs(loc=82, scale=11, size=24)
    
    # One-way ANOVA
    f_stat, p_value_anova = stats.f_oneway(group1, group2, group3, group4)
    
    # Calculate additional statistics
    all_data = np.concatenate([group1, group2, group3, group4])
    group_means = [np.mean(g) for g in [group1, group2, group3, group4]]
    overall_mean = np.mean(all_data)
    
    print(f"   Group means: {[f'{m:.2f}' for m in group_means]}")
    print(f"   Overall mean: {overall_mean:.2f}")
    print(f"   F-statistic: F = {f_stat:.3f}")
    print(f"   p-value: {p_value_anova:.6f}")
    print(f"   Decision (α = 0.05): {'Reject H₀' if p_value_anova < 0.05 else 'Fail to reject H₀'}")
    
    # Effect size (eta-squared)
    k = 4  # number of groups
    n = len(all_data)
    eta_squared = (f_stat * (k-1)) / (f_stat * (k-1) + n - k)
    print(f"   Effect size (η²): {eta_squared:.4f}")
    
    # Example 2: Correlation Analysis
    print(f"\n🔗 Example 2: Correlation Analysis")
    print("   Question: Are two variables linearly related?")
    
    # Generate correlated data
    n_samples = 100
    true_correlation = 0.7
    
    # Create correlated variables
    x = stats.norm.rvs(loc=50, scale=15, size=n_samples)
    y = true_correlation * (x - 50) / 15 + stats.norm.rvs(loc=60, scale=10, size=n_samples)
    
    # Pearson correlation
    pearson_r, pearson_p = stats.pearsonr(x, y)
    
    # Spearman correlation (rank-based, non-parametric)
    spearman_rho, spearman_p = stats.spearmanr(x, y)
    
    # Kendall's tau (another rank-based correlation)
    kendall_tau, kendall_p = stats.kendalltau(x, y)
    
    print(f"   Sample size: n = {n_samples}")
    print(f"   True correlation: r = {true_correlation}")
    print(f"   Pearson correlation:  r = {pearson_r:.4f}, p = {pearson_p:.6f}")
    print(f"   Spearman correlation: ρ = {spearman_rho:.4f}, p = {spearman_p:.6f}")
    print(f"   Kendall's tau:        τ = {kendall_tau:.4f}, p = {kendall_p:.6f}")
    
    # Confidence interval for Pearson correlation
    # Using Fisher transformation
    fisher_z = np.arctanh(pearson_r)
    se_z = 1 / np.sqrt(n_samples - 3)
    z_critical = stats.norm.ppf(0.975)  # 95% CI
    
    ci_lower_z = fisher_z - z_critical * se_z
    ci_upper_z = fisher_z + z_critical * se_z
    
    ci_lower = np.tanh(ci_lower_z)
    ci_upper = np.tanh(ci_upper_z)
    
    print(f"   95% CI for Pearson r: [{ci_lower:.4f}, {ci_upper:.4f}]")
    
    # Example 3: Two-way Chi-square (Independence test)
    print(f"\n📋 Example 3: Chi-Square Test of Independence")
    print("   Question: Are two categorical variables independent?")
    
    # Contingency table: Education level vs Job satisfaction
    # Rows: Education (High School, College, Graduate)
    # Columns: Satisfaction (Low, Medium, High)
    
    contingency_table = np.array([
        [20, 30, 25],  # High School
        [15, 35, 40],  # College
        [10, 20, 45]   # Graduate
    ])
    
    # Chi-square test of independence
    chi2_indep, p_value_indep, dof, expected_freq = stats.chi2_contingency(contingency_table)
    
    print(f"   Contingency Table:")
    print(f"   Education   │ Low Sat │ Med Sat │ High Sat │ Total")
    print(f"   ────────────┼─────────┼─────────┼──────────┼──────")
    
    row_labels = ["High School", "College    ", "Graduate   "]
    for i, label in enumerate(row_labels):
        row_total = sum(contingency_table[i])
        print(f"   {label} │ {contingency_table[i][0]:7d} │ {contingency_table[i][1]:7d} │ {contingency_table[i][2]:8d} │ {row_total:5d}")
    
    col_totals = contingency_table.sum(axis=0)
    grand_total = contingency_table.sum()
    print(f"   ────────────┼─────────┼─────────┼──────────┼──────")
    print(f"   Total       │ {col_totals[0]:7d} │ {col_totals[1]:7d} │ {col_totals[2]:8d} │ {grand_total:5d}")
    
    print(f"\n   Test statistic: χ² = {chi2_indep:.3f}")
    print(f"   Degrees of freedom: df = {dof}")
    print(f"   p-value: {p_value_indep:.6f}")
    print(f"   Decision (α = 0.05): {'Reject H₀' if p_value_indep < 0.05 else 'Fail to reject H₀'}")
    
    # Cramér's V (effect size for chi-square)
    cramers_v = np.sqrt(chi2_indep / (grand_total * (min(contingency_table.shape) - 1)))
    print(f"   Effect size (Cramér's V): {cramers_v:.4f}")
    
    # Example 4: Normality Testing Battery
    print(f"\n📊 Example 4: Normality Testing Battery")
    print("   Question: Does the data follow a normal distribution?")
    
    # Test different distributions
    test_data = [
        ("Normal", stats.norm.rvs(loc=0, scale=1, size=100)),
        ("Uniform", stats.uniform.rvs(loc=-2, scale=4, size=100)),
        ("Skewed", stats.gamma.rvs(a=2, size=100))
    ]
    
    print(f"\n   Normality Test Results:")
    print("   Dataset   │ Shapiro-Wilk    │ D'Agostino      │ Anderson-Darling │ Conclusion")
    print("   ──────────┼─────────────────┼─────────────────┼──────────────────┼───────────")
    
    for name, data in test_data:
        # Shapiro-Wilk test
        shapiro_stat, shapiro_p = stats.shapiro(data)
        
        # D'Agostino's normality test (tests skewness and kurtosis)
        dagostino_stat, dagostino_p = stats.normaltest(data)
        
        # Anderson-Darling test
        ad_stat, ad_critical, ad_significance = stats.anderson(data, dist='norm')
        # Use 5% significance level (index 2 typically corresponds to 5%)
        ad_normal = ad_stat < ad_critical[2] if len(ad_critical) > 2 else ad_stat < ad_critical[-1]
        
        # Overall conclusion
        is_normal = (shapiro_p > 0.05 and dagostino_p > 0.05 and ad_normal)
        
        print(f"   {name:<9} │ {shapiro_stat:.3f} p={shapiro_p:.3f} │ {dagostino_stat:.3f} p={dagostino_p:.3f} │ {ad_stat:.3f}<{ad_critical[2] if len(ad_critical)>2 else ad_critical[-1]:.3f} │ {'Normal' if is_normal else 'Non-normal'}")
    
    return {
        'anova_result': (f_stat, p_value_anova),
        'correlation_results': {
            'pearson': (pearson_r, pearson_p),
            'spearman': (spearman_rho, spearman_p),
            'kendall': (kendall_tau, kendall_p)
        },
        'chi_square_independence': (chi2_indep, p_value_indep),
        'normality_tests': test_data
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive SciPy statistics guide
    """
    print(__doc__)
    
    # Fundamentals
    statistics_fundamentals()
    dist_info = probability_distributions_comprehensive()
    
    # Descriptive statistics
    desc_results = descriptive_statistics_comprehensive()
    
    # Hypothesis testing
    test_results = hypothesis_testing_comprehensive()
    
    # Advanced tests
    advanced_results = advanced_statistical_tests()
    
    return {
        'distributions': dist_info,
        'descriptive_stats': desc_results,
        'hypothesis_tests': test_results,
        'advanced_tests': advanced_results
    }

if __name__ == "__main__":
    """
    Execute comprehensive SciPy statistics guide and demonstrations
    """
    results = main()
    
    print("\n" + "=" * 60)
    print("🎓 SCIPY STATISTICS MASTERY SUMMARY")
    print("=" * 60)
    print("✅ Complete statistical foundations and probability theory")
    print("✅ Comprehensive probability distributions (continuous & discrete)")
    print("✅ Advanced descriptive statistics and data summarization")
    print("✅ Complete hypothesis testing framework and procedures")
    print("✅ One-sample, two-sample, and paired t-tests")
    print("✅ Chi-square tests (goodness of fit & independence)")
    print("✅ Non-parametric tests (Mann-Whitney, Wilcoxon)")
    print("✅ Analysis of Variance (ANOVA)")
    print("✅ Correlation analysis (Pearson, Spearman, Kendall)")
    print("✅ Normality testing and distribution fitting")
    print("✅ Effect sizes and statistical power")
    
    print("\n💡 SciPy Statistics Mastery Key Points:")
    key_points = [
        "Choose appropriate tests based on data type and assumptions",
        "Always check assumptions before applying parametric tests",
        "Interpret p-values correctly and consider practical significance",
        "Report effect sizes along with statistical significance",
        "Use non-parametric tests when assumptions are violated",
        "Understand the difference between correlation and causation",
        "Apply multiple comparison corrections when appropriate",
        "Validate results with confidence intervals and power analysis"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Statistical Analysis Applications:")
    applications = [
        "A/B testing and experimental design",
        "Quality control and process monitoring",
        "Medical and clinical research studies",
        "Market research and customer analytics",
        "Scientific research and hypothesis testing",
        "Risk assessment and reliability analysis",
        "Data science and machine learning preprocessing",
        "Business intelligence and decision making"
    ]
    
    for i, app in enumerate(applications, 1):
        print(f"   {i}. {app}")
    
    print(f"\n🚀 Ready for Advanced Statistical Analysis!")
    print("Master the science of data-driven decision making with SciPy!")