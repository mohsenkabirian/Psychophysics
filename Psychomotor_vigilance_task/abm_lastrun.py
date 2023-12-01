#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on June 10, 2023, at 20:08
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
psychopyVersion = '2022.2.4'
expName = 'abm'  # from the Builder filename that created this script
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
    originPath='E:\\Projects\\pychopy\\vigilance_mine - Copy\\abm\\abm_lastrun.py',
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
    monitor='testMonitor', color='white', colorSpace='rgb',
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

# --- Initialize components for Routine "Instruction" ---
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text='سلام به تسک گوش به زنگی خوش آمدید\nبه محض این که شمارشگر را وسط صفحه دیدید\nکلید فاصله را فشار دهید\nطول تسک : 5 دقیقه',
    font='B Nazanin',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);
key_instruct = keyboard.Keyboard()

# --- Initialize components for Routine "ISI" ---
# Run 'Begin Experiment' code from code
# All the durations are in seconds
# Random ISI between 1 and 4. 
minISI = 1
maxISI = 4

# Task duration
length_of_task = 300

# Feedback duration 
feed = 0.5

# A timer
timing = core.Clock()

# Loading the beep sound
warning_beep = sound.Sound('beep.wav')
ISI_text = visual.TextStim(win=win, name='ISI_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
dontrespond = keyboard.Keyboard()

# --- Initialize components for Routine "Target" ---
up_key = keyboard.Keyboard()
target_text = visual.TextStim(win=win, name='target_text',
    text='',
    font='B Nazanin',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# --- Initialize components for Routine "Feedback" ---
Feedback_text = visual.TextStim(win=win, name='Feedback_text',
    text='',
    font='B Nazanin',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);

# --- Initialize components for Routine "End_task" ---

# --- Initialize components for Routine "The_end" ---
end_key = keyboard.Keyboard()
goodbye_text = visual.TextStim(win=win, name='goodbye_text',
    text='پایان\nممنون از توجه شما\nبرای خروج کلید فاصله را فشار دهید',
    font='B Nazanin',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_instruct.keys = []
key_instruct.rt = []
_key_instruct_allKeys = []
# keep track of which components have finished
InstructionComponents = [instruct_text, key_instruct]
for thisComponent in InstructionComponents:
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

# --- Run Routine "Instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_text* updates
    if instruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text.frameNStart = frameN  # exact frame index
        instruct_text.tStart = t  # local t and not account for scr refresh
        instruct_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruct_text.started')
        instruct_text.setAutoDraw(True)
    
    # *key_instruct* updates
    waitOnFlip = False
    if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruct.frameNStart = frameN  # exact frame index
        key_instruct.tStart = t  # local t and not account for scr refresh
        key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_instruct.started')
        key_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_instruct.getKeys(keyList=['space'], waitRelease=False)
        _key_instruct_allKeys.extend(theseKeys)
        if len(_key_instruct_allKeys):
            key_instruct.keys = _key_instruct_allKeys[-1].name  # just the last key pressed
            key_instruct.rt = _key_instruct_allKeys[-1].rt
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
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction" ---
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_instruct.keys in ['', [], None]:  # No response was made
    key_instruct.keys = None
thisExp.addData('key_instruct.keys',key_instruct.keys)
if key_instruct.keys != None:  # we had a response
    thisExp.addData('key_instruct.rt', key_instruct.rt)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
abm_trials = data.TrialHandler(nReps=120.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='abm_trials')
thisExp.addLoop(abm_trials)  # add the loop to the experiment
thisAbm_trial = abm_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAbm_trial.rgb)
if thisAbm_trial != None:
    for paramName in thisAbm_trial:
        exec('{} = thisAbm_trial[paramName]'.format(paramName))

for thisAbm_trial in abm_trials:
    currentLoop = abm_trials
    # abbreviate parameter names if possible (e.g. rgb = thisAbm_trial.rgb)
    if thisAbm_trial != None:
        for paramName in thisAbm_trial:
            exec('{} = thisAbm_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    # ISI is then set each routine
    randISI = random() * (maxISI - minISI) + minISI
    
    # If it is the first trial
    if abm_trials.thisN == 0:
        overall_timer = core.Clock()
        realISI = 0
        
    if abm_trials.thisN > 0:
        # We count the duration of the feedback as part of the ISI
        realISI = feed
    
    # A message when participant miss
    message = 'You did not hit the button!'
    
    # Adding the ISI so it is saved in the datafile
    thisExp.addData('ISI', randISI)
    dontrespond.keys = []
    dontrespond.rt = []
    _dontrespond_allKeys = []
    # keep track of which components have finished
    ISIComponents = [ISI_text, dontrespond]
    for thisComponent in ISIComponents:
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
    
    # --- Run Routine "ISI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code
        keys = dontrespond.getKeys(keyList=['space'], waitRelease=False)
        keys = [key.name for key in keys]
        
        # Append True to list if a key is pressed, clear list if not
        if "space" in keys:
             message = "خیلی زود!"
             continueRoutine = False
        
        # *ISI_text* updates
        if ISI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_text.frameNStart = frameN  # exact frame index
            ISI_text.tStart = t  # local t and not account for scr refresh
            ISI_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI_text.started')
            ISI_text.setAutoDraw(True)
        if ISI_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_text.tStartRefresh + randISI - realISI-frameTolerance:
                # keep track of stop time/frame for later
                ISI_text.tStop = t  # not accounting for scr refresh
                ISI_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI_text.stopped')
                ISI_text.setAutoDraw(False)
        
        # *dontrespond* updates
        waitOnFlip = False
        if dontrespond.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dontrespond.frameNStart = frameN  # exact frame index
            dontrespond.tStart = t  # local t and not account for scr refresh
            dontrespond.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dontrespond, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dontrespond.started')
            dontrespond.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(dontrespond.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(dontrespond.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if dontrespond.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dontrespond.tStartRefresh + randISI - 1-frameTolerance:
                # keep track of stop time/frame for later
                dontrespond.tStop = t  # not accounting for scr refresh
                dontrespond.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dontrespond.stopped')
                dontrespond.status = FINISHED
        if dontrespond.status == STARTED and not waitOnFlip:
            theseKeys = dontrespond.getKeys(keyList=['up'], waitRelease=False)
            _dontrespond_allKeys.extend(theseKeys)
            if len(_dontrespond_allKeys):
                dontrespond.keys = _dontrespond_allKeys[-1].name  # just the last key pressed
                dontrespond.rt = _dontrespond_allKeys[-1].rt
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
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if dontrespond.keys in ['', [], None]:  # No response was made
        dontrespond.keys = None
    abm_trials.addData('dontrespond.keys',dontrespond.keys)
    if dontrespond.keys != None:  # we had a response
        abm_trials.addData('dontrespond.rt', dontrespond.rt)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Target" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    up_key.keys = []
    up_key.rt = []
    _up_key_allKeys = []
    # Run 'Begin Routine' code from Target_code
    # Reset the timer
    timing.reset()
    
    # Check for response
    if message == 'خیلی زود!':
        # Adding 0 to Accuracy and missing to RTms
        thisExp.addData('Accuracy', 0)
        thisExp.addData('RTms', np.NAN)
        # End the Routine to continue next trial
        continueRoutine = False
        
    positions_list = [0.6,-0.6]
    # keep track of which components have finished
    TargetComponents = [up_key, target_text]
    for thisComponent in TargetComponents:
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
    
    # --- Run Routine "Target" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *up_key* updates
        waitOnFlip = False
        if up_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            up_key.frameNStart = frameN  # exact frame index
            up_key.tStart = t  # local t and not account for scr refresh
            up_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(up_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'up_key.started')
            up_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(up_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(up_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if up_key.status == STARTED and not waitOnFlip:
            theseKeys = up_key.getKeys(keyList=['space'], waitRelease=False)
            _up_key_allKeys.extend(theseKeys)
            if len(_up_key_allKeys):
                up_key.keys = _up_key_allKeys[-1].name  # just the last key pressed
                up_key.rt = _up_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Target_code
        time = int(round(timing.getTime(), 3) * 1000)
        
        # *target_text* updates
        if target_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_text.frameNStart = frameN  # exact frame index
            target_text.tStart = t  # local t and not account for scr refresh
            target_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_text.started')
            target_text.setAutoDraw(True)
        if target_text.status == STARTED:  # only update if drawing
            target_text.setText(time, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TargetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Target" ---
    for thisComponent in TargetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if up_key.keys in ['', [], None]:  # No response was made
        up_key.keys = None
    abm_trials.addData('up_key.keys',up_key.keys)
    if up_key.keys != None:  # we had a response
        abm_trials.addData('up_key.rt', up_key.rt)
    # Run 'End Routine' code from Target_code
    if type(up_key.rt) is float:
        message = str(round(up_key.rt * 1000))
        thisExp.addData('Accuracy', 1)
        thisExp.addData('RTms', up_key.rt * 1000)
        
    # PsychoPy is not running the trial for more than 29.991...
    if timing.getTime() >= 29.99:
            message = 'No response!'
            warning_beep.play()
            up_key.rt = timing.getTime()
            thisExp.addData('RTms', np.NAN)
            thisExp.addData('Accuracy', 0)
            continueRoutine = False
    # the Routine "Target" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Feedback_text.setText(message)
    # keep track of which components have finished
    FeedbackComponents = [Feedback_text]
    for thisComponent in FeedbackComponents:
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
    
    # --- Run Routine "Feedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback_text* updates
        if Feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Feedback_text.frameNStart = frameN  # exact frame index
            Feedback_text.tStart = t  # local t and not account for scr refresh
            Feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Feedback_text.started')
            Feedback_text.setAutoDraw(True)
        if Feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback_text.tStartRefresh + feed-frameTolerance:
                # keep track of stop time/frame for later
                Feedback_text.tStop = t  # not accounting for scr refresh
                Feedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback_text.stopped')
                Feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback" ---
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "End_task" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    End_taskComponents = []
    for thisComponent in End_taskComponents:
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
    
    # --- Run Routine "End_task" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_task" ---
    for thisComponent in End_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from end_code
    # Get the time in the task
    time_in_task = overall_timer.getTime()
    
    # If time_in_task corresponds to the duration we set previously we end te task
    if time_in_task >= length_of_task:
        continueRoutine = False
        abm_trials.finished = True
    # the Routine "End_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 120.0 repeats of 'abm_trials'


# --- Prepare to start Routine "The_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_key.keys = []
end_key.rt = []
_end_key_allKeys = []
# keep track of which components have finished
The_endComponents = [end_key, goodbye_text]
for thisComponent in The_endComponents:
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

# --- Run Routine "The_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_key* updates
    waitOnFlip = False
    if end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key.frameNStart = frameN  # exact frame index
        end_key.tStart = t  # local t and not account for scr refresh
        end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_key.started')
        end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key.status == STARTED and not waitOnFlip:
        theseKeys = end_key.getKeys(keyList=['space'], waitRelease=False)
        _end_key_allKeys.extend(theseKeys)
        if len(_end_key_allKeys):
            end_key.keys = _end_key_allKeys[-1].name  # just the last key pressed
            end_key.rt = _end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *goodbye_text* updates
    if goodbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye_text.frameNStart = frameN  # exact frame index
        goodbye_text.tStart = t  # local t and not account for scr refresh
        goodbye_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'goodbye_text.started')
        goodbye_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in The_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "The_end" ---
for thisComponent in The_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_key.keys in ['', [], None]:  # No response was made
    end_key.keys = None
thisExp.addData('end_key.keys',end_key.keys)
if end_key.keys != None:  # we had a response
    thisExp.addData('end_key.rt', end_key.rt)
thisExp.nextEntry()
# the Routine "The_end" was not non-slip safe, so reset the non-slip timer
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
