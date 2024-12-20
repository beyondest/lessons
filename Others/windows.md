## Q&A

- Q:Google and edge hyjack by 360 website , or organized by organization
    - A:regedit -> HKEY_CURRENT_USER\Software\Policies\Chorme, remove any additions except default; remove any policies in chorme:\\policy
    

- Q: How to disable internal keyboard in win11 lenovo:
    - A: Uninstall driver Standard PS/2 and HID Keyboard Device(this is the one when no external keyboard is connected),
    and then go to` gpedit.msc -> Computer Configuration -> Administrative Templates -> System -> Device Installation -> Device Installation Restrictions -> Prevent installation of devices not described by other policies`, enable this option.
    - P.S.: only delete ps2 fail to disable internal keyboard; use `sc config i8042prt start=disabled` fail to disable internal keyboard.



## User and System Information in GUI
- `netplwiz`  // See user info in GUI
- `whoami`
- `msinfo32`  // See system info in GUI
- `msconfig`  // Change system settings in GUI
- `odbcad32`  // ODBC data source configuration
- `services.msc`  // Manage services in GUI
- `lusrmgr.msc` // Local user and group management in GUI
- `mmc` // Console Platform
- `devmgmt.msc` // Device Manager
- `diskmgmt.msc` // Disk Management
- `compmgmt.msc` // Computer Management
- `regedit`

## Windows Activation
- `irm massgrave.dev/get | iex`  // Activate Windows Pro using settings in prompt

## System Information and Disk Space
- `systeminfo`  // Show all system hardware info, e.g., memory, does not show disk space
- `fsutil volume diskfree C:`  // Show disk space

## Directory 
- `dir . test.txt`
- 
## SSH 
- `ssh rcclub@192.168.1.123`  // 509rcclub GPU best server

## Windows Alias
use `ls $PROFILE` to see which config file 
In *C:/users/Yourname/Documents/Powershell/Microsoft.PowerShell_profile.ps1*, set as below
```
. "D:\PowershellScripts\MyAlias.ps1"
Set-Alias du Get-FolderSizes
Set-Alias work Enter-Workspace
```
In *D:\PowershellScripts\MyAlias.ps1*,set as below
```
function Get-FolderSizes {
    Get-ChildItem -Directory | 
        Select-Object Name, @{Name="Size(MB)";Expression={[math]::Round((Get-ChildItem $_.FullName -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB, 2)}} |
        Sort-Object "Size(MB)" -Descending
}
function Enter-Workspace { Set-Location "D:\VS_ws" }
```






