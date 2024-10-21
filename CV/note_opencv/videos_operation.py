#coding=utf-8
import cv2
cv2.VideoWriter_fourcc('O','O','O','O')

cv2.VideoWriter_fourcc(*'OOOO')


#支持avi格式的有：
'''
I420，YUV编码，视频格式为.avi
PIM1，MPEG-1编码，视频格式为.avi
XVID，MPEG-4编码，视频格式为.avi
'''
#其他编码器
'''
THEO，Ogg Vorbis，视频格式为.ogv
FLV1，Flash视频，视频格式为.flv
AVC1，H264编码
DIV3，MPEG-4.3编码
DIVX，MPEG-4编码
MP42，MPEG-4.2编码
MJPG，motion-jpeg编码
U263，H263编码
I263，H263I编码
'''

#支持mp4格式的有：
'''
MP4V，需要注意的是，英文要么全部大写，要么全部小写
'''
#不同视频压缩编码方式的视频质量对比
'''
HEVC > H.264 > MPEG4 > H.263 > MPEG2

HEVC比H.264节约了50%的码率
'''
#相同质量下，占用空间的顺序为

'''
MPG > AVI > WMV > MP4 > RMVB
'''
