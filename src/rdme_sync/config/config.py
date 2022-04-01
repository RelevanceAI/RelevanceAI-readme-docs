#!/usr/bin/env python3

from typing import Dict, List
from abc import abstractmethod, ABC


class Config(ABC):
    def __init__(
        self,
        fpath: str = None,
        version: str = None,
        *args,
        **kwargs,
    ):
        self.version = f"v{version}" if version[0] != "v" else version
        self.fpath = fpath

    @abstractmethod
    def build(
        self, *args, fpath: str = None, select_fields: List[str] = None, **kwargs
    ) -> Dict:
        """Builds readme config dict and outputs to readme-config file

        Parameters
        ----------
        fpath : Config filepath
            Overrides instance fpath if set
        condensed: bool
            If True, builds a condensed version of the readme-config file as well
        select_fields : List[str]
            select_fields: List
            Fields to include in the search results, empty array/list means all fields

        """
        return NotImplementedError
