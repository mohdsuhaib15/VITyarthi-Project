import os
from datetime import date
file="calorie.txt"
def load_data():
	if not os.path.exists(file):
		return None,0,{}
	g=None
	t=0
	fs={}
	d=""
	with open(file,"r") as f:
		for ln in f:
			ln=ln.strip()
			if not ln:
				continue
			if ln.startswith("GOAL:"):
				g=int(ln[5:])
			elif ln.startswith("DATE:"):
				d=ln[5:]
			elif ln.startswith("TODAY:"):
				t=int(ln[6:])
			elif ":" in ln:
				k,v=ln.split(":",1)
				fs[k.lower()]=int(v)
	if d!=str(date.today()):
		t=0
	return g,t,fs
def save_info(g,t,fs):
	with open(file,"w") as f:
		f.write("GOAL:"+str(g)+"\n")
		f.write("DATE:"+str(date.today())+"\n")
		f.write("TODAY:"+str(t)+"\n")
		f.write("my foods:\n")
		for k in fs:
			f.write(k+":"+str(fs[k])+"\n")
def bmr_calc(w,h,a,g):
	x=g.lower()
	bb=(10*w)+(6.25*h)-(5*a)
	if x.startswith("m"):
		return int((bb+5)*1.55)
	return int((bb-161)*1.55)
def main():
	print("CALORIE TRACKER - simple version")
	print("-"*35)
	g,t,foods=load_data()
	if g is None:
		nm=input("Your name: ") or "User"
		ok=False
		while not ok:
			try:
				w=float(input("Weight (kg): "))
				h=float(input("Height (cm): "))
				a=int(input("Age: "))
				gg=input("Gender (male/female): ")
				if w>30 and h>100 and a>10:
					ok=True
			except:
				print("Enter correct numbers")
		g=bmr_calc(w,h,a,gg)
		t=0
		foods={}
		save_info(g,t,foods)
		print(nm+", your daily goal is "+str(g)+" calories")
	else:
		print("Welcome back! Goal = "+str(g)+" calories")
	print("How to use:")
	print("- Type a number = quick add")
	print("- Type food name")
	print("- Unknown food? I'll ask once")
	while True:
		lf=g-t
		print("-"*35)
		print("Today eaten :",t,"cal")
		print("Still left :",lf,"cal")
		if lf<=0:
			print("Goal reached or over!")
		elif lf<400:
			print("Almost done - be careful")
		fd=input("What did you eat? (q to quit): ").lower().strip()
		if fd=="q":
			save_info(g,t,foods)
			print("Saved.")
			break
		if fd.isdigit():
			c=int(fd)
			t+=c
			print("Added",c,"calories")
			save_info(g,t,foods)
			continue
		if fd in foods:
			c=foods[fd]
			t+=c
			print("Added",fd,"=",c,"calories")
		else:
			tmp=input("How many calories in '"+fd+"'? (0 to skip): ")
			if tmp.isdigit() and int(tmp)>0:
				c=int(tmp)
				foods[fd]=c
				t+=c
				print("Saved '"+fd+"' =",c,"calories")
			else:
				print("Skipped")
		save_info(g,t,foods)
main()