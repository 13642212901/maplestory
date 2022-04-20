;Server
; #Include socketTCP.ahk
#Include socket.ahk
myTcp := new SocketTCP()
myTcp.bind("addr_any", 12345)
myTcp.listen()
myTcp.onAccept := Func("OnTCPAccept")
OnTCPAccept(){
  global myTcp
  newTcp := myTcp.accept()
  Loop, {
    command := newTcp.recvText()
    commandArr := StrSplit(command, ".")
    command := commandArr[1]
    delay := commandArr[2]
    if (command = "combo1") {
      combo2()
      sleep, %delay%
    } else if(command = "iliumnAtt") {
      iliumnAtt()
      sleep, %delay%
    }  else if(command = "aaaAtt") {
      aaaAtt()
      sleep, %delay%
    }  else if(command = "flyRight") {
      flyRight()
      sleep, %delay%
    }  else if(command = "flyLeft") {
      flyLeft()
      sleep, %delay%
    } else if (command = "kannaAtt") {
      kannaAtt()
      sleep, %delay%
    } else if (command = "jumpExorcist") {
      jumpExorcist()
      sleep, %delay%
    } else if (command = "heroJumpAtt") {
      heroJumpAtt()
      sleep, %delay%
    } else if (command = "highJumpAtt") {
      highJumpAtt()
      sleep, %delay%
    } else if (command = "fly") {
      fly()
      sleep, %delay%
    } else if (command = "flyStop") {
      flyStop()
      sleep, %delay%
    } else if (command = "tripleJump") {
      tripleJump()
      sleep, %delay%
    } else if (command = "skillMove") {
      s := commandArr[2]
      d := commandArr[3]
      delay := commandArr[4]
      skillMove(s, d)
      sleep, %delay%
    } else {
      command := StrSplit(command, ",")
      if (command[2] != "") {
        one := command[1]
        two := command[2]
        send, {%one% Down}
        sleep, 80
        send, {%two%}
        sleep, 80
        if (command[3] != "") {
          three := command[3]
          random, r, 40, 60
          sleep, %r%
          send, {%three%}
          random, r, 20, 50
          sleep, %r%
          send, {%three%}
          random, r, 20, 50
          sleep, %r%
        }
        send, {%one% Up}
        sleep, %delay%
      } else {
        command := command[1]
        if (command = "stop") {
          Break
        }
        commandArr := StrSplit(command, "|")
        command := commandArr[1]
        holdTime := commandArr[2]
        if (holdTime != "") {
          Send, {%command% Down}
          sleep, %holdTime%
          Send, {%command% Up}
        } else {
          Send, {%command%}
        }
        sleep, %delay%
      }
    }
    
  }
}

delay(){

}


combo1(){
    send, {s}
    random, r, 300, 310
    sleep, %r%
    send, {d}
    random, r, 300, 310
    sleep, %r%
    send, {f}
    random, r, 350, 370
    sleep, %r%
    send, {w}
    random, r, 300, 310
    sleep, %r%
}

combo2(){
    send, {w}
    random, r, 300, 310
    sleep, %r%
    send, {f}
    random, r, 300, 310
    sleep, %r%
}

combo3(){
    send, {s}
    random, r, 300, 310
    sleep, %r%
    send, {d}
    random, r, 300, 310
    sleep, %r%
    send, {w}
    random, r, 300, 310
    sleep, %r%
}

iliumnAtt(){
    Send, {Ctrl}
    random, r, 600, 620
    sleep, %r%
    Send, {z}
    random, r, 600, 620
    sleep, %r%
}

kannaAtt(){
    Send, {Ctrl}
    sleep, 100
    Send, {Ctrl}
    sleep, 300
}
jumpExorcist(){
    Send, {c}
    sleep, 50
    sleep, 150
    Send, {q}
    sleep, 50
}

Test(){
    Send, {Ctrl}
    sleep, 100
    Send, {Ctrl}
    sleep, 300
}

jumpAtt(){
  Send, {a Down}
  sleep, 250
  Send, {Ctrl}
  sleep, 50
  Send, {Shift}
  sleep, 200
  Send, {a Up}
  sleep, 100
  Send, {c}
  Send, {Alt}
}

noJumpAtt(){
  Send, {a Down}
  sleep, 250
  Send, {Ctrl}
  sleep, 50
  Send, {Shift}
  sleep, 200
  Send, {a Up}
  sleep, 100
  Send, {c}
}

heroJumpAtt(){
  Send, {c}
  sleep, 100
  Send, {c}
  sleep, 30
  Send, {c}
  sleep, 120
  Send, {Alt}
  sleep, 600
}

highJumpAtt(){
  Send, {Ctrl}
  sleep, 400
  Send, {c}
  sleep, 30
  Send, {c}
  sleep, 120
  Send, {Alt}
  sleep, 600
}

fly(){
  Send, {c}
  sleep, 100
  Send, {f Down}
  sleep, 50
}

flyStop(){
  Send, {f Up}
}

tripleJump(){
  Send, {c}
  sleep, 50
  Send, {c}
  sleep, 150
  Send, {c}
  sleep, 100
  Send, {c}
}


skillMove(key, dir){
  Send, {%key%}
  sleep, 270
  Send, {%dir% down}
  sleep, 80
  Send, {%key% down}
  sleep, 100
  Send, {%key% Up}
  sleep, 100
  Send, {%dir% Up}
  sleep, 350
}

aaaAtt(){
    Send, {b}
    sleep, 220
    Send, {b}
    sleep, 240
}

flyRight(){
    Send, {c}
    sleep, 100
    Send, {c Down}
    sleep, 50
    Send, {Right Down}
    sleep, 500
    Send, {Right Up}
    sleep, 50
    Send, {c Up}

}
flyLeft(){
    Send, {c}
    sleep, 100
    Send, {c Down}
    sleep, 50
    Send, {Left Down}
    sleep, 500
    Send, {Left Up}
    sleep, 50
    Send, {c Up}

}
