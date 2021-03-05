from Exscript.protocols import SSH2
from Exscript.protocols.Exception import LoginFailure, InvalidCommandException, TimeoutException
from Exscript.protocols.drivers import ios
from Exscript import Host,Account
import socket

def show_cmd(device_name,cmd):
    password = "sgcib123"
    account = Account('netscript', password)
    try:
        conn = SSH2(driver='generic')
        conn.connect(device_name)
        conn.login(account)
        conn.execute("term len 0")
        conn.execute(cmd)
        result = conn.response
        conn.send('exit\r')
        conn.close()
        return result
    except socket.error:
        return ("Can't connect to %s"%device_name)
    except LoginFailure:
        return "Bad credentials"
    except:
        return "Unknown error"

