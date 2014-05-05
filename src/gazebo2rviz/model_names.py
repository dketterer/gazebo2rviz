import re

worldLinkName = 'gazebo_world'
baseLinkNames = ['link', 'base', 'base_link', 'world_link']
baseLinkNameEndings = ['_base', '_base_link', '_world_link']
splitString = '::'
joinString = '__'

def isBaseLinkName(modelName, linkName):
  return (linkName in baseLinkNames) \
         or (linkName == modelName + '_link') \
         or any(linkName.endswith(suffix) for suffix in baseLinkNameEndings)

def splitName(name):
  nameSplitters = name.split(splitString)
  (modelName, linkName) = nameSplitters[-2:]
  if len(nameSplitters) > 2:
    [parentName] = nameSplitters[-3:-2]
  else:
    parentName = worldLinkName
  return (parentName, modelName, linkName)

def prefixName(name, part):
  if part == worldLinkName:
    return part

  nameSplitters = name.split(splitString)
  #print('name=%s part=%s' % (name, part))
  if not part in nameSplitters:
    raise RuntimeError('prefixName: part name must be part of name string')

  res = ''
  for splitter in nameSplitters:
    if res:
      res += joinString
    res += splitter
    if splitter == part:
      break

  return res


def name2modelName(name):
 # Cope with
 # - adding the same model multiple times through the GUI
 # - renamed models (e.g. because model occurs multiple times as sub-model)
 modelname = re.sub('_[0-9]*$', '', name)
 modelname = re.sub('@.*$', '', modelname)
 return modelname
