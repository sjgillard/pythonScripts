import maya.cmds as cmds


def mirrorLocators():
    cmds.group(cmds.ls(selection=True), n='temp1')
    cmds.duplicate('temp1')
    cmds.setAttr('temp2.scalePivot', 0,0,0)
    cmds.setAttr('temp2.rotatePivot', 0,0,0)
    cmds.setAttr('temp2.scaleX', -1)
    cmds.select( 'temp2')
    cmds.makeIdentity(apply=True)
    
    children = cmds.listRelatives('temp2', children=True, type='transform', fullPath=True)
    prefixL = 'loc_l_'
    prefixR = 'loc_r_'
    newName = ''
    substring = []
    for i in children:
        substring = i.split('_')
        if prefixL in i:
            newName = prefixR + substring[2]
            cmds.rename(i, newName)
        else:
            newName = prefixL + substring[2]
            cmds.rename(i, newName)

    cmds.select('loc*')
    locators = [cmds.ls(selection=True)]
    for i in locators:
        cmds.parent(i, world=True)
        
    cmds.delete('temp1')
    cmds.delete('temp2')

    
mirrorLocators()