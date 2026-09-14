# Membership Inference Attack Competition: Phase 1

Starter kit for the CMU 18-734/17-731 course project. In this warm-up phase,
teams implement and evaluate a membership inference attack (MIA) against a
fine-tuned GPT-2 language model.

## What Is Included

- `MIA_phase1.ipynb`: data loading, model loading, evaluation, and ROC plotting.
- `models/gpt2_phase1/`: fine-tuned GPT-2 checkpoint and tokenizer files.
- `data/wiki_json/test.json`: 2,000 test texts.
- `data/wiki_json/test_label.json`: 2,000 Phase 1 labels, balanced between 1,000
  members and 1,000 non-members.
- `scripts/verify_model.py`: offline checkpoint integrity check.

The notebook intentionally leaves `your_attack` unfinished. That function is the
student implementation for this phase.

## Requirements

- Python 3.11
- Git LFS
- At least 8 GB of system memory recommended
- An NVIDIA GPU or Google Colab GPU runtime is recommended; CPU is also supported

The checkpoint is approximately 475 MiB. A full evaluation of all 2,000 examples
typically takes several minutes on a recent laptop CPU and longer on older
hardware. Use a small subset while developing and evaluate the complete set for
the report. A GPU is preferable when available but is not required.

## Local Setup

Clone the repository with Git LFS enabled:

```bash
git lfs install
git clone https://github.com/CMU-18734-17731-2026-Fall/Project-phase-1.git
cd Project-phase-1
git lfs pull
```

Create the supported Python environment and install the portable dependencies:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1` instead.

Verify the downloaded model before opening the notebook:

```bash
python scripts/verify_model.py
```

Expected final line:

```text
Model checkpoint verification: PASS
```

Then launch the starter kit:

```bash
jupyter notebook MIA_phase1.ipynb
```

Run the notebook from the repository root. It selects the available accelerator
and prints the selected device.

## Optional NVIDIA/CUDA Packages

The core requirements already install PyTorch and are sufficient for the
assignment. On a Linux x86-64 machine with a compatible NVIDIA driver, optional
acceleration packages can be installed with:

```bash
python -m pip install -r requirements-cuda.txt
```

Only use this file on a Linux x86-64 machine with a compatible NVIDIA driver.
CUDA availability depends on the PyTorch build and driver; consult the
[PyTorch installation selector](https://pytorch.org/get-started/locally/) if the
notebook reports `cpu` unexpectedly on an NVIDIA host.

## Google Colab

Start from a blank Colab notebook and run the following setup cells before
opening or uploading `MIA_phase1.ipynb`:

```python
!git lfs install
!git clone https://github.com/CMU-18734-17731-2026-Fall/Project-phase-1.git
%cd Project-phase-1
!git lfs pull
!python scripts/verify_model.py
%pip install -r requirements.txt
```

Restart the Colab runtime after installation if prompted. The starter notebook
does not clone, delete, or download files itself.

## Assignment

Implement at least one of the following attacks:

1. **Loss-based attack:** derive a membership score from token or sequence loss.
2. **Min-K attack:** implement a score based on the least-likely tokens, following
   the [Min-K% Prob paper](https://arxiv.org/abs/2310.16789).
3. **Zlib attack:** calibrate model loss using the compressed byte length from
   Python's [`zlib`](https://docs.python.org/3/library/zlib.html), for example
   `score(x) = loss(x) / zlib_size(x)`.

Phase 1 labels are available for evaluating and tuning the attack. Do not pass
labels into the attack itself.

## Deliverable

Each group submits one report to Gradescope and adds every team member to that
submission. The report contains:

- **Methodology:** one or two paragraphs describing the algorithm and any formula.
- **Results:** AUC, TPR at 0.01 FPR, TPR at 0.05 FPR, the ROC curve, and a short
  discussion of relevant hyperparameters.
- **Appendix:** the implemented attack code.

Only one attack is required. Additional attacks are optional and may be useful in
later project phases. The notebook itself does not need to be submitted unless
course staff announce otherwise.

## Reproducibility

The starter notebook uses random seed `42` and pinned versions for the model and
analysis libraries. Keep the full 2,000-example dataset and the provided labels
unchanged when producing final metrics. Notebook outputs and local environments
should not be committed.

## Troubleshooting

**The checkpoint is only 134 bytes.** This is the Git LFS pointer. Install Git
LFS, run `git lfs pull`, and rerun `python scripts/verify_model.py`.

**The process runs out of memory.** Lower `batch_size` in the notebook. This makes
evaluation slower but should not change per-example scores for a deterministic
attack.

**Jupyter cannot find the packages.** Activate `.venv` before launching Jupyter,
or select the `.venv` Python 3.11 kernel from the notebook interface.

**No GPU is detected.** CPU execution still works, although evaluation will take
longer. In Colab, select a GPU under the runtime hardware settings. On an NVIDIA
machine, confirm that `python -c "import torch; print(torch.cuda.is_available())"`
prints `True`.

## Attribution

The model is based on OpenAI GPT-2, and the fine-tuning/test text derives from
WikiText-103. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for citations
and upstream terms.
