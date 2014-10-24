import maya.cmds as cmds
def makeGroups():
    cmds.group(em=True, name='nameMe')
    cmds.group(em=True, name='geometry')
    cmds.parent('geometry', 'nameMe')
    cmds.group(em=True, name='globalControl')
    cmds.parent('globalControl', 'nameMe')
    cmds.group(em=True, name='globalScale')
    cmds.parent('globalScale', 'globalControl')
    cmds.group(em=True, name='grpJoint')
    cmds.parent('grpJoint', 'globalScale')
    cmds.group(em=True, name='controlCurves')
    cmds.parent('controlCurves', 'globalScale')
    cmds.group(em=True, name='influenceObjects')
    cmds.parent('influenceObjects', 'globalScale')
    cmds.group(em=True, name='clusterHandles')
    cmds.parent('clusterHandles', 'globalScale')
    cmds.group(em=True, name='extraNodes')
    cmds.parent('extraNodes', 'globalScale')
   
    
#Make the Joints


def getLocPos(locators):
    positions = []
    
    for l in locators:
        positions.append(cmds.pointPosition(l))
    return positions
        
def makeJoints(positions):
    length = len(positions)
    num = 0
    
    cmds.select( d=True )
    for p in positions:
        cmds.joint(p=positions[num])
        
        if num<len:
            num+=1
    
    cmds.select('joint*')
    joints = cmds.ls(selection=True)
    
    return joints

#arms
def runItArm():
    #make a right and left locators available
    cmds.select('loc_l_clavicle01', 'loc_l_shoulder01', 'loc_l_elbow01', 'loc_l_wrist01')
    locatorsL = cmds.ls(selection=True)
    cmds.select('loc_r_clavicle01', 'loc_r_shoulder01', 'loc_r_elbow01', 'loc_r_wrist01')
    locatorsR = cmds.ls(selection=True)    
    
    positionL=getLocPos(locatorsL)
    positionR=getLocPos(locatorsR)
    
    #left arm joints, this way we don't have to worry about things getting messed up in mirroring
    armJointsL = makeJoints(positionL)
    prefix = 'rig_'
    newName = ''
    suffix = []
    num = 0
    
    for a in armJointsL:
        suffix = locatorsL[num].split('_')
        if 'wrist' in suffix[2]:
            newName = 'jnt_'+suffix[1]+'_wrist01'
        else:
            newName = prefix + suffix[1] + '_' + suffix[2]
        cmds.rename(a, newName)
        if num<2:
            num += 1
    
    #right arm joints, this way we don't have to worry about things getting messed up in mirroring
    armJointsR = makeJoints(positionR)
    num = 0
    prefix = 'rig_'
    newName = ''
    suffix = []
    num = 0
    
    for a in armJointsR:
        suffix = locatorsR[num].split('_')
        if 'wrist' in suffix[2]:
            newName = 'jnt_'+suffix[1]+'_wrist01'
        else:
            newName = prefix + suffix[1] + '_' + suffix[2]
            
        cmds.rename(a, newName)
        if num<2:
            num += 1
            
    cmds.parent('rig_*_clavicle01', 'grpJoint')
    
    
#feet
def runItFeet():
    #make a right and left locators available
    cmds.select('loc_l_ankle01', 'loc_l_ball01', 'loc_l_toeTip')
    locatorsL = cmds.ls(selection=True)
    cmds.select('loc_r_ankle01', 'loc_r_ball01', 'loc_r_toeTip')
    locatorsR = cmds.ls(selection=True)    
    
    positionL=getLocPos(locatorsL)
    positionR=getLocPos(locatorsR)
    
    #left foot joints, this way we don't have to worry about things getting messed up in mirroring
    footJointsL = makeJoints(positionL)
    prefix = 'rig_'
    newName = ''
    suffix = []
    num = 0
    
    for f in footJointsL:
        suffix = locatorsL[num].split('_')
        if 'Tip' in suffix[2]:
            newName = 'jnt_'+suffix[1]+'_toeTip'
        else:
            newName = prefix + suffix[1] + '_' + suffix[2]
        cmds.rename(f, newName)
        if num<2:
            num += 1
    
    #right foot joints, this way we don't have to worry about things getting messed up in mirroring
    armJointsR = makeJoints(positionR)
    num = 0
    prefix = 'rig_'
    newName = ''
    suffix = []
    num = 0
    
    for f in footJointsL:
        suffix = locatorsR[num].split('_')
        if 'Tip' in suffix[2]:
            newName = 'jnt_'+suffix[1]+'_toeTip'
        else:
            newName = prefix + suffix[1] + '_' + suffix[2]
        cmds.rename(f, newName)
        if num<2:
            num += 1
            
    cmds.parent('rig_*_ankle01', 'grpJoint')
    
#legs
def runItLeg():
    #make a right and left locators available
    cmds.select('loc_l_hip01', 'loc_l_knee01', 'loc_l_ankle01')
    locatorsL = cmds.ls(selection=True)
    cmds.select('loc_r_hip01', 'loc_r_knee01', 'loc_r_ankle01')
    locatorsR = cmds.ls(selection=True)    
    
    positionL=getLocPos(locatorsL)
    positionR=getLocPos(locatorsR)
    
    #left leg joints, this way we don't have to worry about things getting messed up in mirroring
    legJointsL = makeJoints(positionL)
    prefix = 'rig_'
    newName = ''
    suffix = []
    num = 0
    
    for l in legJointsL:
        suffix = locatorsL[num].split('_')
        if 'ankle' in suffix[2]:
            newName = 'jnt_' + suffix[1] + '_' + suffix[2]
        else:
            newName = prefix + suffix[1] + '_' + suffix[2]
        cmds.rename(l, newName)
        if num<3:
            num += 1
    
    #right leg joints, this way we don't have to worry about things getting messed up in mirroring
    legJointsR = makeJoints(positionR)
    prefix = 'rig_'
    newName = ''
    suffix = []
    num = 0
    
    for l in legJointsR:
        suffix = locatorsR[num].split('_')
        if 'ankle' in suffix[2]:
            newName = 'jnt_' + suffix[1] + '_' + suffix[2]
        else:
            newName = prefix + suffix[1] + '_' + suffix[2]
        cmds.rename(l, newName)
        if num<3:
            num += 1
            
    cmds.parent('rig_*_hip01', 'grpJoint')

#Make Center Joints
def runItCenter():
    cmds.select('loc_pelvis01', 'loc_spine01', 'loc_spine02', 'loc_spine03', 'loc_neckBase01', 'loc_neck01', 'loc_headBase01', 'loc_head01', 'loc_headTip', 'loc_jaw01', 'loc_jawTip')
    locators = cmds.ls(selection=True)
    
    positions=getLocPos(locators)
    
    centerJoints = makeJoints(positions)
    
    newName = ''
    suffix = []
    num = 0
    length = len(locators)
    
    for c in centerJoints:
        suffix = locators[num].split('_')
        if 'Tip' in suffix[1]:
            newName = 'jnt_' + suffix[1]
        else:
            newName = 'rig_' + suffix[1]
        cmds.rename(c, newName)
        if num < length:
            num+=1
            
    
    cmds.parent('rig_jaw01', 'rig_head01')
    cmds.parent('rig_pelvis01', 'grpJoint')
    
    
#Make Hand Joints
def runItHand():
    cmds.select('loc_l_wrist01', 'loc_l_palm01', 'loc_l_thumb01', 'loc_l_thumb02', 'loc_l_thumb03', 'loc_l_thumbTip', 'loc_l_index01', 'loc_l_index02', 'loc_l_index03', 'loc_l_indexTip', 'loc_l_middle01', 'loc_l_middle02', 'loc_l_middle03', 'loc_l_middleTip', 'loc_l_ring01', 'loc_l_ring02', 'loc_l_ring03', 'loc_l_ringTip', 'loc_l_pinky01', 'loc_l_pinky02', 'loc_l_pinky03', 'loc_l_pinkyTip', 'loc_r_wrist01', 'loc_r_palm01', 'loc_r_thumb01', 'loc_r_thumb02', 'loc_r_thumb03', 'loc_r_thumbTip', 'loc_r_index01', 'loc_r_index02', 'loc_r_index03', 'loc_r_indexTip', 'loc_r_middle01', 'loc_r_middle02', 'loc_r_middle03', 'loc_r_middleTip', 'loc_r_ring01', 'loc_r_ring02', 'loc_r_ring03', 'loc_r_ringTip', 'loc_r_pinky01', 'loc_r_pinky02', 'loc_r_pinky03', 'loc_r_pinkyTip')
    locators = cmds.ls(selection=True)
    
    positions = getLocPos(locators)

    handJoints = makeJoints(positions)
    
    newName = ''
    suffix = []
    num = 0
    length = len(locators)
    
    for h in handJoints:
        suffix = locators[num].split('_')
        if 'Tip' in suffix[2]:
            newName = 'jnt_' + suffix[1] + '_' + suffix[2]
        else:
            newName = 'rig_' + suffix[1] + '_' + suffix[2]
        cmds.rename(h, newName)
        if num < length:
            num+=1
            
            
    
    cmds.parent('rig_l_index01', 'rig_l_palm01')
    cmds.parent('rig_r_index01', 'rig_r_palm01')
    cmds.parent('rig_l_middle01', 'rig_l_palm01')
    cmds.parent('rig_r_middle01', 'rig_r_palm01')
    cmds.parent('rig_l_ring01', 'rig_l_palm01')
    cmds.parent('rig_r_ring01', 'rig_r_palm01')
    cmds.parent('rig_l_pinky01', 'rig_l_palm01')
    cmds.parent('rig_r_pinky01', 'rig_r_palm01')
    cmds.parent('rig_*_wrist01', 'grpJoint')
    
    

makeGroups()
runItArm()
runItLeg()
runItCenter()
runItHand()
runItFeet()
