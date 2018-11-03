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
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET fizzbuzz,                        ; points to fizzbuzz
        LENGTHOF fizzbuzz - 1,                  ; number of chars in fizzbuzz
        OFFSET bytesWritten, 0                  ; points to bytesWritten
    jmp f_loop

print_fizz:
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET fizz,                            ; points to fizz
        LENGTHOF fizz - 1,                      ; number of chars in fizz
        OFFSET bytesWritten, 0                  ; points to bytesWritten
    jmp f_loop

print_buzz:
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET buzz,                            ; points to buzz
        LENGTHOF buzz - 1,                      ; number of chars in buzz
        OFFSET bytesWritten, 0                  ; points to bytesWritten
    jmp f_loop

print_num:
    INVOKE GetStdHandle,                        ; get standard handle 
        STD_OUTPUT_HANDLE                       ; standard output device

    mov consoleOutHandle, eax                   ; EAX = consoleOutHandle
    INVOKE WriteConsole,                        ; write buffer to console
        consoleOutHandle,                       ; output handle    
        OFFSET num,                             ; points to num
        SIZEOF num - 1,                         ; number of chars in num
        OFFSET bytesWritten, 0                  ; points to bytesWritten
    jmp f_loop

f_end:
    ret
fizzy ENDP

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
	    consoleOutHandle,     	                ; output handle
	    edx,	                                ; points to string
	    eax,	                                ; string length
	    OFFSET bytesWritten,  	                ; returns number of bytes written
	    0

    popad
    ret
PrintStr ENDP

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
	xor eax, eax    	                        ; EAX = character count
L1:
	cmp BYTE PTR [edi],0	                    ; end of string?
	je  L2	                                    ; yes: quit
	inc edi	                                    ; no: point to next
	inc eax	                                    ; count++
	jmp L1
L2: 
    ret
StrLength ENDP

END main