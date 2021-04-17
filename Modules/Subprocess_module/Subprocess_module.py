<<<<<<< HEAD
# %% [markdown]
# Subprocess Module

# %% [codecell]
import subprocess

# %% [markdown]
# Running an external command, because we are on a windows machine we must specify
# the 'shell=True' argument. Caution must be given, when using this argument because
# it is a security risk. An alternative is to use our arguments in a list.

# %% [codecell]
subprocess.run('dir', shell=True)

# %% [codecell]
subprocess.run(['dir'], shell=True)

# %% [markdown]
# We can save our process in a variable, so we can manipulate it further.

# %% [codecell]
process_1 = subprocess.run(['dir'], shell=True)

# %% [markdown]
# Having our subprocess arguments.

# %% [codecell]
print(process_1.args)

# %% [markdown]
# Checking our return code, to see if we have any errors or not. A value greater
# than zero(0) indicates an error.

# %% [codecell]
print(process_1.returncode)

# %% [markdown]
# Grabbing the standard output. In order to do that another argument is required.

# %% [codecell]
process_1 = subprocess.run(['dir'], shell=True, capture_output=True)
print(process_1.stdout)

# %% [markdown]
# We can see that our output is in bytes. There are 2 ways to decode it. Either
# by using the decode method or by passing other arguments.

# %% [codecell]

# print(process_1.stdout.decode())

process_1 = subprocess.run(['dir'], shell=True, capture_output=True, text=True)

print(process_1)
print()
process_1 = subprocess.run(['dir'], shell=True, stdout=subprocess.PIPE, text=True)

print(process_1)

# %% [markdown]
# Redirecting our output to a file. Useful for logging etc.

# %% [codecell]
with open('output.txt', 'w+') as file:
    process_1 = subprocess.run(['dir'], shell=True, stdout=file, text=True)

# %% [markdown]
# Capturing an error on our subprocess.

# %% [codecell]
process_2 = subprocess.run(['dir', 'json'], shell=True, capture_output=True, text=True)

print(process_2.stderr)

# %% [markdown]
# That is useful if we want to perform an operation if our subprocess is
# successful.

# %% [codecell]
if process_1.stderr == 0:
    with open('output.txt', 'w+') as file:
        process_1 = subprocess.run(['dir', 'json'], shell=True, stdout=file, text=True)
else:
    process_1 = subprocess.run(['dir', 'json'], shell=True, capture_output=True,
                                text=True, check=True)

# %% [markdown]
# Parsing a .txt file.

# %% [codecell]
process_1 = subprocess.run(['type', 'output.txt'], shell=True, capture_output=True,
                            text=True)

print(process_1)

# %% [markdown]
# Piping the output of one command to another. In this example powershell is going
# to be used.

# %% [codecell]
process_1 = subprocess.run(["powershell","cat", "output_1.txt"], shell=True,
                            capture_output=True, text=True)
print(process_1.stdout)
print(2*'\n')

process_2 = subprocess. run(["powershell", "grep", "test3"],
                            capture_output=True, text=True, input=process_1.stdout)

print(process_2.stderr)

# %% [codecell]

process_2 = subprocess.run(["powershell", "grep 'test3' output_1.txt"], shell=True,
                            capture_output=True, text=True)

print(process_2.stdout)
=======
# %% [markdown]
# Subprocess Module

# %% [codecell]
import subprocess

# %% [markdown]
# Running an external command, because we are on a windows machine we must specify
# the 'shell=True' argument. Caution must be given, when using this argument because
# it is a security risk. An alternative is to use our arguments in a list.

# %% [codecell]
subprocess.run('dir', shell=True)

# %% [codecell]
subprocess.run(['dir'], shell=True)

# %% [markdown]
# We can save our process in a variable, so we can manipulate it further.

# %% [codecell]
process_1 = subprocess.run(['dir'], shell=True)

# %% [markdown]
# Having our subprocess arguments.

# %% [codecell]
print(process_1.args)

# %% [markdown]
# Checking our return code, to see if we have any errors or not. A value greater
# than zero(0) indicates an error.

# %% [codecell]
print(process_1.returncode)

# %% [markdown]
# Grabbing the standard output. In order to do that another argument is required.

# %% [codecell]
process_1 = subprocess.run(['dir'], shell=True, capture_output=True)
print(process_1.stdout)

# %% [markdown]
# We can see that our output is in bytes. There are 2 ways to decode it. Either
# by using the decode method or by passing other arguments.

# %% [codecell]

# print(process_1.stdout.decode())

process_1 = subprocess.run(['dir'], shell=True, capture_output=True, text=True)

print(process_1)
print()
process_1 = subprocess.run(['dir'], shell=True, stdout=subprocess.PIPE, text=True)

print(process_1)

# %% [markdown]
# Redirecting our output to a file. Useful for logging etc.

# %% [codecell]
with open('output.txt', 'w+') as file:
    process_1 = subprocess.run(['dir'], shell=True, stdout=file, text=True)

# %% [markdown]
# Capturing an error on our subprocess.

# %% [codecell]
process_1 = subprocess.run(['dir', 'json'], shell=True, capture_output=True, text=True)

print(process_1.stderr)

# %% [markdown]
# That is useful if we want to perform an operation if our subprocess is
# successful.

# %% [codecell]
if process_1.stderr == 0:
    with open('output.txt', 'w+') as file:
        process_1 = subprocess.run(['dir', 'json'], shell=True, stdout=file, text=True)
else:
    process_1 = subprocess.run(['dir', 'json'], shell=True, capture_output=True,
                                text=True, check=True)

# %% [markdown]
# Parsing a .txt file.

# %% [codecell]
process_1 = subprocess.run(['type', 'output.txt'], shell=True, capture_output=True,
                            text=True)

print(process_1)

# %% [markdown]
# Piping the output of one command to another. In this example powershell is going
# to be used.

# %% [codecell]
process_1 = subprocess.run(["powershell","cat", "output_1.txt"], shell=True,
                            capture_output=True, text=True)
print(process_1.stdout)
print(2*'\n')

process_2 = subprocess. run(["powershell", "grep", "test3"],
                            capture_output=True, text=True, input=process_1.stdout)

print(process_2.stderr)

# %% [codecell]

process_2 = subprocess.run(["powershell", "grep 'test3' output_1.txt"], shell=True,
                            capture_output=True, text=True)

print(process_2.stdout)
>>>>>>> e48e1c772dcbd95e382a5cc3581f16cdc40aed4c
