<h1 align="center">German Massive Text Embedding Benchmark</h1>

<p align="center">
    <a href="https://github.com/mbeddings-benchmark/mteb/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/embeddings-benchmark/mteb.svg">
    </a>
    <a href="https://arxiv.org/abs/2210.07316">
        <img alt="GitHub release" src="https://img.shields.io/badge/arXiv-2305.14251-b31b1b.svg">
    </a>
    <a href="https://www.python.org/">
            <img alt="Build" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?color=purple">
    </a>
    <a href="https://github.com/embeddings-benchmark/mteb/blob/master/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/embeddings-benchmark/mteb.svg?color=green">
    </a>
    <a href="https://pepy.tech/project/mteb">
        <img alt="Downloads" src="https://static.pepy.tech/personalized-badge/mteb?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads">
    </a>
</p>

<h4 align="center">
    <p>
        <a href="https://arxiv.org/abs/2210.07316">Paper</a> |
        <a href=#leaderboard>Leaderboard</a> |
        <a href="#installation">Installation</a> |
        <a href="#usage">Usage</a> |
        <a href="#available-tasks">Tasks</a> |
        <a href="https://huggingface.co/mteb">Hugging Face</a>
    <p>
</h4>

<h3 align="center">
    <a href="https://huggingface.co/"><img style="float: middle; padding: 10px 10px 10px 10px;" width="60" height="55" src="./images/hf_logo.png" /></a>
</h3>

This is a fork of the [Massive Text Embedding Benchmark](http://github.com/embeddings-benchmark/mteb), adding several German tasks.

Namely:

| Name               | Type               | Description                                                                                                                               |
|--------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| MIRACL             | Reranking          | Multilingual retrieval dataset that focuses on search across 18 different languages                                                       |
| GermanDPR          | Retrieval          | GermanDPR is a German Question Answering dataset for open-domain QA. It associates questions with a textual context containing the answer |
| PawsX              | PairClassification | Human-translated PAWS pairs (paraphrase identification)                                                                                   |
| GermanSTSBenchmark | STS                | Machine-translation of STSBenchmark                                                                                                       |
| XMarket            | Retrieval          | XMarket is an ecommerce category to product retrieval dataset in German                                                                   |                                                    
| GerDaLir           | Retrieval          | GerDaLIR is a legal information retrieval dataset created from the Open Legal Data platform                                               |

## Installation

```bash
pip install git+https://github.com/jina-ai/mteb-de
```

## Usage
To reproduce evaluation results for multilingual E5 and two additional German embedding models, run the following script:

```bash
python scripts.run_mteb_german.py
```

## Citation

If you find MTEB useful, feel free to cite the original publication [MTEB: Massive Text Embedding Benchmark](https://arxiv.org/abs/2210.07316):

```bibtex
@article{muennighoff2022mteb,
  doi = {10.48550/ARXIV.2210.07316},
  url = {https://arxiv.org/abs/2210.07316},
  author = {Muennighoff, Niklas and Tazi, Nouamane and Magne, Lo{\"\i}c and Reimers, Nils},
  title = {MTEB: Massive Text Embedding Benchmark},
  publisher = {arXiv},
  journal={arXiv preprint arXiv:2210.07316},  
  year = {2022}
}
```
