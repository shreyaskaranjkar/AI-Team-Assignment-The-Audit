# A4 – Routing and Cost Memo

## Correction to Findings

The comparison of tokenizers has been conducted on the same 997 parallel sentences for English, Hindi, Kannada, and Tamil.

| Language | GPT-2 tokens/sentence | MuRIL tokens/sentence | Token savings using MuRIL |
|---|---:|---:|---:|
| English | 25.82 | 26.44 | -2.42% |
| Hindi | 192.18 | 30.82 | 83.96% |
| Kannada | 351.07 | 28.06 | 92.01% |
| Tamil | 398.36 | 27.88 | 93.00% |

For the English language, GPT-2 and MuRIL have almost the same tokenization. Yet, GPT-2 provides a much higher number of tokens for Hindi, Kannada, and Tamil languages. MuRIL cuts down the number of tokens by 84% for Hindi and 92–93% for Kannada and Tamil.

It can be seen that the same pattern emerges while analyzing tokens per word and tokens per grapheme.

## Routing Recommendation

With regards to multilingual serving, language routing can take into account the tokenizer and model being used for each language.

For Hindi, Kannada, and Tamil language serving, it is recommended to use an Indic-aware multilingual model like MuRIL rather than GPT-2 provided that all other considerations are the same. This is since the token difference between MuRIL and GPT-2 for Indic languages is relatively high, while for English it is minimal.

The single metric that should be used for routing and cost estimation is the **number of tokens the tokenizer of the serving model generates**. The word and grapheme-based metrics are helpful in analysis, however, they do not constitute the units of measurement consumed by the model.

## Biggest Caveat

Token reduction does not directly translate to equivalent reduction in serving cost and latency. In fact, there are a number of factors involved in serving cost, including the model architecture, sequence length, batching, and hardware configuration.

Also, FLORES-200 development data is another benchmark corpus created from web articles, therefore its tokenization results might differ for other genres such as chat, programming, etc.

## Suggested Production Metric

One suggested production metric is:

**p95 number of tokens per request based on the deployed model’s tokenizer, per language.**

This is a direct measure of the factor that determines sequence length and the work load on inference and can be individually tracked for each routed language.