# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Kendra"
prefix = "kendra"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchDeleteDocument = Action("BatchDeleteDocument")
BatchPutDocument = Action("BatchPutDocument")
CreateDataSource = Action("CreateDataSource")
CreateFaq = Action("CreateFaq")
CreateIndex = Action("CreateIndex")
CreateThesaurus = Action("CreateThesaurus")
DeleteDataSource = Action("DeleteDataSource")
DeleteFaq = Action("DeleteFaq")
DeleteIndex = Action("DeleteIndex")
DeleteThesaurus = Action("DeleteThesaurus")
DescribeDataSource = Action("DescribeDataSource")
DescribeFaq = Action("DescribeFaq")
DescribeIndex = Action("DescribeIndex")
DescribeThesaurus = Action("DescribeThesaurus")
ListDataSourceSyncJobs = Action("ListDataSourceSyncJobs")
ListDataSources = Action("ListDataSources")
ListFaqs = Action("ListFaqs")
ListIndices = Action("ListIndices")
ListTagsForResource = Action("ListTagsForResource")
ListThesauri = Action("ListThesauri")
Query = Action("Query")
StartDataSourceSyncJob = Action("StartDataSourceSyncJob")
StopDataSourceSyncJob = Action("StopDataSourceSyncJob")
SubmitFeedback = Action("SubmitFeedback")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataSource = Action("UpdateDataSource")
UpdateIndex = Action("UpdateIndex")
UpdateThesaurus = Action("UpdateThesaurus")
