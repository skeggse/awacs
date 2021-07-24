# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Lightsail"
prefix = "lightsail"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AllocateStaticIp = Action("AllocateStaticIp")
AttachCertificateToDistribution = Action("AttachCertificateToDistribution")
AttachDisk = Action("AttachDisk")
AttachInstancesToLoadBalancer = Action("AttachInstancesToLoadBalancer")
AttachLoadBalancerTlsCertificate = Action("AttachLoadBalancerTlsCertificate")
AttachStaticIp = Action("AttachStaticIp")
CloseInstancePublicPorts = Action("CloseInstancePublicPorts")
CopySnapshot = Action("CopySnapshot")
CreateBucket = Action("CreateBucket")
CreateBucketAccessKey = Action("CreateBucketAccessKey")
CreateCertificate = Action("CreateCertificate")
CreateCloudFormationStack = Action("CreateCloudFormationStack")
CreateContactMethod = Action("CreateContactMethod")
CreateContainerService = Action("CreateContainerService")
CreateContainerServiceDeployment = Action("CreateContainerServiceDeployment")
CreateContainerServiceRegistryLogin = Action("CreateContainerServiceRegistryLogin")
CreateDisk = Action("CreateDisk")
CreateDiskFromSnapshot = Action("CreateDiskFromSnapshot")
CreateDiskSnapshot = Action("CreateDiskSnapshot")
CreateDistribution = Action("CreateDistribution")
CreateDomain = Action("CreateDomain")
CreateDomainEntry = Action("CreateDomainEntry")
CreateInstanceSnapshot = Action("CreateInstanceSnapshot")
CreateInstances = Action("CreateInstances")
CreateInstancesFromSnapshot = Action("CreateInstancesFromSnapshot")
CreateKeyPair = Action("CreateKeyPair")
CreateLoadBalancer = Action("CreateLoadBalancer")
CreateLoadBalancerTlsCertificate = Action("CreateLoadBalancerTlsCertificate")
CreateRelationalDatabase = Action("CreateRelationalDatabase")
CreateRelationalDatabaseFromSnapshot = Action("CreateRelationalDatabaseFromSnapshot")
CreateRelationalDatabaseSnapshot = Action("CreateRelationalDatabaseSnapshot")
DeleteAlarm = Action("DeleteAlarm")
DeleteAutoSnapshot = Action("DeleteAutoSnapshot")
DeleteBucket = Action("DeleteBucket")
DeleteBucketAccessKey = Action("DeleteBucketAccessKey")
DeleteCertificate = Action("DeleteCertificate")
DeleteContactMethod = Action("DeleteContactMethod")
DeleteContainerImage = Action("DeleteContainerImage")
DeleteContainerService = Action("DeleteContainerService")
DeleteDisk = Action("DeleteDisk")
DeleteDiskSnapshot = Action("DeleteDiskSnapshot")
DeleteDistribution = Action("DeleteDistribution")
DeleteDomain = Action("DeleteDomain")
DeleteDomainEntry = Action("DeleteDomainEntry")
DeleteInstance = Action("DeleteInstance")
DeleteInstanceSnapshot = Action("DeleteInstanceSnapshot")
DeleteKeyPair = Action("DeleteKeyPair")
DeleteKnownHostKeys = Action("DeleteKnownHostKeys")
DeleteLoadBalancer = Action("DeleteLoadBalancer")
DeleteLoadBalancerTlsCertificate = Action("DeleteLoadBalancerTlsCertificate")
DeleteRelationalDatabase = Action("DeleteRelationalDatabase")
DeleteRelationalDatabaseSnapshot = Action("DeleteRelationalDatabaseSnapshot")
DetachCertificateFromDistribution = Action("DetachCertificateFromDistribution")
DetachDisk = Action("DetachDisk")
DetachInstancesFromLoadBalancer = Action("DetachInstancesFromLoadBalancer")
DetachStaticIp = Action("DetachStaticIp")
DisableAddOn = Action("DisableAddOn")
DownloadDefaultKeyPair = Action("DownloadDefaultKeyPair")
EnableAddOn = Action("EnableAddOn")
ExportSnapshot = Action("ExportSnapshot")
GetActiveNames = Action("GetActiveNames")
GetAlarms = Action("GetAlarms")
GetAutoSnapshots = Action("GetAutoSnapshots")
GetBlueprints = Action("GetBlueprints")
GetBucketAccessKeys = Action("GetBucketAccessKeys")
GetBucketBundles = Action("GetBucketBundles")
GetBucketMetricData = Action("GetBucketMetricData")
GetBuckets = Action("GetBuckets")
GetBundles = Action("GetBundles")
GetCertificates = Action("GetCertificates")
GetCloudFormationStackRecords = Action("GetCloudFormationStackRecords")
GetContactMethods = Action("GetContactMethods")
GetContainerAPIMetadata = Action("GetContainerAPIMetadata")
GetContainerImages = Action("GetContainerImages")
GetContainerLog = Action("GetContainerLog")
GetContainerServiceDeployments = Action("GetContainerServiceDeployments")
GetContainerServiceMetricData = Action("GetContainerServiceMetricData")
GetContainerServicePowers = Action("GetContainerServicePowers")
GetContainerServices = Action("GetContainerServices")
GetDisk = Action("GetDisk")
GetDiskSnapshot = Action("GetDiskSnapshot")
GetDiskSnapshots = Action("GetDiskSnapshots")
GetDisks = Action("GetDisks")
GetDistributionBundles = Action("GetDistributionBundles")
GetDistributionLatestCacheReset = Action("GetDistributionLatestCacheReset")
GetDistributionMetricData = Action("GetDistributionMetricData")
GetDistributions = Action("GetDistributions")
GetDomain = Action("GetDomain")
GetDomains = Action("GetDomains")
GetExportSnapshotRecords = Action("GetExportSnapshotRecords")
GetInstance = Action("GetInstance")
GetInstanceAccessDetails = Action("GetInstanceAccessDetails")
GetInstanceMetricData = Action("GetInstanceMetricData")
GetInstancePortStates = Action("GetInstancePortStates")
GetInstanceSnapshot = Action("GetInstanceSnapshot")
GetInstanceSnapshots = Action("GetInstanceSnapshots")
GetInstanceState = Action("GetInstanceState")
GetInstances = Action("GetInstances")
GetKeyPair = Action("GetKeyPair")
GetKeyPairs = Action("GetKeyPairs")
GetLoadBalancer = Action("GetLoadBalancer")
GetLoadBalancerMetricData = Action("GetLoadBalancerMetricData")
GetLoadBalancerTlsCertificates = Action("GetLoadBalancerTlsCertificates")
GetLoadBalancers = Action("GetLoadBalancers")
GetOperation = Action("GetOperation")
GetOperations = Action("GetOperations")
GetOperationsForResource = Action("GetOperationsForResource")
GetRegions = Action("GetRegions")
GetRelationalDatabase = Action("GetRelationalDatabase")
GetRelationalDatabaseBlueprints = Action("GetRelationalDatabaseBlueprints")
GetRelationalDatabaseBundles = Action("GetRelationalDatabaseBundles")
GetRelationalDatabaseEvents = Action("GetRelationalDatabaseEvents")
GetRelationalDatabaseLogEvents = Action("GetRelationalDatabaseLogEvents")
GetRelationalDatabaseLogStreams = Action("GetRelationalDatabaseLogStreams")
GetRelationalDatabaseMasterUserPassword = Action(
    "GetRelationalDatabaseMasterUserPassword"
)
GetRelationalDatabaseMetricData = Action("GetRelationalDatabaseMetricData")
GetRelationalDatabaseParameters = Action("GetRelationalDatabaseParameters")
GetRelationalDatabaseSnapshot = Action("GetRelationalDatabaseSnapshot")
GetRelationalDatabaseSnapshots = Action("GetRelationalDatabaseSnapshots")
GetRelationalDatabases = Action("GetRelationalDatabases")
GetStaticIp = Action("GetStaticIp")
GetStaticIps = Action("GetStaticIps")
ImportKeyPair = Action("ImportKeyPair")
IsVpcPeered = Action("IsVpcPeered")
OpenInstancePublicPorts = Action("OpenInstancePublicPorts")
PeerVpc = Action("PeerVpc")
PutAlarm = Action("PutAlarm")
PutInstancePublicPorts = Action("PutInstancePublicPorts")
RebootInstance = Action("RebootInstance")
RebootRelationalDatabase = Action("RebootRelationalDatabase")
RegisterContainerImage = Action("RegisterContainerImage")
ReleaseStaticIp = Action("ReleaseStaticIp")
ResetDistributionCache = Action("ResetDistributionCache")
SendContactMethodVerification = Action("SendContactMethodVerification")
SetIpAddressType = Action("SetIpAddressType")
SetResourceAccessForBucket = Action("SetResourceAccessForBucket")
StartInstance = Action("StartInstance")
StartRelationalDatabase = Action("StartRelationalDatabase")
StopInstance = Action("StopInstance")
StopRelationalDatabase = Action("StopRelationalDatabase")
TagResource = Action("TagResource")
TestAlarm = Action("TestAlarm")
UnpeerVpc = Action("UnpeerVpc")
UntagResource = Action("UntagResource")
UpdateBucket = Action("UpdateBucket")
UpdateBucketBundle = Action("UpdateBucketBundle")
UpdateContainerService = Action("UpdateContainerService")
UpdateDistribution = Action("UpdateDistribution")
UpdateDistributionBundle = Action("UpdateDistributionBundle")
UpdateDomainEntry = Action("UpdateDomainEntry")
UpdateLoadBalancerAttribute = Action("UpdateLoadBalancerAttribute")
UpdateRelationalDatabase = Action("UpdateRelationalDatabase")
UpdateRelationalDatabaseParameters = Action("UpdateRelationalDatabaseParameters")
