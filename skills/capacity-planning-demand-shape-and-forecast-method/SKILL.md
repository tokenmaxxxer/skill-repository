---
name: capacity-planning-demand-shape-and-forecast-method
description: Use when classifying a resource's demand shape (organic vs. inorganic) and choosing a forecast method — regression trend, scenario/step model, Holt-Winters, ARIMA/SARIMA, or a hybrid — and reporting or reconciling that forecast against actuals.
metadata:
  axis: demand-shape-and-forecast-method
  rule_count_floor: 8
---

# Demand shape classification and forecast-method selection

Research trail: Google SRE literature on organic/inorganic demand (USENIX ;login: Winter 2020, "SRE Best Practices for Capacity Management", Torres et al.), Holt-Winters vs. ARIMA comparative forecasting studies (ScienceDirect 2024 supply-chain comparison; food-retail Holt-Winters/ARIMA comparison), and general demand-forecasting method literature. All fetched/searched this session.

## Trigger

Apply this skill when classifying a resource's demand as organic or
inorganic, choosing between a trend fit, a scenario/step model,
Holt-Winters/SARIMA, or ARIMA, setting the forecast horizon, or
reconciling a new forecast against what actually happened since the
last one.

## Procedure

1. Classify a slow, monotonic, attribution-free increase as organic
   demand and fit a regression trend line (rule 1).
2. Classify a usage increase traceable to a specific planned action as
   inorganic demand and model it as a scenario/step forecast keyed to
   the event (rule 2).
3. Fit Holt-Winters (or SARIMA/ARIMA with a seasonal term) when the
   series shows a calendar-locked repeating pattern (rule 3).
4. Prefer ARIMA over Holt-Winters when the forecast horizon is short
   relative to history and the series is not strongly trending
   (rule 4).
5. When ARIMA/SARIMA is used on a series with a real trend component,
   pair the fit with an explicit trend term rather than trusting the
   raw fit (rule 5).
6. Extend the forecast horizon beyond the lead time needed to acquire
   the capacity (rule 6).
7. When organic and inorganic demand both apply inside the horizon,
   forecast each component separately and sum them (rule 7).
8. Never silently overwrite a prior forecast; diff the new forecast
   against what actually happened and flag persistent divergence
   (rule 8).
9. For a genuinely organic series, drop seasonal machinery rather than
   applying it out of habit (rule 9).
10. Report fitted components (trend rate, seasonal amplitude, event
    term) separately so a forecast-vs-actual divergence can be
    attributed to the specific component that moved (rule 10).

## Output shape

A forecast classified by demand shape (organic, inorganic, or both
summed separately), fit with the method matched to that shape and
horizon, extended past the capacity acquisition lead time, with its
components reported separately and diffed against prior actuals.

## Rules

1. When a resource's usage trend is a slow, roughly monotonic increase tied to natural product adoption (more users, more accounts, more stored data) with no single attributable event driving it, classify it as organic demand and fit a linear or exponential regression trend line to the historical series rather than a seasonal or event model — organic growth has no periodic or step-function component for a seasonal/scenario model to capture. source: https://sre.google/static/pdf/login_winter20_10_torres.pdf

2. When a usage increase is traceable to a specific planned business action (a marketing campaign, a feature launch, an acquisition, a partner integration going live), classify it as inorganic demand and model it as a scenario/step-function forecast keyed to the event's launch date and expected magnitude, not as an extrapolation of the pre-event trend line — extrapolating pre-event history under-forecasts because the event itself, not organic growth, is the demand driver. source: https://sre.google/static/pdf/login_winter20_10_torres.pdf

3. When the demand series shows a repeating pattern locked to calendar structure (daily/weekly cycles, holiday peaks, a recurring sales campaign), fit Holt-Winters exponential smoothing (or SARIMA/ARIMA with a seasonal term) rather than a bare linear trend — a comparative study found Holt-Winters captured the linear/seasonal behavior of the series better on inventory-optimization data, while plain trend fits ignore the periodic component entirely and systematically mis-time the peak. source: https://www.sciencedirect.com/science/article/pii/S294986352400027X

4. When the forecast horizon is short relative to the series' history (near-term, few-period-ahead forecasting) and the series is not strongly trending, prefer ARIMA over Holt-Winters — ARIMA is suitable for short-term forecasting because it prioritizes closer time-series data, while multi-season smoothing models need a longer history to estimate seasonal components reliably. source: https://www.researchgate.net/publication/286314562_Demand_forecasting_in_food_retail_A_comparison_between_the_Holt-Winters_and_ARIMA_models

5. When ARIMA/SARIMA is the chosen method but the underlying series has a real trend component (not just seasonality plus noise), do not trust the raw ARIMA/SARIMA fit unchecked — published comparisons note ARIMA/SARIMA models "usually do not take into account trend fluctuations in the data," so pair the fit with an explicit trend term (SARIMAX with a trend regressor, or a hybrid Holt-Winters/ARIMA) rather than assuming seasonality alone explains the residual growth. source: https://www.sciencedirect.com/science/article/pii/S294986352400027X

6. When building any demand forecast for a capacity decision, always extend the forecast horizon beyond the lead time required to acquire the capacity (hardware order time, quota approval time, provisioning time) — a forecast that only covers what's already knowable inside the lead-time window arrives too late to act on, which is the specific failure mode Google's capacity-management practice calls out as a required property of "an accurate organic demand forecast." source: https://sre.google/static/pdf/login_winter20_10_torres.pdf

7. When a resource is driven by both organic growth and one or more known inorganic events inside the same forecast horizon, forecast the two components separately (trend-fit the organic base, scenario-model each inorganic event) and sum them, rather than fitting one combined model to the blended history — a single model averages the event's step change into the trend slope, which both understates future organic growth in campaign-heavy periods and mis-shapes the event's own step. source: https://sre.google/static/pdf/login_winter20_10_torres.pdf

8. **REMOVAL**: When a prior forecast exists for the same subject/resource and a new forecast is being produced, do not silently overwrite the old number — drop the practice of replacing forecast values with no forecast-vs-actual comparison recorded, and instead diff the new forecast against what actually happened since the last one; a persistent divergence is a model-instability signal (wrong method, mis-classified demand shape, or a missed inorganic event) that must be flagged, not buried under the newer number. source: https://sre.google/static/pdf/login_winter20_10_torres.pdf

9. **REMOVAL**: When a demand series is genuinely organic (steady, no calendar periodicity, no scheduled events), drop Holt-Winters/ARIMA seasonal machinery from the forecast entirely rather than defaulting to it out of habit — fitting seasonal terms to a non-seasonal series adds parameters that fit noise, and a plain regression trend is both simpler and, per the comparative literature, not dominated by the seasonal models outside their actual seasonal use case. source: https://www.sciencedirect.com/science/article/pii/S294986352400027X

10. When a chosen method fits more than one component into the demand series (a trend plus a seasonal/holiday/campaign term), report the fitted components separately — trend growth rate, seasonal amplitude, and any event/holiday term each stated on their own — rather than a single blended growth number; an additive decomposition lets the forecast-vs-actual comparison (rule 8) attribute a divergence to the specific component that moved (trend accelerated vs. a seasonal peak mis-timed) instead of forcing a re-fit of the whole model to locate it.
