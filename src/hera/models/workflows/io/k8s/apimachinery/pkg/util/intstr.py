# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/argoproj/argo-workflows/master/api/openapi-spec/swagger.json
#   timestamp: 2022-12-29T22:26:11+00:00

from __future__ import annotations

from typing import Annotated

from hera import ArgoBaseModel


class IntOrString(ArgoBaseModel):
    __root__: str