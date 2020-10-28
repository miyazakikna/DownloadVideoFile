# coding=utf-8
import ffmpeg

path = r"【格納パス】.mp4"
ffmpeg.input('【ダウンロードしたい動画URL】').output(path).run()
