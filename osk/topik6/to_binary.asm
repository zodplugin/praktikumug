; File: to_binary.asm
;
; Program ini mengkonversi angka desimal yang dimasukkan user ke biner
;

%include "asm_io.inc"

segment .data
;
; Output strings
;
prompt          db    	"Masukkan angka (0 s.d 255): ", 0
nilai0 db "0",0
nilai1 db "1",0

segment .bss
x resd 8


segment .text
     global  _main
_main:
     enter   0,0               ; setup routine
     pusha
     ;; Kode program Anda di bawah
     ;; Jangan modifikasi kode-kode di atas

     ; Prompt user untuk memasukkan angka 0 s.d 255
     mov eax,prompt
     call print_string
     mov eax,0
     call read_int
     mov [x],eax






     ; eax digunakan dalam print_int untuk print angka "0" atau "1"
     ; jadi kita harus memindahkan angka yang dimasukkan user ke register lain
     ; ebx akan kita gunakan untuk nilai bitmask
     ; ecx digunakan sebagai counter loop
     ; sehingga kita harus pindahkan nilai yang dimasukkan user ke register selain eax, ebx, dan ecx
     mov edx,[x]






     ; siapkan angka untuk pembanding nilai bit di register ebx
     ; kita mulai dengan bit ke-7 jadi angka pembanding kita 10000000
     mov ebx,1
     shl ebx, 7




;; loop dari bit 7 ke bit 0
;; pada setiap loop jalankan instruksi test
;; (instruksi test melakukan operasi AND namun tidak menyimpan hasilnya)
;; buat if-else print "0" jika hasil 0, print "1" jika tidak

     ; siapkan counter untuk loop

mov ecx ,0
loop_start:
cmp ecx,7
ja selesai
inc ecx
test [x],ebx
jz print_0
jmp print_1


     ; bandingkan angka yang dimasukkan dengan nilai bitmask
     ; lompat ke label yang sesuai


; jika hasil 1
print_1:

mov eax,nilai1
call print_string
jmp end_if



; jika hasil 0
print_0:
mov eax,nilai0
call print_string




end_if:
shr ebx,1
     ; geser bit nilai bitmask ke kanan pada setiap loop sehingga:
     ; loop ke-1: memeriksa bit 7 dengan nilai bitmask 10000000
     ; loop ke-2: memeriksa bit 6 dengan nilai bitmask 01000000
     ; loop ke-3: memeriksa bit 5 dengan nilai bitmask 00100000
     ; dan seterusnya

jmp loop_start

selesai:




     ;; Kode program Anda di atas
     ;; Jangan modifikasi program di bawah
     popa
     mov     eax, 0            ; return back to C
     leave
     ret