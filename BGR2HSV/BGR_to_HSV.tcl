#############################################################################
# Generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#  Oct 29, 2019 08:56:52 AM CDT  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family Arial -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#
    menu .pop46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop46" "Popupmenu3" vTcl:WidgetProc "" 1

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x409+344+163
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "BGR to HSV Conversion"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but43 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Select Output Directory} 
    vTcl:DefineAlias "$top.but43" "ButtonDir" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but43 <ButtonRelease-1> {
        lambda e: btn_release(e)
    }
    entry $top.ent44 \
        -background white -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable entry_blue 
    vTcl:DefineAlias "$top.ent44" "EntryBlue" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent45 \
        -background white -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable entry_green 
    vTcl:DefineAlias "$top.ent45" "EntryGreen" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent46 \
        -background white -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable entry_red 
    vTcl:DefineAlias "$top.ent46" "EntryRed" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Blue 
    vTcl:DefineAlias "$top.lab47" "LabelBlue" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Green 
    vTcl:DefineAlias "$top.lab48" "LabelGreen" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Red 
    vTcl:DefineAlias "$top.lab49" "LabelRed" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Enter Integer Values  0 - 255} 
    vTcl:DefineAlias "$top.lab43" "LabelEntryInstr" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Convert to HSV} 
    vTcl:DefineAlias "$top.but44" "ButtonConvert" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but44 <ButtonRelease-1> {
        lambda e: btn_convert_RGB_to_HSV(e)
    }
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black -anchor nw \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Results - Hue, Saturation, Value: } 
    vTcl:DefineAlias "$top.lab45" "LabelResults" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground {#f9f9f9} -activeforeground black -anchor nw \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text {Output Directory:} 
    vTcl:DefineAlias "$top.lab44" "LabelOutDir" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -activebackground {#f9f9f9} -activeforeground black -anchor nw \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text {Paint.Net Approx. Hue, Sat, Value:} 
    vTcl:DefineAlias "$top.lab46" "LabelPaintNet" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground {#f9f9f9} -activeforeground black -anchor nw \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text {This program converts Blue, Green, Red values to Hue, Saturation and Value.} 
    vTcl:DefineAlias "$top.lab50" "LabelDesc1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground {#f9f9f9} -activeforeground black -anchor nw \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text {The results are presented on this interface and logged to "Contour_Data.csv"} 
    vTcl:DefineAlias "$top.lab51" "LabelDesc2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground {#f9f9f9} -activeforeground black -anchor nw \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Arial} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text {in the user specified directory.} 
    vTcl:DefineAlias "$top.lab52" "Label3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font {-family {Arial} -size 12 -weight bold} \
        -foreground {#000000} -tearoff 0 
    $site_3_0 add command \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command {#open_instruct} -font TkDefaultFont \
        -foreground {#000000} -label {Detailed Instructions} 
    $site_3_0 add command \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command {#exit} -font TkDefaultFont \
        -foreground {#000000} -label Exit 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but43 \
        -in $top -x 40 -y 110 -width 198 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent44 \
        -in $top -x 40 -y 240 -width 100 -relwidth 0 -height 22 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent45 \
        -in $top -x 180 -y 240 -width 100 -relwidth 0 -height 22 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 320 -y 240 -width 100 -relwidth 0 -height 22 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 40 -y 210 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 180 -y 210 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 320 -y 210 -anchor nw -bordermode ignore 
    place $top.lab43 \
        -in $top -x 40 -y 180 -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 40 -y 280 -width 128 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 40 -y 320 -width 525 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 40 -y 150 -width 525 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 40 -y 350 -width 524 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 40 -y 20 -width 547 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 40 -y 50 -width 545 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 40 -y 80 -width 223 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

