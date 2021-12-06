# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Personalize"
prefix = "personalize"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateBatchInferenceJob = Action("CreateBatchInferenceJob")
CreateBatchSegmentJob = Action("CreateBatchSegmentJob")
CreateCampaign = Action("CreateCampaign")
CreateDataset = Action("CreateDataset")
CreateDatasetExportJob = Action("CreateDatasetExportJob")
CreateDatasetGroup = Action("CreateDatasetGroup")
CreateDatasetImportJob = Action("CreateDatasetImportJob")
CreateEventTracker = Action("CreateEventTracker")
CreateFilter = Action("CreateFilter")
CreateRecommender = Action("CreateRecommender")
CreateSchema = Action("CreateSchema")
CreateSolution = Action("CreateSolution")
CreateSolutionVersion = Action("CreateSolutionVersion")
DeleteCampaign = Action("DeleteCampaign")
DeleteDataset = Action("DeleteDataset")
DeleteDatasetGroup = Action("DeleteDatasetGroup")
DeleteEventTracker = Action("DeleteEventTracker")
DeleteFilter = Action("DeleteFilter")
DeleteRecommender = Action("DeleteRecommender")
DeleteSchema = Action("DeleteSchema")
DeleteSolution = Action("DeleteSolution")
DescribeAlgorithm = Action("DescribeAlgorithm")
DescribeBatchInferenceJob = Action("DescribeBatchInferenceJob")
DescribeBatchSegmentJob = Action("DescribeBatchSegmentJob")
DescribeCampaign = Action("DescribeCampaign")
DescribeDataset = Action("DescribeDataset")
DescribeDatasetExportJob = Action("DescribeDatasetExportJob")
DescribeDatasetGroup = Action("DescribeDatasetGroup")
DescribeDatasetImportJob = Action("DescribeDatasetImportJob")
DescribeEventTracker = Action("DescribeEventTracker")
DescribeFeatureTransformation = Action("DescribeFeatureTransformation")
DescribeFilter = Action("DescribeFilter")
DescribeRecipe = Action("DescribeRecipe")
DescribeRecommender = Action("DescribeRecommender")
DescribeSchema = Action("DescribeSchema")
DescribeSolution = Action("DescribeSolution")
DescribeSolutionVersion = Action("DescribeSolutionVersion")
GetPersonalizedRanking = Action("GetPersonalizedRanking")
GetRecommendations = Action("GetRecommendations")
GetSolutionMetrics = Action("GetSolutionMetrics")
ListBatchInferenceJobs = Action("ListBatchInferenceJobs")
ListBatchSegmentJobs = Action("ListBatchSegmentJobs")
ListCampaigns = Action("ListCampaigns")
ListDatasetExportJobs = Action("ListDatasetExportJobs")
ListDatasetGroups = Action("ListDatasetGroups")
ListDatasetImportJobs = Action("ListDatasetImportJobs")
ListDatasets = Action("ListDatasets")
ListEventTrackers = Action("ListEventTrackers")
ListFilters = Action("ListFilters")
ListRecipes = Action("ListRecipes")
ListRecommenders = Action("ListRecommenders")
ListSchemas = Action("ListSchemas")
ListSolutionVersions = Action("ListSolutionVersions")
ListSolutions = Action("ListSolutions")
PutEvents = Action("PutEvents")
PutItems = Action("PutItems")
PutUsers = Action("PutUsers")
StopSolutionVersionCreation = Action("StopSolutionVersionCreation")
UpdateCampaign = Action("UpdateCampaign")
UpdateRecommender = Action("UpdateRecommender")
