
import inspect
import os
import io
import urllib2

AUTHOR = "loek17"
BUNDLE = "iTVOnline.bundle"

ZIP_URL = "http://github.com/%s/%s/archive/master.zip" % (AUTHOR , BUNDLE)
COMMIT_URL = "https://api.github.com/repos/%s/%s/commits" % (AUTHOR , BUNDLE)

class UpdateException(Exception):
    pass

class UpToDateException(Exception):
    pass

def update(force=False):
    Log.Info("###################### Start Updating iTVonline channel ######################")
    lastCommit = JSON.ObjectFromURL(COMMIT_URL , cacheTime=0)[0]
    if force or lastCommit['sha'] != (Dict['sha'] if 'sha' in Dict else ''):
        try:
            real_update(lastCommit['sha'])
        except UpdateException:
            Log.Exception(str(e))
            raise
        except Exception, e:
            Log.Exception(str(e))
            Log.Info("###################### Updating iTVonline channel - Error in update process ######################")
            raise UpdateException("Update Error - Unknown Error" + str(e))
    else:
        Log.Info("###################### Updating iTVonline channel - No update needed ######################")
        raise UpToDateException("You are running the last version")
    Log.Info("###################### Done Updating iTVonline channel######################")
    return True
        

def real_update(newSHA):
    bundle_path = os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda x : x))).replace(os.path.join("Contents" , "Code") , "")
    version = Dict["sha"] if "sha" in Dict else "unknown"
    zipPath = ZIP_URL
    
    Log.Info("###################### Updating iTVonline channel - Start Args ######################")
    for name, var in (("ZIP_URL", ZIP_URL) , ("version", version) , ("newSHA", newSHA) , ("Platform.OS", Platform.OS) , ("Platform.CPU", Platform.CPU) , ("Plugin.Identifier", Plugin.Identifier)):
        Log.Info("%s   =     %s" % (name , var))
    Log.Info("###################### Updating iTVonline channel - End Args ######################")
    
    #https://github.com/mikedm139/UnSupportedAppstore.bundle/blob/master/Contents/Code/__init__.py
    zipfile = Archive.ZipFromURL(zipPath)
    Log.Info('Extracting to ' + bundle_path)
    
    for filename in zipfile:
        

        if not str(filename).endswith('/'):
            if not str(filename.split('/')[-1]).startswith('.'):
                
                data = zipfile[filename]
                path = join_bundle_path(bundle_path , filename)

                Log.Info('Extracting file' + path)
                save(path, data)
            else:
                Log.Info('Skipping "hidden" file: ' + filename)
        else:
            Log.Info(filename.split('/')[-2])

            if not str(filename.split('/')[-2]).startswith('.'):
                path = join_bundle_path(bundle_path, filename)

                Log.Info('Extracting folder ' + path)
                ensure_dirs(path)
    
    # "touch" the bundle to update the timestamp
    os.utime(bundle_path, None)
    # To help installs/updates register without rebooting PMS...
    # reload the system service if installing a new plugin
    urllib2.urlopen('http://127.0.0.1:32400/:/plugins/%s/reloadServices' % Plugin.Identifier).read()
    Dict["sha"] = newSHA

def join_bundle_path(bundle_path, path):
    fragments = path.split('/')[1:]

    # Remove the first fragment if it matches the bundle name
    if len(fragments) and fragments[0].lower() == os.path.split(bundle_path)[1].lower():
        fragments = fragments[1:]
        
    return os.path.join(bundle_path , *fragments)
    
def save(filename , data , binary=True):
    # Don't attempt to save if no data was passed
    if data == None:
      Log.Info("Attempted to save no data to '%s' - aborting. Nothing has been saved to disk.", filename)
      return
      
    filename = os.path.abspath(filename)
    tempfile = '%s/._%s' % (os.path.dirname(filename), os.path.basename(filename))
    try:
      if os.path.exists(tempfile):
        os.remove(tempfile)
      if binary: mode = 'wb'
      else: mode = 'w'
      f = io.open(tempfile, mode)
      f.write(str(data))
      f.close()
      if os.path.exists(filename):
        os.remove(filename)
      os.rename(tempfile, filename)
    except:
      Log.Info("Exception writing to %s", filename)
      if os.path.exists(tempfile):
        os.remove(tempfile)
      raise
    
def ensure_dirs(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except:
        if not os.path.exists(path):
            raise