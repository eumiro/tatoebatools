import logging

from .config import DATA_DIR
from .datafile import DataFile
from .exceptions import NoDataFile
from .utils import lazy_property
from .version import version

logger = logging.getLogger(__name__)


class Links:
    """The links between the Tatoeba sentences of a pair of languages.  
    """

    _table = "links"
    _dir = DATA_DIR.joinpath(_table)

    def __init__(self, source_language, target_language):
        # the source language of the links
        self._src_lg = source_language
        # the target language of the links
        self._tgt_lg = target_language

    def __iter__(self):

        fieldnames = ["sentence_id", "translation_id"]

        try:
            for row in DataFile(self.path, delimiter="\t", text_col=None):
                row = {fieldnames[i]: x for i, x in enumerate(row)}
                yield Link(**row)
        except NoDataFile:
            msg = (
                f"no data locally available for the '{Links._table}' "
                f"table from {self._src_lg} to {self._tgt_lg}."
            )

            logger.warning(msg)

    @property
    def source_language(self):
        """Get the source language of these links.
        """
        return self._src_lg

    @property
    def target_language(self):
        """Get the target language of these links.
        """
        return self._tgt_lg

    @property
    def filename(self):
        """Get the name of the file where the links for this language
        pair are saved.
        """
        return f"{self._src_lg}-{self._tgt_lg}_{Links._table}.tsv"

    @property
    def path(self):
        """Get the path where the links are saved for this language pair.
        """
        return Links._dir.joinpath(self.filename)

    @lazy_property
    def ids(self):
        """Get all sentences' and translations' ids.
        """
        source_ids = set()
        target_ids = set()
        for link in self:
            source_ids.add(link.sentence_id)
            target_ids.add(link.translation_id)

        return source_ids, target_ids

    @lazy_property
    def version(self):
        """Get the version of the downloaded data of these links.
        """
        return version[Links._table]


class Link:
    """A link between a Tatoeba's sentence and its translation.
    """

    def __init__(self, sentence_id, translation_id):

        self._src_id = sentence_id
        self._tgt_id = translation_id

    @property
    def sentence_id(self):
        """The id of the source sentence.
        """
        return int(self._src_id)

    @property
    def translation_id(self):
        """The id of the target sentence.
        """
        return int(self._tgt_id)
