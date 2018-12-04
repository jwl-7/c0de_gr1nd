;====================================================================
;=                           SHIBA TIME                             =                    
;====================================================================
; such c0de.                                                        |
;--------------------------------------------------------------------

TITLE SHIBA

.386
.MODEL flat, stdcall
.STACK 4096

STD_OUTPUT_HANDLE EQU -11                       ; standard output device
WriteConsole      EQU <WriteConsoleA>           ; alias WriteConsole

ExitProcess PROTO,                              ; ends process and its threads
    dwExitCode: DWORD                           ; the exit code for the thread
GetStdHandle PROTO,                             ; get standard handle
    nStdHandle: DWORD                           ; type of console handle
WriteConsole PROTO,                             ; write a buffer to the console
    handle: DWORD,                              ; output handle
    lpBuffer: PTR BYTE,                         ; pointer to buffer
    nNumberOfCharsToWrite: DWORD,               ; size of buffer
    lpNumberOfCharsWritten: PTR DWORD,          ; number of chars written
    lpReserved: PTR DWORD                       ; 0 (not used)
MuchPrint PROTO,                                ; prints a string to console
    lpString: PTR BYTE                          ; pointer to string

.DATA?
    consoleOutHandle DWORD ?
    bytesWritten     DWORD ?

.CODE
;====================================================================
;=                              MAIN                                =
;====================================================================
; very Main.                                                        |
;--------------------------------------------------------------------
main PROC
    call   shiba
    INVOKE ExitProcess,   0            ; terminate program
main ENDP

;====================================================================
;=                             SHIBA                                =
;====================================================================
; ASCII sh1ba                                                       |
;  Receives: none                                                   |
;   Returns: much doge                                              |
;--------------------------------------------------------------------
shiba PROC
.DATA
    s1  BYTE  32,  32,  32,  32,  32,  32,  32,  32,  32, 219,  32, 
              32,  32,  32,  32,  32,  32,  32,  32,  32,  32,  32,
              32,  32, 219,  13,  10
    
    s2  BYTE  32,  32,  32,  32,  32,  32,  32,  32, 219, 177, 219, 
              32,  32,  32,  32,  32,  32,  32,  32,  32,  32,  32,
             220, 223, 177, 219,  13,  10

    s3  BYTE  32,  32,  32,  32,  32,  32,  32,  32, 219, 177, 177, 
             219,  32,  32,  32,  32,  32,  32,  32,  32, 220, 223, 
             177, 177, 177, 219,  13,  10

    s4  BYTE  32,  32,  32,  32,  32,  32,  32, 219, 220, 223, 177,
             177, 223, 223, 223, 223, 220, 220, 220, 223, 177, 177,
             177, 177, 177, 219,  13,  10
 
    s5  BYTE  32,  32,  32,  32,  32, 220, 220, 223, 177, 176, 177,
             177, 177, 177, 177, 177, 177, 177, 177, 219, 177, 177,
             220, 219, 177, 219,  13,  10

    s6  BYTE  32,  32,  32, 220, 223, 177, 177, 177, 176, 176, 176,
             177, 177, 177, 176, 176, 176, 177, 177, 177, 223, 219,
             219, 223, 177, 219,  13,  10

    s7  BYTE  32,  32, 219, 177, 177, 177, 220, 220, 177, 177, 177,
             177, 176, 176, 176, 177, 177, 177, 177, 177, 177, 177,
             223, 220, 177, 177, 219,  13,  10 

    s8  BYTE  32,  32, 219, 176, 176, 219, 219, 223, 177, 177, 177, 
             177, 177, 220, 223, 219, 220, 177, 177, 177, 177, 177, 
             177, 177, 219, 177, 219,  13,  10

    s9  BYTE  32, 219, 176, 176, 176, 177, 177, 177, 177, 177, 177, 
             177, 177, 219, 219, 219, 223, 177, 177, 176, 176, 176, 
             177, 177, 177, 223, 220, 219,  13,  10

    s10 BYTE  32, 219, 176, 177, 220, 219, 219, 220, 177, 177, 177, 
             177, 177, 177, 177, 177, 177, 176, 176, 176, 176, 176, 
             176, 177, 177, 177, 177, 219,  13,  10

    s11 BYTE 219, 177, 223, 219, 220, 219, 220, 219, 219, 220, 176,
             220, 177, 177, 176, 176, 176, 176, 176, 176, 176, 176,
             176, 176, 177, 177, 177, 219,  13,  10

    s12 BYTE 219, 177, 177, 219, 223, 219, 223, 177, 176, 220, 220,
             177, 220, 177, 177, 177, 177, 177, 177, 176, 177, 176,
             177, 176, 177, 177, 177, 177, 219,  13,  10 
        
    s13 BYTE 219, 177, 177, 177, 223, 223, 220, 220, 177, 177, 177,
             220, 177, 177, 177, 177, 177, 177, 177, 177, 176, 177,
             176, 177, 176, 177, 177, 219,  13,  10  

    s14 BYTE  32, 219, 177, 177, 177, 177, 177, 177, 223, 223, 223, 
             177, 177, 177, 177, 177, 177, 176, 177, 176, 177, 176, 
             177, 176, 177, 177, 177, 219,  13,  10,

    s15 BYTE  32, 219, 177, 177, 177, 177, 177, 177, 177, 177, 177,
             177, 177, 177, 177, 177, 176, 177, 176, 177, 176, 177, 
             177, 220, 177, 177, 219,  13,  10 

    s16 BYTE  32,  32, 223, 220, 177, 177, 177, 177, 177, 177, 177,
             177, 177, 177, 177, 176, 177, 176, 177, 176, 177, 220,
             177, 177, 177, 177, 219,  13,  10

    s17 BYTE  32,  32,  32,  32, 223, 220, 177, 177, 177, 177, 177,
             177, 177, 177, 177, 177, 220, 220, 220, 223, 177, 177,
             177, 177, 220, 223,  13,  10

    s18 BYTE  32,  32,  32,  32,  32,  32, 223, 220, 220, 220, 220,
             220, 220, 223, 223, 223, 177, 177, 177, 177, 177, 220,
             220, 223,  13,  10

    s19 BYTE  32,  32,  32,  32,  32,  32,  32,  32,  32, 177, 177,
             177, 177, 177, 177, 177, 177, 177, 177, 223, 223,  32,
              32,  32,  32,  32,  87,  48, 119,  46,  13,  10,   0      

.CODE
    INVOKE MuchPrint, OFFSET s1
    ret
shiba ENDP

;====================================================================
;=                           MuchPrint                              =
;====================================================================
;  So string. Many BYTES. Very Print.                               |
; Receives: pawString -> string pointer                             |
;  Returns: string to standard output                               |
;--------------------------------------------------------------------
MuchPrint PROC,
    pawString: PTR BYTE                ; points to string

    pushad                             ; save 32-bit registers
    INVOKE GetStdHandle,               ; get standard device handle
           STD_OUTPUT_HANDLE           ; standard output device
    mov    [consoleOutHandle], eax     ; store address of handle
    mov    esi, pawString              ; ESI = pawString
    xor    ecx, ecx                    ; ECX = character count

FindShiBYTES:
    cmp    BYTE PTR [esi], 0           ; end of string?
    je     FoundShibes                 ; yes: quit
    inc    esi                         ; no: point to next
    inc    ecx                         ; count++
    jmp    FindShiBYTES

FoundShibes:
    cld                                ; clear direction flag
    INVOKE WriteConsole,               ; write buffer to console
           consoleOutHandle,           ; output handle
           pawString,                  ; points to string
           ecx,                        ; string length
           OFFSET bytesWritten,        ; returns number of bytes written
           0                           ; not used
    popad                              ; restore 32-bit registers
    ret
MuchPrint ENDP

END main