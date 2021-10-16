# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon FSx"
prefix = "fsx"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFileGateway = Action("AssociateFileGateway")
AssociateFileSystemAliases = Action("AssociateFileSystemAliases")
CancelDataRepositoryTask = Action("CancelDataRepositoryTask")
CopyBackup = Action("CopyBackup")
CreateBackup = Action("CreateBackup")
CreateDataRepositoryTask = Action("CreateDataRepositoryTask")
CreateFileSystem = Action("CreateFileSystem")
CreateFileSystemFromBackup = Action("CreateFileSystemFromBackup")
CreateStorageVirtualMachine = Action("CreateStorageVirtualMachine")
CreateVolume = Action("CreateVolume")
CreateVolumeFromBackup = Action("CreateVolumeFromBackup")
DeleteBackup = Action("DeleteBackup")
DeleteFileSystem = Action("DeleteFileSystem")
DeleteStorageVirtualMachine = Action("DeleteStorageVirtualMachine")
DeleteVolume = Action("DeleteVolume")
DescribeAssociatedFileGateways = Action("DescribeAssociatedFileGateways")
DescribeBackups = Action("DescribeBackups")
DescribeDataRepositoryTasks = Action("DescribeDataRepositoryTasks")
DescribeFileSystemAliases = Action("DescribeFileSystemAliases")
DescribeFileSystems = Action("DescribeFileSystems")
DescribeStorageVirtualMachines = Action("DescribeStorageVirtualMachines")
DescribeVolumes = Action("DescribeVolumes")
DisassociateFileGateway = Action("DisassociateFileGateway")
DisassociateFileSystemAliases = Action("DisassociateFileSystemAliases")
ListTagsForResource = Action("ListTagsForResource")
ManageBackupPrincipalAssociations = Action("ManageBackupPrincipalAssociations")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFileSystem = Action("UpdateFileSystem")
UpdateStorageVirtualMachine = Action("UpdateStorageVirtualMachine")
UpdateVolume = Action("UpdateVolume")
