
## Device Information

```bash
sudo lshw -class system                     # Display system information
cat /proc/device-tree/model                 # Show device model
```

## Check IMU

```bash
sudo i2cdetect -y 1d                        # Detect I2C devices on bus 1d
```

## Magic Command

```bash
sudo jtop                                   # Launch jtop for monitoring Jetson stats
```

- OpenCV Python version: **4.1.1**
- Jetson CUDA Arch Bin: **5.3/6.2/7.2 | nano, tx1/dx2/xavier**

## Build OpenCV with CUDA

```bash
sudo cmake -D WITH_CUDA=ON \
           -D WITH_CUDNN=ON \
           -D CUDA_ARCH_BIN="7.2" \
           -D CUDA_ARCH_PTX="" \
           -D OPENCV_GENERATE_PKGCONFIG=ON \
           -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.6.0/modules \
           -D BUILD_opencv_datasets=ON \
           -D BUILD_opencv_face=ON \
           -D BUILD_opencv_xfeatures2d=ON \
           -D BUILD_opencv_wechat_qrcode=ON \
           -D WITH_GSTREAMER=ON \
           -D WITH_LIBV4L=ON \
           -D BUILD_opencv_python3=ON \
           -D BUILD_TESTS=OFF \
           -D BUILD_PERF_TESTS=OFF \
           -D BUILD_EXAMPLES=OFF \
           -D CMAKE_BUILD_TYPE=RELEASE \
           -D CMAKE_INSTALL_PREFIX=/usr/local \
           -D HTTP_PROXY=http://192.168.137.1:7890 \
           -D HTTPS_PROXY=http://192.168.137.1:7890 -G Ninja ..
make -j$(nproc)
```

## Jetson Wi-Fi Commands

```bash
sudo nmcli device wifi list                 # List available Wi-Fi networks
sudo nmcli device wifi connect SSID password PASSWORD  # Connect to Wi-Fi network
```

## Swap Configuration

```bash
sudo swapoff -a                             # Disable swap
sudo systemctl disable nvzramconfig         # Disable nvzramconfig service
sudo fallocate -l 6GB /mnt/6GB.swap         # Create a 6GB swap file
sudo mkswap /mnt/6GB.swap                   # Set up swap space
sudo vim /etc/fstab                         # Edit fstab to add the new swap
```

Add the following line to `/etc/fstab`:

```plaintext
/mnt/6GB.swap swap swap defaults 0 0
```
