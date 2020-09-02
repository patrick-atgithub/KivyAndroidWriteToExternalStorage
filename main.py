import os

from kivy.logger import Logger
from kivy.app import App
from kivy.uix.label import Label

from android.permissions import Permission, request_permissions, check_permission
from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path

def log(msg):
    Logger.info(msg)


def check_permissions(perms):
    for perm in perms:
        if check_permission(perm) != True:
            return False
    return True

def testwrite():
    
    testfile = bytes([1,2,3,4])                 # file with 4 bytes
    
    perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
    
    if  check_permissions(perms)!= True:
        request_permissions(perms)    # get android permissions     
        exit()                        # app has to be restarted; permissions will work on 2nd start
        
    try:
        Logger.info('Got requested permissions')    
        
        fname = os.path.join( primary_external_storage_path(),'testfile')
        log('writing to: %s' %fname)
        
        with open(fname, 'wb') as f:        # write testfile
            f.write(testfile)
        return fname
    
    except:
        log('could not write to external storage ... missing permissions ?')    

class MyApp(App):

    def build(self):
        return Label(text = 'wrote to: %s' %testwrite() )   # <---- calling testwrite() here
    
MyApp().run()

