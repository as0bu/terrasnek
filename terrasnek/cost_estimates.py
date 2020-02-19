"""
Module for Terraform Cloud API Endpoint: Cost Estimates.
"""

from .endpoint import TFCEndpoint


class TFCCostEstimates(TFCEndpoint):
    """
    A cost estimate represents an estimation of the dollar cost
    of the infrastructure being provisioned in a run in a Terraform
    workspace.

    https://www.terraform.io/docs/cloud/api/cost-estimates.html
    """

    def __init__(self, base_url, organization_name, headers):
        super().__init__(base_url, organization_name, headers)
        self._base_url = f"{base_url}/cost-estimates"

    def show(self, cost_estimate_id):
        """
        GET /cost-estimates/:cost_estimate_id
        """
        url = f"{self._base_url}/{cost_estimate_id}"
        return self._show(url)
