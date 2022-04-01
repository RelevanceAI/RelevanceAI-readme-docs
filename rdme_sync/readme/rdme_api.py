#!/usr/bin/env python3

from typing import Dict, List, Union
import requests
import os
import json


class ReadMeAPI:
    def __init__(self, readme_version: str = None):
        if not readme_version:
            raise ValueError(
                f"Readme version is required. Please specify a version. eg. 'v2.0.0'"
            )

        self.base_url = "https://dash.readme.com/api/v1/"
        self.session = requests.Session()
        self.readme_version = readme_version

        self.readme_api_key = self._check_env_var_exist("RELEVANCEAI_README_API_KEY")
        self.headers = {
            "x-readme-version": readme_version,
            "Authorization": f"Basic {self.readme_api_key}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _check_env_var_exist(env_var: str):
        try:
            return os.environ[env_var]
        except KeyError as e:
            raise KeyError(f"{env_var} environment variable is not set")

    @staticmethod
    def _validate_response(request_params: Dict, response: requests.Response):
        if response.status_code < 200 or response.status_code > 299:
            raise Exception(
                f"Request failed with status code {response.status_code}\n. {json.dumps(request_params)}"
            )
        return response

    @staticmethod
    def _validate_select_fields(select_fields: List[str], available_fields: List[str]):
        """Validates the select_fields parameter.

        Parameters
        ----------
        select_fields : List[str]
            Select Fields to include in the search results, empty array/list means all fields
        available_fields : List[str]
            Available fields in the search results

        Returns
        -------
        select_fields : List[str]
            Select Fields to include in the search results, empty array/list means all fields

        Raises
        ------
        ValueError
            If select_fields contains a field that is not available in the search results
        """
        for f in select_fields:
            if f not in available_fields:
                raise ValueError(f"{f} is not a valid field. \n{available_fields}")
        return select_fields

    def _request(
        self,
        method: Union["POST", "GET"],
        request_url,
        params: Dict = {},
        payload: Dict = {},
        select_fields: List[str] = None,
    ):
        """
        Returns reponse from the API.

        Parameters
        ----------
        method: str
            POST or GET
        request_url:
            URL to send the request to
        params: Dict
            Parameters to send with the request
        payload: Dict
            Payload to send with the request
        select_fields: List
            Fields to include in the search results, empty array/list means all fields

        Returns
        -------
        result: Dict
            Dict of results
        """
        request_params = {
            "method": method,
            "url": request_url,
            "params": params,
            "json": payload,
            "headers": self.headers,
        }
        response = self._validate_response(
            request_params, self.session.request(**request_params)
        )
        result = json.loads(response.text)

        if select_fields:
            available_fields = (
                result[0].keys() if isinstance(result, list) else result.keys()
            )
            result = result if isinstance(result, list) else [result]
            select_fields = self._validate_select_fields(
                select_fields=select_fields, available_fields=available_fields
            )

            select_result = []
            for r in result:
                select_result.append({s: r[s] for s in select_fields})
            return select_result
        else:
            return result

    def get_categories(
        self,
        params: Dict = {"perPage": 100, "page": 1},
        select_fields: List[str] = None,
    ):
        """
        Returns all the categories for a specified version.

        Parameters
        ----------
        params: Dict
            perPage: int
                Number of items to include in pagination (up to 100, defaults to 10)
            page: int
                Used to specify further pages (starts at 1)
        select_fields: List
            Fields to include in the search results, empty array/list means all fields
        """
        request_url = f"{self.base_url}/categories"
        return self._request(
            "GET", request_url, params=params, select_fields=select_fields
        )

    def get_docs_for_category(
        self, category_slug: str, select_fields: List[str] = None
    ):
        """
        Returns the docs and children docs within this category.

        Parameters
        ----------
        category_slug: str
            A URL-safe representation of the category title.
            Slugs must be all lowercase, and replace spaces with hyphens.
            For example, for the the category "Getting Started", enter the slug "getting-started"
        select_fields: List
            Fields to include in the search results, empty array/list means all fields

        """
        request_url = f"{self.base_url}/categories/{category_slug}/docs"
        return self._request("GET", request_url, select_fields=select_fields)

    def get_doc(self, page_slug: str, select_fields: List[str] = None):
        """
        Returns the doc with a given page slug.

        Parameters
        ----------
        page_slug: str
            A URL-safe representation of the doc title.
            Slugs must be all lowercase, and replace spaces with hyphens.
            For example, for the the doc "New Features", enter the slug "new-features"
        select_fields: List
            Fields to include in the search results, empty array/list means all fields
        """
        request_url = f"{self.base_url}/docs/{page_slug}"
        return self._request("GET", request_url, select_fields=select_fields)

    def create_doc(
        self,
        title: str,
        type: Union["basic", "link", "error"],
        category_id: str,
        parent_doc_id: str = None,
        body: str = "",
        hidden: bool = True,
        order: int = 999,
        error_code: Dict = None,
    ):
        """
        Returns the doc with this slug.

        Parameters
        ----------
        title: str
            A URL-safe representation of the doc title.
            Slugs must be all lowercase, and replace spaces with hyphens.
            For example, for the the doc "New Features", enter the slug "new-features"
        type: str
            Type of the page. The available types all show up under the /docs/ URL path of your docs project.
            Can be "basic" (most common), "error" (page desribing an API error), or "link" (page that redirects to an external link).
        category_id: str
            Category ID of the page
        parent_doc_id: str
            Id of the parent doc. If you don't want to have a parent doc, leave this blank.
        body: str
            Body content of the page, formatted in ReadMe or GitHub flavored Markdown. Accepts long page content, for example, greater than 100k characters.
        hidden: bool
            Whether or not the doc should be hidden in Readme.
        order: int
            The position of the page in your project sidebar.
        error_code: dict
            code: str
            The error code for docs with the "error" type

        """
        request_url = f"{self.base_url}/docs"
        payload = {
            "title": title,
            "type": type,
            "category": category_id,
            "body": body,
            "hidden": hidden,
            "order": order,
            "parentDoc": parent_doc_id,
        }

        if type == "error":
            if not error_code:
                error_code={"code": "404"}
            payload["error"] = error_code

        return self._request("POST", request_url, payload=payload)
