# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/argoproj/argo-workflows/master/api/openapi-spec/swagger.json
#   timestamp: 2022-12-31T17:02:53+00:00

from __future__ import annotations

from typing import List, Optional

from hera import BaseModel

from ...google import protobuf


class Error(BaseModel):
    code: Optional[int] = None
    details: Optional[List[protobuf.Any]] = None
    error: Optional[str] = None
    message: Optional[str] = None


class StreamError(BaseModel):
    details: Optional[List[protobuf.Any]] = None
    grpc_code: Optional[int] = None
    http_code: Optional[int] = None
    http_status: Optional[str] = None
    message: Optional[str] = None