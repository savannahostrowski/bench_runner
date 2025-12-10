from __future__ import annotations


import dataclasses
import hashlib
from pathlib import Path


from . import git


@dataclasses.dataclass
class BenchmarkRepo:
    hash: str
    url: str
    dirname: str


BENCHMARK_REPOS = [
    BenchmarkRepo(
        "cdbf33bca8216d4636322a7637917a03b0fba945",
        "https://github.com/python/pyperformance.git",
        "pyperformance",
    ),
    BenchmarkRepo(
        "265655e7f03ace13ec1e00e1ba299179e69f8a00",
        "https://github.com/pyston/python-macrobenchmarks.git",
        "pyston-benchmarks",
    ),
]


def get_benchmark_hash() -> str:
    hash = hashlib.sha256()
    for repo in BENCHMARK_REPOS:
        if Path(repo.dirname).is_dir():
            current_hash = git.get_git_hash(Path(repo.dirname))
        else:
            current_hash = repo.hash
        hash.update(current_hash.encode("ascii")[:7])
    return hash.hexdigest()[:6]
