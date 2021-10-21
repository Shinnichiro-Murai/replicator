errflag = 1

if(@ARG1==0){ 
    set palette defined ( 0 '#ffffff',1 '#ff00ff' )
    errflag = 0
}
if(@ARG1==1){
    if(@ARG3==2){
        color_decision(i) = (real(i)-@ARG2)/33
        set palette cubehelix start 2 cycle 4 saturation 3
        set palette gamma 4
        errflag = 0
    }
    if(@ARG3==3){
        color_decision(i) = (real(i)-@ARG2)/1060
        set palette cubehelix start 2 cycle 4 saturation 3
        set palette gamma 4
        errflag = 0
    }
    if(@ARG3==4){
        color_decision(i) = (real(i)-@ARG2)/23
        set palette cubehelix start 2 cycle 4 saturation 3
        set palette gamma 4
        errflag = 0
    }

}

if(errflag==1){
    print "call argument error"
}