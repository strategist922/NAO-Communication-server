'''
Created on 11.01.2013

@author: hannes
'''
from naoqi import ALProxy
from settings.Settings import Settings

class cmdChangelang(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cmd = "changeLanguage"
        
    def exe(self, args=None, addr=None):
        
        # get proxies
        tts = ALProxy("ALTextToSpeech", Settings.naoHostName, Settings.naoPort)
        asr = ALProxy("ALSpeechRecognition", Settings.naoHostName, Settings.naoPort)
        
        # get language
        lang =str( args[1] )
        
        # set language
        asr.setLanguage( lang )
        tts.setLanguage( lang )
        