from typing import Dict, Any

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.aggs import Agg
from elasticsearch_dsl.query import Query
from elasticsearch_dsl.response import Response


class ElasticsearchService:

    def __init__(self,
                 host: str,
                 index: str) -> None:
        self.index = index
        self._es = Elasticsearch(hosts=[host])

    def execute_query(self,
                      query: Query,
                      offset: int = 0,
                      size: int = 1000) -> Response:
        search_request = Search().query(query)[offset: offset + size]
        return search_request.index(self.index).using(self._es).execute()

    def index_document(self, document: Dict[str, Any]) -> None:
        self._es.index(
            index=self.index,
            document=document
        )

    def execute_query_with_bucketing(self,
                                     query: Query,
                                     bucket_name: str,
                                     aggs: Agg,
                                     offset: int = 0,
                                     size: int = 10000) -> Response:
        search_request = Search().query(query)[offset: offset + size]
        search_request.aggs.bucket(bucket_name, aggs)
        return search_request.using(self._es).execute()

    def execute_query_with_source(self,
                                  query: Query,
                                  offset: int = 0,
                                  size: int = 1000) -> Response:
        search_request = Search().query(query)[offset: offset + size]
        return search_request.index(self.index).using(self._es).execute()
