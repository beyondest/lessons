# Useful WSL and System Commands

## WSL Commands
- `wsl -u <Username> -d <DistributionName>`
- `wsl --shutdown`
- `wsl --list --all`
- `wsl --list --running`
- `wsl -l -v`
- `wsl.exe --system -d Ubuntu-18.04 df -h /mnt/wslg/distro`  // Show status of virtual distro Ubuntu-18.04
- `wsl df -h /`  // Same as above
- `wsl.exe --version`


## USBIPD for WSL
- `usbipd wsl list`
- `usbipd wsl attach --busid`


## Optimize WSL VHDX
- `Optimize-VHD -Path D:\wsl\Ubuntu-18.04\ext4.vhdx -Mode Full`  // Minimize VHDX

## USBIPD Warnings
- **Warning:** USBIPD has been updated; old version commands do not work anymore.
- `usbipd list`
- `usbipd attach --wsl --busid 3-4`
- `usbipd bind --busip`
- `usbipd unbind --busip`

## WSL2 Configuration
- **Do not use this** (or USBIPD will fail because TCP:3240 is not allowed by third-party firewall rules):
  - `autoProxy=true`
  - `networkMode=mirrored`
  - `firewall=true`
  
- **Do not enable this** (or GUI will fail):
  - `dnsTunneling=true`

## Export and Backup WSL Distro
- `wsl.exe --export Ubuntu-20.04 C:\Path\To\Backup\ubuntu-20.04-backup.tar`
- `ubuntu1804 config --default-user root`

## Measure Disk Speed
- `winsat disk`
