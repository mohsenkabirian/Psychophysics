#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on October 28, 2023, at 12:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'GoNoGo'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Projects\\pychopy\\Money\\GoNoGoTask_Mrs_Gharibi\\final_farsi\\GoNoGoTask\\GoNoGo_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Introduction" ---
image_introduction = visual.ImageStim(
    win=win,
    name='image_introduction', 
    image='images/introduction_text_image.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_intro = keyboard.Keyboard()

# --- Initialize components for Routine "trial_training" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
key_resp_training = keyboard.Keyboard()
stop_voice_audio = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stop_voice_audio')
stop_voice_audio.setVolume(1.0)
# Run 'Begin Experiment' code from code_training_trial
timing_temp = core.Clock()
#overall experiment timer
overall_timing = core.Clock()



# --- Initialize components for Routine "feedback" ---
feedback_text_component = visual.TextStim(win=win, name='feedback_text_component',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-1.0);

# --- Initialize components for Routine "rest" ---
plus_image = visual.ImageStim(
    win=win,
    name='plus_image', 
    image='images/172525_plus_icon.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.06, 0.06),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "trial_main" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_main = keyboard.Keyboard()
stop_voice_audio_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stop_voice_audio_2')
stop_voice_audio_2.setVolume(1.0)
# Run 'Begin Experiment' code from code_main_trial




# --- Initialize components for Routine "rest" ---
plus_image = visual.ImageStim(
    win=win,
    name='plus_image', 
    image='images/172525_plus_icon.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.06, 0.06),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "goodbye" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='ممنون از توجه شما\n\nبرای خروج کلید "راست" یا "چپ" را فشار دهید',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);
key_resp_bye = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Introduction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_intro.keys = []
key_resp_intro.rt = []
_key_resp_intro_allKeys = []
# keep track of which components have finished
IntroductionComponents = [image_introduction, key_resp_intro]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_introduction* updates
    if image_introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_introduction.frameNStart = frameN  # exact frame index
        image_introduction.tStart = t  # local t and not account for scr refresh
        image_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_introduction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_introduction.started')
        image_introduction.setAutoDraw(True)
    
    # *key_resp_intro* updates
    waitOnFlip = False
    if key_resp_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_intro.frameNStart = frameN  # exact frame index
        key_resp_intro.tStart = t  # local t and not account for scr refresh
        key_resp_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_intro, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_intro.started')
        key_resp_intro.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_intro.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_intro.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_intro.getKeys(keyList=['left','right'], waitRelease=False)
        _key_resp_intro_allKeys.extend(theseKeys)
        if len(_key_resp_intro_allKeys):
            key_resp_intro.keys = _key_resp_intro_allKeys[-1].name  # just the last key pressed
            key_resp_intro.rt = _key_resp_intro_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction" ---
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_intro.keys in ['', [], None]:  # No response was made
    key_resp_intro.keys = None
thisExp.addData('key_resp_intro.keys',key_resp_intro.keys)
if key_resp_intro.keys != None:  # we had a response
    thisExp.addData('key_resp_intro.rt', key_resp_intro.rt)
thisExp.nextEntry()
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_training = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='trials_training')
thisExp.addLoop(trials_training)  # add the loop to the experiment
thisTrials_training = trials_training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_training.rgb)
if thisTrials_training != None:
    for paramName in thisTrials_training:
        exec('{} = thisTrials_training[paramName]'.format(paramName))

for thisTrials_training in trials_training:
    currentLoop = trials_training
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_training.rgb)
    if thisTrials_training != None:
        for paramName in thisTrials_training:
            exec('{} = thisTrials_training[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial_training" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_training_trial2
    image_text_farsi = 'تست'
    if image_text == 'right':
        image_text_farsi = 'راست'
    elif image_text == 'left':
        image_text_farsi = 'چپ'
    elif image_text == 'No':
        image_text_farsi = 'هیچ'
    image.setImage(cue_image)
    text.setText(image_text_farsi)
    key_resp_training.keys = []
    key_resp_training.rt = []
    _key_resp_training_allKeys = []
    stop_voice_audio.setSound('beep.wav', hamming=True)
    stop_voice_audio.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from code_training_trial
    #I want to create a timer for end routine
    # after 2s if user didn't pressed any button
    
    timing_temp.reset()
    # keep track of which components have finished
    trial_trainingComponents = [image, text, key_resp_training, stop_voice_audio]
    for thisComponent in trial_trainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_training" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # *key_resp_training* updates
        waitOnFlip = False
        if key_resp_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_training.frameNStart = frameN  # exact frame index
            key_resp_training.tStart = t  # local t and not account for scr refresh
            key_resp_training.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_training, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_training.started')
            key_resp_training.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_training.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_training.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_training.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_training_allKeys.extend(theseKeys)
            if len(_key_resp_training_allKeys):
                key_resp_training.keys = _key_resp_training_allKeys[-1].name  # just the last key pressed
                key_resp_training.rt = _key_resp_training_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop stop_voice_audio
        if stop_voice_audio.status == NOT_STARTED and stop_voice_flag == 1:
            # keep track of start time/frame for later
            stop_voice_audio.frameNStart = frameN  # exact frame index
            stop_voice_audio.tStart = t  # local t and not account for scr refresh
            stop_voice_audio.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('stop_voice_audio.started', tThisFlipGlobal)
            stop_voice_audio.play(when=win)  # sync with win flip
        # Run 'Each Frame' code from code_training_trial
        if timing_temp.getTime() >= 2:
            continueRoutine = False
            
        if timing_temp.getTime() >= 300:
            continueRoutine = False
            trials_main.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_training" ---
    for thisComponent in trial_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_training.keys in ['', [], None]:  # No response was made
        key_resp_training.keys = None
    trials_training.addData('key_resp_training.keys',key_resp_training.keys)
    if key_resp_training.keys != None:  # we had a response
        trials_training.addData('key_resp_training.rt', key_resp_training.rt)
    stop_voice_audio.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from code_training_trial
    corr_resp_temp = None
    
    if corr_resp != 'None':
        corr_resp_temp = corr_resp
    
    if corr_resp_temp == key_resp_training.keys:
        accurancy = 1
        thisExp.addData('Accuracy', 1)
    else:
        accurancy = 0
        thisExp.addData('Accuracy', 0)
        
    
    # the Routine "trial_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    timing_temp.reset()
    
    if accurancy == 1:
        feedback_text = 'درست'
        feedback_text_component.color = 'green'
    elif accurancy == 0:
        feedback_text = 'نادرست'
        feedback_text_component.color = 'red'
    
    feedback_text_component.setText(feedback_text)
    # keep track of which components have finished
    feedbackComponents = [feedback_text_component]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from feedback_code
        if timing_temp.getTime() >= 1:
            continueRoutine = False
        
        # *feedback_text_component* updates
        if feedback_text_component.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text_component.frameNStart = frameN  # exact frame index
            feedback_text_component.tStart = t  # local t and not account for scr refresh
            feedback_text_component.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text_component, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text_component.started')
            feedback_text_component.setAutoDraw(True)
        if feedback_text_component.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text_component.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text_component.tStop = t  # not accounting for scr refresh
                feedback_text_component.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_component.stopped')
                feedback_text_component.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from rest_code
    timing_temp.reset()
    # keep track of which components have finished
    restComponents = [plus_image]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *plus_image* updates
        if plus_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            plus_image.frameNStart = frameN  # exact frame index
            plus_image.tStart = t  # local t and not account for scr refresh
            plus_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(plus_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'plus_image.started')
            plus_image.setAutoDraw(True)
        if plus_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > plus_image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                plus_image.tStop = t  # not accounting for scr refresh
                plus_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'plus_image.stopped')
                plus_image.setAutoDraw(False)
        # Run 'Each Frame' code from rest_code
        if timing_temp.getTime() >= 1:
            continueRoutine = False
        
        if overall_timing.getTime() >= 300:
            continueRoutine = False
            trials_main.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'trials_training'


# set up handler to look after randomisation of conditions etc
trials_main = data.TrialHandler(nReps=2000.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='trials_main')
thisExp.addLoop(trials_main)  # add the loop to the experiment
thisTrials_main = trials_main.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_main.rgb)
if thisTrials_main != None:
    for paramName in thisTrials_main:
        exec('{} = thisTrials_main[paramName]'.format(paramName))

for thisTrials_main in trials_main:
    currentLoop = trials_main
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_main.rgb)
    if thisTrials_main != None:
        for paramName in thisTrials_main:
            exec('{} = thisTrials_main[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial_main" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    image_2.setImage(cue_image)
    key_resp_main.keys = []
    key_resp_main.rt = []
    _key_resp_main_allKeys = []
    stop_voice_audio_2.setSound('beep.wav', hamming=True)
    stop_voice_audio_2.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from code_main_trial
    #I want to create a timer for end routine
    # after 2s if user didn't pressed any button
    
    timing_temp.reset()
        
    # keep track of which components have finished
    trial_mainComponents = [image_2, key_resp_main, stop_voice_audio_2]
    for thisComponent in trial_mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_main" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.stopped')
                image_2.setAutoDraw(False)
        
        # *key_resp_main* updates
        waitOnFlip = False
        if key_resp_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_main.frameNStart = frameN  # exact frame index
            key_resp_main.tStart = t  # local t and not account for scr refresh
            key_resp_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_main, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_main.started')
            key_resp_main.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_main.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_main.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_main.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_main_allKeys.extend(theseKeys)
            if len(_key_resp_main_allKeys):
                key_resp_main.keys = _key_resp_main_allKeys[-1].name  # just the last key pressed
                key_resp_main.rt = _key_resp_main_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop stop_voice_audio_2
        if stop_voice_audio_2.status == NOT_STARTED and stop_voice_flag == 1:
            # keep track of start time/frame for later
            stop_voice_audio_2.frameNStart = frameN  # exact frame index
            stop_voice_audio_2.tStart = t  # local t and not account for scr refresh
            stop_voice_audio_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('stop_voice_audio_2.started', tThisFlipGlobal)
            stop_voice_audio_2.play(when=win)  # sync with win flip
        # Run 'Each Frame' code from code_main_trial
        if timing_temp.getTime() >= 2:
            continueRoutine = False
            
        if overall_timing.getTime() >= 300:
            continueRoutine = False
            trials_main.finished = True
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_main" ---
    for thisComponent in trial_mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_main.keys in ['', [], None]:  # No response was made
        key_resp_main.keys = None
    trials_main.addData('key_resp_main.keys',key_resp_main.keys)
    if key_resp_main.keys != None:  # we had a response
        trials_main.addData('key_resp_main.rt', key_resp_main.rt)
    stop_voice_audio_2.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from code_main_trial
    corr_resp_temp = None
    
    if corr_resp != 'None':
        corr_resp_temp = corr_resp
    
    if corr_resp_temp == key_resp_main.keys:
        accurancy = 1
        thisExp.addData('Accuracy', 1)
    else:
        accurancy = 0
        thisExp.addData('Accuracy', 0)
        
    
    # the Routine "trial_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from rest_code
    timing_temp.reset()
    # keep track of which components have finished
    restComponents = [plus_image]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *plus_image* updates
        if plus_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            plus_image.frameNStart = frameN  # exact frame index
            plus_image.tStart = t  # local t and not account for scr refresh
            plus_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(plus_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'plus_image.started')
            plus_image.setAutoDraw(True)
        if plus_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > plus_image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                plus_image.tStop = t  # not accounting for scr refresh
                plus_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'plus_image.stopped')
                plus_image.setAutoDraw(False)
        # Run 'Each Frame' code from rest_code
        if timing_temp.getTime() >= 1:
            continueRoutine = False
        
        if overall_timing.getTime() >= 300:
            continueRoutine = False
            trials_main.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 2000.0 repeats of 'trials_main'


# --- Prepare to start Routine "goodbye" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_bye.keys = []
key_resp_bye.rt = []
_key_resp_bye_allKeys = []
# keep track of which components have finished
goodbyeComponents = [text_2, key_resp_bye]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "goodbye" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    
    # *key_resp_bye* updates
    waitOnFlip = False
    if key_resp_bye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_bye.frameNStart = frameN  # exact frame index
        key_resp_bye.tStart = t  # local t and not account for scr refresh
        key_resp_bye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_bye, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_bye.started')
        key_resp_bye.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_bye.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_bye.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_bye.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_bye.getKeys(keyList=['left','right'], waitRelease=False)
        _key_resp_bye_allKeys.extend(theseKeys)
        if len(_key_resp_bye_allKeys):
            key_resp_bye.keys = _key_resp_bye_allKeys[-1].name  # just the last key pressed
            key_resp_bye.rt = _key_resp_bye_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "goodbye" ---
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_bye.keys in ['', [], None]:  # No response was made
    key_resp_bye.keys = None
thisExp.addData('key_resp_bye.keys',key_resp_bye.keys)
if key_resp_bye.keys != None:  # we had a response
    thisExp.addData('key_resp_bye.rt', key_resp_bye.rt)
thisExp.nextEntry()
# the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
