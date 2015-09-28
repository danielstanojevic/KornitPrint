Set oShell = CreateObject("WScript.Shell")
check = oShell.AppActivate("Messenger Service")
Do While check = true
oShell.SendKeys "{ENTER}"
WScript.Sleep 50
check = oShell.AppActivate("Messenger Service")
Loop
