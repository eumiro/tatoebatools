from pathlib import Path

from pkg_resources import resource_filename

DATA_DIR = Path(resource_filename(__package__, "data"))

SUPPORTED_TABLES = (
    "sentences_detailed",
    "sentences_CC0",
    "transcriptions",
    "links",
    "tags",
    "user_lists",
    "sentences_in_lists",
    "jpn_indices",
    "sentences_with_audio",
    "user_languages",
    "queries",
)

INDEX_SPLIT_TABLES = (
    "links",
    "tags",
    "sentences_in_lists",
    "jpn_indices",
    "sentences_with_audio",
)
SIMPLE_SPLIT_TABLES = (
    "user_languages",
    "queries",
)
