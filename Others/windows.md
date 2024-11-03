## User and System Information in GUI
- `netplwiz`  // See user info in GUI
- `whoami`
- `msinfo32`  // See system info in GUI

## Windows Activation
- `irm massgrave.dev/get | iex`  // Activate Windows Pro using settings in prompt

## System Information and Disk Space
- `systeminfo`  // Show all system hardware info, e.g., memory, does not show disk space
- `fsutil volume diskfree C:`  // Show disk space

## Directory and SSH
- `dir . test.txt`
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






