;====================================================================
;=                            FIZZ BUZZ                             =                    
;====================================================================

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
    num BYTE 1

.DATA?
    consoleOutHandle DWORD ?
    bytesWritten DWORD ?

.CODE
;====================================================================
;=                              MAIN                                =
;====================================================================
main PROC
    call fizzy                                  ; execute fizzy       

    INVOKE ExitProcess, 0                       ; terminate program
main ENDP

;====================================================================
;=                            StrLength                             =
;====================================================================
;- Gets length of a null-terminated string.                         -
;- Receives: pString -> string pointer                              -
;- Returns: EAX = string length                                     -
;--------------------------------------------------------------------
StrLength PROC USES edi,                        
    pString:PTR BYTE                            ; points to string

    mov edi, pString
    xor eax, eax                                ; EAX = character count
L1:
    cmp BYTE PTR [edi],0                        ; end of string?
    je  L2                                      ; yes: quit
    inc edi                                     ; no: point to next
    inc eax                                     ; count++
    jmp L1
L2: 
    ret
StrLength ENDP

;====================================================================
;=                            PrintStr                              =
;====================================================================
;- Writes a null-terminated string to standard output               -
;- EDX -> points to string                                          -
;--------------------------------------------------------------------
PrintStr PROC
    pushad                                      ; save general-purpose registers

    INVOKE StrLength, edx                       ; EAX = length of string
    cld                                         ; clear direction flag

    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle
        edx,                                    ; points to string
        eax,                                    ; string length
        OFFSET bytesWritten,                    ; returns number of bytes written
        0

    popad
    ret
PrintStr ENDP

;====================================================================
;=                             FIZZY                                =
;====================================================================
fizzy PROC USES eax ebx ecx edx
    mov ecx, 1                                  ; counter = 1

f_test:
    push ecx
    xor edx, edx                                ; clear EDX
    mov eax, ecx                                ; EAX = number
    mov ebx, 15                                 ; EBX = 15
    div ebx                                     ; number / 15
    cmp edx, 0                                  ; if divisible by both 3 and 5
    jz print_fizzbuzz                           ;   print 'FizzBuzz'

    xor edx, edx                                ; clear EDX
    mov eax, ecx                                ; EAX = number
    mov ebx, 3                                  ; EBX = 3
    div ebx                                     ; number / 3
    cmp edx, 0                                  ; else if divisible by 3
    jz print_fizz                               ;   print 'Fizz'

    xor edx, edx                                ; clear EDX
    mov eax, ecx                                ; EAX = number
    mov ebx, 5                                  ; EBX = 5
    div ebx                                     ; number / 5
    cmp edx, 0                                  ; else if divisible by 5
    jz print_buzz                               ;   print 'Buzz'
    
    ;jmp print_num                              ; else print number

f_loop:
    pop ecx
    inc ecx                                     ; counter++
    cmp ecx, 100                                ; if counter <= 100
    jbe    f_test                               ;    loop
    jmp f_end                                   ; else exit

print_fizzbuzz:
    pushad                                      ; save general-purpose registers

    INVOKE GetStdHandle,                        ; get standard device handle
        STD_OUTPUT_HANDLE                       ; standard output device
    mov [consoleOutHandle], eax                 ; store address of handle
    mov edx, OFFSET fizzbuzz                    ; get fizzbuzz string
    INVOKE PrintStr                             ; print 'FizzBuzz'

    popad
    jmp f_loop

print_fizz:
    pushad                                      ; save general-purpose registers

    INVOKE GetStdHandle,                        ; get standard device handle
        STD_OUTPUT_HANDLE                       ; standard output device
    mov [consoleOutHandle], eax                 ; store address of handle
    mov edx, OFFSET fizz                        ; get fizz string
    INVOKE PrintStr                             ; print 'fizz'

    popad
    jmp f_loop

print_buzz:
    pushad                                      ; save general-purpose registers

    INVOKE GetStdHandle,                        ; get standard device handle
        STD_OUTPUT_HANDLE                       ; standard output device
    mov [consoleOutHandle], eax                 ; store address of handle
    mov edx, OFFSET buzz                        ; get buzz string
    INVOKE PrintStr                             ; print 'buzz'

    popad
    jmp f_loop

print_num:
    pushad                                      ; save general-purpose registers
    mov [consoleOutHandle], eax                 ; store address of handle
    INVOKE GetStdHandle,                        ; get standard device handle
        STD_OUTPUT_HANDLE                       ; standard output device
    popad
    jmp f_loop

f_end:
    ret
fizzy ENDP

END main