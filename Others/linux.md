
# Command Notes

### System Commands:
- `lscpu`  
- `lsgpu`  
- `lshw`  
- `free -h` // Shows system memory usage (16GB commonly).  
- `top` // Displays more system PIDs and running memory.  
- `df -h` // Shows total disk status.  

### Desktop & LightDM Service:
- `sudo apt-get install ubuntu-desktop`  
- `sudo systemctl start lightdm` // Set default display service.  

### Reset Failed Services:
- `systemctl reset-failed`  

### Set Proxy for WSL:
1. Open Clash and allow LAN.
2. Download service mode.
3. Enable TUN mode.
4. Enable firewall (a shield icon in General page).

### Disk Usage:
- `du -sh *` // Show each folder size in the present working directory (PWD).  
- `du -sh .*` // Show total PWD size.  
- `du -sh` // Same as above.  
- `du -sh --exclude=mnt -sh *`  
- `du -sh * | sort -rh` // Show in order.  
- `du -sh .[!.]* | sort -rh` // Show hidden files size (e.g., `.local/share/Trash`).  

### Log Rotation:
- `sudo logrotate -f /etc/logrotate.d/my_logrotate` // Configure custom logrotate.  
- `sudo logrotate -vf /etc/logrotate.conf`  

```text
/var/log/*.log {
    su root root
    size 100M
    rotate 4
    compress
    missingok
    notifempty
    create 0644 root root
}
```

### Python Virtual Environment:
- `python3 --version` // Python 3.6.9  
- `python3 -m venv myenv` // Create virtual environment for Python 3.6.9.  
- `source myenv/bin/activate`  

### Proxy Setup Script:
- `/home/liyuxuan/proxy/proxy.sh`  
- `~/.bashrc`  
  - `alias proxy="source /home/liyuxuan/proxy/proxy.sh"`  

#### Proxy Commands:
- `proxy set`  
- `proxy unset`  
- `proxy test`  

### Move and Copy Files:
- `mv /path/to/source_file /path/to/destination_directory/`  
- `cp -r /path1/* /path2` // Copy files recursively.  

### File Archiving:
- `tar -czvf file.tar.gz file1 file2`  
- `tar -xzvf file.tar.gz -C /destination_directory`  
- `unrar x target.rar -d /destination_directory`  

### Image Commands:
- `eog img.jpg`  
- `eog img.png`  
- `identify img.png`  

### PIP with Proxy:
- `pip3 install --proxy http://172.23.32.1:7890` // PIP needs to set proxy separately, even when using proxy.sh.

### Package Installation:
- `sudo apt-get install -y ***` // Auto use yes.  
- `sudo apt update`  

### .NET Commands:
- `dotnet new console` // Create C# project in PWD.  
- `dotnet run`  

### Search Build Directory:
- `while [[ "$PWD" != "/" ]] && [ ! -d "build" ]; do cd ..; done && [ -d "build" ] && cd "build"`  

### File Search:
- `find . -type f -ctime -0.083` // Search files modified in the last 2 hours.

### SSH Key Generation:
- `ssh-keygen -f ~/.ssh/github -t ed25519 -C "for github"` // Generate SSH key pair.  
- `eval $(ssh-agent -s)` // Activate SSH agent.  
- `ssh-add ~/.ssh/github` // Add private key to SSH agent.  

### Remote SSH Config:
- `sudo vim /etc/ssh/sshd_config` // In remote Linux, configure `AuthorizedKeysFile .ssh/authorized_keys` and enable `PubkeyAuthentication yes`.  
- `sudo vim ~/.ssh/authorized_keys` // Copy the public key to remote Linux and `ssh-add` the private key locally.

### ADB Commands:
- `adb shell am start -a android.media.action.VIDEO_CAPTURE && adb shell screenrecord --output-format=h264 --size 720x1280 - | nc -l 127.0.0.1 9006`  
- `adb exec-out screenrecord --output-format=h264 - | ffplay -framerate 60 -probesize 32 -sync video`  

### ADB Forward Port:
- `adb forward tcp:8080 tcp:8080` // Set port for Android IP webcam.  
- `rtsp://127.0.0.1:8080/h264_pcm.sdp`  

### TCP Port Status:
- `lsof -i -n` // Show TCP port status.  
- `ss -tuln` // Show TCP/UDP port status.

### Creating Python Package:
```text
--mypack
    |--mypack1-
        __init__.py
    |--mypack2-
        __init__.py
    |--setup.py
```

- Write `setup()` in `setup.py`.  
- `python setup.py bdist_wheel`  
- `cd dist`  
- `pip install mypack-version-py3-none-any.whl`  

### Free Space Commands:
- `journalctl --disk-usage`  
- `sudo journalctl --vacuum-time=3d` // Free up space by cleaning systemd journal logs.  
- `sudo ~/shellscripts/myclean.sh` // Clean snaps.

### Add User to TTY Group:
- `sudo usermod -aG tty $USER`  

### Enable USB Driver in WSL:
1. Download Microsoft's latest WSL2 kernel version.
2. Unzip and follow these steps:
    ```bash
    zcat /proc/config.gz > .config
    make menuconfig
    ```
3. In `menuconfig`, select features to enable (Y to include in kernel, M to build as modules).
4. Save, exit, and then:
    ```bash
    make modules -j $(nproc)
    sudo make modules_install
    make -j $(nproc)
    sudo make install
    cp vmlinux /mnt/c/Users/liyuxuan/wsl_kernel
    ```
5. Edit `.wslconfig`:
    ```ini
    [wsl2]
    kernel=C:\\Users\\liyuxuan\\vmlinux
    ```
6. Restart WSL2.

### USBIP on WSL2:
- In Windows admin PowerShell: `usbipd bind --busid=4-3`.  
- In WSL2: `sudo usbip attach -r localhost --busid=4-3`.  
- Allow port 3240 with: `sudo ufw allow 3240/tcp`.  
- Detach with: `sudo usbip detach -p 0/1/2`.  

### Jetson NX Proxy Setup:
1. Edit sudo permissions:
    ```bash
    sudo visudo:
    rcclub ALL=(ALL:ALL) NOPASSWD: /home/rcclub/ggbond/change.sh
    ```
2. Edit `.bashrc`:
    ```bash
    vim ~/.bashrc:
    sudo ~/ggbond/change.sh
    . ~/ggbond/proxy.sh set
    ```
3. Done, no need to re-enter the password.


## Net Issues:
- Q: change dns to public dns
- A: `sudo vim /etc/resolv.conf` and add `nameserver 8.8.8.8` or `nameserver 8.8.4.4`
