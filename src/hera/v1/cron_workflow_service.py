"""Holds the cron workflow service that supports client cron workflow creations"""
from typing import Tuple

from argo_workflows.apis import CronWorkflowServiceApi
from argo_workflows.models import (
    IoArgoprojWorkflowV1alpha1CreateCronWorkflowRequest,
    IoArgoprojWorkflowV1alpha1CronWorkflow,
    IoArgoprojWorkflowV1alpha1CronWorkflowResumeRequest,
    IoArgoprojWorkflowV1alpha1CronWorkflowSuspendRequest,
)

from hera.v1.client import Client
from hera.v1.config import Config


class CronWorkflowService:
    """Argo cron workflow service for performing actions against cron workflows - creations, deletions, etc.

    Parameters
    ----------
    domain: str
        The Argo deployment domain to create cron workflows in.
    token: str
        The token to use for authentication purposes. Note that this assumes the Argo deployment is fronted with a
        deployment/service that can intercept a request and check the Bearer token.
    namespace: str = 'default'
        The K8S namespace the cron workflow service creates cron workflows in.
        This defaults to the `default` namespace.
    """

    def __init__(self, domain: str, token: str, namespace: str = 'default'):
        self._domain = domain
        self._namespace = namespace
        api_client = Client(Config(domain), token).api_client
        self.service = CronWorkflowServiceApi(api_client=api_client)

    def create(
        self, cron_workflow: IoArgoprojWorkflowV1alpha1CronWorkflow, namespace: str = 'default'
    ) -> IoArgoprojWorkflowV1alpha1CronWorkflow:
        """Creates given cron workflow in the argo server.

        Parameters
        ----------
        cron_workflow: V1alpha1CronWorkflow
            The cron workflow to create.
        namespace: str = 'default'
            The K8S namespace of the Argo server to create the cron workflow in.

        Returns
        -------
        IoArgoprojWorkflowV1alpha1CronWorkflow - created workflow.

        Raises
        ------
        argo_workflows.exceptions.ApiException: Raised upon any HTTP-related errors.
        """
        return self.service.create_cron_workflow(
            namespace,
            IoArgoprojWorkflowV1alpha1CreateCronWorkflowRequest(cron_workflow=cron_workflow, namespace=namespace),
            _check_return_type=False,
        )

    def delete(self, name: str, namespace: str = 'default') -> Tuple[object, int, dict]:
        """Deletes a cron workflow from the given namespace based on the specified name.

        Parameters
        ----------
        name: str
            The name of the cron workflow to delete.
        namespace: str = 'default'
            The K8S namespace of the Argo server to delete the cron workflow from.

        Returns
        -------
            Tuple(object, status_code(int), headers(HTTPHeaderDict))

        Raises
        ------
        argo_workflows.exceptions.ApiException: Raised upon any HTTP-related errors.
        """
        return self.service.delete_cron_workflow(namespace, name, _check_return_type=False)

    def suspend(self, name: str, namespace: str = 'default') -> Tuple[object, int, dict]:
        """Suspends a cron workflow from the given namespace based on the specified name.

        Parameters
        ----------
        name: optional str
            The name of the cron workflow to suspend.
        namespace: str = 'default'
            The K8S namespace of the Argo server to suspend the cron workflow on.

        Returns
        -------
            Tuple(object, status_code(int), headers(HTTPHeaderDict))

        Raises
        ------
        argo_workflows.exceptions.ApiException: Raised upon any HTTP-related errors.
        """
        return self.service.suspend_cron_workflow(
            namespace,
            name,
            IoArgoprojWorkflowV1alpha1CronWorkflowSuspendRequest(name=name, namespace=namespace),
            _check_return_type=False,
        )

    def resume(self, name: str, namespace: str = 'default') -> Tuple[object, int, dict]:
        """Resumes execution of a cron workflow from the given namespace based on the specified name.

        Parameters
        ----------
        name: optional str
            The name of the cron workflow to resume.
        namespace: str = 'default'
            The K8S namespace of the Argo server to resume the cron workflow on.

        Returns
        -------
            Tuple(object, status_code(int), headers(HTTPHeaderDict))

        Raises
        ------
        argo_workflows.exceptions.ApiException: Raised upon any HTTP-related errors.
        """
        return self.service.resume_cron_workflow(
            namespace, name, body=IoArgoprojWorkflowV1alpha1CronWorkflowResumeRequest(name=name, namespace=namespace)
        )

    def get_cron_workflow_link(self, name: str, namespace: str = 'default') -> str:
        """Assembles a cron workflow link for the given cron workflow name.

        Parameters
        ----------
        name: optional str
            The name of the cron workflow to assemble a link for.
        namespace: str = 'default'
            The K8S namespace of the Argo server to get the cron workflow link from.

        Returns
        -------
        str
            The cron workflow link.

        Notes
        -----
        The returned path works only for Argo.
        """
        return f'https://{self._domain}/cron-workflows/{namespace}/{name}'