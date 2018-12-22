# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******
from pyVmomi.VmomiSupport import CreateDataType, CreateManagedType, CreateEnumType, AddVersion, AddVersionParent, F_LINK, F_LINKABLE, F_OPTIONAL, F_SECRET
from pyVmomi.VmomiSupport import newestVersions, currentVersions, stableVersions, matureVersions, publicVersions, oldestVersions

AddVersion("vmodl.query.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version2", "", "", 0, "vim25")
AddVersion("eam.version.version6_5", "eam", "6.5", 0, "eam")
AddVersion("vmodl.query.version.version3", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version4", "", "", 0, "vim25")
AddVersion("eam.version.version6", "eam", "6.0", 0, "eam")
AddVersion("eam.version.version6_7", "eam", "6.7", 0, "eam")
AddVersion("vmodl.reflect.version.version1", "reflect", "1.0", 0, "reflect")
AddVersion("eam.version.version1", "eam", "1.0", 0, "eam")
AddVersion("eam.version.version2", "eam", "2.0", 0, "eam")
AddVersion("eam.version.version3", "eam", "3.0", 0, "eam")
AddVersion("eam.version.version2_5", "eam", "2_5", 0, "eam")
AddVersion("vim.version.version1", "vim2", "2.0", 0, "vim25")
AddVersion("vim.version.version2", "vim25", "2.5", 0, "vim25")
AddVersion("vim.version.version3", "vim25", "2.5u2", 0, "vim25")
AddVersion("vim.version.version4", "vim25", "2.5u2server", 0, "vim25")
AddVersion("vim.version.version5", "vim25", "4.0", 0, "vim25")
AddVersion("vim.version.version6", "vim25", "4.1", 0, "vim25")
AddVersion("vim.version.version7", "vim25", "5.0", 0, "vim25")
AddVersion("vim.version.version8", "vim25", "5.1", 0, "vim25")
AddVersion("vmodl.version.version2", "", "", 0, "vim25")
AddVersion("vmodl.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.version.version0", "", "", 0, "vim25")
AddVersionParent("vmodl.query.version.version1", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version2", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version2", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version2", "vmodl.version.version0")
AddVersionParent("eam.version.version6_5", "vmodl.query.version.version1")
AddVersionParent("eam.version.version6_5", "vmodl.query.version.version2")
AddVersionParent("eam.version.version6_5", "eam.version.version6_5")
AddVersionParent("eam.version.version6_5", "vmodl.query.version.version3")
AddVersionParent("eam.version.version6_5", "vmodl.query.version.version4")
AddVersionParent("eam.version.version6_5", "eam.version.version6")
AddVersionParent("eam.version.version6_5", "vmodl.reflect.version.version1")
AddVersionParent("eam.version.version6_5", "eam.version.version1")
AddVersionParent("eam.version.version6_5", "eam.version.version2")
AddVersionParent("eam.version.version6_5", "eam.version.version3")
AddVersionParent("eam.version.version6_5", "eam.version.version2_5")
AddVersionParent("eam.version.version6_5", "vim.version.version1")
AddVersionParent("eam.version.version6_5", "vim.version.version2")
AddVersionParent("eam.version.version6_5", "vim.version.version3")
AddVersionParent("eam.version.version6_5", "vim.version.version4")
AddVersionParent("eam.version.version6_5", "vim.version.version5")
AddVersionParent("eam.version.version6_5", "vim.version.version6")
AddVersionParent("eam.version.version6_5", "vim.version.version7")
AddVersionParent("eam.version.version6_5", "vim.version.version8")
AddVersionParent("eam.version.version6_5", "vmodl.version.version2")
AddVersionParent("eam.version.version6_5", "vmodl.version.version1")
AddVersionParent("eam.version.version6_5", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version3")
AddVersionParent("vmodl.query.version.version3", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version3", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version3")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version4")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version2")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version0")
AddVersionParent("eam.version.version6", "vmodl.query.version.version1")
AddVersionParent("eam.version.version6", "vmodl.query.version.version2")
AddVersionParent("eam.version.version6", "vmodl.query.version.version3")
AddVersionParent("eam.version.version6", "vmodl.query.version.version4")
AddVersionParent("eam.version.version6", "eam.version.version6")
AddVersionParent("eam.version.version6", "vmodl.reflect.version.version1")
AddVersionParent("eam.version.version6", "eam.version.version1")
AddVersionParent("eam.version.version6", "eam.version.version2")
AddVersionParent("eam.version.version6", "eam.version.version3")
AddVersionParent("eam.version.version6", "eam.version.version2_5")
AddVersionParent("eam.version.version6", "vim.version.version1")
AddVersionParent("eam.version.version6", "vim.version.version2")
AddVersionParent("eam.version.version6", "vim.version.version3")
AddVersionParent("eam.version.version6", "vim.version.version4")
AddVersionParent("eam.version.version6", "vim.version.version5")
AddVersionParent("eam.version.version6", "vim.version.version6")
AddVersionParent("eam.version.version6", "vim.version.version7")
AddVersionParent("eam.version.version6", "vim.version.version8")
AddVersionParent("eam.version.version6", "vmodl.version.version2")
AddVersionParent("eam.version.version6", "vmodl.version.version1")
AddVersionParent("eam.version.version6", "vmodl.version.version0")
AddVersionParent("eam.version.version6_7", "vmodl.query.version.version1")
AddVersionParent("eam.version.version6_7", "vmodl.query.version.version2")
AddVersionParent("eam.version.version6_7", "eam.version.version6_5")
AddVersionParent("eam.version.version6_7", "vmodl.query.version.version3")
AddVersionParent("eam.version.version6_7", "vmodl.query.version.version4")
AddVersionParent("eam.version.version6_7", "eam.version.version6")
AddVersionParent("eam.version.version6_7", "eam.version.version6_7")
AddVersionParent("eam.version.version6_7", "vmodl.reflect.version.version1")
AddVersionParent("eam.version.version6_7", "eam.version.version1")
AddVersionParent("eam.version.version6_7", "eam.version.version2")
AddVersionParent("eam.version.version6_7", "eam.version.version3")
AddVersionParent("eam.version.version6_7", "eam.version.version2_5")
AddVersionParent("eam.version.version6_7", "vim.version.version1")
AddVersionParent("eam.version.version6_7", "vim.version.version2")
AddVersionParent("eam.version.version6_7", "vim.version.version3")
AddVersionParent("eam.version.version6_7", "vim.version.version4")
AddVersionParent("eam.version.version6_7", "vim.version.version5")
AddVersionParent("eam.version.version6_7", "vim.version.version6")
AddVersionParent("eam.version.version6_7", "vim.version.version7")
AddVersionParent("eam.version.version6_7", "vim.version.version8")
AddVersionParent("eam.version.version6_7", "vmodl.version.version2")
AddVersionParent("eam.version.version6_7", "vmodl.version.version1")
AddVersionParent("eam.version.version6_7", "vmodl.version.version0")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.reflect.version.version1")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.version.version2")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.version.version0")
AddVersionParent("eam.version.version1", "vmodl.query.version.version1")
AddVersionParent("eam.version.version1", "vmodl.query.version.version2")
AddVersionParent("eam.version.version1", "vmodl.query.version.version3")
AddVersionParent("eam.version.version1", "vmodl.query.version.version4")
AddVersionParent("eam.version.version1", "vmodl.reflect.version.version1")
AddVersionParent("eam.version.version1", "eam.version.version1")
AddVersionParent("eam.version.version1", "vim.version.version1")
AddVersionParent("eam.version.version1", "vim.version.version2")
AddVersionParent("eam.version.version1", "vim.version.version3")
AddVersionParent("eam.version.version1", "vim.version.version4")
AddVersionParent("eam.version.version1", "vim.version.version5")
AddVersionParent("eam.version.version1", "vim.version.version6")
AddVersionParent("eam.version.version1", "vim.version.version7")
AddVersionParent("eam.version.version1", "vim.version.version8")
AddVersionParent("eam.version.version1", "vmodl.version.version2")
AddVersionParent("eam.version.version1", "vmodl.version.version1")
AddVersionParent("eam.version.version1", "vmodl.version.version0")
AddVersionParent("eam.version.version2", "vmodl.query.version.version1")
AddVersionParent("eam.version.version2", "vmodl.query.version.version2")
AddVersionParent("eam.version.version2", "vmodl.query.version.version3")
AddVersionParent("eam.version.version2", "vmodl.query.version.version4")
AddVersionParent("eam.version.version2", "vmodl.reflect.version.version1")
AddVersionParent("eam.version.version2", "eam.version.version1")
AddVersionParent("eam.version.version2", "eam.version.version2")
AddVersionParent("eam.version.version2", "vim.version.version1")
AddVersionParent("eam.version.version2", "vim.version.version2")
AddVersionParent("eam.version.version2", "vim.version.version3")
AddVersionParent("eam.version.version2", "vim.version.version4")
AddVersionParent("eam.version.version2", "vim.version.version5")
AddVersionParent("eam.version.version2", "vim.version.version6")
AddVersionParent("eam.version.version2", "vim.version.version7")
AddVersionParent("eam.version.version2", "vim.version.version8")
AddVersionParent("eam.version.version2", "vmodl.version.version2")
AddVersionParent("eam.version.version2", "vmodl.version.version1")
AddVersionParent("eam.version.version2", "vmodl.version.version0")
AddVersionParent("eam.version.version3", "vmodl.query.version.version1")
AddVersionParent("eam.version.version3", "vmodl.query.version.version2")
AddVersionParent("eam.version.version3", "vmodl.query.version.version3")
AddVersionParent("eam.version.version3", "vmodl.query.version.version4")
AddVersionParent("eam.version.version3", "vmodl.reflect.version.version1")
AddVersionParent("eam.version.version3", "eam.version.version1")
AddVersionParent("eam.version.version3", "eam.version.version2")
AddVersionParent("eam.version.version3", "eam.version.version3")
AddVersionParent("eam.version.version3", "eam.version.version2_5")
AddVersionParent("eam.version.version3", "vim.version.version1")
AddVersionParent("eam.version.version3", "vim.version.version2")
AddVersionParent("eam.version.version3", "vim.version.version3")
AddVersionParent("eam.version.version3", "vim.version.version4")
AddVersionParent("eam.version.version3", "vim.version.version5")
AddVersionParent("eam.version.version3", "vim.version.version6")
AddVersionParent("eam.version.version3", "vim.version.version7")
AddVersionParent("eam.version.version3", "vim.version.version8")
AddVersionParent("eam.version.version3", "vmodl.version.version2")
AddVersionParent("eam.version.version3", "vmodl.version.version1")
AddVersionParent("eam.version.version3", "vmodl.version.version0")
AddVersionParent("eam.version.version2_5", "vmodl.query.version.version1")
AddVersionParent("eam.version.version2_5", "vmodl.query.version.version2")
AddVersionParent("eam.version.version2_5", "vmodl.query.version.version3")
AddVersionParent("eam.version.version2_5", "vmodl.query.version.version4")
AddVersionParent("eam.version.version2_5", "vmodl.reflect.version.version1")
AddVersionParent("eam.version.version2_5", "eam.version.version1")
AddVersionParent("eam.version.version2_5", "eam.version.version2")
AddVersionParent("eam.version.version2_5", "eam.version.version2_5")
AddVersionParent("eam.version.version2_5", "vim.version.version1")
AddVersionParent("eam.version.version2_5", "vim.version.version2")
AddVersionParent("eam.version.version2_5", "vim.version.version3")
AddVersionParent("eam.version.version2_5", "vim.version.version4")
AddVersionParent("eam.version.version2_5", "vim.version.version5")
AddVersionParent("eam.version.version2_5", "vim.version.version6")
AddVersionParent("eam.version.version2_5", "vim.version.version7")
AddVersionParent("eam.version.version2_5", "vim.version.version8")
AddVersionParent("eam.version.version2_5", "vmodl.version.version2")
AddVersionParent("eam.version.version2_5", "vmodl.version.version1")
AddVersionParent("eam.version.version2_5", "vmodl.version.version0")
AddVersionParent("vim.version.version1", "vmodl.query.version.version1")
AddVersionParent("vim.version.version1", "vim.version.version1")
AddVersionParent("vim.version.version1", "vmodl.version.version0")
AddVersionParent("vim.version.version2", "vmodl.query.version.version1")
AddVersionParent("vim.version.version2", "vim.version.version1")
AddVersionParent("vim.version.version2", "vim.version.version2")
AddVersionParent("vim.version.version2", "vmodl.version.version0")
AddVersionParent("vim.version.version3", "vmodl.query.version.version1")
AddVersionParent("vim.version.version3", "vim.version.version1")
AddVersionParent("vim.version.version3", "vim.version.version2")
AddVersionParent("vim.version.version3", "vim.version.version3")
AddVersionParent("vim.version.version3", "vmodl.version.version0")
AddVersionParent("vim.version.version4", "vmodl.query.version.version1")
AddVersionParent("vim.version.version4", "vim.version.version1")
AddVersionParent("vim.version.version4", "vim.version.version2")
AddVersionParent("vim.version.version4", "vim.version.version3")
AddVersionParent("vim.version.version4", "vim.version.version4")
AddVersionParent("vim.version.version4", "vmodl.version.version0")
AddVersionParent("vim.version.version5", "vmodl.query.version.version1")
AddVersionParent("vim.version.version5", "vmodl.query.version.version2")
AddVersionParent("vim.version.version5", "vim.version.version1")
AddVersionParent("vim.version.version5", "vim.version.version2")
AddVersionParent("vim.version.version5", "vim.version.version3")
AddVersionParent("vim.version.version5", "vim.version.version4")
AddVersionParent("vim.version.version5", "vim.version.version5")
AddVersionParent("vim.version.version5", "vmodl.version.version1")
AddVersionParent("vim.version.version5", "vmodl.version.version0")
AddVersionParent("vim.version.version6", "vmodl.query.version.version1")
AddVersionParent("vim.version.version6", "vmodl.query.version.version2")
AddVersionParent("vim.version.version6", "vmodl.query.version.version3")
AddVersionParent("vim.version.version6", "vim.version.version1")
AddVersionParent("vim.version.version6", "vim.version.version2")
AddVersionParent("vim.version.version6", "vim.version.version3")
AddVersionParent("vim.version.version6", "vim.version.version4")
AddVersionParent("vim.version.version6", "vim.version.version5")
AddVersionParent("vim.version.version6", "vim.version.version6")
AddVersionParent("vim.version.version6", "vmodl.version.version1")
AddVersionParent("vim.version.version6", "vmodl.version.version0")
AddVersionParent("vim.version.version7", "vmodl.query.version.version1")
AddVersionParent("vim.version.version7", "vmodl.query.version.version2")
AddVersionParent("vim.version.version7", "vmodl.query.version.version3")
AddVersionParent("vim.version.version7", "vmodl.query.version.version4")
AddVersionParent("vim.version.version7", "vmodl.reflect.version.version1")
AddVersionParent("vim.version.version7", "vim.version.version1")
AddVersionParent("vim.version.version7", "vim.version.version2")
AddVersionParent("vim.version.version7", "vim.version.version3")
AddVersionParent("vim.version.version7", "vim.version.version4")
AddVersionParent("vim.version.version7", "vim.version.version5")
AddVersionParent("vim.version.version7", "vim.version.version6")
AddVersionParent("vim.version.version7", "vim.version.version7")
AddVersionParent("vim.version.version7", "vmodl.version.version2")
AddVersionParent("vim.version.version7", "vmodl.version.version1")
AddVersionParent("vim.version.version7", "vmodl.version.version0")
AddVersionParent("vim.version.version8", "vmodl.query.version.version1")
AddVersionParent("vim.version.version8", "vmodl.query.version.version2")
AddVersionParent("vim.version.version8", "vmodl.query.version.version3")
AddVersionParent("vim.version.version8", "vmodl.query.version.version4")
AddVersionParent("vim.version.version8", "vmodl.reflect.version.version1")
AddVersionParent("vim.version.version8", "vim.version.version1")
AddVersionParent("vim.version.version8", "vim.version.version2")
AddVersionParent("vim.version.version8", "vim.version.version3")
AddVersionParent("vim.version.version8", "vim.version.version4")
AddVersionParent("vim.version.version8", "vim.version.version5")
AddVersionParent("vim.version.version8", "vim.version.version6")
AddVersionParent("vim.version.version8", "vim.version.version7")
AddVersionParent("vim.version.version8", "vim.version.version8")
AddVersionParent("vim.version.version8", "vmodl.version.version2")
AddVersionParent("vim.version.version8", "vmodl.version.version1")
AddVersionParent("vim.version.version8", "vmodl.version.version0")
AddVersionParent("vmodl.version.version2", "vmodl.version.version2")
AddVersionParent("vmodl.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.version.version0", "vmodl.version.version0")

newestVersions.Add("eam.version.version6_7")
stableVersions.Add("eam.version.version6_7")
publicVersions.Add("eam.version.version6_7")
oldestVersions.Add("eam.version.version1")

CreateManagedType("eam.EamObject", "EamObject", "vmodl.ManagedObject", "eam.version.version1", None, [("resolve", "Resolve", "eam.version.version1", (("issueKey", "int[]", "eam.version.version1", 0, None),), (F_OPTIONAL, "int[]", "int[]"), None, None), ("resolveAll", "ResolveAll", "eam.version.version1", (), (0, "void", "void"), None, None), ("queryIssue", "QueryIssue", "eam.version.version1", (("issueKey", "int[]", "eam.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "eam.issue.Issue[]", "eam.issue.Issue[]"), None, None)])
CreateDataType("eam.EamObject.RuntimeInfo", "EamObjectRuntimeInfo", "vmodl.DynamicData", "eam.version.version1", [("status", "string", "eam.version.version1", 0), ("issue", "eam.issue.Issue[]", "eam.version.version1", F_OPTIONAL), ("goalState", "string", "eam.version.version1", 0), ("entity", "eam.EamObject", "eam.version.version1", 0)])
CreateEnumType("eam.EamObject.RuntimeInfo.Status", "EamObjectRuntimeInfoStatus", "eam.version.version1", ["green", "yellow", "red"])
CreateEnumType("eam.EamObject.RuntimeInfo.GoalState", "EamObjectRuntimeInfoGoalState", "eam.version.version1", ["enabled", "disabled", "uninstalled"])
CreateManagedType("eam.Task", "EamTask", "vmodl.ManagedObject", "eam.version.version1", None, None)
CreateDataType("eam.fault.EamFault", "EamFault", "vmodl.MethodFault", "eam.version.version1", None)
CreateDataType("eam.fault.EamRuntimeFault", "EamRuntimeFault", "vmodl.RuntimeFault", "eam.version.version1", None)
CreateDataType("eam.fault.EamServiceNotInitialized", "EamServiceNotInitialized", "eam.fault.EamRuntimeFault", "eam.version.version6_5", None)
CreateDataType("eam.fault.EamSystemFault", "EamSystemFault", "eam.fault.EamRuntimeFault", "eam.version.version6_5", None)
CreateDataType("eam.fault.InvalidAgencyScope", "InvalidAgencyScope", "eam.fault.EamFault", "eam.version.version1", [("unknownComputeResource", "vim.ComputeResource[]", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.fault.InvalidLogin", "EamInvalidLogin", "eam.fault.EamRuntimeFault", "eam.version.version1", None)
CreateDataType("eam.fault.InvalidUrl", "InvalidUrl", "eam.fault.EamFault", "eam.version.version1", [("url", "string", "eam.version.version1", 0), ("malformedUrl", "boolean", "eam.version.version1", 0), ("unknownHost", "boolean", "eam.version.version1", 0), ("connectionRefused", "boolean", "eam.version.version1", 0), ("responseCode", "int", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.fault.InvalidVibPackage", "EamInvalidVibPackage", "eam.fault.EamRuntimeFault", "eam.version.version1", None)
CreateDataType("eam.fault.NoConnectionToVCenter", "NoConnectionToVCenter", "eam.fault.EamRuntimeFault", "eam.version.version1", None)
CreateDataType("eam.fault.NotAuthorized", "NotAuthorized", "eam.fault.EamRuntimeFault", "eam.version.version1", None)
CreateDataType("eam.issue.Issue", "Issue", "vmodl.DynamicData", "eam.version.version1", [("key", "int", "eam.version.version1", 0), ("description", "string", "eam.version.version1", 0), ("time", "vmodl.DateTime", "eam.version.version1", 0)])
CreateDataType("eam.vib.VibInfo", "VibVibInfo", "vmodl.DynamicData", "eam.version.version6", [("id", "string", "eam.version.version6", 0), ("name", "string", "eam.version.version6", 0), ("version", "string", "eam.version.version6", 0), ("vendor", "string", "eam.version.version6", 0), ("summary", "string", "eam.version.version6", 0), ("softwareTags", "eam.vib.VibInfo.SoftwareTags", "eam.version.version6_5", F_OPTIONAL), ("releaseDate", "vmodl.DateTime", "eam.version.version6", 0)])
CreateDataType("eam.vib.VibInfo.SoftwareTags", "VibVibInfoSoftwareTags", "vmodl.DynamicData", "eam.version.version6_5", [("tags", "string[]", "eam.version.version6_5", F_OPTIONAL)])
CreateManagedType("eam.Agent", "Agent", "eam.EamObject", "eam.version.version1", [("runtime", "eam.Agent.RuntimeInfo", "eam.version.version1", 0, None), ("config", "eam.Agent.ConfigInfo", "eam.version.version1", 0, None)], [("queryRuntime", "AgentQueryRuntime", "eam.version.version1", (), (0, "eam.Agent.RuntimeInfo", "eam.Agent.RuntimeInfo"), None, None), ("markAsAvailable", "MarkAsAvailable", "eam.version.version1", (), (0, "void", "void"), None, None), ("queryConfig", "AgentQueryConfig", "eam.version.version1", (), (0, "eam.Agent.ConfigInfo", "eam.Agent.ConfigInfo"), None, None)])
CreateDataType("eam.Agent.RuntimeInfo", "AgentRuntimeInfo", "eam.EamObject.RuntimeInfo", "eam.version.version1", [("vmPowerState", "vim.VirtualMachine.PowerState", "eam.version.version1", 0), ("receivingHeartBeat", "boolean", "eam.version.version1", 0), ("host", "vim.HostSystem", "eam.version.version1", F_OPTIONAL), ("vm", "vim.VirtualMachine", "eam.version.version1", F_OPTIONAL), ("vmIp", "string", "eam.version.version1", F_OPTIONAL), ("vmName", "string", "eam.version.version1", 0), ("esxAgentResourcePool", "vim.ResourcePool", "eam.version.version1", F_OPTIONAL), ("esxAgentFolder", "vim.Folder", "eam.version.version1", F_OPTIONAL), ("installedBulletin", "string[]", "eam.version.version1", F_OPTIONAL), ("installedVibs", "eam.vib.VibInfo[]", "eam.version.version6", F_OPTIONAL), ("agency", "eam.Agency", "eam.version.version2", F_OPTIONAL), ("vmHook", "eam.Agent.VmHook", "eam.version.version6_7", F_OPTIONAL)])
CreateDataType("eam.Agent.VmHook", "AgentVmHook", "vmodl.DynamicData", "eam.version.version6_7", [("vm", "vim.VirtualMachine", "eam.version.version6_7", 0), ("vmState", "string", "eam.version.version6_7", 0)])
CreateEnumType("eam.Agent.VmHook.VmState", "AgentVmHookVmState", "eam.version.version1", ["provisioned", "poweredOn"])
CreateDataType("eam.Agent.ConfigInfo", "AgentConfigInfo", "vmodl.DynamicData", "eam.version.version1", [("productLineId", "string", "eam.version.version1", F_OPTIONAL), ("hostVersion", "string", "eam.version.version1", F_OPTIONAL), ("ovfPackageUrl", "string", "eam.version.version1", F_OPTIONAL), ("ovfEnvironment", "eam.Agent.OvfEnvironmentInfo", "eam.version.version1", F_OPTIONAL), ("vibUrl", "string", "eam.version.version1", F_OPTIONAL), ("vibMatchingRules", "eam.Agent.VibMatchingRule[]", "eam.version.version2_5", F_OPTIONAL), ("vibName", "string", "eam.version.version2", F_OPTIONAL), ("dvFilterEnabled", "boolean", "eam.version.version1", F_OPTIONAL), ("rebootHostAfterVibUninstall", "boolean", "eam.version.version1", F_OPTIONAL), ("vmciService", "string[]", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.Agent.OvfEnvironmentInfo", "AgentOvfEnvironmentInfo", "vmodl.DynamicData", "eam.version.version1", [("ovfProperty", "eam.Agent.OvfEnvironmentInfo.OvfProperty[]", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.Agent.OvfEnvironmentInfo.OvfProperty", "AgentOvfEnvironmentInfoOvfProperty", "vmodl.DynamicData", "eam.version.version1", [("key", "string", "eam.version.version1", 0), ("value", "string", "eam.version.version1", 0)])
CreateDataType("eam.Agent.VibMatchingRule", "AgentVibMatchingRule", "vmodl.DynamicData", "eam.version.version1", [("vibNameRegex", "string", "eam.version.version1", 0), ("vibVersionRegex", "string", "eam.version.version1", 0)])
CreateDataType("eam.fault.EamAppFault", "EamAppFault", "eam.fault.EamRuntimeFault", "eam.version.version6", None)
CreateDataType("eam.fault.EamIOFault", "EamIOFault", "eam.fault.EamRuntimeFault", "eam.version.version6", None)
CreateDataType("eam.fault.InvalidAgentConfiguration", "InvalidAgentConfiguration", "eam.fault.EamFault", "eam.version.version1", [("invalidAgentConfiguration", "eam.Agent.ConfigInfo", "eam.version.version1", F_OPTIONAL), ("invalidField", "string", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.issue.AgencyIssue", "AgencyIssue", "eam.issue.Issue", "eam.version.version1", [("agency", "eam.Agency", "eam.version.version1", 0), ("agencyName", "string", "eam.version.version1", 0), ("solutionId", "string", "eam.version.version1", 0), ("solutionName", "string", "eam.version.version1", 0)])
CreateDataType("eam.issue.AgentIssue", "AgentIssue", "eam.issue.AgencyIssue", "eam.version.version1", [("agent", "eam.Agent", "eam.version.version1", 0), ("agentName", "string", "eam.version.version1", 0), ("host", "vim.HostSystem", "eam.version.version1", 0), ("hostName", "string", "eam.version.version1", 0)])
CreateDataType("eam.issue.ExtensibleIssue", "ExtensibleIssue", "eam.issue.Issue", "eam.version.version2", [("typeId", "string", "eam.version.version2", 0), ("argument", "vmodl.KeyAnyValue[]", "eam.version.version2", F_OPTIONAL), ("target", "vim.ManagedEntity", "eam.version.version2", F_OPTIONAL), ("agent", "eam.Agent", "eam.version.version2", F_OPTIONAL), ("agency", "eam.Agency", "eam.version.version2", F_OPTIONAL)])
CreateDataType("eam.issue.HostIssue", "HostIssue", "eam.issue.Issue", "eam.version.version1", [("host", "vim.HostSystem", "eam.version.version1", 0)])
CreateDataType("eam.issue.MissingDvFilterSwitch", "MissingDvFilterSwitch", "eam.issue.AgentIssue", "eam.version.version1", None)
CreateDataType("eam.issue.OrphanedAgency", "OrphanedAgency", "eam.issue.AgencyIssue", "eam.version.version1", None)
CreateDataType("eam.issue.OrphanedDvFilterSwitch", "OrphanedDvFilterSwitch", "eam.issue.HostIssue", "eam.version.version1", None)
CreateDataType("eam.issue.OvfInvalidProperty", "OvfInvalidProperty", "eam.issue.AgentIssue", "eam.version.version1", [("error", "vmodl.MethodFault[]", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.issue.UnknownAgentVm", "UnknownAgentVm", "eam.issue.HostIssue", "eam.version.version1", [("vm", "vim.VirtualMachine", "eam.version.version1", 0)])
CreateDataType("eam.issue.VibIssue", "VibIssue", "eam.issue.AgentIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VibNotInstalled", "VibNotInstalled", "eam.issue.VibIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VibRequiresHostInMaintenanceMode", "VibRequiresHostInMaintenanceMode", "eam.issue.VibIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VibRequiresHostReboot", "VibRequiresHostReboot", "eam.issue.VibIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VibRequiresManualInstallation", "VibRequiresManualInstallation", "eam.issue.VibIssue", "eam.version.version1", [("bulletin", "string[]", "eam.version.version1", 0)])
CreateDataType("eam.issue.VibRequiresManualUninstallation", "VibRequiresManualUninstallation", "eam.issue.VibIssue", "eam.version.version1", [("bulletin", "string[]", "eam.version.version1", 0)])
CreateDataType("eam.issue.VmIssue", "VmIssue", "eam.issue.AgentIssue", "eam.version.version1", [("vm", "vim.VirtualMachine", "eam.version.version1", 0)])
CreateDataType("eam.issue.VmMarkedAsTemplate", "VmMarkedAsTemplate", "eam.issue.VmIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VmNotDeployed", "VmNotDeployed", "eam.issue.AgentIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VmOrphaned", "VmOrphaned", "eam.issue.VmIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VmPoweredOff", "VmPoweredOff", "eam.issue.VmIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VmPoweredOn", "VmPoweredOn", "eam.issue.VmIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VmSuspended", "VmSuspended", "eam.issue.VmIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VmWrongFolder", "VmWrongFolder", "eam.issue.VmIssue", "eam.version.version1", [("currentFolder", "vim.Folder", "eam.version.version1", 0), ("requiredFolder", "vim.Folder", "eam.version.version1", 0)])
CreateDataType("eam.issue.VmWrongResourcePool", "VmWrongResourcePool", "eam.issue.VmIssue", "eam.version.version1", [("currentResourcePool", "vim.ResourcePool", "eam.version.version1", 0), ("requiredResourcePool", "vim.ResourcePool", "eam.version.version1", 0)])
CreateDataType("eam.issue.integrity.agency.VUMIssue", "IntegrityAgencyVUMIssue", "eam.issue.AgencyIssue", "eam.version.version6_7", None)
CreateDataType("eam.issue.integrity.agency.VUMUnavailable", "IntegrityAgencyVUMUnavailable", "eam.issue.integrity.agency.VUMIssue", "eam.version.version6_7", None)
CreateManagedType("eam.Agency", "Agency", "eam.EamObject", "eam.version.version1", [("solutionId", "string", "eam.version.version1", 0, None), ("owner", "string", "eam.version.version6", F_OPTIONAL, None), ("config", "eam.Agency.ConfigInfo", "eam.version.version1", 0, None), ("runtime", "eam.EamObject.RuntimeInfo", "eam.version.version1", 0, None), ("agent", "eam.Agent[]", "eam.version.version1", F_OPTIONAL, None)], [("querySolutionId", "QuerySolutionId", "eam.version.version1", (), (0, "string", "string"), None, None), ("queryConfig", "QueryConfig", "eam.version.version1", (), (0, "eam.Agency.ConfigInfo", "eam.Agency.ConfigInfo"), None, None), ("update", "Update", "eam.version.version1", (("config", "eam.Agency.ConfigInfo", "eam.version.version1", 0, None),), (0, "void", "void"), None, ["eam.fault.InvalidAgentConfiguration", "eam.fault.InvalidAgencyScope", "eam.fault.InvalidUrl", ]), ("queryRuntime", "AgencyQueryRuntime", "eam.version.version1", (), (0, "eam.EamObject.RuntimeInfo", "eam.EamObject.RuntimeInfo"), None, None), ("queryAgent", "QueryAgent", "eam.version.version1", (), (F_OPTIONAL, "eam.Agent[]", "eam.Agent[]"), None, None), ("registerAgentVm", "RegisterAgentVm", "eam.version.version2", (("agentVm", "vim.VirtualMachine", "eam.version.version2", 0, None),), (0, "eam.Agent", "eam.Agent"), None, ["vmodl.fault.ManagedObjectNotFound", ]), ("unregisterAgentVm", "UnregisterAgentVm", "eam.version.version2", (("agentVm", "vim.VirtualMachine", "eam.version.version2", 0, None),), (0, "void", "void"), None, None), ("enable", "Enable", "eam.version.version1", (), (0, "void", "void"), None, None), ("disable", "Disable", "eam.version.version1", (), (0, "void", "void"), None, None), ("uninstall", "Uninstall", "eam.version.version1", (), (0, "void", "void"), None, None), ("destroyAgency", "DestroyAgency", "eam.version.version1", (), (0, "void", "void"), None, None), ("addIssue", "AddIssue", "eam.version.version2", (("issue", "eam.issue.Issue", "eam.version.version2", 0, None),), (0, "eam.issue.Issue", "eam.issue.Issue"), None, ["vmodl.fault.InvalidArgument", ])])
CreateDataType("eam.Agency.ConfigInfo", "AgencyConfigInfo", "vmodl.DynamicData", "eam.version.version1", [("agentConfig", "eam.Agent.ConfigInfo[]", "eam.version.version1", F_OPTIONAL), ("scope", "eam.Agency.Scope", "eam.version.version1", F_OPTIONAL), ("manuallyMarkAgentVmAvailableAfterProvisioning", "boolean", "eam.version.version1", F_OPTIONAL), ("manuallyMarkAgentVmAvailableAfterPowerOn", "boolean", "eam.version.version1", F_OPTIONAL), ("optimizedDeploymentEnabled", "boolean", "eam.version.version1", F_OPTIONAL), ("agentName", "string", "eam.version.version1", F_OPTIONAL), ("agencyName", "string", "eam.version.version1", F_OPTIONAL), ("manuallyProvisioned", "boolean", "eam.version.version2", F_OPTIONAL), ("manuallyMonitored", "boolean", "eam.version.version2", F_OPTIONAL), ("bypassVumEnabled", "boolean", "eam.version.version2", F_OPTIONAL), ("agentVmNetwork", "vim.Network[]", "eam.version.version2", F_OPTIONAL), ("agentVmDatastore", "vim.Datastore[]", "eam.version.version2_5", F_OPTIONAL), ("preferHostConfiguration", "boolean", "eam.version.version2_5", F_OPTIONAL), ("ipPool", "vim.vApp.IpPool", "eam.version.version3", F_OPTIONAL)])
CreateDataType("eam.Agency.Scope", "AgencyScope", "vmodl.DynamicData", "eam.version.version1", None)
CreateDataType("eam.Agency.ComputeResourceScope", "AgencyComputeResourceScope", "eam.Agency.Scope", "eam.version.version1", [("computeResource", "vim.ComputeResource[]", "eam.version.version1", F_OPTIONAL)])
CreateManagedType("eam.EsxAgentManager", "EsxAgentManager", "eam.EamObject", "eam.version.version1", [("agency", "eam.Agency[]", "eam.version.version1", F_OPTIONAL, None), ("issue", "eam.issue.Issue[]", "eam.version.version1", F_OPTIONAL, None)], [("queryAgency", "QueryAgency", "eam.version.version1", (), (F_OPTIONAL, "eam.Agency[]", "eam.Agency[]"), None, None), ("createAgency", "CreateAgency", "eam.version.version1", (("agencyConfigInfo", "eam.Agency.ConfigInfo", "eam.version.version1", 0, None),("initialGoalState", "string", "eam.version.version1", 0, None),), (0, "eam.Agency", "eam.Agency"), None, ["eam.fault.InvalidAgentConfiguration", "eam.fault.InvalidAgencyScope", "eam.fault.InvalidUrl", ]), ("scanForUnknownAgentVm", "ScanForUnknownAgentVm", "eam.version.version1", (), (0, "void", "void"), None, None)])
CreateDataType("eam.issue.CannotAccessAgentOVF", "CannotAccessAgentOVF", "eam.issue.VmNotDeployed", "eam.version.version1", [("downloadUrl", "string", "eam.version.version1", 0)])
CreateDataType("eam.issue.CannotAccessAgentVib", "CannotAccessAgentVib", "eam.issue.VibNotInstalled", "eam.version.version1", [("downloadUrl", "string", "eam.version.version1", 0)])
CreateDataType("eam.issue.IncompatibleHostVersion", "IncompatibleHostVersion", "eam.issue.VmNotDeployed", "eam.version.version1", None)
CreateDataType("eam.issue.InsufficientIpAddresses", "InsufficientIpAddresses", "eam.issue.VmPoweredOff", "eam.version.version1", [("network", "vim.Network", "eam.version.version1", 0)])
CreateDataType("eam.issue.InsufficientResources", "InsufficientResources", "eam.issue.VmNotDeployed", "eam.version.version1", None)
CreateDataType("eam.issue.InsufficientSpace", "InsufficientSpace", "eam.issue.VmNotDeployed", "eam.version.version1", None)
CreateDataType("eam.issue.MissingAgentIpPool", "MissingAgentIpPool", "eam.issue.VmPoweredOff", "eam.version.version1", [("network", "vim.Network", "eam.version.version1", 0)])
CreateDataType("eam.issue.NoAgentVmDatastore", "NoAgentVmDatastore", "eam.issue.VmNotDeployed", "eam.version.version1", None)
CreateDataType("eam.issue.NoAgentVmNetwork", "NoAgentVmNetwork", "eam.issue.VmNotDeployed", "eam.version.version1", None)
CreateDataType("eam.issue.NoCustomAgentVmDatastore", "NoCustomAgentVmDatastore", "eam.issue.NoAgentVmDatastore", "eam.version.version1", [("customAgentVmDatastore", "vim.Datastore[]", "eam.version.version1", 0), ("customAgentVmDatastoreName", "string[]", "eam.version.version1", 0)])
CreateDataType("eam.issue.NoCustomAgentVmNetwork", "NoCustomAgentVmNetwork", "eam.issue.NoAgentVmNetwork", "eam.version.version1", [("customAgentVmNetwork", "vim.Network[]", "eam.version.version1", 0), ("customAgentVmNetworkName", "string[]", "eam.version.version1", 0)])
CreateDataType("eam.issue.OvfInvalidFormat", "OvfInvalidFormat", "eam.issue.VmNotDeployed", "eam.version.version1", [("error", "vmodl.MethodFault[]", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.issue.VibCannotPutHostInMaintenanceMode", "VibCannotPutHostInMaintenanceMode", "eam.issue.VibIssue", "eam.version.version1", None)
CreateDataType("eam.issue.VibCannotPutHostOutOfMaintenanceMode", "VibCannotPutHostOutOfMaintenanceMode", "eam.issue.VibIssue", "eam.version.version6_5", None)
CreateDataType("eam.issue.VibInvalidFormat", "VibInvalidFormat", "eam.issue.VibNotInstalled", "eam.version.version1", None)
CreateDataType("eam.issue.VmCorrupted", "VmCorrupted", "eam.issue.VmIssue", "eam.version.version1", [("missingFile", "string", "eam.version.version1", F_OPTIONAL)])
CreateDataType("eam.issue.VmDeployed", "VmDeployed", "eam.issue.VmIssue", "eam.version.version1", None)
CreateDataType("eam.issue.integrity.agency.CannotDeleteSoftware", "IntegrityAgencyCannotDeleteSoftware", "eam.issue.integrity.agency.VUMIssue", "eam.version.version6_7", None)
CreateDataType("eam.issue.integrity.agency.CannotStageSoftware", "IntegrityAgencyCannotStageSoftware", "eam.issue.integrity.agency.VUMIssue", "eam.version.version6_7", None)
CreateDataType("eam.issue.HostInMaintenanceMode", "HostInMaintenanceMode", "eam.issue.VmDeployed", "eam.version.version1", None)
CreateDataType("eam.issue.HostInStandbyMode", "HostInStandbyMode", "eam.issue.VmDeployed", "eam.version.version1", None)
CreateDataType("eam.issue.HostPoweredOff", "HostPoweredOff", "eam.issue.VmDeployed", "eam.version.version1", None)
