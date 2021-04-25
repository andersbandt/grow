from crontab import Crontab


my_cron = CronTab(user='pi')


def createJob(commandPath, commentString):
  job = my_cron.new(command = commandPath, comment = commentString)
  job.hour.every(12) # just put every 12 hours for now, should change immediately
  my_cron.write()
  print("Cron job created at this path ", commandPath)
  
def printJobs():
  for job in my_cron:
    print job

def updateJob(commentString, scheduleArray):
  for job in my_cron:
    if job.comment == commentString:
      if scheduleArray[0] != 0:
        job.minute.every(scheduleArray[0]
      elif scheduleArray[1] != 0:
        job.hour.every(scheduleArray[1])
