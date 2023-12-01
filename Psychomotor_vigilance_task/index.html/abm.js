/************ 
 * Abm Test *
 ************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'abm';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionRoutineBegin());
flowScheduler.add(InstructionRoutineEachFrame());
flowScheduler.add(InstructionRoutineEnd());
const abm_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(abm_trialsLoopBegin(abm_trialsLoopScheduler));
flowScheduler.add(abm_trialsLoopScheduler);
flowScheduler.add(abm_trialsLoopEnd);
flowScheduler.add(The_endRoutineBegin());
flowScheduler.add(The_endRoutineEachFrame());
flowScheduler.add(The_endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var InstructionClock;
var instruct_text;
var key_instruct;
var ISIClock;
var ISI_text;
var dontrespond;
var TargetClock;
var up_key;
var target_text;
var FeedbackClock;
var Feedback_text;
var End_taskClock;
var The_endClock;
var end_key;
var goodbye_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instruction"
  InstructionClock = new util.Clock();
  instruct_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text',
    text: 'پوریا پورپ',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_instruct = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISI_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ISI_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  dontrespond = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Target"
  TargetClock = new util.Clock();
  up_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  target_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'target_text',
    text: '',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  Feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback_text',
    text: '',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "End_task"
  End_taskClock = new util.Clock();
  // Initialize components for Routine "The_end"
  The_endClock = new util.Clock();
  end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  goodbye_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'goodbye_text',
    text: 'Finished.\nThank you for your attention.\nPress "SPACE" for end.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_instruct_allKeys;
var InstructionComponents;
function InstructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction' ---
    t = 0;
    InstructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_instruct.keys = undefined;
    key_instruct.rt = undefined;
    _key_instruct_allKeys = [];
    // keep track of which components have finished
    InstructionComponents = [];
    InstructionComponents.push(instruct_text);
    InstructionComponents.push(key_instruct);
    
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction' ---
    // get current time
    t = InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruct_text* updates
    if (t >= 0.0 && instruct_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_text.tStart = t;  // (not accounting for frame time here)
      instruct_text.frameNStart = frameN;  // exact frame index
      
      instruct_text.setAutoDraw(true);
    }

    
    // *key_instruct* updates
    if (t >= 0.0 && key_instruct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_instruct.tStart = t;  // (not accounting for frame time here)
      key_instruct.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_instruct.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_instruct.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_instruct.clearEvents(); });
    }

    if (key_instruct.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_instruct.getKeys({keyList: ['space'], waitRelease: false});
      _key_instruct_allKeys = _key_instruct_allKeys.concat(theseKeys);
      if (_key_instruct_allKeys.length > 0) {
        key_instruct.keys = _key_instruct_allKeys[_key_instruct_allKeys.length - 1].name;  // just the last key pressed
        key_instruct.rt = _key_instruct_allKeys[_key_instruct_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction' ---
    for (const thisComponent of InstructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_instruct.corr, level);
    }
    psychoJS.experiment.addData('key_instruct.keys', key_instruct.keys);
    if (typeof key_instruct.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_instruct.rt', key_instruct.rt);
        routineTimer.reset();
        }
    
    key_instruct.stop();
    // the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var abm_trials;
function abm_trialsLoopBegin(abm_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    abm_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 120, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'abm_trials'
    });
    psychoJS.experiment.addLoop(abm_trials); // add the loop to the experiment
    currentLoop = abm_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisAbm_trial of abm_trials) {
      snapshot = abm_trials.getSnapshot();
      abm_trialsLoopScheduler.add(importConditions(snapshot));
      abm_trialsLoopScheduler.add(ISIRoutineBegin(snapshot));
      abm_trialsLoopScheduler.add(ISIRoutineEachFrame());
      abm_trialsLoopScheduler.add(ISIRoutineEnd(snapshot));
      abm_trialsLoopScheduler.add(TargetRoutineBegin(snapshot));
      abm_trialsLoopScheduler.add(TargetRoutineEachFrame());
      abm_trialsLoopScheduler.add(TargetRoutineEnd(snapshot));
      abm_trialsLoopScheduler.add(FeedbackRoutineBegin(snapshot));
      abm_trialsLoopScheduler.add(FeedbackRoutineEachFrame());
      abm_trialsLoopScheduler.add(FeedbackRoutineEnd(snapshot));
      abm_trialsLoopScheduler.add(End_taskRoutineBegin(snapshot));
      abm_trialsLoopScheduler.add(End_taskRoutineEachFrame());
      abm_trialsLoopScheduler.add(End_taskRoutineEnd(snapshot));
      abm_trialsLoopScheduler.add(abm_trialsLoopEndIteration(abm_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function abm_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(abm_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function abm_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _dontrespond_allKeys;
var ISIComponents;
function ISIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ISI' ---
    t = 0;
    ISIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dontrespond.keys = undefined;
    dontrespond.rt = undefined;
    _dontrespond_allKeys = [];
    // keep track of which components have finished
    ISIComponents = [];
    ISIComponents.push(ISI_text);
    ISIComponents.push(dontrespond);
    
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ISIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ISI' ---
    // get current time
    t = ISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ISI_text* updates
    if (t >= 0.0 && ISI_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI_text.tStart = t;  // (not accounting for frame time here)
      ISI_text.frameNStart = frameN;  // exact frame index
      
      ISI_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + (randISI - realISI) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ISI_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ISI_text.setAutoDraw(false);
    }
    
    // *dontrespond* updates
    if (t >= 0.0 && dontrespond.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dontrespond.tStart = t;  // (not accounting for frame time here)
      dontrespond.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { dontrespond.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { dontrespond.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { dontrespond.clearEvents(); });
    }

    frameRemains = 0.0 + (randISI - 1) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dontrespond.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dontrespond.status = PsychoJS.Status.FINISHED;
  }

    if (dontrespond.status === PsychoJS.Status.STARTED) {
      let theseKeys = dontrespond.getKeys({keyList: ['up'], waitRelease: false});
      _dontrespond_allKeys = _dontrespond_allKeys.concat(theseKeys);
      if (_dontrespond_allKeys.length > 0) {
        dontrespond.keys = _dontrespond_allKeys[_dontrespond_allKeys.length - 1].name;  // just the last key pressed
        dontrespond.rt = _dontrespond_allKeys[_dontrespond_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ISI' ---
    for (const thisComponent of ISIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(dontrespond.corr, level);
    }
    psychoJS.experiment.addData('dontrespond.keys', dontrespond.keys);
    if (typeof dontrespond.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('dontrespond.rt', dontrespond.rt);
        routineTimer.reset();
        }
    
    dontrespond.stop();
    // the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _up_key_allKeys;
var TargetComponents;
function TargetRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Target' ---
    t = 0;
    TargetClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    up_key.keys = undefined;
    up_key.rt = undefined;
    _up_key_allKeys = [];
    // keep track of which components have finished
    TargetComponents = [];
    TargetComponents.push(up_key);
    TargetComponents.push(target_text);
    
    for (const thisComponent of TargetComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TargetRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Target' ---
    // get current time
    t = TargetClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *up_key* updates
    if (t >= 0.0 && up_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      up_key.tStart = t;  // (not accounting for frame time here)
      up_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { up_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { up_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { up_key.clearEvents(); });
    }

    if (up_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = up_key.getKeys({keyList: ['space'], waitRelease: false});
      _up_key_allKeys = _up_key_allKeys.concat(theseKeys);
      if (_up_key_allKeys.length > 0) {
        up_key.keys = _up_key_allKeys[_up_key_allKeys.length - 1].name;  // just the last key pressed
        up_key.rt = _up_key_allKeys[_up_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *target_text* updates
    if (t >= 0.0 && target_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_text.tStart = t;  // (not accounting for frame time here)
      target_text.frameNStart = frameN;  // exact frame index
      
      target_text.setAutoDraw(true);
    }

    
    if (target_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      target_text.setText(time, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TargetComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TargetRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Target' ---
    for (const thisComponent of TargetComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(up_key.corr, level);
    }
    psychoJS.experiment.addData('up_key.keys', up_key.keys);
    if (typeof up_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('up_key.rt', up_key.rt);
        routineTimer.reset();
        }
    
    up_key.stop();
    // the Routine "Target" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackComponents;
function FeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Feedback' ---
    t = 0;
    FeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Feedback_text.setText(message);
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(Feedback_text);
    
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Feedback' ---
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Feedback_text* updates
    if (t >= 0.0 && Feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Feedback_text.tStart = t;  // (not accounting for frame time here)
      Feedback_text.frameNStart = frameN;  // exact frame index
      
      Feedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + feed - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Feedback' ---
    for (const thisComponent of FeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var End_taskComponents;
function End_taskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End_task' ---
    t = 0;
    End_taskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    End_taskComponents = [];
    
    for (const thisComponent of End_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function End_taskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End_task' ---
    // get current time
    t = End_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of End_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function End_taskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End_task' ---
    for (const thisComponent of End_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "End_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _end_key_allKeys;
var The_endComponents;
function The_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'The_end' ---
    t = 0;
    The_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    end_key.keys = undefined;
    end_key.rt = undefined;
    _end_key_allKeys = [];
    // keep track of which components have finished
    The_endComponents = [];
    The_endComponents.push(end_key);
    The_endComponents.push(goodbye_text);
    
    for (const thisComponent of The_endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function The_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'The_end' ---
    // get current time
    t = The_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_key* updates
    if (t >= 0.0 && end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_key.tStart = t;  // (not accounting for frame time here)
      end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_key.clearEvents(); });
    }

    if (end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_key.getKeys({keyList: ['space'], waitRelease: false});
      _end_key_allKeys = _end_key_allKeys.concat(theseKeys);
      if (_end_key_allKeys.length > 0) {
        end_key.keys = _end_key_allKeys[_end_key_allKeys.length - 1].name;  // just the last key pressed
        end_key.rt = _end_key_allKeys[_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *goodbye_text* updates
    if (t >= 0.0 && goodbye_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goodbye_text.tStart = t;  // (not accounting for frame time here)
      goodbye_text.frameNStart = frameN;  // exact frame index
      
      goodbye_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of The_endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function The_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'The_end' ---
    for (const thisComponent of The_endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(end_key.corr, level);
    }
    psychoJS.experiment.addData('end_key.keys', end_key.keys);
    if (typeof end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_key.rt', end_key.rt);
        routineTimer.reset();
        }
    
    end_key.stop();
    // the Routine "The_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
