---
layout: post
title:  "Useful Linux commands"
category: Programming
---

<!-- # Useful linux commands -->

### Compress files (e.g. making a backup)
```bash
tar -zcvf archive-name.tar.gz directory-name
```
Options:

- z: Compress archive using gzip program
- c: Create archive
- v: Verbose i.e display progress while creating archive
- f: Archive File name

### Uncompress files (e.g. restoring a backup)
```bash
tar -zxvf archive-name.tar.gz
```
Options:

- x: Extract files


### Accessing a remote machine
Having a `.pem` file:
```bash
ssh -i key.pem ubuntu@0.0.0.0
```


### Copy files between machines
Having a `.pem` file:
```bash
scp -i key.pem file1 (...) fileN ubuntu@0.0.0.0://home/ubuntu
```


### Search for files

```bash
find $directory -name '*.json'
```
The command above will search for all files that have the extesion 'json' in the directory specified (including subdirectories).


### Search for strings in many files
```bash
grep -rn "string"
```
Options:

- r: Recursive
- n: Show line Number


### Space usage
```bash
du -sh [file_path]
```
Options:

- s (`--summarize`): display only a total of each argument
- h (`--human-readable`): print sizes in human readable format (e.g., 1K 234M 2G)


### Screen (terminal sessions in the background)

List current screen sessions:
```bash
screen -ls
```

Start a new screen session with name [name]:
```bash
screen -S [name]
```

Resume (reconnect) to the screen named [name]
```bash
screen -r [name]
```

#### Commands when you are inside a screen

Detach from current screen:
`Ctrl-a` `d`

Rename current screen to [name]:
`Ctrl-a` `:` `sessionname [name]`


### System statistics

Performance statistics for all logical processors:
```bash
mpstat -P ALL 1
```

Memory usage statistics:
```bash
vmstat -s
```

Memory and CPU usage per process:
```bash
top
```

### Git

Pretty logging
```bash
git log --pretty=oneline --all --decorate --graph
```

Pull only a specific directory:
```bash
git fetch REMOTE_NAME
git checkout REMOTE_NAME/BRANCH -- relative/path/to/dir
```

Download only a specific directory (without having to clone the whole repo):
check [this answer](https://stackoverflow.com/a/18194523/5103881).


### Packages on Ubuntu

See where a package is installed:
```bash
dpkg -L <packagename>
```
