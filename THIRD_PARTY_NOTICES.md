# Third-Party Materials

This teaching repository contains or derives from the following third-party materials.
These notices do not grant a license to original course materials.

## GPT-2

The tokenizer, model architecture, and initial model weights are based on
[OpenAI GPT-2](https://github.com/openai/gpt-2). The upstream GPT-2 repository
is distributed under its [Modified MIT License](https://github.com/openai/gpt-2/blob/master/LICENSE).
The checkpoint in this repository is a course-specific fine-tune and is provided
for this membership-inference exercise.

## WikiText-103

The course checkpoint and test examples derive from the `wikitext-103-raw-v1`
configuration of [Salesforce WikiText](https://huggingface.co/datasets/Salesforce/wikitext).
The upstream dataset card lists Creative Commons Attribution-ShareAlike and GFDL
license metadata. Consult the upstream dataset card for the applicable terms.

When describing the dataset in a report, cite:

> Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher.
> "Pointer Sentinel Mixture Models." arXiv:1609.07843, 2016.

## Python Dependencies

Python dependencies are installed from their upstream distributions and remain
subject to their respective licenses. See `requirements.txt` and
`requirements-cuda.txt` for the exact packages used by this project.
