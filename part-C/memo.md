# Part C – Casualization Strategy Memo

## Decision

First, use a prompt-only solution as the starting point on Day-1. If it does not reach the required quality bar, evaluate SFT as an alternative approach. Consider using a ≤1B rewriter only if SFT fails to offer a better quality/price/latency trade-off.

## Assumptions

- Target languages: Hindi, Kannada, Tamil, Telugu, Bengali, and Marathi.
- Availability of one reviewer for 10 hours/week who can review in Hindi and Kannada.
- Time taken per review is 2 minutes per example.
- For SFT preparation, consider 1,000 synthetic examples (formal-to-casual pair per language). This is a planning assumption, not data requirement.
- An approach is considered successful if ≥80% of reviewed outputs have desired casual tone and ≥95% retain the original meaning.

## Back-of-the-Envelope Calculations

Reviewer throughput:

    10 hours/week × 60 = 600 minutes/week

    600 / 2 = 300 evaluations/week

In 3 weeks:

    300 × 3 = 900 evaluations

The planned initial day-1 evaluation of 50 Hindi and 50 Kannada examples, i.e., 100 examples:

    100 × 2 = 200 minutes
    = 3.3 reviewer-hours

For SFT, the planning data set size is:

    1,000 pairs/language × 6 languages
    = 6,000 synthetic pairs

The training compute available is 1×A100-80GB for 2 weeks. It is impossible to calculate the exact dollar training cost from the available information because the cloud pricing or the throughput per unit time is not available. For the ≤1B rewriter, an inference step will be involved, thereby adding to the serving compute latency. Prompt only adds no cost for model training.

## Option Comparison

| Approach | Cost/effort | Key advantage | Key disadvantage |
|---|---|---|---|
| Prompt-only | Lowest | Instant and no new model | Does not necessarily address the style issue |
| ≤1B rewriter | Medium | Main model stays the same | Additional latency/processing and meaning modifications |
| SFT | Highest | Modification of the main model behavior | Data requirement, training and evaluation |

## Day-1 Experiment

Generate 100 cases for evaluation: 50 Hindi and 50 Kannada.

For each case, compare the output of the baseline with prompt-only casual version. If there is a rewriter or SFT pilot, then use the same set of cases for their comparison.

The evaluator evaluates:

1. The ability of the output to be in the required casual style.
2. Whether the original meaning was kept.

The first and main success criterion is at least 80% pass rate on the style and 95% pass rate on meaning preservation.

## Kill Criterion

If an approach fails one of the thresholds above in the Day-1 experiment, do not waste the remaining compute budget on scaling the approach. Try another approach instead.

## Recommendation

Prompt-only should be tried first since it does not incur extra training or serving costs.

If prompt-only fails to meet the quality requirements, SFT pilot would be the way forward since it involves modifying the behavior of the original assistant rather than introducing another inference step, which might be sub-optimal. The ≤1B rewriter would be the other choice as long as the quality, preservation, latency, and serving costs measure up to the SFT choice.

One concern to note is that the reviewer only covers Hindi and Kannada; thus, any quality claims on the four other languages need verification before launch.