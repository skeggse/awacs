# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3"
prefix = "s3"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        # account is empty for S3 buckets
        if not resource.startswith(("accesspoint/", "job/", "storage-lens/")):
            account = ""
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AbortMultipartUpload = Action("AbortMultipartUpload")
BypassGovernanceRetention = Action("BypassGovernanceRetention")
CreateAccessPoint = Action("CreateAccessPoint")
CreateAccessPointForObjectLambda = Action("CreateAccessPointForObjectLambda")
CreateBucket = Action("CreateBucket")
CreateJob = Action("CreateJob")
CreateMultiRegionAccessPoint = Action("CreateMultiRegionAccessPoint")
CreateStorageLensGroup = Action("CreateStorageLensGroup")
DeleteAccessPoint = Action("DeleteAccessPoint")
DeleteAccessPointForObjectLambda = Action("DeleteAccessPointForObjectLambda")
DeleteAccessPointPolicy = Action("DeleteAccessPointPolicy")
DeleteAccessPointPolicyForObjectLambda = Action(
    "DeleteAccessPointPolicyForObjectLambda"
)
DeleteBucket = Action("DeleteBucket")
DeleteBucketOwnershipControls = Action("DeleteBucketOwnershipControls")
DeleteBucketPolicy = Action("DeleteBucketPolicy")
DeleteBucketWebsite = Action("DeleteBucketWebsite")
DeleteJobTagging = Action("DeleteJobTagging")
DeleteMultiRegionAccessPoint = Action("DeleteMultiRegionAccessPoint")
DeleteObject = Action("DeleteObject")
DeleteObjectTagging = Action("DeleteObjectTagging")
DeleteObjectVersion = Action("DeleteObjectVersion")
DeleteObjectVersionTagging = Action("DeleteObjectVersionTagging")
DeleteStorageLensConfiguration = Action("DeleteStorageLensConfiguration")
DeleteStorageLensConfigurationTagging = Action("DeleteStorageLensConfigurationTagging")
DeleteStorageLensGroup = Action("DeleteStorageLensGroup")
DescribeJob = Action("DescribeJob")
DescribeMultiRegionAccessPointOperation = Action(
    "DescribeMultiRegionAccessPointOperation"
)
GetAccelerateConfiguration = Action("GetAccelerateConfiguration")
GetAccessPoint = Action("GetAccessPoint")
GetAccessPointConfigurationForObjectLambda = Action(
    "GetAccessPointConfigurationForObjectLambda"
)
GetAccessPointForObjectLambda = Action("GetAccessPointForObjectLambda")
GetAccessPointPolicy = Action("GetAccessPointPolicy")
GetAccessPointPolicyForObjectLambda = Action("GetAccessPointPolicyForObjectLambda")
GetAccessPointPolicyStatus = Action("GetAccessPointPolicyStatus")
GetAccessPointPolicyStatusForObjectLambda = Action(
    "GetAccessPointPolicyStatusForObjectLambda"
)
GetAccountPublicAccessBlock = Action("GetAccountPublicAccessBlock")
GetAnalyticsConfiguration = Action("GetAnalyticsConfiguration")
GetBucketAcl = Action("GetBucketAcl")
GetBucketCORS = Action("GetBucketCORS")
GetBucketLocation = Action("GetBucketLocation")
GetBucketLogging = Action("GetBucketLogging")
GetBucketNotification = Action("GetBucketNotification")
GetBucketObjectLockConfiguration = Action("GetBucketObjectLockConfiguration")
GetBucketOwnershipControls = Action("GetBucketOwnershipControls")
GetBucketPolicy = Action("GetBucketPolicy")
GetBucketPolicyStatus = Action("GetBucketPolicyStatus")
GetBucketPublicAccessBlock = Action("GetBucketPublicAccessBlock")
GetBucketRequestPayment = Action("GetBucketRequestPayment")
GetBucketTagging = Action("GetBucketTagging")
GetBucketVersioning = Action("GetBucketVersioning")
GetBucketWebsite = Action("GetBucketWebsite")
GetEncryptionConfiguration = Action("GetEncryptionConfiguration")
GetIntelligentTieringConfiguration = Action("GetIntelligentTieringConfiguration")
GetInventoryConfiguration = Action("GetInventoryConfiguration")
GetIpConfiguration = Action("GetIpConfiguration")
GetJobTagging = Action("GetJobTagging")
GetLifecycleConfiguration = Action("GetLifecycleConfiguration")
GetMetricsConfiguration = Action("GetMetricsConfiguration")
GetMultiRegionAccessPoint = Action("GetMultiRegionAccessPoint")
GetMultiRegionAccessPointPolicy = Action("GetMultiRegionAccessPointPolicy")
GetMultiRegionAccessPointPolicyStatus = Action("GetMultiRegionAccessPointPolicyStatus")
GetMultiRegionAccessPointRoutes = Action("GetMultiRegionAccessPointRoutes")
GetObject = Action("GetObject")
GetObjectAcl = Action("GetObjectAcl")
GetObjectAttributes = Action("GetObjectAttributes")
GetObjectLegalHold = Action("GetObjectLegalHold")
GetObjectRetention = Action("GetObjectRetention")
GetObjectTagging = Action("GetObjectTagging")
GetObjectTorrent = Action("GetObjectTorrent")
GetObjectVersion = Action("GetObjectVersion")
GetObjectVersionAcl = Action("GetObjectVersionAcl")
GetObjectVersionAttributes = Action("GetObjectVersionAttributes")
GetObjectVersionForReplication = Action("GetObjectVersionForReplication")
GetObjectVersionTagging = Action("GetObjectVersionTagging")
GetObjectVersionTorrent = Action("GetObjectVersionTorrent")
GetReplicationConfiguration = Action("GetReplicationConfiguration")
GetStorageLensConfiguration = Action("GetStorageLensConfiguration")
GetStorageLensConfigurationTagging = Action("GetStorageLensConfigurationTagging")
GetStorageLensDashboard = Action("GetStorageLensDashboard")
GetStorageLensGroup = Action("GetStorageLensGroup")
HeadBucket = Action("HeadBucket")
InitiateReplication = Action("InitiateReplication")
ListAccessPoints = Action("ListAccessPoints")
ListAccessPointsForObjectLambda = Action("ListAccessPointsForObjectLambda")
ListAllMyBuckets = Action("ListAllMyBuckets")
ListBucket = Action("ListBucket")
ListBucketByTags = Action("ListBucketByTags")
ListBucketMultipartUploads = Action("ListBucketMultipartUploads")
ListBucketVersions = Action("ListBucketVersions")
ListJobs = Action("ListJobs")
ListMultiRegionAccessPoints = Action("ListMultiRegionAccessPoints")
ListMultipartUploadParts = Action("ListMultipartUploadParts")
ListObjects = Action("ListObjects")
ListStorageLensConfigurations = Action("ListStorageLensConfigurations")
ListStorageLensGroups = Action("ListStorageLensGroups")
ListTagsForResource = Action("ListTagsForResource")
ObjectOwnerOverrideToBucketOwner = Action("ObjectOwnerOverrideToBucketOwner")
PutAccelerateConfiguration = Action("PutAccelerateConfiguration")
PutAccessPointConfigurationForObjectLambda = Action(
    "PutAccessPointConfigurationForObjectLambda"
)
PutAccessPointPolicy = Action("PutAccessPointPolicy")
PutAccessPointPolicyForObjectLambda = Action("PutAccessPointPolicyForObjectLambda")
PutAccessPointPublicAccessBlock = Action("PutAccessPointPublicAccessBlock")
PutAccountPublicAccessBlock = Action("PutAccountPublicAccessBlock")
PutAnalyticsConfiguration = Action("PutAnalyticsConfiguration")
PutBucketAcl = Action("PutBucketAcl")
PutBucketCORS = Action("PutBucketCORS")
PutBucketLogging = Action("PutBucketLogging")
PutBucketNotification = Action("PutBucketNotification")
PutBucketObjectLockConfiguration = Action("PutBucketObjectLockConfiguration")
PutBucketOwnershipControls = Action("PutBucketOwnershipControls")
PutBucketPolicy = Action("PutBucketPolicy")
PutBucketPublicAccessBlock = Action("PutBucketPublicAccessBlock")
PutBucketRequestPayment = Action("PutBucketRequestPayment")
PutBucketTagging = Action("PutBucketTagging")
PutBucketVersioning = Action("PutBucketVersioning")
PutBucketWebsite = Action("PutBucketWebsite")
PutEncryptionConfiguration = Action("PutEncryptionConfiguration")
PutIntelligentTieringConfiguration = Action("PutIntelligentTieringConfiguration")
PutInventoryConfiguration = Action("PutInventoryConfiguration")
PutIpConfiguration = Action("PutIpConfiguration")
PutJobTagging = Action("PutJobTagging")
PutLifecycleConfiguration = Action("PutLifecycleConfiguration")
PutMetricsConfiguration = Action("PutMetricsConfiguration")
PutMultiRegionAccessPointPolicy = Action("PutMultiRegionAccessPointPolicy")
PutObject = Action("PutObject")
PutObjectAcl = Action("PutObjectAcl")
PutObjectLegalHold = Action("PutObjectLegalHold")
PutObjectRetention = Action("PutObjectRetention")
PutObjectTagging = Action("PutObjectTagging")
PutObjectVersionAcl = Action("PutObjectVersionAcl")
PutObjectVersionTagging = Action("PutObjectVersionTagging")
PutReplicationConfiguration = Action("PutReplicationConfiguration")
PutStorageLensConfiguration = Action("PutStorageLensConfiguration")
PutStorageLensConfigurationTagging = Action("PutStorageLensConfigurationTagging")
ReplicateDelete = Action("ReplicateDelete")
ReplicateObject = Action("ReplicateObject")
ReplicateTags = Action("ReplicateTags")
RestoreObject = Action("RestoreObject")
SubmitMultiRegionAccessPointRoutes = Action("SubmitMultiRegionAccessPointRoutes")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateJobPriority = Action("UpdateJobPriority")
UpdateJobStatus = Action("UpdateJobStatus")
UpdateStorageLensGroup = Action("UpdateStorageLensGroup")
