# AI Assistance

AI assistance was sought throughout the assignment process as a tool for comprehending the assignment itself, planning experiments, debugging, interpreting results, and preparing the final documentation.

## AI Assistance Use Cases

AI was mainly used for:

- Understanding the technical concepts required for each part of the assignment before starting the corresponding experiments, so that the  experiments and their results could be interpreted correctly.
- Comprehending the assignment requirements and splitting the assignment into smaller experiments.
- Discussing different hypotheses and figuring out which measurements were necessary.
- Elucidating technical notions like tokenizer fertility, grapheme clusters, KV-cache memory, throughput, and serving behavior.
- Coming up with possible commands, calculations, and experiments that could be done locally.
- Fixing the implementation issues and interpreting the errors.
- Interpreting the experiment outputs and determining if the obtained result corroborated the hypothesis.
- Helping in structuring `NOTEBOOK.md`, `part-A/A4_memo.md`, and `part-C/memo.md`.
- Formulating possible questions and counterfactuals for the final defense.

## Human Verification and Execution

Experiments were conducted locally via the given files and experiment scripts from the repository.

Results obtained in the notebook were verified against the actual experiment outputs. Screenshot/log files were used as evidence rather than relying on AI-given values for verification.

Therefore, the AI recommendations were regarded as hypotheses or possible solutions, not experimental outcomes. The results came after the experiments had been conducted and the output observed.

## Example of Using AI for Troubleshooting

While comparing tokenizers, the first attempt to use an Indic tokenizer failed due to it being gated on Hugging Face repository. The AI pointed out the reason behind the issue and proposed an alternative publicly available multilingual/Indic tokenizer. It was installed and tested locally prior to conducting the experiment.

## Use of AI in Interpretation

AI was utilized in interpreting the following observations:

- The impact of `split(" ")` function on the computation of fertility.
- The difference between the number of Unicode code points and grapheme clusters.
- The significant difference in Indic tokens counts between GPT-2 and MuRIL.
- The connection between the use of KV-cache, preempted sequence, and throughput problem.
- The disparity between reported token throughput and goodput generated tokens.

These interpretations were made based on the measurements that were derived from the experiments and benchmark/model information provided.

## Limitations

Use of AI was employed to quicken the process of reasoning and documentation but was not taken to be an alternative to conducting experiments and verification of claims. In a case where an AI suggestion contradicted an observation from an experiment, the local experimental observation was considered.

The final conclusions and recommendations were made according to the available evidence from the experiments and limitations of the assignment.