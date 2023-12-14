
$TaskName = "Run Fitness subscription ogni Mercroledi"
$TaskDescription = "This task will run MyScript.py every Wednesday at 10:00 AM"


$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Wednesday -At 10am


$Action = New-ScheduledTaskAction -Execute "C:\Users\bronner\anaconda3\python.exe" -Argument "C:\Users\bronner\Dropbox\small_tasks\automation\subscrib_finess.py"

Register-ScheduledTask -TaskName $TaskName -Description $TaskDescription -Trigger $Trigger -Action $Action
