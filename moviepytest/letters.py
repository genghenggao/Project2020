'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-27 15:16:24
@LastEditors: Henggao
@LastEditTime: 2020-03-27 15:17:18
'''
import numpy as np
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
 
# 目标是创建炫动的文字，先创建TextClip，然后设置它居中
 
screensize = (720,460)
txtClip = TextClip('Cool effect',color='white', font="Amiri-Bold",
                   kerning = 5, fontsize=100)
cvc = CompositeVideoClip( [txtClip.set_pos('center')],
                        size=screensize)
 
# 下面的四个函数，定义了四种移动字母的方式
 
# helper function
rotMatrix = lambda a: np.array( [[np.cos(a),np.sin(a)], 
                                 [-np.sin(a),np.cos(a)]] )
 
def vortex(screenpos,i,nletters):
    d = lambda t : 1.0/(0.3+t**8) #damping
    a = i*np.pi/ nletters # angle of the movement
    v = rotMatrix(a).dot([-1,0])
    if i%2 : v[1] = -v[1]
    return lambda t: screenpos+400*d(t)*rotMatrix(0.5*d(t)*a).dot(v)
    
def cascade(screenpos,i,nletters):
    v = np.array([0,-1])
    d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1+t**4))
    return lambda t: screenpos+v*400*d(t-0.15*i)
 
def arrive(screenpos,i,nletters):
    v = np.array([-1,0])
    d = lambda t : max(0, 3-3*t)
    return lambda t: screenpos-400*v*d(t-0.2*i)
    
def vortexout(screenpos,i,nletters):
    d = lambda t : max(0,t) #damping
    a = i*np.pi/ nletters # angle of the movement
    v = rotMatrix(a).dot([-1,0])
    if i%2 : v[1] = -v[1]
    return lambda t: screenpos+400*d(t-0.1*i)*rotMatrix(-0.2*d(t)*a).dot(v)
 
 
 
# WE USE THE PLUGIN findObjects TO LOCATE AND SEPARATE EACH LETTER
 
letters = findObjects(cvc) # a list of ImageClips
 
 
# 让字母动起来
def moveLetters(letters, funcpos):
    return [ letter.set_pos(funcpos(letter.screenpos,i,len(letters)))
              for i,letter in enumerate(letters)]
 
clips = [ CompositeVideoClip( moveLetters(letters,funcpos),
                              size = screensize).subclip(0,5)
          for funcpos in [vortex, cascade, arrive, vortexout] ]
 
# 连接，写入文件
final_clip = concatenate_videoclips(clips)
final_clip.write_videofile('../../coolTextEffects.avi',fps=25,codec='mpeg4')