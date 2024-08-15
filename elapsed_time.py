time = 4545
hours = time//3600
minutes = time%hours//60
seconds = time%hours%60

print(str(hours)+" hours "+str(minutes) +" minutes" +str(seconds) + " seconds")