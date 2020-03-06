---
layout: post
title:  "Configure SSH Keys Authentication"
category: Programming
---

Secure Shell (SSH) is a cryptographic network protocol, i.e., a set of network rules that use cryptography for operating network services securely. The typical application is using SSH to access remote machines and perform command-line, login, and remote command execution, but any network service can be secured with SSH. [1]

The freely available version of SSH present in most Linux environments is called **OpenSSH**. [2]


## The `~/.ssh` directory

OpenSSH stores its configurations on the `.ssh` directory, present under the user's root directory. The .ssh directory is automatically created when the user runs the ssh command for the first time. If it doesn't exist in your computer yet, you may created it using the command below (notice the 700 permission for security). [3]

```console
mkdir -p ~/.ssh && chmod 700 ~/.ssh
```

## SSH Keys configuration

*SSH Keys* allow authentication without the need of a password [2]. It uses two keys, one *private* and one *public*. The public key has the `.pub` extension as its filetype. The name of these keys is usually `id_rsa` and `id_rsa.pub`, and they are usually placed in the `~/.ssh` directory.

To generate the keys using the RSA algorithm, run:
```console
ssh-keygen -t rsa
```
At this step you will be prompted for a password; you may choose to leave it empty, but be aware that whoever gains access to your private key file will be able to login to your remote machines. [5]

In order to SSH into another machine without typing a password, the remote machine must have a copy of your client's public key under its `~/.ssh/authorized_keys` file. You can either manually [append to that file](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys#copying-your-public-ssh-key-to-a-server-without-ssh-copy-id) (if you need to manually create the file, make sure it has permissions "600" for security) or use the utility command `ssh-copy-id`:
```console
ssh-copy-id username@remotehost
```

## SSH Agent and related utilities

### The built-in `ssh-agent` utility

By default, you will have to enter your private key passphrase every time you use it. However, you can avoid to repeatedly do this by running an SSH agent (`ssh-agent -s`), a small utility that stores your private key after you have entered the passphrase for the first time [5]. After your SSH-agent is running, add your key via `ssh-add`, and type your passphrase. Now, every time you need to use your private key, no passphrase will be prompted.

### The smarter [`ssh-ident`](https://github.com/ccontavalli/ssh-ident) utility

Ideally, your SSH-agent would automatically be run at startup, so that you don't have to manually start it and add the keys yourself. However, this approach has the inconvinience that you will need to type your passphrase for all keys even if not using them throughout your session. To solve this issue, a [number of solutions](https://unix.stackexchange.com/a/90869/173702) have been proposed, one of them being [`ssh-ident`](https://github.com/ccontavalli/ssh-ident), which creates SSH agents on demand as your SSH keys are first needed. Read the repository's documentation for more information.


## OpenSSH client-side configuration

Configuration on the client side is done via the `~/.ssh/config` file, which should be readable and writable only by the user (permission 600).

```console
touch ~/.ssh/config && chmod 600 ~/.ssh/config
```

The structure of the file defines, for each block, an alias for host you want to access, followed by the actual hostname and additional configuration. Below you find an example configuration, adapted from [3].

```
Host myalias
    HostName 192.168.1.10
    User myuser
    Port 3022
    IdentityFile ~/.ssh/targaryen.key
    LocalForward 31086 14.120.240.50:31086
```

The example above can be edited to keep only the lines useful for your configuration. It is possible to use wildcards like `Host *` in your config file also. [3,4]


### Prevent SSH connection time outs

An example of wildcards use in your client's SSH configuration is when you want to make sure the SSH connections are not timed out by firewalls or related. To do so, you can add to your client's `~/.ssh/config` file (create if it doesn't exist) the snippet below:
```
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 2
```
For more details see references [6] and [7].


## References

1. https://en.wikipedia.org/wiki/Secure_Shell
2. https://help.ubuntu.com/lts/serverguide/openssh-server.html
3. https://linuxize.com/post/using-the-ssh-config-file
4. https://superuser.com/a/1462597/629663
5. https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys
6. https://patrickmn.com/aside/how-to-keep-alive-ssh-sessions/
7. https://unix.stackexchange.com/questions/3026/what-options-serveraliveinterval-and-clientaliveinterval-in-sshd-config-exac
