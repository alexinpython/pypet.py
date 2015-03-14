## With much thanks! - Pypet game based on guide from:
## http://www.thinkful.com/learn/python-programming-fundamentals/
## Special thanks to the author(s) of the guide:
## http://inventwithpython.com/inventwithpython_3rd.pdf

##pets##
fish = {
  'name': 'Fishy',
  'hungry': True,
  'weight': 2.6,
  'age': 2,
  'photo': '<`)))><',
  'adopted': False,
  'mood': 'Sad',
}

mouse = {
  'name': 'Mousey',
  'hungry': True,
  'weight': 0.4,
  'age': 3,
  'photo': '<:3 )~~~~',
  'adopted': False,
  'mood': 'Sad',
}

pig = {
  'name': 'Piggy',
  'hungry': True,
  'weight': 150,
  'age': 4,
  'photo': '^(*(oo)*)^ ',
  'adopted': False,
  'mood': 'Sad',
}

##lists##
pets = [fish, mouse, pig]

##pet functions##
def inspect(pet):
  print '-------------------------------------'
  print pet['photo']  
  print 'Name: ' + pet['name']
  print 'Age: ' + str(pet['age']) + ' years'
  print 'Weight: ' + str(pet['weight']) + ' lbs'
  print 'Mood: ' + pet['mood']
  print 'Hungry? ' + str(pet['hungry'])
  print '-------------------------------------'
  pausecommand()
  petmenu(pet)
  
def sleep(pet):
  if pet['mood'] == 'Happy':
    pet['mood'] = 'Content'
    print pet['name'] + ' has taken a nap.'
    pausecommand()
    petmenu(pet)    
  elif pet['mood'] == 'Content':
    pet['hungry'] = True
    pet['mood'] = 'Sad'
    print pet['name'] + ' has slept for hours.'
    pausecommand()
    petmenu(pet)
  elif pet['hungry'] == True:
    print pet['name'] + ' is too hungry to sleep!'
    pausecommand()
    petmenu(pet)
  else:
    print pet['name'] + ' is too sad to sleep!'
    pausecommand()
    petmenu(pet)
    
def feed(pet):
  if pet['hungry'] == True:
    pet['hungry'] = False
    pet['weight'] = pet['weight'] + 1
    print 'yummy!'
    pausecommand()
    petmenu(pet)
  else:
    print pet['name'] + ' is not hungry!'
    pausecommand()
    petmenu(pet)

def play(pet):
  if pet['hungry'] == True:
    print 'Your pet is too hungry to play!'
    pausecommand()
    petmenu(pet)
  elif pet['mood'] == 'Sad':
    pet['mood'] = 'Content'
    pet['weight'] = pet['weight'] - 0.25
    print 'yay!'
    pausecommand()
    petmenu(pet)
  elif pet['mood'] == 'Content':
    pet['mood'] = 'Happy'
    pet['weight'] = pet['weight'] - 0.75
    print 'wow! yay! woo!'
    pausecommand()
    petmenu(pet)
  else:
    print pet['name'] + ' is so happy!'
    pausecommand()
    petmenu(pet)
  
def adopt(pet):
  if pet['adopted'] == False:
    pet['adopted'] = True
    pet['mood'] = 'Happy'
    print 'You have adopted ' + pet['name'] + '!'
    pausecommand()
    adoptmenu()
  else:
    print pet['name'] + ' has already been adopted!'
    pausecommand()
    adoptmenu()
    
##pause command##
def pausecommand():
  while True:
    if not raw_input('Press Enter to continue '):
        break

##menu - adoption##
def adoptmenu():
  print '-------------------------------------'
  print 'The following pets are available for'
  print 'adpotion.'
  print 'Which pet would you like to adopt?'
  print '1. ' + fish['name']
  print '2. ' + mouse['name']
  print '3. ' + pig['name']
  print '4. return to main menu'
  print '-------------------------------------'
  adoptinput = raw_input(':')
  if adoptinput == '1':
    adopt(fish)
  elif adoptinput == '2':
    adopt(mouse)
  elif adoptinput == '3':
    adopt(pig)
  elif adoptinput == '4':
    mainmenu()
  else:
    print 'ERROR, please choose option 1, 2, 3, or 4.'
    pausecommand()
    adoptmenu()
    
##is adopted check function##
def isadopted(pet):
  if pet['adopted'] == False:
    print 'You have not adopted this pet yet!'
    pausecommand()
    mymenu()
  else:
    petmenu(pet)

##menu - my adopted pypets##
def mymenu():
  print '-------------------------------------'
  print 'Here are your adopted pypets.'
  print 'Which pet would you like to visit?'
  print '1. ' + fish['name']
  print '2. ' + mouse['name']
  print '3. ' + pig['name']
  print '4. return to main menu'
  print '-------------------------------------'
  myinput = raw_input(':')
  if myinput == '1':
    isadopted(fish)
  elif myinput == '2':
    isadopted(mouse)
  elif myinput == '3':
    isadopted(pig)
  elif myinput == '4':
    mainmenu()
  else:
    print 'ERROR, please choose option 1, 2, 3, or 4.'
    pausecommand()
    mymenu()

##menu - pet interaction menu##
def petmenu(pet):
  print '-------------------------------------'
  print 'You are now with ' + pet['name']
  print 'What would you like to do?'
  print '1. Inspect ' + pet['name']
  print '2. Feed ' + pet['name'] + ' food'
  print '3. Play with ' + pet['name']
  print '4. Put ' + pet['name'] + ' to bed'
  print '5. Return to my pets menu'
  print '-------------------------------------'
  petinput = raw_input(':')
  if petinput == '1':
    inspect(pet)
  elif petinput == '2':
    feed(pet)
  elif petinput == '3':
    play(pet)
  elif petinput == '4':
    sleep(pet)
  elif petinput == '5':
    mymenu()
  else:
    print 'ERROR, please choose option 1, 2, 3, 4, or 5.'
    pausecommand()
    petmenu(pet)    
    
##menu - exit##
def exitmenu():
  print '-------------------------------------'
  print 'Do you really want to Exit?'
  print '1. Yes'
  print '2. No'
  print '-------------------------------------'
  exitinput = raw_input(':')
  if exitinput == '1':
    import sys
    sys.exit(0)
  elif exitinput == '2':
    mainmenu()
  else:
    print 'ERROR, please choose option 1, or 2.'
    pausecommand()
    exitmenu()

##main menu##
def mainmenu():
  print '----------Welcome to Pypet!----------'
  print 'Please choose an option:'
  print '1. See Pypets available for adoption'
  print '2. See your adopted Pypet(s)'
  print '3. Exit'
  print '-------------------------------------'
  maininput = raw_input(':')
  if maininput == '1':
    adoptmenu()
  elif maininput == '2':
    mymenu()
  elif maininput == '3':
    exitmenu()
  else:
    print 'ERROR, please choose option 1, 2, or 3.'
    pausecommand()
    mainmenu()
    
##Start##

mainmenu()
