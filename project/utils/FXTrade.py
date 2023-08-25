import subprocess


x = subprocess.run(["bash", "FX.sh"], capture_output=True)


# to get the mid rate of the currency exchange
print("this is x", x.stdout.decode('utf-8').strip().split()[10])