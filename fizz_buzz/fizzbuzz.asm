;=====================
;=     FIZZ BUZZ     =
;=====================

; This is written in x86 assembly for MASM.
; This program prints each number from 1 to 100 on a new line.
; For each multiple of 3, it prints 'Fizz' instead of the number.
; For each multiple of 5, it prints 'Buzz' instead of the number.
; For numbers which are multiples of both 3 and 5, it prints 'FizzBuzz' instead of the number.

TITLE FizzBuzz

.386
.MODEL flat, stdcall
.STACK 4096

STD_OUTPUT_HANDLE EQU -11                       ; standard output device
WriteConsole EQU <WriteConsoleA>                ; alias WriteConsole

ExitProcess PROTO, dwExitCode:DWORD             ; ends process and its threads
GetStdHandle PROTO,                             ; get standard handle
    nStdHandle:DWORD                            ; type of console handle
WriteConsole PROTO,                             ; write a buffer to the console
    handle:DWORD,                               ; output handle
    lpBuffer:PTR BYTE,                          ; pointer to buffer
    nNumberOfCharsToWrite:DWORD,                ; size of buffer
    lpNumberOfCharsWritten:PTR DWORD,           ; number of chars written
    lpReserved:PTR DWORD                        ; 0 (not used)

.DATA
    fizz BYTE 'Fizz', 0
    buzz BYTE 'Buzz', 0
    fizzbuzz BYTE 'FizzBuzz', 0

.DATA?
    consoleOutHandle DWORD ?
    bytesWritten DWORD ?

.CODE
;=====================
;=       MAIN        =
;=====================
main PROC
    call fizzy                                  ; execute fizzy       

    INVOKE ExitProcess, 0                       ; exit code = 0
main ENDP

;=====================
;=       FIZZY       =
;=====================
fizzy PROC USES eax ebx ecx edx
    mov ecx, 1                                  ; counter = 1

f_loop:
    mov eax, ecx                                ; EAX = number
    mov ebx, 15                                 ; EBX = 15
    div ebx                                     ; number / 15
    cmp edx, 0                                  ; if divisible by both 3 and 5
    jz print_fizzbuzz                           ;   print 'FizzBuzz'

    mov eax, ecx                                ; EAX = number
    mov ebx, 3                                  ; EBX = 3
    div ebx                                     ; number / 3
    cmp edx, 0                                  ; if divisible by 3
    jz print_fizz                               ;   print 'Fizz'

    mov eax, ecx                                ; EAX = number
    mov ebx, 5                                  ; EBX = 5
    div ebx                                     ; number / 5
    cmp edx, 0                                  ; if divisible by 5
    jz print_buzz                               ;   print 'Buzz'

    inc ecx                                     ; counter++
    cmp ecx, 100                                ; if counter = 100
    je f_end                                    ;   exit loop
    loop f_loop

print_fizzbuzz:
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET fizzbuzz,                        ; points to fizzbuzz
        LENGTHOF fizzbuzz - 1,                  ; number of chars in fizzbuzz
        OFFSET bytesWritten, 0                  ; points to bytesWritten

    ret

print_fizz:
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET fizz,                            ; points to fizz
        LENGTHOF fizz - 1,                      ; number of chars in fizz
        OFFSET bytesWritten, 0                  ; points to bytesWritten

    ret

print_buzz:
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET buzz,                            ; points to buzz
        LENGTHOF buzz - 1,                      ; number of chars in buzz
        OFFSET bytesWritten, 0                  ; points to bytesWritten

    ret

print_num:
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET buzz,                            ; points to buzz
        LENGTHOF buzz - 1,                      ; number of chars in buzz
        OFFSET bytesWritten, 0                  ; points to bytesWritten

    ret

f_end:
    ret
fizzy ENDP

END main