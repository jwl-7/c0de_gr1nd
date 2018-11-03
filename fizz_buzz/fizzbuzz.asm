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
PrintStr PROTO,                                 ; prints a string to console
    lpString:PTR BYTE                           ; pointer to string

.DATA
    fizz BYTE 'Fizz', 0
    buzz BYTE 'Buzz', 0
    fizzbuzz BYTE 'FizzBuzz', 0
    xtable BYTE '0123456789ABCDEF'
    new_line BYTE ' ', 13, 10, 0
    num_buffer_size = 12
    num_buffer BYTE num_buffer_size DUP(?), 0

.DATA?
    consoleOutHandle DWORD ?
    bytesWritten DWORD ?

.CODE
;====================================================================
;=                              MAIN                                =
;====================================================================
main PROC
    INVOKE PrintStr, OFFSET fizz
    call fizzy

    INVOKE ExitProcess, 0              ; terminate program
main ENDP

;====================================================================
;=                             FIZZY                                =
;====================================================================
fizzy PROC USES eax ebx ecx edx
    mov ecx, 1                         ; counter = 1

f_test:
    push ecx
    xor edx, edx                       ; clear EDX
    mov eax, ecx                       ; EAX = number
    mov ebx, 15                        ; EBX = 15
    div ebx                            ; number / 15
    cmp edx, 0                         ; if divisible by both 3 and 5
    jz print_fizzbuzz                  ;   print 'FizzBuzz'

    xor edx, edx                       ; clear EDX
    mov eax, ecx                       ; EAX = number
    mov ebx, 3                         ; EBX = 3
    div ebx                            ; number / 3
    cmp edx, 0                         ; else if divisible by 3
    jz print_fizz                      ;   print 'Fizz'

    xor edx, edx                       ; clear EDX
    mov eax, ecx                       ; EAX = number
    mov ebx, 5                         ; EBX = 5
    div ebx                            ; number / 5
    cmp edx, 0                         ; else if divisible by 5
    jz print_buzz                      ;   print 'Buzz'
    
    jmp print_num                      ; else print number

f_loop:
    pop ecx
    inc ecx                            ; counter++
    cmp ecx, 100                       ; if counter <= 100
    jbe f_test                         ;    loop
    jmp f_end                          ; else exit

print_fizzbuzz:
    pushad                             ; save 32-bit registers

    INVOKE PrintStr, OFFSET fizzbuzz   ; print 'FizzBuzz'
    call NewLine                       ; print '\n'

    popad                              ; restore 32-bit registers
    jmp f_loop

print_fizz:
    pushad                             ; save 32-bit registers

    INVOKE PrintStr, OFFSET fizz       ; print 'fizz'
    call NewLine                       ; print '\n'

    popad                              ; restore 32-bit registers
    jmp f_loop

print_buzz:
    pushad                             ; save 32-bit registers

    INVOKE PrintStr, OFFSET buzz       ; print 'buzz'
    call NewLine                       ; print '\n'

    popad                              ; restore 32-bit registers
    jmp f_loop

print_num:
    pushad                             ; save 32-bit registers

    mov eax, ecx                       ; EAX = number
    call PrintNum                      ; print number
    call NewLine                       ; print '\n'

    popad                              ; restore 32-bit registers
    jmp f_loop

f_end:
    ret
fizzy ENDP

;====================================================================
;=                            StrLength                             =
;====================================================================
;- Gets length of a null-terminated string.                         -
;- Receives: pString -> string pointer                              -
;- Returns: EAX = string length                                     -
;--------------------------------------------------------------------
StrLength PROC USES edi,                        
    pString:PTR BYTE                   ; points to string

    mov edi, pString
    xor eax, eax                       ; EAX = character count
L1:
    cmp BYTE PTR [edi],0               ; end of string?
    je L2                              ; yes: quit
    inc edi                            ; no: point to next
    inc eax                            ; count++
    jmp L1
L2: 
    ret
StrLength ENDP

;====================================================================
;=                            PrintStr                              =
;====================================================================
;- Writes a null-terminated string to console.                      -
;- EDX -> points to string                                          -
;--------------------------------------------------------------------
PrintStr PROC,
    pString:PTR BYTE                   ; points to string
    pushad                             ; save 32-bit registers

    INVOKE GetStdHandle,               ; get standard device handle
        STD_OUTPUT_HANDLE              ; standard output device
    mov [consoleOutHandle], eax        ; store address of handle

    INVOKE StrLength, pString          ; EAX = length of string
    cld                                ; clear direction flag

    INVOKE WriteConsole,               ; write buffer to console
        consoleOutHandle,              ; output handle
        pString,                       ; points to string
        eax,                           ; string length
        OFFSET bytesWritten,           ; returns number of bytes written
        0

    popad                              ; restore 32-bit registers
    ret
PrintStr ENDP

;====================================================================
;=                            PrintNum                              =
;====================================================================
;- Writes an unsigned 32-bit decimal number to console.             -
;- EAX = number to print                                            -
;--------------------------------------------------------------------
PrintNum PROC
    pushad                             ; save 32-bit registers

    xor ecx, ecx                       ; digit counter
    mov edi, OFFSET num_buffer
    add edi, (num_buffer_size - 1)
    mov ebx, 10                        ; decimal number base
L1:
    xor edx, edx                       ; dividend = 0
    div ebx                            ; EAX / radix

    xchg eax, edx                      ; swap quotient, remainder
    push ebx
    mov ebx, OFFSET xtable             ; get translation table
    xlat                               ; convert to ASCII
    pop ebx

    mov [edi], al                      ; save the digit
    dec edi                               ; back up in buffer
    xchg eax, edx                      ; swap quotient, remainder

    inc ecx                            ; digit counter++
    or eax, eax                        ; quotient = 0?
    jnz L1                             ; no: divide again

    inc edi                             
    ;mov edx, edi                      ; EDX = number string
    INVOKE PrintStr, edi                    ; print digits

    popad                              ; restore 32-bit registers
    ret
PrintNum ENDP

;====================================================================
;=                             NewLine                              =
;====================================================================
;- Writes a carriage return to console.                             -
;--------------------------------------------------------------------
NewLine PROC
    pushad                             ; save 32-bit registers
    INVOKE PrintStr, OFFSET new_line   ; print '\n'
    popad                              ; restore 32-bit registers
    ret
NewLine ENDP

END main