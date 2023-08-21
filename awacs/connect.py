# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect"
prefix = "connect"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateEvaluationForm = Action("ActivateEvaluationForm")
AssociateApprovedOrigin = Action("AssociateApprovedOrigin")
AssociateBot = Action("AssociateBot")
AssociateCustomerProfilesDomain = Action("AssociateCustomerProfilesDomain")
AssociateDefaultVocabulary = Action("AssociateDefaultVocabulary")
AssociateInstanceStorageConfig = Action("AssociateInstanceStorageConfig")
AssociateLambdaFunction = Action("AssociateLambdaFunction")
AssociateLexBot = Action("AssociateLexBot")
AssociatePhoneNumberContactFlow = Action("AssociatePhoneNumberContactFlow")
AssociateQueueQuickConnects = Action("AssociateQueueQuickConnects")
AssociateRoutingProfileQueues = Action("AssociateRoutingProfileQueues")
AssociateSecurityKey = Action("AssociateSecurityKey")
AssociateTrafficDistributionGroupUser = Action("AssociateTrafficDistributionGroupUser")
BatchAssociateAnalyticsDataSet = Action("BatchAssociateAnalyticsDataSet")
BatchDisassociateAnalyticsDataSet = Action("BatchDisassociateAnalyticsDataSet")
ClaimPhoneNumber = Action("ClaimPhoneNumber")
CreateAgentStatus = Action("CreateAgentStatus")
CreateContactFlow = Action("CreateContactFlow")
CreateContactFlowModule = Action("CreateContactFlowModule")
CreateEvaluationForm = Action("CreateEvaluationForm")
CreateHoursOfOperation = Action("CreateHoursOfOperation")
CreateInstance = Action("CreateInstance")
CreateIntegrationAssociation = Action("CreateIntegrationAssociation")
CreateParticipant = Action("CreateParticipant")
CreatePrompt = Action("CreatePrompt")
CreateQueue = Action("CreateQueue")
CreateQuickConnect = Action("CreateQuickConnect")
CreateRoutingProfile = Action("CreateRoutingProfile")
CreateRule = Action("CreateRule")
CreateSecurityProfile = Action("CreateSecurityProfile")
CreateTaskTemplate = Action("CreateTaskTemplate")
CreateTrafficDistributionGroup = Action("CreateTrafficDistributionGroup")
CreateUseCase = Action("CreateUseCase")
CreateUser = Action("CreateUser")
CreateUserHierarchyGroup = Action("CreateUserHierarchyGroup")
CreateVocabulary = Action("CreateVocabulary")
DeactivateEvaluationForm = Action("DeactivateEvaluationForm")
DeleteContactEvaluation = Action("DeleteContactEvaluation")
DeleteContactFlow = Action("DeleteContactFlow")
DeleteContactFlowModule = Action("DeleteContactFlowModule")
DeleteEvaluationForm = Action("DeleteEvaluationForm")
DeleteHoursOfOperation = Action("DeleteHoursOfOperation")
DeleteInstance = Action("DeleteInstance")
DeleteIntegrationAssociation = Action("DeleteIntegrationAssociation")
DeletePrompt = Action("DeletePrompt")
DeleteQueue = Action("DeleteQueue")
DeleteQuickConnect = Action("DeleteQuickConnect")
DeleteRoutingProfile = Action("DeleteRoutingProfile")
DeleteRule = Action("DeleteRule")
DeleteSecurityProfile = Action("DeleteSecurityProfile")
DeleteTaskTemplate = Action("DeleteTaskTemplate")
DeleteTrafficDistributionGroup = Action("DeleteTrafficDistributionGroup")
DeleteUseCase = Action("DeleteUseCase")
DeleteUser = Action("DeleteUser")
DeleteUserHierarchyGroup = Action("DeleteUserHierarchyGroup")
DeleteVocabulary = Action("DeleteVocabulary")
DescribeAgentStatus = Action("DescribeAgentStatus")
DescribeContact = Action("DescribeContact")
DescribeContactEvaluation = Action("DescribeContactEvaluation")
DescribeContactFlow = Action("DescribeContactFlow")
DescribeContactFlowModule = Action("DescribeContactFlowModule")
DescribeEvaluationForm = Action("DescribeEvaluationForm")
DescribeForecastingPlanningSchedulingIntegration = Action(
    "DescribeForecastingPlanningSchedulingIntegration"
)
DescribeHoursOfOperation = Action("DescribeHoursOfOperation")
DescribeInstance = Action("DescribeInstance")
DescribeInstanceAttribute = Action("DescribeInstanceAttribute")
DescribeInstanceStorageConfig = Action("DescribeInstanceStorageConfig")
DescribePhoneNumber = Action("DescribePhoneNumber")
DescribePrompt = Action("DescribePrompt")
DescribeQueue = Action("DescribeQueue")
DescribeQuickConnect = Action("DescribeQuickConnect")
DescribeRoutingProfile = Action("DescribeRoutingProfile")
DescribeRule = Action("DescribeRule")
DescribeSecurityProfile = Action("DescribeSecurityProfile")
DescribeTrafficDistributionGroup = Action("DescribeTrafficDistributionGroup")
DescribeUser = Action("DescribeUser")
DescribeUserHierarchyGroup = Action("DescribeUserHierarchyGroup")
DescribeUserHierarchyStructure = Action("DescribeUserHierarchyStructure")
DescribeVocabulary = Action("DescribeVocabulary")
DestroyInstance = Action("DestroyInstance")
DisassociateApprovedOrigin = Action("DisassociateApprovedOrigin")
DisassociateBot = Action("DisassociateBot")
DisassociateCustomerProfilesDomain = Action("DisassociateCustomerProfilesDomain")
DisassociateInstanceStorageConfig = Action("DisassociateInstanceStorageConfig")
DisassociateLambdaFunction = Action("DisassociateLambdaFunction")
DisassociateLexBot = Action("DisassociateLexBot")
DisassociatePhoneNumberContactFlow = Action("DisassociatePhoneNumberContactFlow")
DisassociateQueueQuickConnects = Action("DisassociateQueueQuickConnects")
DisassociateRoutingProfileQueues = Action("DisassociateRoutingProfileQueues")
DisassociateSecurityKey = Action("DisassociateSecurityKey")
DisassociateTrafficDistributionGroupUser = Action(
    "DisassociateTrafficDistributionGroupUser"
)
DismissUserContact = Action("DismissUserContact")
GetContactAttributes = Action("GetContactAttributes")
GetCurrentMetricData = Action("GetCurrentMetricData")
GetCurrentUserData = Action("GetCurrentUserData")
GetFederationToken = Action("GetFederationToken")
GetFederationTokens = Action("GetFederationTokens")
GetMetricData = Action("GetMetricData")
GetMetricDataV2 = Action("GetMetricDataV2")
GetPromptFile = Action("GetPromptFile")
GetTaskTemplate = Action("GetTaskTemplate")
GetTrafficDistribution = Action("GetTrafficDistribution")
ListAgentStatuses = Action("ListAgentStatuses")
ListApprovedOrigins = Action("ListApprovedOrigins")
ListBots = Action("ListBots")
ListContactEvaluations = Action("ListContactEvaluations")
ListContactFlowModules = Action("ListContactFlowModules")
ListContactFlows = Action("ListContactFlows")
ListContactReferences = Action("ListContactReferences")
ListDefaultVocabularies = Action("ListDefaultVocabularies")
ListEvaluationFormVersions = Action("ListEvaluationFormVersions")
ListEvaluationForms = Action("ListEvaluationForms")
ListHoursOfOperations = Action("ListHoursOfOperations")
ListInstanceAttributes = Action("ListInstanceAttributes")
ListInstanceStorageConfigs = Action("ListInstanceStorageConfigs")
ListInstances = Action("ListInstances")
ListIntegrationAssociations = Action("ListIntegrationAssociations")
ListLambdaFunctions = Action("ListLambdaFunctions")
ListLexBots = Action("ListLexBots")
ListPhoneNumbers = Action("ListPhoneNumbers")
ListPhoneNumbersV2 = Action("ListPhoneNumbersV2")
ListPrompts = Action("ListPrompts")
ListQueueQuickConnects = Action("ListQueueQuickConnects")
ListQueues = Action("ListQueues")
ListQuickConnects = Action("ListQuickConnects")
ListRealtimeContactAnalysisSegments = Action("ListRealtimeContactAnalysisSegments")
ListRoutingProfileQueues = Action("ListRoutingProfileQueues")
ListRoutingProfiles = Action("ListRoutingProfiles")
ListRule = Action("ListRule")
ListRules = Action("ListRules")
ListSecurityKeys = Action("ListSecurityKeys")
ListSecurityProfilePermissions = Action("ListSecurityProfilePermissions")
ListSecurityProfiles = Action("ListSecurityProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListTaskTemplates = Action("ListTaskTemplates")
ListTrafficDistributionGroupUsers = Action("ListTrafficDistributionGroupUsers")
ListTrafficDistributionGroups = Action("ListTrafficDistributionGroups")
ListUseCases = Action("ListUseCases")
ListUserHierarchyGroups = Action("ListUserHierarchyGroups")
ListUsers = Action("ListUsers")
ModifyInstance = Action("ModifyInstance")
MonitorContact = Action("MonitorContact")
PutUserStatus = Action("PutUserStatus")
ReleasePhoneNumber = Action("ReleasePhoneNumber")
ReplicateInstance = Action("ReplicateInstance")
ResumeContactRecording = Action("ResumeContactRecording")
SearchAvailablePhoneNumbers = Action("SearchAvailablePhoneNumbers")
SearchHoursOfOperations = Action("SearchHoursOfOperations")
SearchPrompts = Action("SearchPrompts")
SearchQueues = Action("SearchQueues")
SearchQuickConnects = Action("SearchQuickConnects")
SearchResourceTags = Action("SearchResourceTags")
SearchRoutingProfiles = Action("SearchRoutingProfiles")
SearchSecurityProfiles = Action("SearchSecurityProfiles")
SearchUsers = Action("SearchUsers")
SearchVocabularies = Action("SearchVocabularies")
StartChatContact = Action("StartChatContact")
StartContactEvaluation = Action("StartContactEvaluation")
StartContactRecording = Action("StartContactRecording")
StartContactStreaming = Action("StartContactStreaming")
StartForecastingPlanningSchedulingIntegration = Action(
    "StartForecastingPlanningSchedulingIntegration"
)
StartOutboundVoiceContact = Action("StartOutboundVoiceContact")
StartTaskContact = Action("StartTaskContact")
StopContact = Action("StopContact")
StopContactRecording = Action("StopContactRecording")
StopContactStreaming = Action("StopContactStreaming")
StopForecastingPlanningSchedulingIntegration = Action(
    "StopForecastingPlanningSchedulingIntegration"
)
SubmitContactEvaluation = Action("SubmitContactEvaluation")
SuspendContactRecording = Action("SuspendContactRecording")
TagResource = Action("TagResource")
TransferContact = Action("TransferContact")
UntagResource = Action("UntagResource")
UpdateAgentStatus = Action("UpdateAgentStatus")
UpdateContact = Action("UpdateContact")
UpdateContactAttributes = Action("UpdateContactAttributes")
UpdateContactEvaluation = Action("UpdateContactEvaluation")
UpdateContactFlowContent = Action("UpdateContactFlowContent")
UpdateContactFlowMetadata = Action("UpdateContactFlowMetadata")
UpdateContactFlowModuleContent = Action("UpdateContactFlowModuleContent")
UpdateContactFlowModuleMetadata = Action("UpdateContactFlowModuleMetadata")
UpdateContactFlowName = Action("UpdateContactFlowName")
UpdateContactSchedule = Action("UpdateContactSchedule")
UpdateEvaluationForm = Action("UpdateEvaluationForm")
UpdateHoursOfOperation = Action("UpdateHoursOfOperation")
UpdateInstanceAttribute = Action("UpdateInstanceAttribute")
UpdateInstanceStorageConfig = Action("UpdateInstanceStorageConfig")
UpdateParticipantRoleConfig = Action("UpdateParticipantRoleConfig")
UpdatePhoneNumber = Action("UpdatePhoneNumber")
UpdatePrompt = Action("UpdatePrompt")
UpdateQueueHoursOfOperation = Action("UpdateQueueHoursOfOperation")
UpdateQueueMaxContacts = Action("UpdateQueueMaxContacts")
UpdateQueueName = Action("UpdateQueueName")
UpdateQueueOutboundCallerConfig = Action("UpdateQueueOutboundCallerConfig")
UpdateQueueStatus = Action("UpdateQueueStatus")
UpdateQuickConnectConfig = Action("UpdateQuickConnectConfig")
UpdateQuickConnectName = Action("UpdateQuickConnectName")
UpdateRoutingProfileAgentAvailabilityTimer = Action(
    "UpdateRoutingProfileAgentAvailabilityTimer"
)
UpdateRoutingProfileConcurrency = Action("UpdateRoutingProfileConcurrency")
UpdateRoutingProfileDefaultOutboundQueue = Action(
    "UpdateRoutingProfileDefaultOutboundQueue"
)
UpdateRoutingProfileName = Action("UpdateRoutingProfileName")
UpdateRoutingProfileQueues = Action("UpdateRoutingProfileQueues")
UpdateRule = Action("UpdateRule")
UpdateSecurityProfile = Action("UpdateSecurityProfile")
UpdateTaskTemplate = Action("UpdateTaskTemplate")
UpdateTrafficDistribution = Action("UpdateTrafficDistribution")
UpdateUserHierarchy = Action("UpdateUserHierarchy")
UpdateUserHierarchyGroupName = Action("UpdateUserHierarchyGroupName")
UpdateUserHierarchyStructure = Action("UpdateUserHierarchyStructure")
UpdateUserIdentityInfo = Action("UpdateUserIdentityInfo")
UpdateUserPhoneConfig = Action("UpdateUserPhoneConfig")
UpdateUserRoutingProfile = Action("UpdateUserRoutingProfile")
UpdateUserSecurityProfiles = Action("UpdateUserSecurityProfiles")
UpdatedescribeContent = Action("UpdatedescribeContent")
