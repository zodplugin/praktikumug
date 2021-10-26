; directive include
%include "asm_io.inc"

segment .data
   ; directive Dx
   hello  db 'Selamat Datang di Universitas Gunadarma', 0 ; string "Selamat Datang"
	
segment .bss
   ; directive RESx

segment .text
   global _main
   _main:
      ; Routine “setup”
      enter  0, 0
      pusha

      ; Program Anda di bawah
      mov   eax, hello    ; taruh alamat memori variabel hello ke register eax
      call  print_string  ; panggil fungsi print_string dari library asm_io


      ; Routine “cleanup”
      popa
      mov    eax, 0
      leave
      ret
